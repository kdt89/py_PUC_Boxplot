
rowskip = 'Khang'
# Load the data
if rowskip == 'None':
    rowskip = None
else:
    rowskip = rowskip.split(' ')
    rowskip = list(map(int, rowskip))
    rowskip = [num for num in rowskip if num.isnumeric()] # Filter out non-numeric string
    rowskip = [row for row in rowskip if row >= 0]
    if len(rowskip) == 0:
        rowskip = None