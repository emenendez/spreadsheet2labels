#!/usr/bin/python

from __future__ import print_function
import csv
import getpass
import gspread

__version__ = '0.1.0.dev1'


def fromworksheet(Worksheet):
    # Parse this spreadsheet into list
    rows = Worksheet.row_count
    cols = Worksheet.col_count

    for col in range(1, Worksheet.col_count):
        category = None

        for value in Worksheet.col_values(col):
            if value and not category:
                category = value
            elif value:
                yield [category.encode('ascii', 'replace').replace('?', ' '),
                       value.encode('ascii', 'replace').replace('?', ' ')]
            elif not value:
                category = None


def main():
    user = raw_input('User: ')
    pw = getpass.getpass()

    # Login with your Google account
    gc = gspread.login(user, pw)

    # Open spreadsheet
    Spreadsheet = gc.open("2014 BSC info")

    # Prepare output file
    with open('output.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Category', 'Name'])

        for Worksheet in Spreadsheet.worksheets():
            worksheetPrompt = raw_input('Use %s? [n]: ' % Worksheet.title)
            if worksheetPrompt.lower().startswith('y'):
                worksheetPrompt = True
            else:
                worksheetPrompt = False
            if worksheetPrompt:
                # Parse this spreadsheet into csv
                writer.writerows(fromworksheet(Worksheet))


if __name__ == '__main__':
    main()
