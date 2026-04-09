### 2.2 CDF Descriptor Record

All dotCDF files contain a single CDF Descriptor Record (CDR) at file offset 0x00000008. The CDR contains general
information about the CDF (as does the GDR described in Section 2.3).

The CDR, as shown in Figure 2.4, contains the following contiguous fields...


RecordSize - Signed 8-byte integer, big-endian byte ordering. The size in bytes of this CDR (including this field).

RecordType - Signed 4-byte integer, big-endian byte ordering. The value 1 which identifies this as the CDR.

GDRoffset - Signed 8-byte integer, big-endian byte ordering. The file offset of the GDR. The GDR is described in Section 2.3.

Version -  Signed 4-byte integer, big-endian byte ordering. The version of the CDF distribution (library) that created this CDF. CDF distributions are identified with four values: version, release, increment, and sub-increment. For example, CDF V2.5.8a is CDF version 2, release 5, and increment 8, sub-increment ‘a’. Note that the sub-increment is not stored in a CDF.

Release - Signed 4-byte integer, big-endian byte ordering. The release of the CDF distribution that created this CDF. See the Version field above.

Encoding - Signed 4-byte integer, big-endian byte ordering. The data encoding for attribute entry and variable values. Section 5.3 describes the supported data encodings and their corresponding internal values.

Flags - Signed 4-byte integer, big-endian byte ordering. Boolean flags, one per bit, describing some aspect of the CDF. Bit numbering is described in Chapter 5. The meaning of each bit is as follows...
0 - The majority of variable values within a variable record. Variable records are described in Chapter 4. Set indicates row-majority. Clear indicates column-majority.
1 - The file format of the CDF. Set indicates single-file. Clear indicates multi-file.
2 - The checksum of the CDF. Set indicates a checksum method is used.
3 - The MD5 checksum method indicator. Set indicates MD5 method is used for the checksum. Bit 2 must be set.
4 - Reserved for another checksum method. Bit 2 must be set and bit 3 must be clear.
5-31 Reserved for future use. These bits are always clear.

rfuA - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Always set to zero (0).

rfuB - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Always set to zero (0).

Increment - Signed 4-byte integer, big-endian byte ordering. The increment of the CDF distribution that created this CDF. See the Version field above. Prior to CDF V2.1 this field was always set to zero (0).

Identifier - Signed 4-byte integer, big-endian byte ordering. This field indicates how the file was created. A value of negative one (-1) means the file was created by the normal way through the CDF’s C-based library. It has a value of one (1) if the file was created directly by Java without the use of the library. A values of two (2) indicates that the file was created by Python without the use of the library.

rfuE - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Always set to negative one (-1).

Copyright - Character string, ASCII character set. The CDF copyright notice. This consists of a string of characters containing one or more
lines of text with each line of text separated by a newline character (0x0A). If the total number of characters in the copyright is less than the size of this field, a NUL character (0x00) will be used to terminate the string. In that case, the characters beyond the NUL-terminator (up to the size of this field) are undefined. This field may be one of two sizes. Prior to CDF V2.5, this field consisted of 1945 characters (bytes). Since the release of CDF V2.5, this field has been reduced to 256 characters (bytes).


A table of the CDR is below

| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | Offset:0 |
| RecordType | 4 bytes | Offset:8 |
| GDRoffset | 8 bytes | Offset:12 |
| Version | 4 bytes | Offset:20 |
| Release | 4 bytes | Offset:24 |
| Encoding | 4 bytes | Offset:28 |
| Flags | 4 bytes | Offset:32 |
| rfuA | 4 bytes | Offset:36 |
| rfuB | 4 bytes | Offset:40 |
| Increment | 4 | bytes Offset:44 |
| Identifier | 4 | bytes Offset:48 |
| rfuE | 4 bytes | Offset:52 |
| Copyright | variable | Offset:56. 1945 or 256 bytes in length depending on the CDF distribution that created/modified the CDF. |
