---
name: ISTP Compliance
description: Rules and standard formatting for ISTP compliance in CDF files.
---

You are an expert in validating CDF files against ISTP compliance standards.

## Common Data Format (CDF)
CDF originated in 1984 and is now available via libraries in many programming languages. The main advantages of CDF include:

- Self-describing data format for storage of scalar and multidimensional data in a platform- and discipline-independent way
- Scientific data management package (CDF Library) for transparent access to data and metadata via Application Programming Interfaces (APIs) and a suite of CLI tools
- Standard APIs for C, Fortran, Java, Perl, C#/Visual Basic, IDL, MATLAB and user-supplied APIs for, e.g., Python, Sybase, MySQL.
- Dedicated time data types and time encoding/decoding functions for precise time definition and handling
- Built-in support for checksums and  data compression (gzip, RLE, Huffman) with automatic uncompression on file and individual variable levels
- Large file support (> 2G-bytes)

See [CDF web site](https://cdf.gsfc.nasa.gov/) for complete documentation and CDF Library and tools. There are native CDF libraries in Python, Java, C#, and other software languages, in addition to the original C library.

### CDF Variables

Variables in CDF format store data as arrays of values, ranging from 0 (scalar data) to 10 dimensions. CDF supports two types of variables: zVariables and old style rVariables, and both types can coexist in a single CDF file. Each zVariable can have its own dimensionality (number of dimensions and their sizes), while all rVariables in a file have the same dimensionality. Since rVariables are inherently much less efficient than zVariables in both data storing and handling, and are preserved in CDF for backwards compatibility, **use of only zVariables is strongly encouraged for all new datasets**.

Independent of variable type, and in addition to dimensionality, each dimensional (1-D or higher) variable in a CDF file is defined with its dimension variances, specifying if values may change along the corresponding dimensions. Each variable is also defined with a data specification, consisting of a data type and a number of elements of that data type at each variable value. CDF supports a variety of character, integer, real, and time data types. (See below for introduction and the [CDF User's Guide](https://spdf.gsfc.nasa.gov/pub/software/cdf/doc/cdf_User_Guide.pdf) for complete definition of the data types.) **For non-character data type variables, the number of elements must always be one**. For a character data type variables, multiple elements (1-D array) are allowed at each value, allowing storing a string (1-D array of characters) as a value and an array of strings (up to 10 dimensions) as an array of values. Since the number of elements is defined as a constant for all values of a variable, for a character data type variable it must be specified as the maximum number of characters in all values (all strings over all dimensions) for that variable.

Each array of variable values is stored as a variable record. And each variable may have multiple (and independent of other variables) number of records. This **record dimension is always associated with the time dimension** in ISTP usage, with multiple records for a variable corresponding to multiple timestamps. Note that since a variable is simply an array of values (or multiple arrays of values for a variable with multiple records), it does not carry information about the correspondence between records and timestamps. This correspondence is always defined via the ISTP variable attribute `DEPEND_0`, with its value equal to the name of a scalar time data type variable in the same CDF file with the same number of records as the data variable. (Multiple time variables are supported, allowing data variables with different time cadences to be stored in the same CDF file.) Similarly, the meanings of the variable dimension are defined via variable attributes, e.g., the `DEPEND_1` attribute holds as its value the name of a 1-D variable in the same CDF file with its size equal to the data variable's first dimension size, and its values and attributes describing that data variable's first dimension.

When a variable is created in a CDF file, it must be defined as either record-varying, meaning that multiple records for that variable may be written in the file, or non-record-varying, meaning that only one variable record may be written.

Each variable in a CDF file must have a unique name, limited to characters in the ASCII set, with the same name space shared between zVariables and rVariables. Variable names are always case sensitive, regardless of the operating system.

### CDF Attributes

CDF attributes, used to store metadata, are divided into two types: global scope attributes (describe properties of the whole file) and variable scope attributes (describe properties of individual variables). The actual metadata are stored in the attribute entries, and each attribute can have 0 or more associated entries, independently of other attributes. For a variable attribute, an entry number is the actual variable number, and each variable attribute can be associated with multiple variables via multiple entries. For a global attribute, entry numbers do not carry special meaning, and all entries for a global attribute can be seen as simply a list of entries.

Each entry for an attribute is defined with a data specification, and different entries of the same attribute have independent data specifications. A data specification consists of a data type and a number of elements of that data type at the attribute entry. For an attribute entry, multiple elements (1-D array) are allowed for each of the CDF data type.  For character data types, the number of elements is the number of characters in the string, allowing storage of a string (array of characters) as an attribute entry value. For non-character data types, the number of elements is the size of an array of that data type, allowing storage of a scalar (1 element) or a 1-D array as an attribute entry.

Each attribute in a CDF file must have a unique name, limited to characters in the ASCII set. Attribute names are always case sensitive, regardless of the operating system.

### CDF Data Types
CDF supports a variety of data types consistent with the types available with C and Fortran compilers on most computers. All data types are based on an 8-bit byte. See [CDF User's Guide](https://spdf.gsfc.nasa.gov/pub/software/cdf/doc/cdf_User_Guide.pdf) for a complete description.

#### Character Data Types
| Data Type | Description|
|-|-|
|CDF_CHAR   |1-byte character          |
|CDF_UCHAR  |1-byte unsigned character |

These two
types are considered interchangeable. Character data types are unique for variables in that they are the only data types for which more than one element per
value is allowed.

#### Integer Data Types
| Data Type | Description|
|-|-|
|CDF_BYTE  |1-byte signed integer  |
|CDF_INT1  |1-byte signed integer  |
|CDF_UINT1 |1-byte unsigned integer|
|CDF_INT2  |2-byte signed integer  |
|CDF_UINT2 |2-byte unsigned integer|
|CDF_INT4  |4-byte signed integer  |
|CDF_UINT4 |4-byte unsigned integer|
|CDF_INT8  |8-byte signed integer  |

#### Floating Point Data Types
| Data Type | Description|
|-|-|
|CDF_REAL4 & CDF_FLOAT  |4-byte single-precision floating-point |
|CDF_REAL8 & CDF_DOUBLE |8-byte double-precision floating-point |

#### Time Data Types
| Data Type | Description|
|-|-|
| CDF_EPOCH       | milliseconds since 0AD as 8-byte floating-point|
| CDF_EPOCH16     | picoseconds since 0AD as two 8-byte floating-point numbers |
| CDF_TIME_TT2000 | nanoseconds since J2000 in Terrestrial Time, including leap seconds, as 8-byte signed integer|

---

Use the supplementary markdown files in this directory to find the exact rules needed to answer the user's query:
* If the user asks about global attributes, read the `metadata-global-attributes.md` file.
* If the user asks about CDF variables, read the `metadata-variables.md` file.
* If the user asks about variable attributes, read the `metadata-variable-attributes.md` file.

Do not guess the ISTP standards. Always read the relevant markdown file before answering or validating code.
