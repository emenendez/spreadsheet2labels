#!/usr/bin/python
#
# Based on Google sample code. 

from __future__ import print_function

import getpass
import gspread

def main():
    user = raw_input('User: ')
    pw = getpass.getpass()

    # Login with your Google account
    gc = gspread.login(user, pw)

    # Open spreadsheet
    Spreadsheet = gc.open("2014 BSC info")


    # # Fetch a cell range
    # cell_list = wks.range('A1:B7')

    for Worksheet in Spreadsheet.worksheets():
        worksheetPrompt = raw_input('Use %s? [n]: ' % Worksheet.title)
        if worksheetPrompt.lower().startswith('y'):
            worksheetPrompt = True
        else:
            worksheetPrompt = False
        if worksheetPrompt:
            # Parse this spreadsheet into csv
            rows = Worksheet.row_count
            cols = Worksheet.col_count

            for col in range(1, Worksheet.col_count):
                values = Worksheet.col_values(col)
                print(values[0])



if __name__ == '__main__':
    main()
