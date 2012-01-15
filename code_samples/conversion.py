#!/usr/bin/env python

"""
Convert excel spreadsheet to hdf5 format
"""

import datetime
import time

import xlrd
import tables


HDF5_FILENAME = 'oil_production.h5'
XLS_FILENAME = './sample_data/PET_CRD_CRPDN_ADC_MBBL_M.xls'


class OilProductionByMonth(tables.IsDescription):
    """Data model class for oil production by month"""

    date = tables.Time64Col()
    barrels = tables.Int32Col()


class ExcelToHdf5(object):
    """Create hdf5 file from excel workbook"""

    def __init__(self, xls_filename, hdf5_filename, sheet=1):
        """Convert given filename an sheet to hdf5"""
    
        self.xls_filename = xls_filename
        self.hdf5_filename = hdf5_filename
        self.sheet = sheet

    def get_xls_data(self):
        """Get data from given xls filename and sheet"""

        workbook = xlrd.open_workbook(filename=self.xls_filename)
        return (workbook, workbook.sheet_by_index(self.sheet))


    def create_hdf5_file(self):
        """Create hdf5 file with given filename, return file and table"""

        # Open a file in "w"rite mode
        h5file = tables.openFile(self.hdf5_filename, mode="w",
                                                title="Oil Production by Year")

        # Create a new group under "/" (root)
        group = h5file.createGroup("/", 'data', 'Production by Year')

        if self.sheet == 1:
            table = h5file.createTable(group, 'production',
                                                        OilProductionByMonth,
                                                        "Oil Production")
        else:
            table = h5file.createTable(group, 'production',
                                        OilProductionByStateAndMonth,
                                        "Oil Production")
        return (h5file, table)


    def convert_xldate_to_timestamp(self, xldate, data_book):
        """Convert an xldate tuple (from xlrd.xldate_as_tuple) to timestamp"""

        xldate = xlrd.xldate_as_tuple(xldate, data_book.datemode)
        date = datetime.date(xldate[0], xldate[1], xldate[2])
        return time.mktime(date.timetuple())


    def populate_hdf5(self, data_book, data_sheet, hdf5_table):
        """Populate given hdf5 table with given data"""

        oil = hdf5_table.row

        for row in xrange(3, data_sheet.nrows):
            values = data_sheet.row_values(row)[:2]
            oil['date'] = self.convert_xldate_to_timestamp(values[0],
                                                                    data_book)
            oil['barrels'] = values[1]
            oil.append()

    def convert(self):
        """Convert excel sheet to hdf5 file"""

        (book, sheet) = self.get_xls_data()
        (hdf5_file, table) = self.create_hdf5_file()
        self.populate_hdf5(book, sheet, table)
        hdf5_file.close()


def convert_xls_to_hdf5(xls_filename, hdf5_filename, sheet):
    """Convert given xls data to hdf5"""

    converter = ExcelToHdf5(xls_filename, hdf5_filename, sheet)
    converter.convert()


if __name__ == "__main__":
    convert_xls_to_hdf5(XLS_FILENAME, HDF5_FILENAME, sheet=1)
