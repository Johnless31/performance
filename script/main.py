# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import csv
with open('output.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    column = [row[4] for row in reader]
for i in range(len(column)):
	if column[i].isnumeric():
		column[i] = float(column[i])
	else:
		column[i] = 0.0
plt.plot(column)
plt.ylabel('some numbers')
plt.show()