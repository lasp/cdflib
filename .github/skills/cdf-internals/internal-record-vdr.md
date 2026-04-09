### 2.6 Variable Descriptor Record

A Variable Descriptor Record (VDR) contains a description of a variable in a CDF. There are two types of VDRs: rVDRs describing rVariables and zVDRs describing zVariables. The term VDR is used when something applies to both rVDRs and zVDRs. The terms rVDR and zVDR will be used
when a distinction must be made. The rVDRhead field of the GDR contains the file offset of the first rVDR. Likewise, the zVDRhead field of the GDR contains the file offset of the first zVDR. The linked lists of VDRs starting at rVDRhead and zVDRhead will contain only VDRs of that type - rVDRs or zVDRs, respectively. If this variable is compressed, a pointer to a Compressed Parameters Record (CPR) is set in the CPRorSPRoffset field.

Each VDR contains the following contiguous fields (with the exceptions for rVariables being noted)...

RecordSize - Signed 8-byte integer, big-endian byte ordering. The size in bytes of this VDR (including this field).

RecordType - Signed 4-byte integer, big-endian byte ordering. Either the value 3, which identifies this as an rVDR or the value 8 if a zVDR.

VDRnext - Signed 8-byte integer, big-endian byte ordering. The file offset of the next VDR.

DataType - Signed 4-byte integer, big-endian byte ordering. The data type of this entry. The possible data type internal values are described in Section 5.3.

MaxRec - Signed 4-byte integer, big-endian byte ordering. The maximum record number physically written to this variable. This is the last written
record number. More records might be allocated after this record so future written record(s) can be in contiguous form to eliminate the potential data fragmentation. Variable records are numbered beginning at zero (0). If no records have been written to this variable, this field
will contain negative one (-1).

VXRhead - Signed 8-byte integer, big-endian byte ordering. The file offset of the first Variable Index Record (VXR). VXRs are used in single-file CDFs to store the locations of Variable Value Records (VVRs). VVRs are used to store variable records in single-file CDFs. VXRs are described in Section 2.7 and VVRs are described in Section 2.8. The first VXR contains the file offset of the next VXR and so on. The last VXR contains a file offset of 0x00000000 for the file offset of the next VXR (to indicate the end of the VXRs). In single-file CDFs, if no records have been written to this variable, this field will contain a file offset of 0x0000000000000000. For multi-file CDFs variable records are stored in separate files and this field will always contain a file offset of 0x00000000. The variable files of a multi-file CDF are described in Chapter 3.

VXRtail - Signed 8-byte integer, big-endian byte ordering. The file offset of the last VXR. See the VXRhead field above for a description of VXRs.

Flags - Signed 4-byte integer, big-endian byte ordering. Boolean flags, one per bit, describing some aspect of this variable. Bit numbering is
described in Chapter 5. The meaning of each bit is as follows...
0: The record variance of this variable. Set indicates a TRUE record variance. Clear indicates a FALSE record variance.
1: Whether or not a pad value is specified for this variable. Set indicates that a pad value has been specified. Clear indicates that a pad value has not been specified. The PadValue field described below is only present if a pad value has been specified.
2: Whether or not a compression method might be applied to this variable data. Set indicates that a compression is chosen by the user and the data might be compressed, depending on the data size and content. If the compressed data becomes larger than its uncompressed data, no compression is applied and the data are stored as uncompressed, even the compression bit is set. The compressed data is stored in Compressed Variable Value Record (CVVR) while uncompressed data go into Variable Value Record (VVR). Clear indicates that a compression will not be used. The CPRorSPRoffset field described below provides the offset of the Compressed Parameters Record if this compression bit is set and the compression used.
3-31:  Reserved for future use. These bits are always clear.

sRecords - Signed 4-byte integer, big-endian byte ordering. Type of sparse records: no sparserecords, padded sparserecords (using the default/defined pad value), or previous sparserecords (using the last written value). When reading a record(s) from a variable with sparserecords that is not written, data value(s) will be returned based on the type of sparse records. In this case, a non-zero, but postive status code will be returned, indicating a virtual record(s) is involved. A variable with sparserecords tends to be less efficient than a variable of non-sparserecords. Try to limit the number of sparserecords if possible.

