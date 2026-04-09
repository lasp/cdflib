### 2.9 Compressed CDF Record

A Compressed CDF Record (CCR) is used to store the data from a compressed single-file CDF. A CCR is created when the whole CDF is compressed. It will not be created if only variables (some or even all) are compressed. Only two internal records exist in a fully compressed CDF. Other than a CCR, another record is a Compression Parameters Record (CPR), which is pointed to by the CCR. The CPR provides the compression information, e.g., compression method and level, etc., used to compress the CDF file. A CCR will not exist in multi-file CDFs.

Each CCR contains the following contiguous fields...

RecordSize - Signed 8-byte integer, big-endian byte ordering. The size in bytes of this CCR (including this field).

RecordType - Signed 4-byte integer, big-endian byte ordering. The value 10, which identifies this as a CCR.

CPRoffset - Signed 8-byte integer, big-endian byte ordering. File offset to the Compressed Parameters Record (CPR) (bytes).

uSize - Signed 8-byte integer, big-endian byte ordering. Size of the CDF in its uncompressed form. This byte count does NOT include the 8-byte magic numbers, and 16-byte checksum if it exists.

rfuA - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Set to zero.

data - The compressed CDF data begins.

Below is a table of byte offsets in the CCR.

| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | Offset:0 |
| RecordType | 4 bytes | Offset:8 |
| CPRoffset | 8 bytes | Offset:12 |
| uSize | 8 bytes | Offset:20 |
| rfuA | 4 bytes | Offset:28 |
| data | variable | Offset:32. Compressed data size is RecordSize - 32 bytes. |
