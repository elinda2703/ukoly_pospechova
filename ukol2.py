import csv
with open(r"vstup.csv", encoding="utf-8") as csvinfile, open(r"vystup_7denni.csv", "w", encoding="utf-8", newline="") as csvoutfile, open(r"vystup_rok.csv", "w", encoding="utf-8", newline="") as csvoutfile_rok:
    reader = csv.reader(csvinfile, delimiter=",")
    writer = csv.writer(csvoutfile)
    writer_rok = csv.writer(csvoutfile_rok)
    n=0
    m=0
    sedm_prutoku=[] #sem se nacte 7 prutoku z jednoho tydne
    ostatni_udaje=[]
    seznam_prumeru=[]
    seznam_za_rok=[]
    prutoky_rok=[]
    seznam_rocnich_prumeru=[]
    ostatni_udaje=[]
    seznam_rocnich_prutoku=[]
    ostatni_udaje_rok=[]
    
    for row in reader:
        n+=1
        m+=1
        rok=int(row[2])
 
        sedm_prutoku.append(float(row[5])) 

        if m%7==0:
            prumer = round((sum(sedm_prutoku)/len(sedm_prutoku)),4)
            seznam_prumeru.append(prumer)
            sedm_prutoku.clear()
        
        if n%7==1:
            ostatni_udaje.append(row[0:5])
        
        if len(prutoky_rok)==0 or rok==int(prutoky_rok[-1][2]):
            prutoky_rok.append(row[0:5])
            seznam_rocnich_prutoku.append(float(row[5]))

        else:
            ostatni_udaje_rok.append(prutoky_rok[0])
            prumer = round((sum(seznam_rocnich_prutoku)/len(seznam_rocnich_prutoku)),4)
            seznam_rocnich_prumeru.append(prumer)
            seznam_rocnich_prutoku.clear()
            prutoky_rok.clear()
            prutoky_rok.append(row[0:5])
            seznam_rocnich_prutoku.append(float(row[5]))

    prumer = round((sum(seznam_rocnich_prutoku)/len(seznam_rocnich_prutoku)),4)    
    seznam_rocnich_prumeru.append(prumer)
    ostatni_udaje_rok.append(prutoky_rok[0])    
   
   
    
    for i in range (len(seznam_prumeru)):
        ostatni_udaje[i].append(seznam_prumeru[i])
    
    for i in range (len(seznam_rocnich_prumeru)):
        ostatni_udaje_rok[i].append(seznam_rocnich_prumeru[i])
    print(ostatni_udaje_rok)
    writer.writerows(ostatni_udaje)
    writer_rok.writerows(ostatni_udaje_rok)

        