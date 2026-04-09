### 2.13 Unused Internal Record

Internal records in the dotCDF file of a CDF may become unused due to a number of reasons. When that occurs, the internal record is marked as being unused and is placed on a double-linked list of Unused Internal Records (UIRs). The UIRhead field of the GDR contains the file offset of the first UIR. The first UIR contains the file offset of the next UIR and so on. The last UIR contains a file offset of 0x00000000 as the file offset of the next UIR (to indicate the end of the UIRs). Likewise, the last UIR contains the file offset of the previous UIR and so on. The first UIR contains a file offset of 0x00000000 as the file offset of the previous UIR (to indicate the start of the UIRs).

Each UIR contains the following contiguous fields...

RecordSize Signed 8-byte integer, big-endian byte ordering.
The size in bytes of this UIR (including this field).

RecordType Signed 4-byte integer, big-endian byte ordering.
The value -1, which identifies this as a UIR. (See the section on UUIRs below for a slight
complication.)

NextUIR Signed 8-byte integer, big-endian byte ordering.
The file offset of the next UIR. The last UIR will contain a file offset of 0x00000000 in this
field (to indicate the end of the UIRs).

PrevUIR Signed 8-byte integer, big-endian byte ordering. The file offset of the previous UIR. The first UIR will contain a file offset of 0x00000000 in this field (to indicate the start of the UIRs). Remainder Zero or more unused bytes, which constitute the remainder of the UIR. The contents of this field are undefined.


| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | Offset:0 |
| RecordType | 4 bytes | Offset:8 |
| NextUIR | 8 bytes | Offset:12 |
| PrevUIR | 8 bytes | Offset:20 |
| Remainder | variable | Offset:28. Size depends on the size of this UIR. |



It is possible to have internal records in the dotCDF file of a CDF that are unused but are not considered UIRs. Let's call them Unsociable Unused Internal Records (UUIRs) because they are not on the double-linked list of UIRs that begins at the file offset contained in the UIRhead field of the GDR. Beginning with CDF V2.5, UUIRs may also exist due to special circumstances (e.g., if an internal record that is no longer needed is less than 16 bytes which means that it is too small to be made a UIR).

Each UUIR contains the following contiguous fields...

RecordSize - Signed 8-byte integer, big-endian byte ordering. The size in bytes of this UUIR (including this field).

RecordType - Signed 4-byte integer, big-endian byte ordering. The value -1, which identifies this as a UUIR. Unfortunately this is the same value as that used for UIRs. UUIRs are distinguished from UIRs by the fact that they are not on the double-linked list of UIRs.

Remainder - Zero or more unused bytes that constitute the remainder of the UUIR. The contents of this field are undefined.


| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | Offset:0 |
| RecordType | 4 bytes | Offset:8 |
| Remainder | variable | Offset:12. Size depends on the size of this UUIR. |
