### 2.11 Sparseness Parameters Record

A Sparseness parameters Record (SPR) is used to store sparse array information used by a variable record in a CDF. Currently, it has not yet been implemented in the V2.6, V2.7 or V3.0 distribution. This record is not being implemented.

Each SPR contains the following contiguous fields...

RecordSize - Signed 8-byte integer, big-endian byte ordering. The size in bytes of this SPR (including this field).

RecordType - Signed 4-byte integer, big-endian byte ordering. The value 12, which identifies this as a SPR.

sArraysType - Signed 4-byte integer, big-endian byte ordering. include the magic numbers.

rfuA - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Set to zero.

pCount - Signed 4-byte integer, big-endian byte ordering. Sparseness parameter count.

sArraysParms - Signed 4-byte integer, big-endian byte ordering. Parameters for sparseness arrays.

Below is a table of the SPR byte ordering.

| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | No comments |
| RecordType | 4 bytes | No comments |
| sArraysType | 4 bytes | No comments |
| rufA | 4 bytes | No comments |
| pCount | 4 bytes | No comments |
| sArraysParms | variable Size depends on pCount | No comments |