rfuB - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Always set to zero (0).

rfuC - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Always set to negative one (-1).

rfuF - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Always set to negative one (-1).

NumElems - Signed 4-byte integer, big-endian byte ordering. The number of elements of the data type (specified by the DataType field)
for this variable at each value. For character type, i.e., CDF_CHAR or CDF_UCHAR, it’s the length of the string. For numeric type, it’s the number of items, which is 1 for most cases. However, it can be multiple items. This field can not be zero (0) or less.

Num - Signed 4-byte integer, big-endian byte ordering. This variable's number. Variables are numbered beginning with zero (0). Note that rVariables and zVariables are each numbered beginning with zero (0) and are considered two separate groups of variables.

CPRorSPRoffset - Signed 8-byte integer, big-endian byte ordering. CPR/SPR offset depending on bits set in 'Flags' and compression used. If neither
compression nor sparse arrays, set to 0xFFFFFFFFFFFFFFFF.

BlockingFactor - Signed 4-byte integer, big-endian byte ordering. Blocking factor for this variable.

Name - Character string, ASCII character set. The name of this variable. This field is always 256 bytes in length. If the number of characters in the name is less than 256, a NUL character (0x00) will be used to terminate the string. In that case, the characters beyond the NUL-terminator (up to the size of this field) are undefined.

zNumDims - Signed 4-byte integer, big-endian byte ordering. The number of dimensions for this zVariable. This field will not be present if this is an rVDR (rVariable).

zDimSizes - Signed 4-byte integers, big-endian byte ordering within each. Zero or more contiguous dimension sizes for this zVariable depending on the value of the zNumDims field. This field will not be present if this is an rVDR (rVariable).

DimVarys - Signed 4-byte integers, big-endian byte ordering within each. Zero or more contiguous dimension variances. If this is an rVDR, the number of dimension variances will correspond to the value of the rNumDims field of the GDR. If this is a zVDR, the number of dimension variances will correspond to the value of the zNumDims field in this zVDR. A value of negative one (-1) indicates a TRUE dimension variance and a value of zero (0) indicates a FALSE dimension variance.

PadValue - The variable's pad value. If bit 1 of the Flags field of this VDR is clear, then a pad value has not been specified for this variable and this field will not be present. If a pad value has been specified, the size of this field depends on the number of elements and the size of the data type. The encoding of the elements depends on the encoding of the CDF (which is contained in the Encoding field of the CDR). The possible encodings are described in Section 5.3.

Below is a table of byte offsets in a VDR.

| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | Offset:0 |
| RecordType | 4 bytes | Offset:8 |
| VDRnext | 8 bytes | Offset:12 |
| DataType | 4 bytes | Offset:20 |
| MaxRec | 4 bytes | Offset:24 |
| VXRhead | 8 bytes | Offset:28 |
| VXRtail | 8 bytes | Offset:36 |
| Flags | 4 bytes | Offset:44 |
| SRecords | 4 bytes | Offset:48 |
| rfuB | 4 bytes | Offset:52 |
| rfuC | 4 bytes | Offset:56 |
| rfuF | 4 bytes | Offset:60 |
| NumElems | 4 bytes | Offset:64 |
| Num | 4 bytes | Offset:68 |
| CPRorSPRoffset | 8 bytes | Offset:72 |
| BlockingFactor | 4 bytes | Offset:80 |
| Name | 256 bytes | Offset:84. Was 64 bytes in earlier V2.* |
| zNumDims | 4 bytes | Offset:340 if a zVDR. Not present if an rVDR. |
| zDimSizes | 4 bytes | Offset:344. Size depends on the zNumDims field if a zVDR (but not present if zero dimensions). Not present if an rVDR. |
| DimVarys | 4 bytes | Size depends on the zNumDims field if a zVDR (but not present if zero dimensions). Size depends on the rNumDims field of the GDR if an rVDR (but not present if zero dimensions). Offset:340 if an rVDR.  |
| PadValue | Variable Size depends on DataType and NumElems fields. Not present if bit 1 of Flags field is not set. |
