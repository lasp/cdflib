# ISTP Variable Attributes

Variable attributes are linked with and provide additional information about the individual variables. The following tables list all the ISTP variable attributes with examples and requirements based on the ISTP variable type (**_data_**, **_support_data_**, or **_metadata_**; defined by the `VAR_TYPE` attribute value). If a variable type is not listed for an attribute, then that attribute need not be included for that particular variable type; however, if a given variable has an attribute that is not needed, it will be ignored by most of the ISTP compliant applications. **RV** means record or time-varying variable. See [Variable Attribute Definitions](#variable-attribute-definitions) for the full set of defined variable attributes in alphabetical order. Variable attributes can be listed in any order.

Note that attribute names are case sensitive, and the names of the ISTP variable attributes **must match** the case as shown.  Also, for variable attributes with numerical values, the attribute data type **must match** the variable data type. E.g., for a variable of CDF_REAL4 data type, its `FILLVAL`, `VALIDMIN`, `VALIDMAX` attributes must be of CDF_REAL4 data type to enable exact bit matching.

Additional variable attributes may be defined. Their names must start with a letter and can contain letters, numbers, the underscore character, but no other special or Unicode characters. Though attribute names are case sensitive, the names must not be distinguished by case only.


| **Attribute Name** | **NASA Archive Requirement** | **Example Value, <br> Required Data Type** | **Notes** |
| -------------- | ---------------- | ------------- | --------- |
| [`CATDESC`](#catdesc) | Required | `"Electron count rate"` <br> CDF_CHAR | Required for all variables (**_data_**, **_support_data_**, and **_metadata_**). No more than 120, but preferably 80, characters.  |
| [`long_name`](#catdesc) <br> (**netCDF only**) | Required | `"Electron count rate"` <br> CDF_CHAR | All variables.  |
| [`COORDINATE_SYSTEM`](#coordinate_system) (**PROPOSAL ONLY**) | Required | `"GSE"` <br> CDF_CHAR | Vectors, tensors, and individual components.  |
| [`DEPEND_0`](#depend_0) | Required |  `"Epoch"` <br> CDF_CHAR  | **_Data_**, *RV* **_support_data_**, and *RV* **_metadata_**.  |
| [`DEPEND_1`](#depend_i) | Required |  `"Electron_Energy"` <br> CDF_CHAR | **_Data_** of the following form:  1-D *spectrogram*, 1-D *stack_plot*, 2-D *spectrogram*, *image*. |
| [`DEPEND_2`](#depend_i) | Required |  `"Telescope_angle"` <br> CDF_CHAR | **_Data_** of the following form:  2-D *spectrogram*, *image*.  |
| [`DEPEND_3`](#depend_i) | Required | `"Sector_angle"` <br> CDF_CHAR  | **_Data_** of the following form:  3-D *spectrogram*.  |
| [`DISPLAY_TYPE`](#display_type) | Required |  `"time_series"` <br> CDF_CHAR | **_Data_**.|
| [`FIELDNAM`](#fieldnam) | Required |  `"Electron count rate"` <br> CDF_CHAR  | All variables. No more than 50, but preferably 30, characters. |
| [`FILLVAL`](#fillval) | Required |  `-1.0e+31` <br> **Variable data type** | **_Data_**, *RV* **_support_data_**, and *RV* **_metadata_**.  |
| [`_FillValue`](#fillval)  <br> (**netCDF only**) | Required |  `-1.0e+31` <br> **Variable data type** | **_Data_**, *RV* **_support_data_**, and *RV* **_metadata_**.  |
| [`FORMAT`](#format) | Required |  `"F10.1"` <br> CDF_CHAR  | All not using `FORM_PTR`. |
| [`FORM_PTR`](#form_ptr) | Required |  `"formats_E_cnt_rate"` <br> CDF_CHAR | 1-D **_data_**, **_support_data_**, and **_metadata_** not using `FORMAT`. Points to a 1-D string **_metadata_** variable with the same dimension size. |
| [`LABLAXIS`](#lablaxis) | Required | `"E count rate"` <br> CDF_CHAR | **_Data_** of the following form:  *image*, scalar *time_series*, 1-D *spectrogram*. Also needed for **_support_data_** that does not utilize `LABL_PTR_i`. No more than 20, but preferably 10, characters. |
| [`LABL_PTR_1`](#labl_ptr_i) | Required | `"Electron_Energy_Label"` <br> CDF_CHAR  | **_Data_** of the following form: 1-D *Time_series*, 2-D *Spectrogram*. Also needed for 1-D and 2-D **_support_data_** without a `LABLAXIS`. Points to a 1-D string **_metadata_** variable with the same dimension size. |
| [`LABL_PTR_2`](#labl_ptr_i) | Required | `"Telescope_Label"` <br> CDF_CHAR  | **_Data_** of the following form: 2-D *spectrogram*, 3-D *spectrogram*. Also needed for 2-D **_support_data_** without `LABLAXIS`. Points to a 1-D string **_metadata_** variable with the same dimension size. |
| [`LABL_PTR_3`](#labl_ptr_i) | Required | `"Sector_Label"` <br> CDF_CHAR  | **_Data_** of the following form: 3-D *Spectrogram*. Points to a 1-D string **_metadata_** variable with the same dimension size. |
| [`REPRESENTATION_i`](#representation_i) | Cluster Required | `"representation_xyz"`  <br> CDF_CHAR  | **_Data_** vectors and tensors. Points to a 1-D string **_metadata_** variable with the same dimension size.|
| [`TENSOR_FRAME`](#tensor_frame) | Cluster Required | `"GSE"`  <br> CDF_CHAR  | _**Data**_ vectors and tensors.|
| [`TENSOR_ORDER`](#tensor_order) | Cluster Required | `2`  <br> Integer | _**Data**_ vectors and tensors. |
| [`UNITS`](#units) | Required |  `"count/ms` <br> CDF_CHAR | **_Data_** and **_support_data_** not using `UNIT_PTR`. |
| [`units`](#units)  <br> (**netCDF only**) | Required |  `"count/ms` <br> CDF_CHAR | **_Data_** and **_support_data_** not using `UNIT_PTR`. |
| [`UNIT_PTR`](#unit_ptr) | Required |  `"units_E_cnt_rate"` <br> CDF_CHAR | 1-D **_data_** and **_support_data_** not using `UNITS`. Points to a 1-D string **_metadata_** variable with the same dimension size. |
| [`VALIDMIN`](#validmin-validmax) | Required | `0.0` <br> **Variable data type** | **_Data_** and RV **_support_data_**.  |
| [`VALIDMAX`](#validmin-validmax) | Required | `1000.0` <br> **Variable data type** | **_Data_** and RV **_support_data_**.  |
| [`VAR_TYPE`](#var_type) | Required | `"data"` <br> CDF_CHAR | All variables, defines the ISTP variable type. |
| [`DICT_KEY`](#dict_key) | Recommended | `"particle_flux>number_rate"` <br> CDF_CHAR | Recommended for _**data**_ and _**support_data**_ variables; describes the variable using controlled vocabulary. |
| [`FRAME_ORIGIN`](#frame_origin) (**PROPOSAL ONLY**) | Recommended | `"Observatory"`  <br> CDF_CHAR  | _**Data**_ vectors, tensors, and individual components. |
| [`FRAME_VELOCITY`](#frame_velocity) (**PROPOSAL ONLY**) | Recommended | `"Observatory"`  <br> CDF_CHAR  | _**Data**_ vectors, tensors, and individual components. |
| [`SCALETYP`](#scaletyp) | Recommended  |  `"linear"` <br> CDF_CHAR | **_Data_** not using `SCAL_PTR` and **_support_data_**. |
| [`SCAL_PTR`](#scal_ptr) | Recommended  |  `"scales_E_cnt_rate"` <br> CDF_CHAR | 1-D **_data_** not using `SCALETYP`. Points to a 1-D string **_metadata_** variable with the same dimension size. |
| [`sig_digits`](#sig_digits) | Cluster Recommended  | `5` <br> Integer | **_Data_**. |
| [`VAR_NOTES`](#var_notes) | Recommended  | `"Particle Energy mode. Corrected for deadtime. May contain substantial non-electron background."` <br> CDF_CHAR | All variables; unlimited character length. |
| [`AVG_TYPE`](#avg_type) | *Optional* | `"standard"` <br> CDF_CHAR | **_Data_** or RV **_support_data_**. |
| [`DELTA_MINUS` ](#delta_plus-delta_minus) (**PROPOSAL ONLY**) | *Optional* | `5.0` <br> **Variable data type** | **_Data_** or **_support_data_**. |
| [`DELTA_MINUS_VAR`](#delta_plus_var-delta_minus_var)  | *Optional* |  `"E_cnt_rate_DELTA"` <br> CDF_CHAR | **_Data_** or **_support_data_** variables. Points to a  **_support_data_** variable with the same dimension sizes.|
| [`DELTA_PLUS`](#delta_plus-delta_minus) (**PROPOSAL ONLY**) | *Optional*   | `5.0` <br> **Variable data type** | **_Data_** or **_support_data_**. |
| [`DELTA_PLUS_VAR`](#delta_plus_var-delta_minus_var) | *Optional* |  `"E_cnt_rate_DELTA"` <br> CDF_CHAR | **_Data_** or **_support_data_** variables. Points to a  **_support_data_** variable with the same dimension sizes. |
| [`FRAME`](#frame) | *Cluster Optional* | `"vector>gse_xyz"` <br> CDF_CHAR | **Data**. |
| [`LIMITS_WARN_MIN`](#limits_warn_min-limits_warn_max) | *Optional* |  `100.0` <br> **Variable data type** | **_Data_** or *RV* **_support_data_**.  |
| [`LIMITS_WARN_MAX`](#limits_warn_min-limits_warn_max) | *Optional* | `900.0` <br> **Variable data type**  | **_Data_** or *RV* **_support_data_**.  |
| [`LIMITS_NOMINAL_MIN`](#limits_nominal_min-limits_nominal_max) | *Optional* | `200.0` <br> **Variable data type**  | **_Data_** or *RV* **_support_data_**.  |
| [`LIMITS_NOMINAL_MAX`](#limits_nominal_min-limits_nominal_max) | *Optional* | `800.0` <br> **Variable data type**  | **_Data_** or *RV* **_support_data_**.  |
| [`MONOTON`](#monoton) | *Optional* |  `"INCREASE"` | Epoch variables (**_support_data_**). |
| [`SCALEMIN`](#scalemin-scalemax) | *Optional* | `200.0` <br> **Variable data type** | **_Data_** or *RV* **_support_data_**. |
| [`SCALEMAX`](#scalemin-scalemax) | *Optional* | `800.0` <br> **Variable data type** | **_Data_** or *RV* **_support_data_**. |
| [`SI_CONVERSION`](#si_conversion) | *Optional* | `"1.0E3>count/s"`  | **_Data_** or **_support_data_**. |
| [`VARIABLE_PURPOSE`](#variable_purpose) | *Optional* | `"PRIMARY_VAR"` <br> CDF_CHAR | **_Data_**.  |
| [`V_PARENT`](#v_parent) | *Optional* |  `"E_cnt_rate_all"` <br> CDF_CHAR  | **_Data_**.  |



## Variable Attributes for Time Documentation

The attributes in the table below should be used for precise definition of a time variable, and especially for time variables in netCDF with no dedicated time data type. Note that they are **not needed for the CDF_TIME_TT2000 time data type**, internally precisely defined as:
```
TIME_BASE = "J2000"
TIME_SCALE = "Terrestrial Time"
REFERENCE_POSITION = "Rotating Earth Geoid"
UNITS = "ns"
```
See CDF_TIME_TT2000 [requirements analysis](http://cdf.gsfc.nasa.gov/html/leapseconds_requirements.html) and [development approach](http://cdf.gsfc.nasa.gov/html/leapseconds.html) for more details.

| **Attribute** | **NASA Archive Requirement** | **Example Value, <br> Required Data Type** | **Notes** |
| ------------- | ---------------- | ----------- | -------------- |
| [`TIME_BASE`](#time_base) | Recommended (Important for netCDF files and clarity) | `"J2000"` <br> CDF_CHAR | Fixed (`"0 AD"` (used by CDF_EPOCH and CDF_EPOCH16), `"1900"`, `"1970"` (POSIX), `"J2000"` (used by CDF_TIME_TT2000), `"4714 BC"` (Julian)) or `"flexible"` (provider-defined). |
| [`TIME_SCALE`](#time_scale) | Recommended  |  `"TT"` <br> CDF_CHAR | `"TT"` (same as TDT, used by CDF_TIME_TT2000), `"TAI"` (same as IAT, TT-32.184s), `"UTC"` (includes leap seconds), `"TDB"` (same as SPICE ET), `"EME1950"` [default: `"UTC"`]. |
| [`LEAP_SECONDS_INCLUDED`](#leap_seconds_included) | Recommended for UTC only | `"1961JAN01+1.42282s,` ... `,2017JAN01+1s"` <br> CDF_CHAR  | Comma-delimited list of leap seconds.  |
| [`ABSOLUTE_ERROR`](#absolute_error) | *Optional* | `0.3` <br> **Variable data type** | Absolute or systematic error, in same units as `UNITS` attribute. |
| [`BIN_LOCATION`](#bin_location) | *Optional* | `0.5` <br> CDF_REAL4, CDF_REAL8, or equivalent  | Relative position of time stamp to the data measurement bin, with `0.0` at the beginning of time bin and `1.0` at the end. Default is `0.5` for the time at the center of the data measurement. |
| [`REFERENCE_POSITION`](#reference_position) | *Optional* | `"Geocenter"` <br> CDF_CHAR | `"Topocenter"` (local), `"Geocenter"`, `"Rotating Earth Geoid"` (used by CDF_TIME_TT2000). |
| [`RELATIVE_ERROR`](#relative_error) | *Optional* |  `0.4` <br> **Variable data type** | Relative or random error, in same units as `UNITS` attribute - to specify the accuracy of the time stamps relative to each other. |
| [`RESOLUTION`](#resolution) | *Optional* | `"1ms"` <br> CDF_CHAR  | Using ISO8601 relative time format, for example: `"1ms"` = 1 millisecond. Resolution provides the smallest change in time that is measured. |
| [`UNITS`](#units) | *Optional* |  `"ns"` <br> CDF_CHAR | SI measurement unit: `"s"`, `"ms"`(milliseconds for CDF_EPOCH variables), `"ns"`(nanoseconds for CDF_TIME_TT2000), `"ps"`(picoseconds for CDF_EPOCH16).  |


## Variable Attribute Definitions

### ABSOLUTE_ERROR
(*Optional*.) Absolute or systematic error, in same units as `UNITS` attribute.

### AVG_TYPE
(*Optional*.) The default averaging technique that should be performed on the data to reduce resolution. If this attribute is not present, standard average, i.e., simple arithmetic mean, is assumed. The value of this attribute can be used with application software. The valid options are listed below:

- `"standard"` - simple arithmetic mean.
- `"angle_degrees"` - "direction" average over 360 deg e.g., average of 5 and 355 is 0 instead of 180.
- `"angle_radians"` - "direction" average over 2 pi.
- `"angle_hour"` - "direction" average over local times (hours), e.g., average of 2 and 22 is 0 instead of 12.
- `"RMS"` - square root of the average of the squares of the values.
- `"log"` - logarithm of the average of the anti-logarithms of the values.
- `"decibel"` - 10 times the logarithm of the average of the anti-logarithms of the
(values/10).
- `"cosine"` - cosine of the average of the arc-cosines of the values.
- `"none"` - no meaningful averaging calculation is possible.
- `"Geometric"` - anti-logarithm of the average of the logarithms of the values.

### BIN_LOCATION
(*Optional*.) Relative position of time stamp to the data measurement bin, with `0.0` at the beginning of time bin and `1.0` at the end. Default is `0.5` for the time at the center of the data measurement bin. Since clock readings are usually truncated, the real value may be closer to `0.0`.

### CATDESC
(*Required for all variables. **netCDF** additionally requires `long_name` attribute with the same value.*) Catalog description, `CATDESC`, is no more than 120, but preferably 80, characters textual description of the variable, and includes a description of what the variable depends on. This information needs to be complete enough that users can select variables of interest based only on this value. (See, e.g., [CDAWeb web interface](https://cdaweb.gsfc.nasa.gov/)). If necessary, more detailed variable description, including, e.g., caveats or description of all possible values for a flag variable, should be included in the [`VAR_NOTS`](#var_notes) attribute. `CATDESC` examples for different instrument types:

- **Geotail CPI**: `"Ion number density (Solar Wind Analyzer), scalar"`
- **Geotail EPI**: `"Ion Diff. Intensity, at 12 energies 67-1361 keV"`
- **Wind MFI**: `"Magnetic Field, Cartesian GSM coordinates"`
- **Geotail EFD**: `"Electric Field from spherical probe, sunwd \ duskwd comp"`
- **Canopus MPA**: `"42 values of 5577A Intensities from Geodetic Lat 46-67, Long=265"`
- **Canopus MARI**: `"Local Auroral Electrojet index, lower bound (CL), scalar"`

### COORDINATE_SYSTEM
(*Required for vectors, tensors, and individual components*, **PROPOSAL ONLY**.) The name of the coordinate system of a tensor, e.g., `"GSE"`. Same as `TENSOR_FRAME`.


### DELTA_PLUS, DELTA_MINUS
(*Optional*. **PROPOSAL ONLY**.) Similar to `DELTA_PLUS_VAR` and `DELTA_MINUS_VAR`, with the difference that, instead of pointing to variables, `DELTA_PLUS` and `DELTA_MINUS` hold single (+/-) values that apply to all original variable values. `DELTA_PLUS` and `DELTA_MINUS` can also hold 1-D arrays of values (of the same size as the original variable) in case the original variable is a 1-D variable with each value requiring a separate (+/-) pair. **Exact data type match** between the attribute values and the original variable values is also required. Also, see `DELTA_PLUS_VAR` and `DELTA_MINUS_VAR` description on using with time data types.

### DELTA_PLUS_VAR, DELTA_MINUS_VAR
(*Optional*.) The two attributes, always used together, have as their values the names of variables (in the same dataset) which store the uncertainty (or range) of the original variable values. The uncertainty (or range) is stored as a (+/-) on the value of the original variable. In many cases, the original variable will be at the center of the interval, so that only one uncertainty (or range) variable will need to be defined to which both `DELTA_PLUS_VAR` and `DELTA_MINUS_VAR` will point to. See [example of use](07_example-variables.md#example-of-1-d-flux-variable).

 The variables pointed to by `DELTA_PLUS_VAR` and `DELTA_MINUS_VAR` must be of the same dimensionality and the same data type as the original variable, and can be either time-varying or time invariant. In case of the original variable being of a time data type (CDF_TIME_TT2000, CDF_EPOCH, or CDF_EPOCH16), variables pointed to by `DELTA_PLUS_VAR` and `DELTA_MINUS_VAR` should be of the underlying basic data type (CDF_INT8 for CDF_TIME_TT2000 and CDF_REAL8 for both CDF_EPOCH and CDF_EPOCH16).

### DEPEND_0
(*Required for RV variables.*) Explicitly ties a variable to the time variable on which it depends. All variables which change with time must have a `DEPEND_0` attribute defined. The value of `DEPEND_0` is the name of a time variable (time ordering parameter for ISTP), e.g., `"Epoch"`. Different time resolution data variables can be supported in a single dataset by defining multiple time variables, e.g., `Epoch`, `Epoch_1`, `Epoch_2`, etc., each representing a different time resolution. These are attached appropriately to variables in the dataset via their `DEPEND_0` attribute. The value of the attribute must be the name of a variable in the same dataset. See [example of use](07_example-variables.md#example-of-vector-magnetic-field-variable).

### DEPEND_i
(*Required for dimensional variables, as shown in the table above. Note that 1-D **time series** data variables do not need `DEPEND_1`.*) Ties a dimensional **_data_** variable to a **_support_data_** variable on which the i-th dimension of the ***_data_*** variable depends. The number of `DEPEND_i` attributes must match the dimensionality of the variable, i.e., a one-dimensional variable must have a `DEPEND_1`, a two-dimensional variable must have `DEPEND_1` and `DEPEND_2` attributes, etc. The value of the attribute must be the name of a variable in the same dataset. See [example of use](07_example-variables.md#example-of-2-d-flux-variable).

### DICT_KEY
(*Recommended for **data** and **support_data** variables*.) Describes the variable to which it is attached by using keywords from a **controlled dictionary** (either original ISTP dictionary or [SPASE](https://spase-group.org) dictionary). Use of both options is described in [Dictionary Keywords](06_metadata-keywords.md).

### DISPLAY_TYPE
(Required for **_data_** variables.) Tells automated software what type of plot to make and what associated variables in the CDF are required in order to do so. Some valid values are listed below. See [example of use](07_example-variables.md).
- `"time_series"`
- `"spectrogram"`
- `"stack_plot"`
- `"image"`
- `"no_plot"`

### FIELDNAM
(*Required for all variables.*) Holds a short character string (no more than 50, but preferably 30, characters) which names the variable. It can be used to label a plot either above or below the axis, or can be used as a data listing heading. Therefore, consideration should be given to the use of upper- and lower-case letters where the appearance of the output plot or data listing heading will be affected. Note that [`CATDESC`](#catdesc) attribute is used for complete variable description.

### FILLVAL
(*Required for RV variables. **netCDF** additionally requires `_FillValue` attribute with the same value*.) The attribute holds a special value that is used in place of the variable values that are known to be non-valid or missing. The `FILLVAL` attribute data type for each variable **must match** the data type of that variable. The ISTP recommended `FILLVAL` values for different data type are listed below. However, different `FILLVAL` values, and possibly different for different variables of the same data type, may be used as long as for each variable its `FILLVAL` value is outside of the `[VALIDMIN, VALIDMAX]` range for that variable. Additionally, for CDF_REAL4 and CDF_REAL8 data types, `NaN` (IEEE 754) can be used.

Also listed below, but **for information purpose only**, are the default values (for different data type) of the `PadValue` CDF variable property. `PadValue` is used, e.g., to fill allocated variable records when a variable in a CDF file is first created and before the actual data records are written for the variable. `PadValue` is also returned when a variable record outside of the maximum record for the variables is read. The default `PadValue` is set **automatically** by the CDF Library when a CDF variable is created.

| Data Type | FILLVAL| PadValue |
|:--------- | ------:|------:|
| CDF_REAL4 | `-1.0E31` or `NaN` |  `-1.0E30` |
| CDF_REAL8 | `-1.0E31` or `NaN` |  `-1.0E30` |
| CDF_BYTE  | `-128` | `-127` |
| CDF_UINT1 | `255` | `254` |
| CDF_INT2  | `-32768` | `-32767` |
| CDF_UINT2 | `65535` | `65534` |
| CDF_INT4  | `-2147483648` | `-2147483647` |
| CDF_UINT4 | `4294967295` | `4294967294` |
| CDF_INT8  | `-9223372036854775808` | `-9223372036854775807` |

Additionally, the ISTP Guidelines require the following special `FILLVAL` values (and the CDF Library sets default `PadValue` values) for variables of the three time types defined in CDF. The shown Input/Output String is the time sting (ISO 8601) corresponding to the stored `FILLVAL` or `PadValue` value. Note that for the time types defined in CDF, corresponding CDF Library functions **must be used** for converting between values and the string representations.

| Time Type | FILLVAL, PadValue| Stored Value  | Input/Output String  |
| :------------------ | :----------------- | ----------------------: | :-------------------------------- |
| CDF_TIME_TT2000   | `FILLVAL`   | `-9223372036854775808`  | `"9999-12-31T23:59:59.999999999"`  |
|          | `PadValue`  | `-9223372036854775807`  | `"0000-01-01T00:00:00.000000000"`  |
| CDF_EPOCH    | `FILLVAL`   |             `-1.0E31`   | `"9999-12-31T23:59:59.999"`        |
|          | `PadValue`  |                 `0.0`   | `"0000-01-01T00:00:00.000"`        |
| CDF_EPOCH16  | `FILLVAL`   |    `-1.0E31`, `-1.0E31` | `"9999-12-31T23:59:59.999999999999"` |
|          | `PadValue`  |            `0.0`, `0.0`  | `"0000-01-01T00:00:00.000000000000"` |

### FORMAT
(*Required for all variables not using `FORM_PTR`*.) Is the output format used when extracting data values out to a file or screen (e.g., using CDFlist utility of CDF Library). The magnitude and the number of significant figures needed should be carefully considered. A good check is to consider it with respect to the values of `VALIDMIN` and `VALIDMAX` attributes. The output should be in Fortran format, i.e., `"I10"` for an integer or `"F10.3"` for a floating-point data type.

### FORM_PTR
(*Required for dimensional variables not using `FORMAT`*.) `FORM_PTR` is used instead of `FORMAT` when one format string is not sufficient for a dimensional variable. Its value is the name of a variable (in the same dataset) of the same dimensionality as the original variable, which stores the character strings representing the desired output formats for the original variable.

### FRAME

(*Cluster optional*.) Optional and partially redundant with the more powerful description provided by the three concepts `TENSOR_ORDER`, `REPRESENTATION_i`, and `TENSOR_FRAME`.

### FRAME_ORIGIN

(*Recommended for vectors, tensors, and individual components*. **PROPOSAL ONLY**.). Identifies the location of the coordinate system origin (e.g., `"Observatory"`) if different from that implied by the value in `COORDINATE_SYSTEM`.

### FRAME_VELOCITY

(*Recommended for vectors, tensors, and individual components.* **PROPOSAL ONLY**.). Identifies the motion of the coordinate system origin (e.g., `"Observatory"`) if different from that implied by the value in `COORDINATE_SYSTEM`.

### LABLAXIS
(*Required, as shown in the table above, not using `LABL_PTR_1`*.) Should be a short string (no more than 20, but preferably 10, characters), which can be used to label the y-axis for a plot or to provide a heading for a data listing. Note that the units strings are included separately via the `UNITS`/`UNIT_PTR` attributes.

### LABL_PTR_i
(*Required for dimensional variables, as shown in the table above, not using `LABLAXIS`*.) Is used to label a dimensional variable when one value of `LABLAXIS` is not sufficient to describe the variable or to label all the axes. `LABL_PTR_i` is used instead of `LABLAXIS`, where `i` can be from 1 to the total number of dimensions of the original variable. E.g., the value of `LABL_PTR_1` is the name of a variable (in the same dataset) which holds a 1-D array of character strings corresponding to the first dimension of the original variable. The actual labels should be short as described above for `LABLAXIS`. See [example of use](07_example-variables.md#example-of-a-2d-sizes-2812-data-variable).

### LEAP_SECONDS_INCLUDED
(*Recommended for UTC only.*) A comma-delimited list of times when leap seconds were added, appended with each leap second size [default: standard list of leap seconds up to time of data]. `LEAP_SECONDS_INCLUDED` is needed to account for time scales that don't have all 37 (in 2022) leap seconds and for the clocks in various countries that started using leap seconds at different times. The full list is required to handle the equally or more common case where a time scale starts at a specific Universal Time Coordinate (UTC) but continues on without leap seconds in TAI mode; this is basically what missions that don't add leap seconds are doing.

```
LEAP_SECONDS_INCLUDED="1961JAN01+1.42282s,1961AUG01-0.05s,1962JAN01+0.47304s,1963NOV01+0.1s,1964JAN01+1.29427s,1964APR01+0.1s,1964SEP01+0.1s,1965JAN01+0.1s,1965MAR01+0.1s,1965JUL01+0.1s,1965SEP01+0.1s,1966JAN01+0.47304s,1968FEB010.1s,1972JAN01+5.78683s,1972JUL01+1s,1973JAN01+1s,1974JAN01+1s,1975JAN01+1s,1976JAN01+1s,1977JAN01+1s,1978JAN01+1s,1979JAN01+1s,1980JAN01+1s,1981JUL01+1s,1982JUL01+1s,1983JUL01+1s,1985JUL01+1s,1988JAN01+1s,1990JAN01+1s,1991JAN01+1s,1992JUL01+1s,1993JUL01+1s,1994JUL01+1s,1996JAN01+1s,1997JUL01+1s,1999JAN01+1s,2006JAN01+1s,2009JAN01+1s,2012JUL01+1s,2015JUL01+1s,2017JAN01+1s"
```

### LIMITS_NOMINAL_MIN, LIMITS_NOMINAL_MAX
(*Optional*.) Values which define the range of nominal operations, and where values outside the range should be flagged as warnings (often referred to as yellow
limits). Visualization software can use these attributes for indicating limits on plots or other warnings. The range of `LIMITS_NOMINAL_MIN` and `LIMITS_NOMINAL_MAX` fall within the range of `LIMITS_WARN_MIN` and `LIMITS_WARN_MAX` (often referred to as red limits). Yellow limits are often set a certain percentage away from the red limits to give the operator a chance to respond before the red limits are reached. The attribute data type must match the data type of the variable.

### LIMITS_WARN_MIN, LIMITS_WARN_MAX
(*Optional*.) Values which define the limits where damage is likely to occur for values outside of this range (often referred to as red limits). Visualization software can use these attributes for indicating limits on plots or other warnings. The attribute data type must match the data type of the variable.

### MONOTON
(*Optional*.) Indicates whether the variable is monotonically increasing or monotonically decreasing. Use of `MONOTON` is strongly recommended for Epoch/time variables, and it can significantly increase the data retrieval speed. Valid values: `"INCREASE"` and `"DECREASE"`.

### RELATIVE_ERROR
(*Optional*.) Relative or random error (in same units as `UNITS` attribute) - to specify the accuracy of the time stamps relative to each other. This is usually much smaller than `ABSOLUTE_ERROR`.

### REFERENCE_POSITION
(*Optional*.) Used to account for time variance with position in the gravity wells and with relative velocity. E.g, `"Topocenter"` (local), `"Geocenter"`, `"Rotating Earth Geoid"` (used by CDF_TIME_TT2000). While we could use a combined `TimeSystem` attribute that defines mission-specific time scales where needed, such as `"UTC-at-STEREO-B"`, it is cleaner to keep them separate as `TIME_SCALE = "UTC"` and `REFERENCE_POSITION = "STEREO-B"`.

### REPRESENTATION_i
(*Cluster required for vectors and tensors*.) Points to a 1-D metadata variable holding string representations of the i-th dimension of the data variable, e.g., [`"x"`,`"y"`,`"z"`] for Cartesian components in the x-y-z order, [`"r"`,`"p"`,`"t"`] for spherical polar, [`"r"`,"`p`",`"z"`] for cylindrical polar. Number of `REPRESENTATION_i` attributes must match the number of dimensions of the data variable. When `REPRESENTATION_i` is used, labels for tensor components are created by concatenating to the `LABLAXIS` value the corresponding value in the variable pointed to by `REPRESENTATION_i`, e.g., `"Vx"`, `"Vy"`, `"Vz"` for a 1-D vector (using `LABLAXIS = "V"` and `REPRESENTATION_1` pointing to a variable holding [`"x"`,`"y"`,`"z"`]) or `"Pxx"`, `"Pxy"`, `"Pxz"`, `"Pyx"`, etc., for a tensor of order 2 (using `LABLAXIS = "P"` and both `REPRESENTATION_1` and `REPRESENTATION_2` pointing to a variable holding [`"x"`,`"y"`,`"z"`]).

### RESOLUTION
(*Optional*.) Using ISO8601 relative time format, e.g. `"1s"`. Resolution provides the smallest change in time that is measured.

### SCALEMIN, SCALEMAX
(*Optional*.) Minimum/maximum values which can be based on the actual values of data found in the dataset or on the probable uses of the data, e.g., plotting multiple files at the same scale. Visualization software can use these attributes as defaults for plotting. The attribute data type must match the data type of the variable.

### SCALETYP
(*Recommended for **data** not using `SCAL_PTR` and for **support_data***.) Indicates whether the variable should have a `"linear"` or a `"log"` scale as a default.

### SCAL_PTR
(*Recommended for dimensional **data** not using `SCALETYP`*.) Used for dimensional variables when one value of `SCALTYP` is not sufficient. `SCAL_PTR` is used instead of `SCALTYP`, and will point to a variable which will be of the same dimensionality as the original variable. The allowed values are `"linear"` and `"log"`. The value of the attribute must be the name of a variable in the same dataset.

### SI_CONVERSION
(*Optional*.) The multiplicative factor for converting `UNITS` value into International System of Units (SI) units. The factor is expressed in the form `"number>x"`, where `number` is a numerical value and `x` is the appropriate SI units. The basic SI units are: m (meter), N (newton), kg (kilogram), Pa (pascal), s (second), Hz (hertz), A (ampere), V (volt), K (kelvin), W (watt), rad (radian), J (joule), sr (steradian), C (coulomb), T (tesla), ohm (ohm), mho (mho or seimens), H (henry), and F (farad). Two useful units which are not SI units are: degree (angle), and unitless (no units). An example is `"1e-9>T"` which converts the units of magnetic field data expressed in nT to T. Another example is `"1E+3>m/s"`, which converts a velocity expressed in km/s to m/s.

### sig_digits
(*Cluster recommended*.) This attribute provides the number of significant digits or other measure of data accuracy in a TBD manner. It is to allow compression software to optimize the number of digits to retain, and users to assess the accuracy of products. This operation is subject to the deliberations of the 'network traffic report' Task Group, DS-CFC-TN-0001, on compression algorithms and implementation. Restrictions on data compression may also influence the format and choice of data type used by the CDF generation software.

### TENSOR_FRAME
(*Cluster required for vectors and tensors*.) The name of the frame (coordinate system) of a tensor, e.g., `"GSE"`.

### TENSOR_ORDER
(*Cluster required for vectors and tensors*.) The order of a tensor, i.e. `1` for a vector, `2` for a 3x3 tensor.


### TIME_BASE
(*Recommended for time variables, important for **netCDF** files and clarity.*) Fixed: `"0 AD"` (used by CDF_EPOCH and CDF_EPOCH16), `"1900"`, `"1970"` (POSIX), `"J2000"` (used by CDF_TIME_TT2000), `"4714 BC"` (Julian), or `"flexible"` (provider-defined).

### TIME_SCALE
(*Recommended for time variables.*) `"TT"` (same as TDT, used by CDF_TIME_TT2000), `"TAI"` (same as IAT, TT-32.184s), `"UTC"` (includes leap seconds), `"TDB"` (same as `"SPICE ET"`), `"EME1950"`. Default: `"UTC"`.

### UNITS
(*Required for **data** and **support_data** not using `UNIT_PTR`, optional for time variables. **netCDF** additionally requires `units` attribute with the same value.*) Is a short string (no more than 20, but preferably 10, characters) representing the units of the variable, *e.g.,* `"nT"` for magnetic field. If the standard abbreviation used is short then the units value can be added to a data listing heading or plot label. Use a blank character `" "`, rather than "None" or "unitless", for variables that have no units (e.g., a ratio or a direction cosine). For time variables, `UNITS = "ns"` (nanoseconds) for CDF_TIME_TT2000 type, `UNITS = "ms"` (milliseconds) for CDF_EPOCH type, and `UNITS = "ps"` (picoseconds) for CDF_EPOCH16 type.

### UNIT_PTR
(*Required for **data** and **support_data** not using `UNITS`*) Points to a variable (in the same dataset) which stores short strings (no more than 20, but preferably 10, characters) representing the units of the original variable, which can be added to a data listing heading or plot label. Use a blank character, rather than "None" or "unitless", for variables that have no units (e.g., a ratio or a direction cosine). If this attribute is used, then `UNITS` is not used.

### VALIDMIN, VALIDMAX
(*Required for RV **_data_** and **_support_data_**.*) Hold values which are, respectively, the minimum and maximum valid values for a particular variable that are expected over the lifetime of the mission (**not** individual files). The value data types must match the data type of the variable.

### VAR_NOTES
(*Optional*.) Holds additional information about the variable, caveats, or references to related algorithms, models, and software. (Note: use `TEXT` global attribute for all information related to the whole dataset and for very long variable descriptions.) For a quality flag variable, this attribute should include complete description of all flag values, while the flag value corresponding to the science quality data can also be included in the `UNITS` attribute, e.g., `UNITS = "0=good"`.

### VAR_TYPE
(*Required for all variables.*) Identifies ISTP variable type as either:

- `"data"` - plottable variables of integer or real type (used in CDAWeb and similar software in the list of variables to select from for processing or display).
- `"support_data"` - support (attached to **data**) variables of integer or real type.
- `"metadata"` - labels or other character type variables.
- `"ignore_data"` - variables to be ignored by applications/APIs.


### VARIABLE_PURPOSE
(*Optional*.) List of **free text** tags/keywords separated by commas that indicate probable uses of the variable and its function. Software can use this attribute to find the primary variables in the dataset, find variables with a common function, indicate variables suitable for specific purposes such as summary plots or educational displays, etc. Tags could indicate a common geophysical quantity to enable matching several variables of the same kind. For instance, all magnetic field variables could be tagged with `VARIABLE_PURPOSE = "Magnetic_Field"` even though they have different coordinate systems or cadences. Software could use this tag to identify variables with a common theme for easier distinguishing between groups of variables and selecting between them. Suggested tags/keywords include:

- `"PRIMARY_VAR"` - one of the primary variables in the dataset.
- `"EDUCATION"`  - one of the variables suitable for displaying in an educational context.
- `"SUMMARY"` - one the variables to display on automatic summary plots.
- `"CARTESIAN"`, `"ANGULAR"` - distinguish variables by coordinate system.
- `"Magnetic_Field"`, `"Electric_Field"`, etc. - common instrument tag to relate similar variables.

### V_PARENT
(*Optional, for use with derived variables.*) Points to a variable which stores the parent variables (including variables from different files/datasets) of a derived variable. The pointed to variable can be dimensional and sized to hold as many parents as necessary. The syntax of each value would be a string in the form `Logical_file_id>variable_name`.

---
Return to [Table of Contents](../README.md)
