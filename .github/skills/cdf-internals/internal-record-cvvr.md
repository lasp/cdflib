### 2.12 Compressed Variable Values Record

A Compressed Variable Values Record (CVVR) is used to store one section of compressed variable values records (VVRs) for a variable in a single-file CDF. This section of VVRs while uncompressed are contiguous in the physical file or scratch temporary file. CVVRs will not exist in multi-file CDFs.

Each CVVR contains the following contiguous fields...

RecordSize - Signed 8-byte integer, big-endian byte ordering. The size in bytes of this CVVR (including this field).

RecordType - Signed 4-byte integer, big-endian byte ordering. The value 13, which identifies this as a CVVR.

rfuA - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Set to zero.

cSize - Signed 8-byte integer, big-endian byte ordering. Size in bytes of the post-compressed data, which follows.

data - Compressed data.


| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | Offset:0 |
| RecordType | 4 bytes | Offset:8 |
| rufA | 4 byte | Offset:12 |
| cSize | 8 bytes | Offset:16 |
| data | variable | Offset:24. Size is specified in cSize |
