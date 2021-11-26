import csv


def vysledny_seznam(zbytek,prumery):
    for i in range (len(prumery)):
        zbytek[i].append(prumery[i])

def spocitej_a_pridej_prumer (prutoky,vysledny_seznam_prumeru):
    prumer = round((sum(prutoky)/len(prutoky)),4)
    vysledny_seznam_prumeru.append(prumer)

def pridej_prvni_radek_do_seznamu (vysledny_seznam,vstupni_seznam):
    vysledny_seznam.append(vstupni_seznam[0])

def rozdel_radek_a_pridej_do_seznamu(zbytek,prumery,radek):
    zbytek.append(radek[0:5])
    prumery.append(float(radek[5]))

with open(r"vstup.csv", encoding="utf-8") as csvinfile, open(r"vystup_7denni.csv", "w", encoding="utf-8", newline="") as csvoutfile, open(r"vystup_rok.csv", "w", encoding="utf-8", newline="") as csvoutfile_rok:
    reader = csv.reader(csvinfile, delimiter=",")
    writer = csv.writer(csvoutfile)
    writer_rok = csv.writer(csvoutfile_rok)
    n=0
    sedm_prutoku=[] #sem se nacte 7 prutoku z jednoho tydne (krome posledniho tydne)
    ostatni_udaje=[]
    seznam_prumeru=[]
    prutoky_rok=[]
    seznam_rocnich_prumeru=[]
    seznam_rocnich_prutoku=[]
    ostatni_udaje_rok=[]
    
    for row in reader:
        n+=1
        rok=int(row[2])
        sedm_prutoku.append(float(row[5])) 

        if n%7==0:
            spocitej_a_pridej_prumer(sedm_prutoku,seznam_prumeru)
            sedm_prutoku.clear()
        
        if n%7==1:
            ostatni_udaje.append(row[0:5])
        
        if len(prutoky_rok)==0 or rok==int(prutoky_rok[-1][2]):
            rozdel_radek_a_pridej_do_seznamu(prutoky_rok,seznam_rocnich_prutoku,row)

        else:
            pridej_prvni_radek_do_seznamu(ostatni_udaje_rok,prutoky_rok)
            spocitej_a_pridej_prumer(seznam_rocnich_prutoku,seznam_rocnich_prumeru)
            seznam_rocnich_prutoku.clear()
            prutoky_rok.clear()
            rozdel_radek_a_pridej_do_seznamu(prutoky_rok,seznam_rocnich_prutoku,row)

    

    spocitej_a_pridej_prumer(sedm_prutoku,seznam_prumeru)

    spocitej_a_pridej_prumer(seznam_rocnich_prutoku,seznam_rocnich_prumeru)
    pridej_prvni_radek_do_seznamu(ostatni_udaje_rok,prutoky_rok)   
   
    
    

    vysledny_seznam(ostatni_udaje,seznam_prumeru)
    vysledny_seznam(ostatni_udaje_rok,seznam_rocnich_prumeru)

    writer.writerows(ostatni_udaje)
    writer_rok.writerows(ostatni_udaje_rok)

        