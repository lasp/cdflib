### 2.4 Attribute Descriptor Record

An Attribute Descriptor Record (ADR) contains a description of an attribute in a CDF. There will be one ADR per attribute. The ADRhead field of the GDR contains the file offset of the first ADR.

Each ADR contains the following contiguous fields...

RecordSize - Signed 8-byte integer, big-endian byte ordering. The size in bytes of this ADR (including this field).

RecordType - Signed 4-byte integer, big-endian byte ordering. The value 4, which identifies this as an ADR.

ADRnext - Signed 8-byte integer, big-endian byte ordering. The file offset of the next ADR. Beginning with CDF V2.1 the last ADR will contain a file offset of 0x0000000000000000 in this field (to indicate the end of the ADRs). Prior to CDF V2.1 this file offset is undefined in the last ADR.


AgrEDRhead - Signed 8-byte integer, big-endian byte ordering. The file offset of the first Attribute g/rEntry Descriptor Record (AgrEDR) for this attribute. The first AgrEDR contains a file offset to the next AgrEDR and so on. An AgrEDR will exist for each g/rEntry for this attribute. This field will contain 0x0000000000000000 if the attribute has no g/rEntries. Beginning with CDF V2.1 the last AgrEDR will contain a file offset of 0x0000000000000000 for the file offset of the next AgrEDR (to indicate the end of the AgrEDRs). Prior to CDF V2.1 the “next AgrEDR" file offset in the last AgrEDR is undefined. Note that the term g/rEntry is used to refer to an entry that may be either a gEntry or an rEntry. The type of entry described by an AgrEDR depends on the scope of the corresponding attribute. AgrEDRs of a global-scoped attribute describe gEntries. AgrEDRs of a variable-scoped attribute describe rEntries.

Scope - Signed 4-byte integer, big-endian byte ordering. The intended scope of this attribute. The following internal values are possible...
1 Global scope.
2 Variable scope.
3 Global scope assumed.
4 Variable scope assumed.
Note that assumed scopes only exist prior to CDF V2.5.

Num - Signed 4-byte integer, big-endian byte ordering. This attribute's number. Attributes are numbered beginning with zero (0).

NgrEntries - Signed 4-byte integer, big-endian byte ordering. The number of g/rEntries for this attribute.

MAXgrEntry - Signed 4-byte integer, big-endian byte ordering. The maximum numbered g/rEntry for this attribute. g/rEntries are numbered beginning with zero (0). If there are no g/rEntries, this field will contain negative one (-1).

rfuA - Signed 4-byte integer, big-endian byte ordering. Reserved for future used. Always set to zero (0).

AzEDRhead - Signed 8-byte integer, big-endian byte ordering. The file offset of the first Attribute zEntry Descriptor Record (AzEDR) for this attribute. The first AzEDR contains a file offset to the next AzEDR and so on. An AzEDR will exist for each zEntry for this attribute. This field will contain 0x0000000000000000 if this attribute has no zEntries. The last AzEDR will contain a file offset of 0x0000000000000000 for the file offset of the next AzEDR (to indicate the end of the AzEDRs).

NzEntries - Signed 4-byte integer, big-endian byte ordering. The number of zEntries for this attribute. Prior to CDF V2.2 this field will always contain a value of zero (0).

MAXzEntry - Signed 4-byte integer, big-endian byte ordering. The maximum numbered zEntry for this attribute. zEntries are numbered beginning with zero (0). Prior to CDF V2.2 this field will always contain a value of negative one (-1).

rfuE - Signed 4-byte integer, big-endian byte ordering. Reserved for future use. Always set to negative one (-1).

Name - Character string, ASCII character set. The name of this attribute. This field is always 256 bytes in length. If the number of characters in the name is less than 256, a NUL character (0x00) will be used to terminate the string. In that case, the characters beyond the NUL-terminator (up to the size of this field) are undefined.


Below is a table describing the byte ordering of the ADR.

| Field | Size | Comments |
|--------|--------|---------------|
| RecordSize | 8 bytes | Offset:0 |
| RecordType | 4 bytes | Offset:8 |
| ADRnext | 8 bytes | Offset:12 |
| AgrEDRhead | 8 bytes | Offset:20 |
| Scope | 4 bytes | Offset:28 |
| Num | 4 bytes | Offset:32 |
| NgrEntries | 4 bytes | Offset:36 |
| MAXgrEntry | 4 bytes | Offset:40 |
| rfuA | 4 bytes | Offset:44 |
| AzEDRhead | 8 bytes | Offset:48 |
| NzEntries | 4 bytes | Offset:56 |
| MAXzEntry | 4 bytes | Offset:60 |
| rfuE | 4 bytes | Offset:64 |
| Name | 256 bytes | Offset:68. Was 64 bytes in earlier V2. |
