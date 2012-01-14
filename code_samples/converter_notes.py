from tablib.packages import xlrd
f = xlrd.open_workbook(
            filename='/Users/durden/Downloads/PET_CRD_CRPDN_ADC_MBBL_M.xls')
s = f.sheet_by_index(1)
for row in xrange(3, s.nrows):
    values = s.row_values(row)[:2]
    date_val = xlrd.xldate_as_tuple(values[0], f.datemode)
    barrels_in_thousands = values[1]
    print date_val, barrels_in_thousands
