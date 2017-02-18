import csv
import sys

if len(sys.argv) != 3:
    print "Execution format: python dat2csv.py <source_file> <destination_file>"
else:
    with open(sys.argv[1], 'r') as input_file:
        lines = input_file.readlines()
        newLines = []
        for line in lines:
            newLine = line.strip(' ').split()
            newLines.append(newLine)

    with open(sys.argv[2], 'w') as output_file:
        file_writer = csv.writer(output_file)
        file_writer.writerows(newLines)
