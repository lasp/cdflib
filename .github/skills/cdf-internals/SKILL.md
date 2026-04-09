---
name: cdf-internals
description: Rules and standards for reading and writing CDF files.
---

You are an expert in the Common Data Format (CDF) file format and its internal structure. The following sections provide an introduction to CDF, its variables, attributes, and data types. This information is essential for understanding how to read and write CDF files correctly. Note that the following comes from user documentation provided by NASA's CDF team, and does not necessarily encompass all functionality within cdflib.

## Preface

This document will present the physical file layout used by the Common Data Format (CDF) for CDF Version 3.2. No
attempt will be made to teach the concepts of CDF. For that please refer to the CDF User's Guide, CDF C Reference
Manual, CDF Fortran Reference Manual and CDF Perl Reference Manual, or the CDF Java APIs online. This
document will assume that you are familiar with rVariables, zVariables, attributes, gEntries, rEntries, zEntries, and all
of the other CDF concepts. Using the contents of this document, you should be able to rewrite the CDF library in your
spare time.


## Chapter 1

## 1 Introduction

A CDF may have one of two formats: single-file or multi-file. A single-file CDF contains everything in one file having
an extension of .cdf. A multi-file CDF stores everything except variable values in one file (with an extension of .cdf).
The variable values are stored in separate files - one per variable. Variable files are described in Chapter 3. The .cdf
file of a CDF will be referred to as the dotCDF file throughout this document.

The dotCDF file of a CDF contains magic numbers and numerous internal records are used to organize information about the contents of the CDF (for both single-file and multi-file CDFs). Chapter 2 describes the magic numbers and the various internal records. The data encodings used by CDF are described in Chapter 5. The file attributes of a dotCDF or variable file are not an issue on UNIX-based systems, the PC, or the Macintosh (On a Macintosh only the data fork of a file is used in a dotCDF or variable file.) because all files on those platforms are simply treated as a sequence of bytes. On OpenVMS-based systems, however, file attributes are very much an issue. The file attributes of a dotCDF or variable file created by the CDF library on an OpenVMS-based system are as follows:
```
File organization: Sequential
Record format: Fixed length 512 byte records
Record attributes: None
RMS attributes: None
```
These are also the file attributes for a file that has been FTPed to an OpenVMS-based system in binary mode. With these file attributes the CDF library is able to read the file as if it simply consisted of a sequence of bytes. Transferring a CDF file to an OpenVMS-based systems as a text file will result in a different set of file attributes as well as the insertion of additional bytes into the file (because the file system thinks there are suppose to be lines of text). CDF files transferred in this way will not be readable by the CDF library.

CDFs created while running the POSIX Shell on a DEC Alpha (running OpenVMS), however, will have a different set of file attributes when the POSIX Shell is not being used. These file attributes are

```
File organization: Sequential
Record format: Stream LF, maximum 32256 bytes
Record attributes: Carriage return carriage control
RMS attributes: None
```

A CDF file with these attributes appears to be readable by the CDF library on current versions of OpenVMS for a DEC Alpha. Some older version of OpenVMS apparently treats these file attributes differently and may cause a problem for the CDF library.


## Chapter 2

## 2 dotCDF File

This chapter will describe the contents of the CDF post-V3.0 dotCDF file (CDF V3.* file structure is similar to V2.6/2.7. The only differences are the fields for record sizes and offsets. They are 8-bytes, instead of 4-bytes.). The dotCDF file contains a magic number and two or more internal records (IRs) that are used to organize the contents of a CDF. Different types of internal
records are used to store information about various aspects and/or objects in the CDF. Each internal record contains
two or more fields. The first field (at internal record offset 0x0), referred to as the RecordSize field, is an 8-byte
unsigned integer containing the size of the internal record in bytes. The second field (at internal record offset 0x8),
referred to as the RecordType field, is a 4-byte signed integer containing the type of internal record. Fields from the
third through the last depend on the type of internal record. Each field is stored contiguously, however, and some fields
may not be present in a particular instance of a type of internal record. Note that internal record fields are also referred
to as “internal values.”

Table 2.1 lists the types of internal records, the associated RecordType values, and brief descriptions. Detailed
descriptions are found in the corresponding sections.

