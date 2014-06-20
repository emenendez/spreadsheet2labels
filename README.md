spreadsheet2labels
==================

Convert Google Spreadsheets with multiple columns and categories into a single 2-column .csv for mail merge.

Dependencies
------------
- Python 2.7
- gspread

Example
-------

Turn a spreadsheet like this:

|   | A          | B          |
|---|------------|------------|
| 1 | California | Maine      |
| 2 | Half Dome  | Katahdin   |
| 3 | Whitney    | Saddleback |
| 4 |            | Cadillac   |		   
| 5 | Washington |            |
| 6 | Rainier    |            |
| 7 | Olympus    |            |

Into this:

```
Category, Value
California, Half Dome
California, Whitney
Washington, Rainier
Washington, Olympus
Maine, Katahdin
Maine, Saddleback
Maine, Cadillac
```

Usage
-----
1. `python setup.py install`
2. `spreadsheet2labels [-h]`