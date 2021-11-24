import csv
import itertools
with open("vstup.csv", encoding="utf-8") as csvinfile,\
	open("vystup_7denni.csv", "w", encoding="utf-8") as csvoutfile:
    reader = csv.reader(csvinfile, delimiter=",")
    writer = csv.writer(csvoutfile)
    next(reader)
    n=0
    m=0
    average=0
    prutok = 0
    for row in reader:
        n+=1
        prutok += float(row[5])
        if n%7==1:
            sum_prutoku = round(prutok, 4)
            writer.writerow([row[0:5], sum_prutoku])
            prutok = 0
            sum_prutoku = 0
        while True:
            m+=1
            average+=float(row[5])
            if m%7==0:
                break