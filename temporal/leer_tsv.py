import csv

filedata  = open('data/test.tsv', "rb")
reader = csv.reader(filedata, delimiter='\t')

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
