import csv
with open(r"ukoly\vstup.csv", encoding="utf-8") as csvinfile, open(r"ukoly\vystup_7denni.csv", "w", encoding="utf-8", newline="") as csvoutfile:
    reader = csv.reader(csvinfile, delimiter=",")
    writer = csv.writer(csvoutfile)
    writer_rok = csv.writer(csvoutfile)
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
            prumer = round((sum(seznam_rocnich_prutoku)/len(seznam_rocnich_prutoku)),4)
            seznam_rocnich_prumeru.append(prumer)
            prutoky_rok.clear()
        
        
   
   
    print(seznam_rocnich_prutoku)
    for i in range (len(seznam_prumeru)):
        ostatni_udaje[i].append(seznam_prumeru[i])

    writer.writerows(ostatni_udaje)
    

        