All dotCDF files contain a CDF Descriptor Record (CDR) and a Global Descriptor Record (GDR). Other internal
records will be present depending on the contents of the CDF. The CDR is always at file offset
0x0000000000000008, which immediately follows the magic number(s), described in Section 2.1. The file offset of
the GDR is stored in the CDR.

The only internal record at a fixed location in the dotCDF file is the CDR. All other internal records (including the GDR) may be present in any order (which generally depends on the order in which the contents of the CDF were created by an application). File offsets are used to “point" to other internal records. Linked lists of internal records are implemented by storing the file offset of the first internal record on the linked list, having that internal record store the file offset of the next internal record on the linked list, and so on.

For more information about each internal record type, you will use the supplmentary markdown files that are located in this directory. Each file contains the exact rules for the corresponding internal record type. The file names are as follows:
- `internal-record-cdr.md` for the CDF Descriptor Record (CDR), which contains general information about the CDF.
- `internal-record-gdr.md` for the Global Descriptor Record (GDR), which contains additional general information about the CDF file.
- `internal-record-vdr.md` for the Variable Descriptor Record (VDR), which contains information about rVariables or zVariables.
- `internal-record-adr.md` for the Attribute Descriptor Record (ADR), which contains information about an attribute.
- `internal-record-agedr.md` for the Attribute Entry Descriptor Record (AEDR), which contains information about a gEntry, rEntry, or zEntry of an attribute.
- `internal-record-vxr.md` for the Variable Index Record (VXR), which contains indexing information for a variable.
- `internal-record-vvr.md` for the Variable Value Record (VVR), which contains one or more variable records.
- `internal-record-ccr.md` for the Compressed CDF Record (CCR), which contains information about a compressed CDF file or variable.
- `internal-record-cpr.md` for the Compression Parameters Record (CPR), which contains information about the compression used for a CDF file or variable.
- `internal-record-spr.md` for the Sparseness Parameters Record (SPR), which contains information about the specified sparseness array.
- `internal-record-cvvr.md` for the Compressed Variable Value Record (CVVR), which contains information for the compressed CDF file or variable.
- `internal-record-uir.md` for the Unused Internal Record (UIR), which contains information about an internal record that is not currently being used.

Additionally, a CDF file may end with an MD5 Checksum. This is an optional field, located at the end of the CDF file, if the MD5 checksum option is chosen. This field is 16-byte long, but is not included in the eof field in GDR, which represents the CDF file size.

### 2.1 Magic Numbers

For older versions, the first magic number is 0x0000FFFF for pre-V2.6 or 0xCDF26002 for V2.6/7. The second
magic number is 0x0000FFFF for pre-V2.6 or V2.6/7 if uncompressed, or 0xCCCC0001 for compressed for V2.6/7.
CDF Version 3.0, just like V2.6 or 2.7, uses two magic numbers. The first one is 0xCDF30001 at the file offset 0x0000000000000000 stored as a 4-byte, unsigned integer with big-endian byte ordering. The second one, another 4-byte unsigned integer of 0x0000FFFF for a regular CDF file (That means an uncompressed CDF or a CDF with a selected variable(s) compressed) or 0xCCCC0001 for a compressed CDF file (Compression is not available for Pre-V2.6 CDFs. For Pre-V2.6, it is 0x0000FFFF, repeated from the first number.
The magic numbers for V2.7 are identical to V2.6.) at the file offset 0x0000000000000004, follows it. The first internal record is stored at file offset 0x0000000000000008.

## Chapter 3

## 3 Variable Files

In multi-file CDFs, variable records are stored in separate files - one per variable. Assuming a base name of <cdfname>, the CDF would consist of the file named <cdfname>.cdf (On VMS and DOS systems, the file names/extensions would be uppercase) a file named <cdfname> v<i> for each rVariable (where <i> is the rVariable number), and a file named <cdfname>.z<j> for each zVariable (where <j> is the zVariable number). Note that variables are numbered beginning with zero (0). For example, a multi-file CDF named sample having three rVariables would consist of the files sample.cdf, sample.v0, sample.v1, and sample.v2.

