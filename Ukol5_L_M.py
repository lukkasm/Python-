import os
import csv

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

f = open("ukol.csv", "r", encoding="ISO-8859-1")
reader = csv.reader(f, delimiter=";")
over20 = []
next(reader)

for line in reader:
    if int(line[-1]) > 20:
        over20.append(line)

f.close()

f = open("ukol-20.csv", "w", encoding="ISO-8859-1")
writer = csv.writer(f, delimiter=";")

for line in over20:
    writer.writerow(line)
f.close()

        

