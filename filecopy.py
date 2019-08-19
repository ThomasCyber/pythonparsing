from shutil import copyfile
import os

filelocation = "c:\\csv_test\\files\\init.csv"

for i in range(1 , 10000):

	name = str(i) + ".csv"
	
	copyfile(filelocation, os.path.join("c:\\csv_test\\files\\", name) )
	
	