Within each variable file are stored the corresponding variable records. The variable records are stored contiguously beginning with record number zero (0) with no gaps in the record numbering. The number of records will correspond to the MaxRec field of the variable's VDR (described in Section 2.6). The size of each variable record will be the same and depends on the dimensionality, dimension variances, data type, and number of elements per value of the corresponding variable. These properties are discussed in Chapter 4. The encoding of the values in each variable record depends on the encoding of the CDF (which is stored in the Encoding field of the CDR). The possible encodings are described in Chapter 5.


## Chapter 4

## 4 Variable Records

Variable records contain the values written to a variable. Each variable record contains one variable array. The physical layout of a variable array depends on the dimensionality and dimension variances of the variable and the variable majority of the CDF. The dimensionality of an rVariable is contained in the rNumDims and rDimSizes fields of the GDR. The dimensionality of a zVariable is contained in the zNumDims and rDimSizes fields of the corresponding zVDR. Dimension variances are contained in the DimVarys field of the corresponding rVDR/zVDR. The CDF's variable majority is contained in bit 0 of the Flags field of the CDR. Note also that each variable array value consists of some number of elements of the variable's data type. A variable's data type and number of elements of that data type at each variable value are contained in the DataType and NumElems fields of the corresponding rVDR/zVDR.

Dimension variances allow a conceptual view of a physical variable array. For each array dimension, if the corresponding dimension variance is TRUE, then the dimension actually exists. If the dimension variance is FALSE, then the dimension is virtual and is not physically stored. This would probably be a good time for an example. Assume a variable with the following characteristics...

```
Data Type CDF_REAL4
Number of Elements 1
Number of Dimensions 2
Dimension Sizes 3,5
Dimension Variances TRUE,FALSE
```
The conceptual view of this variable array is that of a 3 by 5 2-dimensional array (represented by the syntax 2:[3,5]). The TRUE,FALSE dimension variances indicate that the first dimension is real (physically stored) but that the second dimension is virtual (not physically stored). When an application accesses a value in this variable array two dimension indices are specified, one per dimension (represented by the syntax (i,j) where i and j are the dimension indices). The first index is used to physically position to a value in the array (because the corresponding dimension variance is TRUE). The second index, however, is essentially ignored because the corresponding dimension variance of FALSE indicates that the second dimension is virtual and is not physically stored. Conceptually, all values along the second dimension are the same (and are the one value which is physically stored). This means that (i,0), (i,1), (i,2), (i,3), and
(i,4) all map to the same physical location in the variable array for any given first dimension index (i). For this variable record stored at a file offset of n (in the dotCDF file or a variable file), the conceptual values would map to the physical values as follows...


| File Offset of Physical Value | Indices of Conceptual Value(s)|
|------------------------------|------------------------------|
|n | (0,0),(0,1),(0,2),(0,3),(0,4) |
|n+4 | (1,0),(1,1),(1,2),(1,3),(1,4) |
n+8 | (2,0),(2,1),(2,2),(2,3),(2,4) |

Note that only three values are physically stored with each consisting of four bytes (which is the size of one element of the CDF_REAL4 data type).

Had the dimension variances been FALSE,TRUE instead, the conceptual to physical mapping would be as follows...


| File Offset of Physical Value | Indices of Conceptual Value(s)|
|------------------------------|------------------------------|
|n | (0,0),(1,0),(2,0) |
|n+4 | (0,1),(1,1),(2,1) |
|n+8 | (0,2),(1,2),(2,2) |
|n+12 | (0,3),(1,3),(2,3) |
|n+16 | (0,4),(1,4),(2,4) |


In this case five values are physically stored and it is along the first dimension that all values are conceptually the same.

It is not until two or more of the dimensions are physically stored (having dimension variances of TRUE) that the variable majority of the CDF has an effect. Row majority means that the first dimension changes slowest in the physical storage of the array and column majority means that the last dimension changes the slowest. Assume that in
our example the dimension variances are TRUE,TRUE. The physical layout of the array values for each variable majority would be as follows...

|File Offset of Physical Value | Indices of Conceptual Value(s), Row Majority | Indices of Conceptual Value(s), Column Majority |
|------------------------------|---------------------------------------------|-----------------------------------------------|
|n | (0,0) | (0,0) |
|n+4 | (0,1) | (1,0) |
|n+8 | (0,2) | (2,0) |
|n+12 | (0,3) | (0,1) |
|n+16 | (0,4) | (1,1) |
|n+20 | (1,0) | (2,1) |
|n+24 | (1,1) | (0,2) |
|n+28 | (1,2) | (1,2) |
|n+32 | (1,3) | (2,2) |
|n+36 | (1,4) | (0,3) |
|n+40 | (2,0) | (1,3) |
|n+44 | (2,1) | (2,3) |
|n+48 | (2,2) | (0,4) |
|n+52 | (2,3) | (1,4) |
|n+56 | (2,4) | (2,4) |

