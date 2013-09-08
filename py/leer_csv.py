import csv

filedata  = open('testdata.csv', "rb")
reader = csv.reader(filedata)

rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for valcol in row:
            print '%s: %s' % (header[colnum], valcol)
            colnum += 1
            
    rownum += 1

filedata.close()

