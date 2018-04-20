from ij import IJ
from ij.measure import ResultsTable
import os, sys

filepath = "filepath" # 替换为总目录地址
dirs = os.listdir(filepath)
f = open('saving file path', 'w') # 替换为保存地址
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
	IJ.saveAs("Results", "saving file path/Results.csv") # 替换为保存地址
	IJ.run("Close")

	column = [[] for i in range(7)]
	with open('saving file path/Results.csv', 'r') as read_file: # 替换为保存地址
		next(read_file)
		for row in read_file:
			a = row.strip().split(',')
			for i in range(0, len(a)):
				column[i].append(float(a[i]))

	f.write(str(files))
	f.write(str(sum(column[1])) + ',')
	f.write(str((sum(column[2])/len(column[2]))) + ',')
	f.write(str(min(column[3])) + ',')
	f.write(str(max(column[4])) + ',')
	f.write(str(sum(column[5])) + ',')
	f.write(str(sum(column[6])) + '\n')
	imp = IJ.getImage()
	imp.close()

f.close()