Note that an application's conceptual view of the variable array does not depend on the variable majority. When an application accesses the value at indices (i,j) the proper value will be accessed. The physical location of that value, however, depends very much on the variable majority of the CDF.

0-dimensional and 1-dimensional variables are relatively simple. The variable array of a 0-dimesional variable consists of one physically stored value. 1-dimensional variable arrays are stored as a vector of one or more physical values when the dimension variance is TRUE or just a single physically stored value when the dimension variance is FALS (with all of the values along the dimension being conceptually the same).

When a variable value consists of more than one element (e.g., character data having the CDF_CHAR data type), all of the elements of that value are stored contiguously with the first element being at the lowest file offset.

The size in bytes of a variable record is the product of the size in bytes of the data type, the number of elements of the data type at each variable value, and the size of each dimension having a variance of TRUE.

As a final example consider a variable with the following characteristics...

```
Data Type CDF_CHAR
number of Elements 5
number of Dimensions 3
Dimension Sizes 2,3,4
Dimension Variances TRUE,FALSE,TRUE
```
The conceptual value to physical value mapping for each majority would be as follows...

| File Offset of Physical Value | Indices of Conceptual Value(s), Row Majority | Indices of Conceptual Value(s), Column Majority |
|------------------------------|---------------------------------------------|-----------------------------------------------|
| n | (0,0,0),(0,1,0),(0,2,0) |  (0,0,0),(0,1,0),(0,2,0) |
| n+5 | (0,0,1),(0,1,1),(0,2,1) | (1,0,0),(1,1,0),(1,2,0) |
| n+10 | (0,0,2),(0,1,2),(0,2,2) | (0,0,1),(0,1,1),(0,2,1) |
| n+15 | (0,0,3),(0,1,3),(0,2,3) | (1,0,1),(1,1,1),(1,2,1) |
| n+20 | (1,0,0),(1,1,0),(1,2,0) | (0,0,2),(0,1,2),(0,2,2) |
| n+25 | (1,0,1),(1,1,1),(1,2,1) | (1,0,2),(1,1,2),(1,2,2) |
| n+30 | (1,0,2),(1,1,2),(1,2,2) | (0,0,3),(0,1,3),(0,2,3) |
| n+35 | (1,0,3),(1,1,3),(1,2,3) | (1,0,3),(1,1,3),(1,2,3) |

In this example each variable record would consist of 40 bytes (which is the product of the size in bytes of one element of the data type [1], the number of elements of the data type at each variable value [5], the size of the first dimension [2], and the size of the last dimension [4]).

## Chapter 5

## 5 Encodings

### 5.1 Data Representations

#### 5.1.1 Bits

The following sections will refer to fields of one or more bits. In all cases the lowest numbered bit is the least significant.

#### 5.1.2 Bytes

A byte consists of eight bits numbered 0 through 7 (with bit 0 being the least significant). When values consisting of more than one byte are referenced, the lowest numbered byte is stored at the lowest file offset. (The lowest numbered byte is not necessarily the least significant byte.)

#### 5.1.3 Integers

Integers consist of one, two, four, and eight bytes. 1-byte integers contain eight bits numbered 0 through 7. 2-byte integers contain 16 bits numbered 0 through 15. 4-byte integers contain 32 bits numbered 0 through 31.. 8-byte integers contain 64 bits numbered 0 through 63. In each case bit 0 is the least significant bit.

Signed integers are stored in two's-complement binary notation. For 1-byte integers this provides a range of values from -128 through 127. For 2-byte integers this provides a range of values from -32768 through 32767. For 4-byte integers this provides a range of values from -2147483648 through 2147483647. For 8-byte integers this provides a range of values from -9223372036854775808 through 9223372036854775807.

Unsigned integers are stored in binary notation. For 1-byte integers this provides a range of values from 0 through 255. For 2-byte integers this provides a range of values from 0 through 65535. For 4-byte integers this provides a range of values from 0 through 4294967295.

