### 2.5 Attribute Entry Descriptor Record

An Attribute Entry Descriptor Record (AEDR) contains a description of an attribute entry. There are two types of AEDRs: AgrEDRs describing g/rEntries and AzEDRs describing zEntries. Because the only difference between AgrEDRs and AzEDRs is the value of the RecordType field, they will be referred to as AEDRs throughout this document. The AgrEDRhead field of an ADR contains the file offset of the first AgrEDR for the corresponding attribute. Likewise, the AzEDRhead field of an ADR contains the file offset of the first AzEDR. The linked lists of AEDRs starting at AgrEDRhead and AzEDRhead will contain only AEDRs of that type - AgrEDRs or AzEDRs, respectively.

Note that the term g/rEntry is used to refer to an entry that may be either a gEntry or an rEntry. The type of entry described by an AgrEDR depends on the scope of the corresponding attribute. AgrEDRs of a global-scoped attribute describe gEntries. AgrEDRs of a variable-scoped attribute describe rEntries. The scope of an attribute is stored in the Scope field of the corresponding ADR.

Each AEDR contains the following contiguous fields...

RecordSize - Signed 8-byte integer, big-endian byte ordering. The size in bytes of this AEDR (including this field).

RecordType - Signed 4-byte integer, big-endian byte ordering. Either the value 5 which identifies this as an AgrEDR or the value 9 if
an AzEDR. Because zEntries were not supported until CDF V2.2, prior to CDF V2.2 AzEDRs will not occur in a dotCDF file.

AEDRnext - Signed 8-byte integer, big-endian byte ordering. The file offset of the next AEDR. Beginning with CDF V2.1 the last AEDR will contain a file offset of 0x0000000000000000 in this field (to indicate the end of the AEDRs).

AttrNum Signed 4-byte integer, big-endian byte ordering. The attribute number to which this entry corresponds. Attributes are numbered beginning
with zero (0).

DataType - Signed 4-byte integer, big-endian byte ordering. The data type of this entry. The possible data type internal values are described in Section 5.3.

Num - Signed 4-byte integer, big-endian byte ordering. This entry's number: an entry number in a global attribute, or the variable number for an
rVariable or zVariable in a variable attribute. Entries are numbered beginning with zero (0).

NumElems - Signed 4-byte integer, big-endian byte ordering. The number of elements of the data type (specified by the DataType field) for this entry. For character type, i.e., CDF_CHAR or CDF_UCHAR, it’s the length of the string. For numeric type, it’s the number of items, which is 1 for most cases. However, it can be multiple items. This field cannot be zero (0) or less.

NumStrings - Signed 4-byte integer, big-endian byte ordering. The number of strings in the Value field. This applies only for string-type data from variable entry. Strings are delimited by “\\N “, a three-character string, in the Value field. This field shows the number of strings concatenated into a single one at the Value field. A value of 0 (from pre-3.7.0) or 1 indicates that the Value field contains a single string. For non-string data, it should be 0. In pre-3.7.0 versions, this field is identified as rfuA, a reserved field, with a value of 0.

rfuB - Signed 4-byte integer, big-endian byte ordering. Reserved for future used. Always set to zero (0).

rfuC - Signed 4-byte integer, big-endian byte ordering. Reserved for future used. Always set to zero (0).

rfuD - Signed 4-byte integer, big-endian byte ordering. Reserved for future used. Always set to negative one (-1).

rfuE - Signed 4-byte integer, big-endian byte ordering. Reserved for future used. Always set to negative one (-1).

Value - This entry's value. This consists of the number of elements (specified by the NumElems field) of the data type (specified by the DataType field). This can be thought of as a 1-dimensional array of values (stored contiguously). The size of this field is the product of the number of elements and the size in bytes of each element. The encoding of the elements depends on the data encoding of the CDF (which is contained in the Encoding field of the CDR). The possible encodings are described in Section 5.3. For a string type entry, it can have a null value, which it contains a single byte of \x00, along with NumElems being 1.


Below is a table describing the byte ordering of the AEDR.


| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | Offset: |
| RecordType | 4 bytes | Offset: |
| AEDRnext | 8 bytes | Offset: |
| AttrNum | 4 bytes | Offset: |
| DataType | 4 bytes | Offset: |
| Num | 4 bytes | Offset: |
| NumElem |s 4 bytes | Offset: |
| NumStrings | 4 bytes | Offset: |
| rfuB | 4 bytes | Offset: |
| rfuC | 4 bytes | Offset: |
| rfuD | 4 bytes | Offset: |
| rfuE | 4 bytes | Offset: |
| Value | Variable | Offset:56. Size depends on the DataType and NumElems fields. |
