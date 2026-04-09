### 2.3 Global Descriptor Record

All dotCDF files contain a single Global Descriptor Record (GDR) at the file offset contained in the GDRoffset field of
the CDF Descriptor Record (CDR). The GDR contains general information about the CDF (as does the CDR).

The GDR, contains the following contiguous fields...


RecordSize - Signed 8-byte integer, big-endian byte ordering. The size in bytes of this GDR (including this field).

RecordType - Signed 4-byte integer, big-endian byte ordering. The value 2, which identifies this as the GDR.


rVDRhead - Signed 8-byte integer, big-endian byte ordering. The file offset of the first rVariable Descriptor Record (rVDR). The first rVDR contains a file offset to the next rVDR and so on. An rVDR will exist for each rVariable in the CDF. This field will contain 0x0000000000000000 if the CDF contains no rVariables. Beginning with CDF V2.1 the last rVDR will contain a file offset of 0x0000000000000000 for the file offset of the next rVDR (to indicate the end of the rVDRs). Prior to CDF V2.1 the “next VDR” file offset in the last rVDR is undefined. rVDRs are described in Section 2.6.

zVDRhead - Signed 8-byte integer, big-endian byte ordering. The file offset of the first zVariable Descriptor Record (zVDR). The first zVDR contains a file offset to the next zVDR and so on. A zVDR will exist for each zVariable in the CDF. Because zVariables were not supported by CDF until CDF V2.2, prior to CDF V2.2 this field is undefined. Beginning with CDF V2.2 this field will contain either a file offset to the first zVDR or 0x0000000000000000 if the CDF contains no zVariables. The last zVDR will always contain 0x0000000000000000 for the file offset of the next zVDR (to indicate the end of the zVDRs). zVDRs are described in Section 2.6.

ADRhead - Signed 8-byte integer, big-endian byte ordering. The file offset of the first Attribute Descriptor Record (ADR). The first ADR contains a file offset to the next ADR and so on. An ADR will exist for each attribute in the CDF. This field will contain 0x0000000000000000 if the CDF contains no attributes. Beginning with CDF V2.1 the last ADR will contain a file offset of 0x0000000000000000 for the file offset of the next ADR (to indicate the end of the ADRs). Prior to CDF V2.1 the “next ADR" file offset in the last ADR is undefined. ADRs are described in Section 2.4.

eof - Signed 8-byte integer, big-endian byte ordering. The end-of-file (EOF) position in the dotCDF file. This is the file offset of the byte that is one beyond the last byte of the last internal record. (This value is also the total number of bytes used in the dotCDF file.) Prior to CDF V2.1, this field is undefined.

NrVars - Signed 4-byte integer, big-endian byte ordering. The number of rVariables in the CDF. This will correspond to the number of rVDRs in the
dotCDF file.

NumAttr - Signed 4-byte integer, big-endian byte ordering. The number of attributes in the CDF. This will correspond to the number of ADRs in the
dotCDF file.

rMaxRec - Signed 4-byte integer, big-endian byte ordering. The maximum rVariable record number in the CDF. Note that variable record numbers are numbered beginning with zero (0). If no rVariable records exist, this value will be negative one (-1).

rNumDims - Signed 4-byte integer, big-endian byte ordering. The number of dimensions for rVariables.

NzVars - Signed 4-byte integer, big-endian byte ordering. The number of zVariables in the CDF. This will correspond to the number of zVDRs in the
dotCDF file. Prior to CDF V2.2 this value will always be zero (0).

UIRhead - Signed 8-byte integer, big-endian byte ordering. The file offset of the first Unused Internal Record (UIR). The first UIR contains the file offset of the next UIR and so on. The last UIR contains a file offset of 0x0000000000000000 for the file offset of the next UIR (indicating the end of the UIRs).

rfuC - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Always set to zero (0).

LeapSecondLastUpdated - Signed 4-byte integer, big-endian byte ordering. The date of the last entry in the leap second table (in YYYYMMDD form). It is negative one (-1) for the previous version. A value of zero (0) is also accepted, which means a CDF was not created based on a leap second table. This field is applicable to CDFs with CDF_TIME_TT2000 data type.

rfuE - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Always set to negative one (-1).

rDimSizes - Signed 4-byte integers, big-endian byte ordering within each. Zero or more contiguous rVariable dimension sizes depending on the value of the rNumDims field described above.


| Field | Size | Comments |
|-----------|-------------|-------------|
| RecordSize | 8 bytes | Offset:0 |
| RecordType | 4 bytes | Offset:8 |
| rVDRhead | 8 bytes | Offset:12 |
| zVDRhead | 8 bytes | Offset:20 |
| ADRhead | 8 bytes | Offset:28 |
| eof | 8 bytes | Offset:36 |
| NrVars | 4 bytes | Offset:44 |
| NumAttr | 4 bytes | Offset:48 |
| rMaxRec | 4 bytes | Offset:52 |
| rNumDims | 4 bytes | Offset:56 |
| NzVars | 4 bytes | Offset:60 |
| UIRhead | 8 bytes | Offset:64 |
| rfuC | 4 bytes | Offset:72 |
| LeapSecondLastUpdated | 4 bytes | Offset:76 |
| rfuE | 4 bytes | Offset:80 |
| rDimSizes | variable | Offset:84. Size depends on rNumDims field. If zero rVariable dimensions, this field will not be present. |