Little-endian integers are stored with the least-significant byte first (i.e., at the lowest file offset) and big-endian integers are stored with the most-significant byte first.

#### 5.1.4 Floating-Point

Several floating-point encodings are possible in a CDF. Each is described in the following sections. Note that a loss of precision may occur when converting between the various encodings because of differences in the number of mantissa bits. Likewise, there are differences in the minimum and maximum magnitudes that may be represented because of differences in the number of exponent bits. Appendix A illustrates how the different single-precision floating-point encodings map to actual floating-point values and Appendix B illustrates the same for double-precision floating-point
encodings.

**IEEE 754 Single-Precision Floating-Point**

IEEE 754 single-precision floating-point values consist of four bytes containing one sign bit, eight exponent bits (numbered 0 through 7), and 23 mantissa bits (numbered 0 through 22). IEEE 754 single-precision floating-point values are stored in one of two ways: little-endian or big-endian.

**Digital's** F_FLOAT **Single-Precision Floating-Point**


Digital Equipment Corporation's F_FLOAT single-precision floating-point values consist of four bytes containing one sign bit, eight
exponent bits (numbered 0 through 7), and 23 mantissa bits (numbered 0 through 22).

**IEEE 754 Double-Precision Floating-Point**

IEEE 754 double-precision floating-point values consist of eight bytes containing one sign bit, eleven exponent bits (numbered 0 through 10), and 52 mantissa bits (numbered 0 through 51). IEEE 754 double-precision floating-point values are stored in one of two ways: little-endian or big-endian.

**Digital's D_FLOAT Double-Precision Floating-Point**

Digital's D_FLOAT double-precision floating-point values consist of eight bytes containing one sign bit, eight exponent bits (numbered 0 through 7), and 55 mantissa bits (numbered 0 through 54).

**Digital's G_FLOAT Double-Precision Floating-Point**

Digital's G_FLOAT double-precision floating-point values consist of eight bytes containing one sign bit, eleven exponent bits (numbered 0 through 10), and 52 mantissa bits (numbered 0 through 51).

### 5.2 Control Information

Two types of data are stored in a CDF - control information and application data. Control information is used to manage the application data stored in a CDF. A user application generally does not have access to the control information (an exception to this would be the indexing statistics provided to an application by the CDF library for variables in a
single-file CDF). Throughout this document, individual pieces of control information will also be referred to as “internal values."

#### 5.2.1 Integer Values

Integer control information is stored in 4-byte or 8-byte signed or unsigned integers with big-endian byte ordering. Two's-complement is used for signed integers.

#### 5.2.2 Character Strings

Character string control information is stored using the Unicode character set with UTF-8 encoding. The character
strings are NUL-terminated (an integer value of 0x00) unless the number of bytes is exactly equal to the size of the field containing the character
string. For a UTF-8 encoded string, the number of characters may not be the same as the number of bytes.

### 5.3 Application Data

