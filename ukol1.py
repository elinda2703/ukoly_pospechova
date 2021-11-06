from turtle import forward, left, right, penup, pendown, speed, exitonclick, circle, setposition, color, pensize
from math import sqrt
speed(0)

# nakreslí hrací pole


def nakresli_hraci_pole(sirka, delka, velikost_policka):
    for j in range(delka):
        for i in range(sirka):
            for k in range(4):
                forward(velikost_policka)
                left(90)
            forward(velikost_policka)
        left(180)
        forward(sirka*velikost_policka)
        right(90)
        forward(velikost_policka)
        right(90)
    penup()

# získá parametry pole a ošetří chybné vstupy


def ziskej_kladne_cislo(vyzvani_hrace, dolni_mez):
    while(True):
        p = int(input(vyzvani_hrace))
        if (dolni_mez > p):
            print("Chybný vstup")
        else:
            return p

# vrátí parametry pole


def nacti_parametry_pole():
    a = ziskej_kladne_cislo("zadej počet řádků", 1)
    b = ziskej_kladne_cislo("zadej počet sloupců", 1)
    d = ziskej_kladne_cislo("zadej velikost políčka (aspoň 20, ať to jde vidět)", 20)
    return a, b, d

# získá souřadnice na hracím poli a oštří chybné vstupy


def ziskej_souradnici(vyzvani_hrace, dolni_mez, horni_mez):
    while(True):
        p = int(input(vyzvani_hrace))
        if (p > horni_mez) or (dolni_mez > p):
            print("Chybný vstup")
        else:
            return p

# vrátí souřadnice


def ziskej_souradnice(sirka, vyska, hrac):
    x = ziskej_souradnici(f"Hráči {hrac}, zadej souřadnici x", 1, sirka)
    y = ziskej_souradnici(f"Hráči {hrac}, zadej souřadnici y", 1, vyska)
    return x, y


# nakreslí kolečko
def kolecko(x, y, velikost_policka):
    setposition((x-1)*velikost_policka+velikost_policka/2, (y-1)*velikost_policka+velikost_policka/6)
    pendown()
    color('blue')
    circle(velikost_policka/3)
    penup()

# nakreslí křížek


def krizek(x, y, velikost_policka):
    setposition((x-1)*velikost_policka+velikost_policka/6, (y-1)*velikost_policka+velikost_policka/6)
    pendown()
    color('red')
    left(45)
    forward(2/3*velikost_policka*sqrt(2))
    penup()
    right(135)
    forward(2*velikost_policka/3)
    pendown()
    right(135)
    forward(2/3*velikost_policka*sqrt(2))
    right(135)
    penup()

# výsledná funkce


def piskvorky(sirka, vyska, velikost_policka):
    nakresli_hraci_pole(sirka, vyska, velikost_policka)
    pensize(3)
    for r in range(sirka*vyska):
        if (r % 2 == 1):
            x, y = ziskej_souradnice(sirka, vyska, 2)
            kolecko(x, y, velikost_policka)
        else:
            x, y = ziskej_souradnice(sirka, vyska, 1)
            krizek(x, y, velikost_policka)
    exitonclick()


pocet_radku, delka, velikost_policka = nacti_parametry_pole()
piskvorky(pocet_radku, delka, velikost_policka)
