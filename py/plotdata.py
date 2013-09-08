
import csv
import datetime as dt
import matplotlib.pyplot as plt

filedata  = open('data/test.tsv', "rb")
reader = csv.reader(filedata, delimiter='\t')

x, y = [], []

rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
    	x.append(row[3])
    	y.append(row[4])
            
    rownum += 1

filedata.close()

print header


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(y, x, 'o-')
fig.autofmt_xdate()

plt.show()