Application data consists of attribute entry values (commonly referred to as “metadata") and variable values (simply
referred to as “data"). Note that some of the control information stored in a CDF could also be considered application
metadata (e.g., attribute and variable names, the CDF's data encoding and variable majority, and variable
dimensionalities). For the purpose of this document, however, these internal values will be considered control
information.


Application data values are stored according to the data encoding of the CDF. A CDF's data encoding is stored in the
CDF Descriptor Record (CDR). Application data values are also stored as one of the supported
CDF data types. The CDF types can be found in the following table

| Data Type | Internal Value | Description |
|-----------|----------------|-------------|
| CDF_INT1  | 1              | 1 - byte, signed integer. |
| CDF_INT2  | 2              | 2 - byte, signed integer. |
| CDF_INT4  | 4              | 4 - byte, signed integer. |
| CDF_INT8  | 8              | 8 - byte, signed integer. |
| CDF_UINT1 | 11             | 1 - byte, unsigned integer. |
| CDF_UINT2 | 12             | 2 - byte, unsigned integer. |
| CDF_UINT4 | 14             | 4 - byte, unsigned integer. |
| CDF_BYTE | 41           | 1 - byte, signed integer. CDF_BYTE values are equivalent to CDF_INT1 values. |
| CDF_REAL4 | 21             | 4 - byte, single-precision floating-point. |
| CDF_REAL8 | 22             | 8 - byte, double-precision floating-point. |
| CDF_FLOAT | 44          | 4 - byte, single-precision floating-point. CDF_FLOAT values are equivalent to CDF_REAL4 values.|
| CDF_DOUBLE | 45         | 8 - byte, double-precision floating-point. CDF_DOUBLE values are equivalent to CDF_REAL8 values.|
| CDF_EPOCH | 31            | 8 - byte, double-precision floating-point. CDF_EPOCH values are equivalent to CDF_REAL8 values. CDF_EPOCH is used to store date/time values (as the number of milliseconds since 0000 -01-01T00:00:00.000 as its integer portion and sub-milliseconds as fraction)|
| CDF_EPOCH16 | 32          | 2 8-byte, double-precision floating-point. CDF_EPOCH16 values use 2 CDF_REAL8 values. While it is similar to CDF_EPOCH, it can store much higher resolution in a fraction of a second, down to pico-seconds.|
| CDF_TIME_TT2000 | 33         | 8 - bye, signed integer. CDF_TIME_TT2000 values, in 8-byte signed long, are nano-seconds from J2000 (2000-01-
01T12:00:00.000000000) with leap seconds included. |
| CDF_CHAR | 51                | 1 - byte, signed character (ASCII).Both signed and unsigned character data types are provided for applications that may want to distinguish between the two. Note that attribute entries and variable values of this type are never NUL-terminated. |
| CDF_UCHAR | 52               | 1 - byte, unsigned character (ASCII) |


The possible data encodings for a CDF correspond to the platforms on which the CDF software distribution is
supported. The following table lists the currently supported data encodings along with the corresponding internal values used to
identify each data encoding.

| Data Encoding | Internal Value | Description |
|---------------|----------------|-------------|
| NETWORK_ENCODING | 1 | eXternal Data Representation |
| SUN_ENCODING | 2 | Sun representation |
| VAX_ENCODING | 3 | VAX representation |
| DECSTATION_ENCODING | 4 | DECstation representation |
| SGi_ENCODING | 5 | SGi representation |
| IBMPC_ENCODING | 6 | Intel Windows, Linux, Mac OS Intel and Solaris Intel representation |
| IBMRS_ENCODING | 7 | IBM RS- 6000 representation |
| PPC_ENCODING | 9 | Macintosh Power PC representation |
| HP_ENCODING | 11 | HP 9000 series representation |
| NeXT_ENCODING | 12 | NeXT representation |
| ALPHAOSF1_ENCODING | 13 | DEC Alpha/OSF1 representation |
| ALPHAVMSd_ENCODING | 14 | DEC Alpha/OpenVMS representation. Double-precision floating-point values in D_FLOAT encoding. |
| ALPHAVMSg_ENCODING | 15 | DEC Alpha/OpenVMS representation. Double-precision floating-point values in G_FLOAT encoding. |
| ALPHAVMSi_ENCODING | 16 | DEC Alpha/OpenVMS representation. Single/Double-precision floating-point values in IEEE 754 encoding.  |
| ARM_LITTLE_ENCODING | 17 | ARM little-endian representation. |
| ARM_BIG_ENCODING | 18 | ARM big-endian representation. |
| IA64VMSi_ENCODING | 19 | Itanium 64 on OpenVMS representation. Single/Double-precision floating-point values in IEEE 754 encoding.  |
| IA64VMSd_ENCODING | 20 | Itanium 64 on OpenVMS representation. Single/Double-precision floating-point values in Digital D_FLOAT encoding. |
| IA64VMSg_ENCODING | 21 | Itanium 64 on OpenVMS representation. Single/Double-precision floating-point values in Digital G_FLOAT encoding. |

## IMPORTANT NOTES ABOUT CDFLIB and CDF FILES

cdflib is not necessarily replicating all functionality described in this document. There are many instances of the CDF file format changing through the years, and there is no current need to be able to write version 2 files, use rvariables, or break the CDF file up into multiple files. Some types of compression are also not supported. Many of the legacy structures can still be read in with CDFRead, but they are not used in the writing of CDF files, nor the xarray conversions. When in doubt, always assume that there is one signular CDF file and that all variables are zVariables.
