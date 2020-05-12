#!/usr/bin/env python3

import sys
import csv

# use arguments given outside function to get in and out files
flin=sys.argv[1]
flout=sys.argv[2]

#
def unfussy_reader(csv_reader):
   while True:
      try:
         yield next(csv_reader)
      except csv.Error:
      # log the problem or whatever
         print("Problem with some row")
         continue

# START
with open(flin, 'r') as fin, open(flout, 'w', newline='') as fout:
    # define reader and writer objects
    reader = unfussy_reader(csv.reader(fin, skipinitialspace=True))
    writer = csv.writer(fout, delimiter=',')
    # write headers
    writer.writerow(next(reader))
    # iterate and write rows based on condition
    for i in reader:
          if i[4] == 'concentration' or i[4] == 'temperature' or i[3] == 'current' or i[3]=='audio': 
              writer.writerow(i)


