from __future__ import print_function
import argparse
import csv
import getpass
import sys
import gspread

__version__ = '0.1.0'


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
    def prompt(prompt):
        if prompt.lower() == 'password':
            return lambda value: getpass.getpass() if value is '-' else value
        else:
            return lambda value: raw_input(prompt + ': ') if value is '-' else value

    parser = argparse.ArgumentParser(description='Turn a Google spreadsheet into a category, value CSV file suitable for making labels.')
    parser.add_argument('-u', '--user', nargs='?', type=prompt('User'), default='-', const='-', help='Google account')
    parser.add_argument('-p', '--password', nargs='?', type=prompt('Password'), default='-', const='-', help='Google account password')
    parser.add_argument('-o', '--output', nargs='?', type=argparse.FileType('wb'), default=sys.stdout, help='output file')
    parser.add_argument('spreadsheet', nargs='?', type=prompt('Spreadsheet'), default='-', help='spreadsheet to parse')
    parser.add_argument('worksheet', nargs='*', help='worksheets to parse')
    args = parser.parse_args()

    # Login with Google account
    gc = gspread.login(args.user, args.password)

    # Open spreadsheet
    Spreadsheet = gc.open(args.spreadsheet)

    # Prepare output file
    writer = csv.writer(args.output)
    writer.writerow(['Category', 'Name'])

    # Iterate through worksheets in Spreadsheet
    for Worksheet in Spreadsheet.worksheets():
        if args.worksheet:
            if Worksheet.title in args.worksheet:
                worksheetPrompt = True
            else:
                worksheetPrompt = False
        else:
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
