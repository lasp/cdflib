### 2.10 Compressed Parameters Record

A Compressed Parameters Record (CPR) is used to keep the information as the compression method and level used to create a CDF or variable. This record is pointed to by either a CCR or a VDR. When a compression is applied to the whole CDF, the CPR is pointed to by the CCR. If a compression is only applied to a variable, a CPR is pointed to by a VDR. Currently, only Run-Length Encoding (RLE), Huffman (HUFF), Adaptive Huffman (AHUFF) and GNU GZIP compression algorithms are supported. Due to a huge memory requirement, the GZIP compression is disabled for the PCs running the 16-bit DOS/Windows.

Each CPR contains the following contiguous fields...

RecordSize Signed 8-byte integer, big-endian byte ordering. The size in bytes of this CPR (including this field).

RecordType Signed 4-byte integer, big-endian byte ordering. The value 11, which identifies this as a CPR.

cType - Signed 4-byte integer, big-endian byte ordering. Type of compression: NO_COMPRESSION (0), RLE_COMPRESSION (1),
HUFF_COMPRESSION (2), AHUFF_COMPRESSION (3) and GZIP_COMPRESSION (5)

rfuA - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Set to zero.

pCount - Signed 4-byte integer, big-endian byte ordering. Compression parameter count. Currently, it is 1.

cParms - Signed 4-byte integer, big-endian byte ordering. Compression level. For RLE, HUFF and AHUFF, cParms[0] is 0. For GZIP, it is between 1 and 9.


| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | Offset:0 |
| RecordType | 4 bytes | Offset:8 |
| cType | 4 bytes | Offset:12 |
| rufA | 4 bytes | Offset:16 |
| pCount | 4 bytes | Offset:20 |
| cParms | variable | Offset:24. Size depends on pCount |
