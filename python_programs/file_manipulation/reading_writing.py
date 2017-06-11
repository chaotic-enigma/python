import csv
# for reading a file
with open('file_name.txt', 'r') as sourceFile: # same thing follows for reading csv files (file_name.csv)
	sourceFileReader = csv.reader(sourceFile)
	sourceList = []
	for row in sourceFileReader:
		if len(row) != 0:
			sourceList = sourceList + [row]

sourceFile.close()
print (sourceList)

# for writing a file
attribute1 = input('enter your age: ')
attribute2 = input('enter your details: ')
with open('file_name.txt', 'w') as sourceFile: # samething follows for writing csv files (file_name.csv)
	sourceFileWriter = csv.writer(sourceFile)
	sourceFileWriter.writerow([attribute1, attribute2])

sourceFile.close()
