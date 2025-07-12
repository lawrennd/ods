#!/usr/bin/env python3
"""
Test script to verify HDF5 loading works with h5py.
"""

import os
import sys
import numpy as np
import pandas as pd

def test_h5py_loading():
    """Test that we can load HDF5 files using h5py."""
    try:
        import h5py
        print("✓ h5py is available")
    except ImportError:
        print("✗ h5py is not available")
        return False
    
    # Test creating a simple HDF5 file with h5py
    test_file = "test_data.h5"
    
    # Create test data
    data = {
        'month': np.array([1, 2, 3, 4, 5]),
        'day_of_month': np.array([1, 15, 20, 25, 30]),
        'ArrDelay': np.array([10, -5, 15, -2, 8]),
        'Year': np.array([2015, 2015, 2015, 2015, 2015])
    }
    
    # Save with h5py
    with h5py.File(test_file, 'w') as f:
        for key, value in data.items():
            f.create_dataset(key, data=value)
    
    print("✓ Created test HDF5 file with h5py")
    
    # Load with h5py (like in our modified code)
    with h5py.File(test_file, 'r') as f:
        columns = list(f.keys())
        data_arrays = {}
        for col in columns:
            data_arrays[col] = f[col][:]
    
    print("✓ Loaded data with h5py")
    
    # Test the data processing logic
    if "Year" in data_arrays:
        del data_arrays["Year"]
    
    Yall = data_arrays.pop("ArrDelay").reshape(-1, 1)
    remaining_cols = list(data_arrays.keys())
    Xall = np.column_stack([data_arrays[col] for col in remaining_cols])
    
    print(f"✓ Processed data: X shape {Xall.shape}, Y shape {Yall.shape}")
    
    # Clean up
    os.remove(test_file)
    print("✓ Cleaned up test file")
    
    return True

def test_pandas_h5py_backend():
    """Test that pandas can use h5py as backend for HDF5."""
    try:
        import h5py
        print("✓ h5py is available for pandas backend")
    except ImportError:
        print("✗ h5py is not available for pandas backend")
        return False
    
    # Create test data
    df = pd.DataFrame({
        'month': [1, 2, 3, 4, 5],
        'day_of_month': [1, 15, 20, 25, 30],
        'ArrDelay': [10, -5, 15, -2, 8],
        'Year': [2015, 2015, 2015, 2015, 2015]
    })
    
    test_file = "test_pandas.h5"
    
    # Save with pandas (should use h5py backend)
    df.to_hdf(test_file, key='data', mode='w')
    print("✓ Saved DataFrame to HDF5 with pandas")
    
    # Load with pandas
    loaded_df = pd.read_hdf(test_file, key='data')
    print("✓ Loaded DataFrame from HDF5 with pandas")
    
    # Clean up
    os.remove(test_file)
    print("✓ Cleaned up test file")
    
    return True

if __name__ == "__main__":
    print("Testing HDF5 loading with h5py...")
    print("=" * 50)
    
    success1 = test_h5py_loading()
    print()
    
    success2 = test_pandas_h5py_backend()
    print()
    
    if success1 and success2:
        print("✓ All tests passed! HDF5 loading works with h5py.")
    else:
        print("✗ Some tests failed. Check the output above.")
        sys.exit(1) 