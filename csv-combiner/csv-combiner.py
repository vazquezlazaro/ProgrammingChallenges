#csv-combiner.py
import sys
import os
import csv

def combiner():
    # creating writer and setting headers
    writer=csv.writer(sys.stdout)
    header = ['email_hash','category','filename']
    writer.writerow(header)
    # Getting CSV files from arguments
    files = sys.argv[1:]
    # Read each file and perform task
    for file in files:
        with open(file,'r') as f:
            reader = csv.reader(f)
            reader.__next__()
            base_filename = os.path.basename(file)
            for line in reader:
                line.append(base_filename)
                writer.writerow(line)

combiner()
