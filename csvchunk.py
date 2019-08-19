import os
import csv
import time

CSV_LOCATION = "c:\\csv_test\\files"
CSV_RESULTS = "c:\\csv_test\\results"

def chunk(file_name):

	chunksize = 2048
	
	filename = os.path.join(CSV_LOCATION,file_name)
	
	with open(filename, 'r') as f:
		while True:
			columns=f.readline()
			read_data = f.readlines(chunksize)
			if not read_data:
				break # done
				
			csv_data = csv.reader(read_data)	
	
			with open(os.path.join(CSV_RESULTS,file_name), "a") as s:			
				for row in csv_data:
					columns=row[0]+ "," + row[1]+ "," + row[2] + "\n"
					datas=''.join(columns)					
					s.write(datas)


def main():

	# start timer for file
	start = time.time()
	# end timer
	end = time.time()
	
	count = 0
	
	for root, dir, files in os.walk(CSV_LOCATION):	
		for f in files:		
			if count < 2:			
				chunk(f)				
				count = count + 1		
	
	# math
	end - start
	print(end)


if __name__ == "__main__":

	main()