### 2.8 Variable Values Record

Variable Value Records (VVRs) are used to store one or more variable records in a single-file CDF. VVRs will not exist in multi-file CDFs (where variable records are stored in separate files). The contents of a variable record are described in Chapter 4.

Each VVR contains the following contiguous fields...

RecordSize - Signed 8-byte integer, big-endian byte ordering. The size in bytes of this VVR (including this field).

RecordType - Signed 4-byte integer, big-endian byte ordering. The value 7, which identifies this as a VVR.

Records - A group of one or more variable records. The record numbers in this group will be contiguous. The size of this field depends on the number of variable records in the group and the size of each record. The size of each record will be the same and depends on the dimensionality, dimension variances, data type, and number of elements per value of the corresponding variable. These properties are discussed in Chapter 4. The encoding of the values in each variable record depends on the encoding of the CDF (which is stored in the Encoding field of the CDR). The possible encodings are described in Chapter 5.

Below is a table of byte offsets in the VVR.


| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | Offset:0 |
| RecordType | 4 bytes | Offset:8 |
| Records | variable | Offset:12. Size depends on the number of variable records in this VVR and the variable's data type, number of elements per value dimensionality, and dimension variances. |
