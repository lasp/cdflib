import numpy as np
import pytest

from cdflib import CDF, cdfwrite


def test_read(cdf_path):
    cdf = CDF(cdf_path)

    info = cdf.cdf_info()

    # Smoke test variable access
    for var in info.zVariables:
        cdf.varattsget(var)
        cdf.varget(var)

    # Smoke test context manager
    with CDF(cdf_path) as cdf:
        cdf.cdf_info()

    # Smoke test global attributes
    globalatts = cdf.globalattsget()
    for att in globalatts:
        if len(globalatts[att]) > 1:
            # Make sure multiple entries are unique
            assert len(globalatts[att]) == len(set(globalatts[att]))


def test_nonexist_file_errors(tmp_path):
    with pytest.raises(FileNotFoundError, match="not found"):
        CDF(tmp_path / "nonexist.cdf")


def test_nonexist_path_with_extra_suffix_errors(cdf_path):
    # A non-existent path built from a real CDF path plus extra characters
    # must raise instead of silently reading the real file. Previously the
    # ``.cdf`` fallback used ``Path.with_suffix`` which replaces the suffix,
    # so ``<real>.cdfINVALID`` resolved back to ``<real>.cdf`` (GH #328).
    bad_path = str(cdf_path) + "INVALID"
    with pytest.raises(FileNotFoundError, match="not found"):
        CDF(bad_path)
        
def test_varget_no_records(tmp_path):
    # A variable with no written records (max_rec = -1) should return an empty array
    fn = tmp_path / "no_records.cdf"
    with cdfwrite.CDF(fn) as cdf:
        cdf.write_var({"Variable": "Mode", "Data_Type": 11, "Num_Elements": 1, "Rec_Vary": True, "Dim_Sizes": []})
        cdf.write_var({"Variable": "Flux", "Data_Type": 21, "Num_Elements": 1, "Rec_Vary": True, "Dim_Sizes": [3, 2]})

    cdf = CDF(fn)
    assert cdf.vdr_info("Mode").max_rec == -1

    mode = cdf.varget("Mode")
    assert mode.shape == (0,)
    assert mode.dtype == np.uint8

    flux = cdf.varget("Flux")
    assert flux.shape == (0, 3, 2)
    assert flux.dtype == np.float32
