from ij import IJ
from ij.measure import ResultsTable
import os, sys

filepath = "/Users/inchOuOsis/test" #替换为总目录地址
dirs = os.listdir(filepath)
f = open('/Users/inchOuOsis/Documents/output.csv', 'w') #替换为保存地址
IJ.run("Set Measurements...", "area mean min integrated redirect=None decimal=3")

for files in dirs:
	if not os.path.isdir(filepath + '/' + str(files)):
		continue

	img = IJ.open(filepath + '/' + str(files) + '/' + str(files) + ".tif")
	IJ.run("Split Channels")
	imp = IJ.getImage()
	imp.close()
	IJ.setThreshold(10000, 65535)
	IJ.run("Analyze Particles...", "size=0-Infinity circularity=0-1.00 show=Nothing display clear")
	IJ.saveAs("Results", "/Users/inchOuOsis/Documents/Results.csv")
	IJ.run("Close")

	column = [[] for i in range(7)]
	with open('/Users/inchOuOsis/Documents/Results.csv', 'r') as read_file:
		next(read_file)
		for row in read_file:
			a = row.strip().split(',')
			for i in range(0, len(a)):
				column[i].append(float(a[i]))

	f.write(str(sum(column[1])) + ',')
	f.write(str((sum(column[2])/len(column[2]))) + ',')
	f.write(str(min(column[3])) + ',')
	f.write(str(max(column[4])) + ',')
	f.write(str(sum(column[5])) + ',')
	f.write(str(sum(column[6])) + '\n')
	imp = IJ.getImage()
	imp.close()

f.close()
