### 2.7 Variable Index Record

Variable Index Records (VXRs) are used in single-file CDFs to store the file offsets of any lower level of VXRs, Variable Values Records (VVRs), or Compressed Variable Value Records (CVVRs). A VXR tree structure is present if a VXR points to another VXR(s). This can happen when a CDF file becomes very fragmented. At the lowest levels, the offsets in VXRs point to VVRs. To make a CDF file cleaner, keep VXRs, and their levels, as few as possible. The best performer is one (1) VXR and one (1) VVR for a variable’s whole records.

VVRs contain a group of records written to a variable and are described in Section 2.8. VXRs (and VVRs) will not exist in the dotCDF file of a multi-file CDF (because the variable records are stored in separate files as described in Chapter 3).

The VXRhead field of a VDR in a single-file CDF contains the file offset of the first VXR for the corresponding variable. The first VXR contains the file offset of the next VXR and so on. As many VXRs as are necessary will exist (depending on the number of VVRs for the variable). The VXRtail field of a VDR contains the file offset of the last VXR for the corresponding variable.

Each VXR contains the following contiguous fields...

RecordSize - Signed 8-byte integer, big-endian byte ordering. The size in bytes of this VXR (including this field).

RecordType - Signed 4-byte integer, big-endian byte ordering. The value 6, which identifies this as a VXR.

VXRnext - Signed 8-byte integer, big-endian byte ordering. The file offset of the next VXR. The last VXR will contain a file offset of 0x0000000000000000 in this field (to indicate the end of the VXRs).

Nentries - Signed 4-byte integer, big-endian byte ordering. The number of index entries in this VXR. This is the maximum number of
VVRs that may be indexed using this VXR. Since using the hierarchical scheme for the VXR indexing in V2.6, the maximum number of entries has been set as 7. Prior version has it as 10.

NusedEntries - Signed 4-byte integer, big-endian byte ordering. The number of index entries actually used in this VXR. First Signed 4-byte integers, big-endian byte ordering within each. This is a contiguous array of variable record numbers with each record number being the first variable record in the corresponding VVR or lower level VXRs. The size of this array depends on the value of the Nentries field. The nth entry in this array corresponds to the nth entry in the Last and Offset fields. Unused entries in this array contain 0xFFFFFFFF. Note that variable records are numbered beginning with zero (0).

Last - Signed 4-byte integers, big-endian byte ordering within each. This is a contiguous array of variable record numbers with each record number being the last variable record in the corresponding VVR or lower level VXRs. The size of this array depends on the value of the Nentries field. The nth entry in this array corresponds to the nth entry in the First and Offset fields. Unused entries in this array contain 0xFFFFFFFF. Note
that variable records are numbered beginning with zero (0).

Offset - Signed 8-byte integers, big-endian byte ordering within each. This is a contiguous array of file offsets with each being the file offset of the corresponding VVR, CVVR or a lower level of VXR. If the offset is pointing to a VXR, the prior, corresponding first/last fields are the record range this VXR tree will hold. The size of this array depends on the value of the Nentries field. The nth entry in this array corresponds to
the nth entry in the First and Last fields. Unused entries in this array contain 0xFFFFFFFFFFFFFFFF.

Below is a table of byte offsets of a VXR.

| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | Offset:0 |
| RecordType | 4 bytes | Offset:8 |
| VXRnext | 8 bytes | Offset:12 |
| Nentries | 4 bytes | Offset:20 |
| NusedEntries | 4 bytes | Offset:24 |
| First | variable | Offset:28. Size depends on the Nentries field. |
| Last | variable | Offset:28+4*Nentries. Size depends on the Nentries field. |
| Offset | variable | Offset:28+8*Nentries. Size depends on the Nentries field. |


Consider the following example VXR contents (for a variable having only one VXR)...

```
RecordSize: 140
RecordType: 6
VXRnext: 0x0000000000000000
Nentries: 7
NusedEntries: 2
First: 0, 100, 0xFFFFFFFF, 0xFFFFFFFF, ...
Last: 99, 149, 0xFFFFFFFF, 0xFFFFFFFF, ...
Offset: 0x000000000000A400, 0x000000000000B554, 0xFFFFFFFFFFFFFFFF,
0xFFFFFFFFFFFFFFFF, ...
```

There are two index entries being used. The first indicates that variable records 0 through 99 are stored in the VVR at
file offset 0x0000A400 and the second indicates that variable records 100 through 149 are stored in the VVR at file
offset 0x0000B554.
