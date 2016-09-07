"""
Test the IO operations
"""

from unittest import TestCase
import xarray as xr
import os

from ect.ops.io import load_dataset, save_dataset

class TestIO(TestCase):
    def test_load_dataset(self):
        # Test normal functionality
        dset = None
        dset = load_dataset('AEROSOL_AATSR_SU_L3_V4.21_MONTHLY', '2008-01-01', '2008-03-01')
        self.assertIsNotNone(dset)

        # Test swapped dates
        with self.assertRaises(ValueError):
            dset = load_dataset('AEROSOL_AATSR_SU_L3_V4.21_MONTHLY', '2008-03-01', '2008-01-01')

        # Test required arguments
        with self.assertRaises(TypeError):
            dset = load_dataset('AEROSOL_AATSR_SU_L3_V4.21_MONTHLY', '2008-03-01')

    def test_save_dataset(self):
        # Test normal functionality
        dset = None
        dset = load_dataset('AEROSOL_AATSR_SU_L3_V4.21_MONTHLY', '2008-01-01', '2008-03-01')
        save_dataset(dset, 'remove_me.nc')
        self.assertTrue(os.path.isfile('remove_me.nc'))
        os.remove('remove_me.nc')

        # Test required arguments
        with self.assertRaises(TypeError):
            save_dataset(dset)

        # Test behavior when passing unexpected type
        with self.assertRaises(NotImplementedError):
            dset = ('a',1,3,5)
            save_dataset(dset, 'remove_me.nc')

        self.assertFalse(os.path.isfile('remove_me.nc'))
