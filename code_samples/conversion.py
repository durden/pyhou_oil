#!/usr/bin/env python

import xlrd
import tables


HDF5_FILENAME = 'oil_production.h5'
XLS_FILENAME = './sample_data/PET_CRD_CRPDN_ADC_MBBL_M.xls'


class OilProductionByYear(tables.IsDescription):
    """Data model class for oil production by year"""

    month = tables.Int32Col()
    barrels = tables.Int64Col()


def get_xls_data(filename):
    """Get data from given xls filename"""

    f = xlrd.open_workbook(filename=filename)
    return f.sheet_by_index(1)


def create_hdf5_file(filename):
    """Create hdf5 file with given filename, return file and table"""

    # Open a file in "w"rite mode
    h5file = tables.openFile(filename, mode="w",
                                                title="Oil Production by Year")

    # Create a new group under "/" (root)
    group = h5file.createGroup("/", 'root', 'Production by Year')

    # Create one table on it
    table = h5file.createTable(group, 'production', OilProductionByYear,
                                                            "Oil Production")
    return (h5file, table)


def populate_hdf5(data, hdf5_table):
    """Populate given hdf5 table with given data"""

    oil = hdf5_table.row

    for row in xrange(3, data.nrows):
        values = data.row_values(row)[:2]
        #date_val = xlrd.xldate_as_tuple(values[0], f.datemode)
        oil['month'] = values[0]
        oil['barrels'] = values[1]
        oil.append()


def convert_xls_to_hdf5(xls_filename, hdf5_filename):
    """Convert given xls data to hdf5"""

    xls = get_xls_data(xls_filename)
    (hdf5_file, table) = create_hdf5_file(hdf5_filename)
    populate_hdf5(xls, table)
    hdf5_file.close()


if __name__ == "__main__":
    convert_xls_to_hdf5(XLS_FILENAME, HDF5_FILENAME)
