# ISTP Variables

## Variable Types

ISTP Guidelines divide all variables into three types, identified by the value of the[`VAR_TYPE` ](./05_metadata-variable-attributes.md#var_type) variable attribute:
- **_Data_** variables (`VAR_TYPE = "data"`) of primary importance (e.g., density, magnetic field, particle flux).
- **_Support_data_** variables (`VAR_TYPE = "support_data"`) of secondary importance (e.g., time and energy associated with particle flux).
- **_Metadata_** variables (`VAR_TYPE = "metadata"`) used for labeling dimensional data (e.g., a variable holding  string array [`"Bx GSE"`,`"By GSE"`,`"Bz GSE"`] for labeling vector magnetic field).

Examples of **_data_** and **_support_data_** variables commonly found in ISTP datasets are shown below. They are mapped to their corresponding dimensions and sizes in CDF (and could be in netCDF and other structured file formats).

<p align="center">
    <img width=550 src="./_images/CDF_Planning.gif"/>
</p>

- `DENSITY` and `TEMPERATURE` (**_data_**) are scalars; in CDF they are associated with zero dimensions and no size.
- `VELOCITY`, `ELECTRIC_FIELD` and `MAGNETIC_FIELD` (**_data_**) are vectors, i.e., three orthogonal components in some coordinate system, stored as 1-D variables of size 3.
- `FLUX` has values at eight energy channels. `FLUX` (**_data_**) and `ENERGY` (**_support_data_**) are stored as 1-D variables of size 8.
- The `IMAGE` array (**_data_**) maps into a 2-D variable with sizes 256 and 256. `LATITUDE` and `LONGITUDE` (**_support_data_**) are 1-D variables of size 256, providing the necessary coordinates for the `IMAGE` array.

Each ISTP variable type is defined with CDF (or netCDF) specifications and required attributes. **_Data_** variables also have attached variables for time and dependencies (**_support_data_**) and for labels (**_metadata_**). **_Support_data_** variables can be attached to **_data_** variables via, e.g., the **_data_** variable's `DEPEND_i` attributes, with `DEPEND_0` always pointing (by name) to a time variable. **_Metadata_** variables can be attached to **_data_** variables via, e.g., **_data_** variable's `LABL_PTR_i`, `UNIT_PTR`, `FORM_PTR`,  `SCAL_PTR` attributes.

An ISTP dataset usually spans over many files, over which the dataset definitions must remain static, meaning that **variables cannot be added or removed, or have their data types, number of dimensions, dimension sizes, or variances within records and dimensions changed.** When defining record or dimension variances of a variable, the whole dataset life, and not just a particular file, must be considered. Similarly, the variable dimensions must be defined with the maximum sizes expected over the dataset life, with currently unused values filled with the `FILLVAL` attribute value. There also must be no duplication of data over all dataset files, with all files seamlessly concatenating into one whole dataset.

(_**CDF-specific**_.) If extremely rare changes occur in the variable values over time, a CDF variable can be defined with **record sparseness set to previous record**. In this case, only records with changes need to be explicitly written into the CDF file, while reading any record will return the last explicitly written record before the requested one. See the [CDF User's Guide](https://spdf.gsfc.nasa.gov/pub/software/cdf/doc/cdf_User_Guide.pdf) for details on CDF variable sparse records. Alternatively, a rarely changing variable can have all records written, but variable compression should be enabled in this case. Variable compression should also be enabled for large size variables, while file-level compression is generally discouraged since reading is slower. Note that for efficient data access, time variables should **never** be compressed.

 Each variable in a dataset must have a unique name that **starts with a letter and can contain numbers, underscores, but no other special characters**. Variable names are case sensitive, but the names must never be distinguished by case only. This enables broad support across many programming languages and analysis packages. Variable names should also carry sufficient information for initial understanding of their meaning by a dataset user and for clear distinguishing between different variables. **Otherwise, the ISTP Guidelines do not prescribe a specific scheme for variable naming**.

 The variable names are used by CDF/netCDF files internally but generally not visible to a user. `FIELDNAM` variable attribute is used for user-friendly name for a variable/parameter, while `CATDESC` holds longer and more complete variable description, particularly used for distinguishing between different variables. Additional information for a variable can be stored in the `VAR_NOTES` attribute. `LABLAXIS`/`LABL_PTR_i` are used for plot labeling, and they do not include units, which are stored in the separate `UNITS` attribute also displayed in the plots.

### Data Variables

**_Data_** variables are variables of primary importance (e.g., density, magnetic field, particle flux). **_Data_** variables are almost always of either a floating-point or integer data type, almost always time (record) varying, and can be a scalar or an array of values of up to 10 dimensions. Note that floating-point and integer data type variables are always defined as having one element at each variable value.

For a **_data_** variable, the following variable attributes are required:

- [`CATDESC`](./05_metadata-variable-attributes.md#catdesc)
- [`DEPEND_0`](./05_metadata-variable-attributes.md#depend_0) = `"Epoch"` (time data type variable)
- [`DEPEND_i`](./05_metadata-variable-attributes.md#depend_i)
- [`DISPLAY_TYPE`](./05_metadata-variable-attributes.md#display_type) (`"time_series"`, `"spectrogram"`, `"stack_plot"`,`"image"`)
- [`FIELDNAM`](./05_metadata-variable-attributes.md#fieldnam)
- [`FILLVAL`](./05_metadata-variable-attributes.md#fillval)
- [`FORMAT`](./05_metadata-variable-attributes.md#format)/[`FORM_PTR`](./05_metadata-variable-attributes.md#form_ptr)
- [`LABLAXIS`](./05_metadata-variable-attributes.md#lablaxis)/[`LABL_PTR_i`](./05_metadata-variable-attributes.md#labl_ptr_i)
- [`UNITS`](./05_metadata-variable-attributes.md#units)/[`UNIT_PTR`](./05_metadata-variable-attributes.md#unit_ptr)
- [`VALIDMIN`](./05_metadata-variable-attributes.md#validmin-validmax)
- [`VALIDMAX`](./05_metadata-variable-attributes.md#validmin-validmax)
- [`VAR_TYPE`](./05_metadata-variable-attributes.md#var_type) = `"data"`


Note that need for `DEPEND_i` (other than `DEPEND_0`) and either `LABLAXIS` or `LABL_PTR_i` depends on the data itself and how it will be displayed.

See examples of [**_data_** variable definitions and their displays](./07_example-variables.md#data-variables). **Additional display examples are available at [CDAWeb](https://cdaweb.gsfc.nasa.gov/about.html)**.



### Support_Data Variables

**_Support_data_** variables are variables of secondary importance holding numerical data, e.g., time or energy associated with particle flux. A **_support_data_** variable is always of either a floating-point or integer data type (including CDF time data types). It can be either time (record) invariant or time varying. An epoch (time) **_support_data_** variable attached to a **_data_** variable via `DEPEND_0` attribute  must have the same number of records as the **_data_** variable. If a **_support_data_** variable is attached to a **_data_** variable via `DEPEND_i` (`i > 0`), it must be of the same size as the corresponding dimension of the **_data_** variable. Also note that floating-point and integer data type variables are always defined as having one element at each variable value.

For a **_support_data_** variable, the following variable attributes are required:
- [`CATDESC`](./05_metadata-variable-attributes.md#catdesc)
- [`DEPEND_0`](./05_metadata-variable-attributes.md#depend_0) = `"Epoch"` (if time varying)
- [`FIELDNAM`](./05_metadata-variable-attributes.md#fieldnam)
- [`FILLVAL`](./05_metadata-variable-attributes.md#fillval) (if time varying)
- [`FORMAT`](./05_metadata-variable-attributes.md#format)/[`FORM_PTR`](./05_metadata-variable-attributes.md#form_ptr)
- [`LABLAXIS`](./05_metadata-variable-attributes.md#lablaxis)/[`LABL_PTR_i`](./05_metadata-variable-attributes.md#labl_ptr_i)
- [`UNITS`](./05_metadata-variable-attributes.md#units)/[`UNIT_PTR`](./05_metadata-variable-attributes.md#unit_ptr)
- [`VALIDMIN`](./05_metadata-variable-attributes.md#validmin-validmax)
- [`VALIDMAX`](./05_metadata-variable-attributes.md#validmin-validmax)
- [`VAR_TYPE`](./05_metadata-variable-attributes.md#var_type) = `"support_data"`

See examples of [**_support_data_** variable definitions](./07_example-variables.md#support_data-variables).


### Metadata Variables

**_Metadata_** variables are variables of secondary importance holding strings, e.g., a variable holding  array of strings for labeling magnetic field vector components. A **_metadata_** variable is always of a character type and is always time invariant if used to label a **_data_** variable. It can be time-varying only if it is NOT used as a label. If a **_metadata_** variable is attached to a **_data_** variable (via, e.g., `LABL_PTR_i`), it must be of the same size as the corresponding dimension of the **_data_** variable.

(_**CDF-specific**_.) A character data type variable must be defined with the number of elements equal to the maximum number of characters used in its values. For example, the number of elements is `6` in case of a variable holding an array of six-character strings [`"Bx GSE"`,`"By GSE"`,`"Bz GSE"`].

The following variable attributes are required:
- [`CATDESC`](./05_metadata-variable-attributes.md#catdesc)
- [`DEPEND_0`](./05_metadata-variable-attributes.md#depend_0)` = "Epoch"` (if time varying)
- [`FIELDNAM`](./05_metadata-variable-attributes.md#fieldnam)
- [`FILLVAL`](./05_metadata-variable-attributes.md#fillval) (if time varying)
- [`FORMAT`](./05_metadata-variable-attributes.md#format)/[`FORM_PTR`](./05_metadata-variable-attributes.md#form_ptr)
- [`VAR_TYPE`](./05_metadata-variable-attributes.md#var_type) = `"metadata"`

See examples of [**_metadata_** variable definitions](./07_example-variables.md#metadata-variables).



## Required and Recommended Variables

### Epoch (required)
An epoch (time) variable (**_support_data_**) must be included and should be the first variable in each dataset. Each time-varying variable in a dataset depends (via `DEPEND_0` attribute) on an epoch variable. Multiple epoch variables can be included in a dataset allowing time descriptions of variables with different time cadences. An epoch variable must be either monotonically increasing or decreasing, and it is strongly recommended that `MONOTON` variable attribute with either `"INCREASE"` or `"DECREASE"` value is included for each epoch variable. An epoch variable also should not contain `FILLVAL` values; instead, invalid epoch variable records, and the corresponding data variable records, should not be included in the dataset.

CDF includes three time data types:
- CDF_TIME_TT2000: nanoseconds since J2000 in Terrestrial Time as 8-byte signed integer; includes leap seconds and is well-defined; UTC conversion requires an up-to-date leap second table (last value is stored in CDF header as a check).
- CDF_EPOCH: milliseconds since 0AD as 8-byte floating-point number; usually UTC but no leap seconds.
- CDF_EPOCH16: picoseconds since 0AD as two 8-byte floating-point numbers; usually UTC but no leap seconds.

**Note that for CDF_TIME_TT2000, CDF_EPOCH, and CDF_EPOCH16 data types, time encoding and decoding MUST be done using the dedicated [CDF Library](https://cdf.gsfc.nasa.gov/) functions (also in the Python [cdflib](https://github.com/MAVENSDC/cdflib/tree/main) library).**

Since CDF_TIME_TT2000 data type is precisely defined internally (as `TIME_BASE = "J2000"`, `TIME_SCALE = "Terrestrial Time"`, `REFERENCE_POSITION = "Rotating Earth Geoid"`, `UNITS = "ns"`), it does not require explicit [time attribute](./05_metadata-variable-attributes.md#variable-attributes-for-time-documentation) definitions, and **is strongly recommended for new datasets.**

The ISTP Guidelines define the time value of a record as the center of the measurement period, if the measurement is not an instantaneous one. To describe time values that are different from the measurement period center, the epoch variable must include `BIN_LOCATION` attribute with a floating-point value between `0.0` (measurement period beginning) and `1.0` (measurement period end). Such epoch variable should also include description of the time position within measurement period in `VAR_NOTES` attribute and, preferably, also in `CATDESC` attribute. Alternatively, in order to completely describe the measurement periods, and especially in case of time varying measurement periods, `DELTA_PLUS_VAR` and `DELTA_MINUS_VAR` attribute pair can be used.

See examples of [*epoch* variable definitions](./07_example-variables.md#examples-of-epoch-variables).

#### netCDF Times
netCDF files can include the CDF time variables, with CDF_TIME_TT2000 especially recommended, but will require using the CDF library time routines for conversion. Otherwise, netCDF times are typically something like seconds from some specific time epoch, with `UNITS = "seconds from 2000-01-01 UTC"` or similar.  In either case, the ISTP time variable attributes should be added.

### Quality Flag (recommended)

Each dataset should include at least one quality or status flag variable which is time varying. Multiple quality/status flags should be included if **_data_** variables of different cadences are present in the dataset, or if the individual **_data_** variables of the same cadence require separate quality/status flags.

The dataset designer should consider defining quality/status flag variables as **_data_** (instead of **_support_data_**) if they are essential for correct interpretation of the primary **_data_** variables. **_Data_** (as opposed to **_support_data_**) variables are displayed in the list of dataset variables by the Coordinated Data Analysis Web ([CDAWeb)](https://cdaweb.gsfc.nasa.gov/) Display and Retrieval system. They are also always returned by the APIs accessing data from SPDF.

The quality flag may be a set of binary flags, with all zeros as the fully good case. `UNITS` variable attribute might be of the form `"(0=good, 2=off, 4=cal)"`.


###  Time_PB5 (ISTP KP datasets)

(_No longer relevant_.) Time_PB5 is the second variable in an ISTP KP CDF dataset. It is not required for IACG or ISTP higher resolution or event data. Time_PB5 is a way of presenting time as an array of three integers: YEAR, DAY OF YEAR, and MSEC OF DAY. This allows for easy recognition of the time value when looking at the data, for instance in a data dump. See example of [*Time_BP5* and related variable definitions](./07_example-variables.md#example-of-time_pb5-variable).

###  Post Gap Flag (ISTP KP datasets)

(_No longer relevant_.) At the May 1992 ISTP SWG it was decided that a record varying "Post Gap" Quality
Flag would also be included in each KP record. This I*4 Flag is included in every record and is defined in the following way: 0 - no gap occurred immediately prior to this record (thus most of the time this Flag would be set to 0); 1 - the gap occurred because the instrument was not in a mode that allowed for the production of KPs; 2 - the gap occurred because Level Zero or SIRIUS data were missing; 3 - the gap occurred because Level Zero or SIRIUS data were too noisy to compute KPs. Integer numbers above 9 can be used by the PI team to define other gap conditions, as required.

A variable similar to this is recommended for inclusion in CDFs to indicate real and substantial data gaps. The detailed definition of this flag should appear in the CDF metadata in the `VAR_NOTES` attribute.

---
Return to [Table of Contents](../README.md)
