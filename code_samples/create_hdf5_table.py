#!/usr/bin/env python

import xlrd
import tables


class OilProductionByYear(tables.IsDescription):
    month = tables.Int32Col()
    barrels = tables.Int64Col()


def get_xls_data():
    """"""
    f = xlrd.open_workbook(
                        filename='./sample_data/PET_CRD_CRPDN_ADC_MBBL_M.xls')
    return f.sheet_by_index(1)


def create_hdf5_file():
    """"""
    filename = "test.h5"

    # Open a file in "w"rite mode
    h5file = tables.openFile(filename, mode="w", title="Test file")

    # Create a new group under "/" (root)
    group = h5file.createGroup("/", 'production', 'Production by Year')

    # Create one table on it
    table = h5file.createTable(group, 'readout', OilProductionByYear,
                                                            "Readout example")
    return (h5file, table)


def populate_hdf5(data, hdf5_table):
    """"""

    oil = table.row

    for row in xrange(3, data.nrows):
        values = data.row_values(row)[:2]
        #date_val = xlrd.xldate_as_tuple(values[0], f.datemode)
        oil['month'] = values[0]
        oil['barrels'] = values[1]
        oil.append()


if __name__ == "__main__":
    xls = get_xls_data()
    (hdf5_file, table) = create_hdf5_file()
    populate_hdf5(xls, table)
    hdf5_file.close()
