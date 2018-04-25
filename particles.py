from ij import IJ, ImageStack
#from ij.measure import ResultsTable
import os, sys

filepath = "filpath" # 替换为总目录地址
dirs = os.listdir(filepath)
f = open(filepath + '/output.csv', 'w')
f.write('Label,Area,Mean,Min,Max,IntDen,RawIntDen\n')

suffix = "_MMStack_Pos0.ome"

IJ.run("Set Measurements...","area mean min integrated redirect=None decimal=3")

for files in dirs:
  if not os.path.isdir(filepath + '/' + str(files)):
    continue

  img = IJ.open(filepath + '/' + str(files) + '/' + str(files) + suffix +
                ".tif")

  img = IJ.getImage()
  if img.getNSlices() > 1:
    IJ.run("Split Channels")
    img = IJ.getImage()
    img.close()
  
  IJ.setThreshold(10000, 65535) # 设置threshold
  IJ.run("Analyze Particles...", "size=0-Infinity circularity=0-1.00 show=Nothing display clear")
  IJ.saveAs("Results", filepath + '/' + str(files) + '/' + "/Results.csv")
  IJ.run("Close")

  column = [[] for i in range(7)]
  with open(filepath + '/' + str(files) + '/' + '/Results.csv', 'r') as read_file:
    next(read_file)
    for row in read_file:
      a = row.strip().split(',')
      for i in range(0, len(a)):
        column[i].append(float(a[i]))

  
  f.write(str(files) + suffix + ',')
  f.write(str(sum(column[1])) + ',')
  f.write(str((sum(column[2])/len(column[2]))) + ',')
  f.write(str(min(column[3])) + ',')
  f.write(str(max(column[4])) + ',')
  f.write(str(sum(column[5])) + ',')
  f.write(str(sum(column[6])) + '\n')
  imp = IJ.getImage()
  imp.close()

f.close()
