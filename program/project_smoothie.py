import os, re, inquirer, signal, time, sys
from itertools import islice
# os - vyčištění okna
# re, inquirer - balíček menu
# signal - umožňuje zavření terminálu
# time, sys - importuje časové funkce - samo pokračuje v textu po x sekundách
# islice - umožňuje vyčíst konkrétní řádky z dokumentu - používáme k vyčítání obrázku z jednoho dokumentu

def pokracujici_text(text): # po 3 sekundách samo pokračuje v textu - stačí psát pokracujici_text(""), použito na "mezitím v mexiku"
  for char in str(text):
    sys.stdout.write(char)
    sys.stdout.flush()
  time.sleep(3)

# Barvy pro obrázky
class colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"

    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"

    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"

    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"

input("""###########################################################################
#\033[31mPro ideální zážitek ze hry prosím maximalizujte okno a stiskněte klávesu.\033[0m#
###########################################################################
""")
# Logo hry
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 2
obrazek_stop = 47
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))

# Začátek menu
otazka = [
    inquirer.List("main_menu",
    message="VYBER SI",
    choices=["Nová hra", "Kredit", "Zavřít"],
    ),
]
odpoved = inquirer.prompt(otazka)

if odpoved == {'main_menu': 'Kredit'}:  # Volba Kredit v menu
    os.system("cls||clear") # Vyčištění obazovky
    obrazek_start = 48
    obrazek_stop = 80
    with open("ASCII_pictures.ans") as f:
        radky_obrazku = islice(f, obrazek_start, obrazek_stop)
        print("".join(radky_obrazku))
    print("""    Společný projekt dua \033[34;1mHacker Ninjas\033[0m. První pokus o hříčku po třech týdnech učení se programování.
    ------------------------------------------------------------------------------------------------
    Jakub Kolář e:\ kolarkuba@gmail.com
    Martin Holomek e:\ santexD@seznam.cz
    ---------------2021------------------
    """)
    input("Pokračovat do hry >>>")
elif odpoved == {"main_menu": "Zavřít"}:  # Zavře okno terminálu
    os.kill(os.getppid(), signal.SIGHUP)
# Konec menu

# Začátek hry, mezitím v mexiku
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 81
obrazek_stop = 126
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
pokracujici_text("-----------------\033[32;1mMEZITÍM V MEXIKU\033[0m-----------------")
os.system("cls||clear") # Vyčištění obazovky

# Tv zprávy a rozhovor z Cucu
obrazek_start = 127
obrazek_stop = 172
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print("\033[32mKESADILLA TV\033[0m: ....to je vše ze zahraničního zpradodajství. Nyní novinky z našeho města!!")
input(">>>")
print("""\033[32mRamína Petrželková\033[0m:...Děkuji za předání slova ze studia Alejandro Pomodorová. Tady Ramína Petrželková z ranního vysílání KesadillaTV!
Zrovna se nacházíme na jižní straně města del Nachos a to konkrétně v provincii El brote más Brillante,
kde je spolu semnou místní hrdina, filantrop a zastánce chudých a muž jenž plní žaludky všech bez různých skrupulí seňor Cucumberto.
Tímhle Vás chci za celou naši televizi pozdravit a poděkovat, že jste přijal naše pozvání, ale zrovna k věci!
Chtěla bych Vás požádat, abyste nám takhle do úvodu našeho rozhovoru řekl pár slov.
""")
input(">>>")
print("""Určitě mnoho našich diváků a také posluchačů zajímá právě důvod, který u Vás odstartoval tu myšlenku, která vedla k největšímu masovému celoplošnému
hnojení v dějinách celého Mechika? A proč zrovna přišel nápad vše vyzkoušet tady u nás ve Vale de la Nachos, když je veřejně známo, že jste do města přijel 
teprve nedávno a nemáte vůči němu žádné závazky ani jiný osobní vztah?
""")
input(">>>")

os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 173
obrazek_stop = 218
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print("""\033[32mCucumberto\033[0m: Samosebou paninko, řeknu Vám co budete chtít. Jak se tak dívám, to je to nejmenší co bych pro vás udělal. HAHAHAHAA
\033[32mRamína Petrželková\033[0m: Ehmmmm no... Zpět k tématu prosím.
\033[32mCucumberto\033[0m: Ale jo promiňte. (Netykavka jedna) No prostě nemám rád a vůbec nechápu tu dávnou nevraživost a nedůvěru mezi ovocňáky a zeleňáky.
A tady ve vašem městě je to prý opravdu veliký problém. No a tak jsem neváhal ani chvilku a přispěchal na pomoc. Jsem prostě dobrák víte.
Já jakožto okurek, jeden z řad zeleňáků nabízím každému ovocňákovi moje superultrapremium kvalitní syntetické hnojivo. A to prosím zdarma!
...........
""")
input(">>>")
os.system("cls||clear") # Vyčištění obazovky

pokracujici_text("-----------------\033[32;1mO NĚJAKÝ ČAS POZDĚJI\033[0m-----------------")
os.system("cls||clear") # Vyčištění obazovky