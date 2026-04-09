# GitHub Copilot Instructions for cdflib

This repository contains `cdflib`, a pure Python library for reading and writing NASA Common Data Format (CDF) files. It does not rely on the NASA CDF C library.

## Project Architecture & Core Components

- **Pure Python Implementation**: The core logic uses `numpy` and `struct` to parse binary CDF files. No C extensions are used.
- **Reading (`cdflib/cdfread.py`)**:
  - The `CDF` class is the main entry point for reading.
  - Supports reading from local files, URLs, and S3 buckets.
  - **Key Method**: `CDF.varget(variable_name)` retrieves variable data.
  - **Key Method**: `CDF.cdf_info()` returns global file information.
- **Writing (`cdflib/cdfwrite.py`)**:
  - The `CDF` class in this module is used to create new CDF files.
  - Requires a `cdf_spec` dictionary to define file properties (encoding, majority, etc.).
- **Xarray Integration (`cdflib/xarray/`)**:
  - `cdf_to_xarray`: Converts CDF files to `xarray.Dataset` objects, mapping ISTP attributes to xarray conventions.
  - `xarray_to_cdf`: Converts `xarray.Dataset` objects back to CDF files.
- **Time Handling (`cdflib/epochs.py`)**:
  - `CDFepoch` class handles conversions between CDF time types (CDF_EPOCH, CDF_EPOCH16, TT2000) and Python `datetime`, `numpy.datetime64`, or Unix timestamps.

## Developer Workflows

- **Dependency Management**: Dependencies are defined in `pyproject.toml`.
  - Core: `numpy`
  - Optional/Test: `xarray`, `astropy`, `hypothesis`, `pytest`
- **Testing**:
  - Run tests using `tox` to test across multiple Python versions.
  - Run specific tests with `pytest`: `pytest tests/test_cdfread.py`.
  - Tests are located in the `tests/` directory.
- **Formatting**:
  - The project uses `black` for code formatting and `isort` for import sorting.
  - Configuration is in `pyproject.toml`.

## Coding Conventions & Patterns

- **Type Hinting**: Use Python type hints extensively (e.g., `Union[str, Path]`, `npt.ArrayLike`).
- **Path Handling**: Support both `str` and `pathlib.Path` objects for file paths. Internally, paths are often resolved to strings or `Path` objects.
- **Numpy Usage**: Use `numpy` for all array operations. Avoid explicit loops over data where possible.
- **S3 Support**: When handling S3 paths (`s3://`), use the internal `cdflib.s3` module logic.

## Common Code Examples

### Reading a CDF File
```python
import cdflib
cdf_file = cdflib.CDF('/path/to/file.cdf')
info = cdf_file.cdf_info()
data = cdf_file.varget("VariableName")
```

### Converting to Xarray
```python
from cdflib import cdf_to_xarray
ds = cdf_to_xarray('/path/to/file.cdf', to_datetime=True)
```

### Time Conversion
```python
from cdflib.epochs import CDFepoch
# Convert CDF epoch to datetime
dt = CDFepoch.to_datetime(cdf_epoch_value)
# Convert datetime to CDF epoch
epoch = CDFepoch.compute(dt)
```

### Writing a CDF File
```python
from cdflib.cdfwrite import CDF
spec = {'Majority': 'row_major', 'Encoding': 6} # 6 is IBMPC_ENCODING
with CDF('new_file.cdf', cdf_spec=spec) as cdf:
    cdf.write_globalattrs(global_attrs)
    cdf.write_var(var_spec, var_attrs, var_data)
```

### Rules
NEVER RUN GIT COMMANDS IN THIS REPOSITORY. A human will review all code changes and merge them manually.
