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

live = ["O", "O", "O"]

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
obrazek_start = 173 # Obrázek Cucu
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

# O nějaký čas později
obrazek_start = 219 # Čas
obrazek_stop = 264
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
pokracujici_text("-----------------\033[32;1mO NĚJAKÝ ČAS POZDĚJI\033[0m-----------------")
os.system("cls||clear") # Vyčištění obazovky

# Pomelo de Tonto spí
obrazek_start = 265 # Pomelo de Tonto_sleep
obrazek_stop = 310
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
print("Už dlouho spíš a venku je bílý den. Měl by jsi konečně vstávat...")
vstavat = [ # Otázka vstávat?
    inquirer.List("menu",
    message="Vstávat?",
    choices=["Ano", "Ne"],
    ),
]
odpoved = inquirer.prompt(vstavat)
if odpoved == {'menu': 'Ne'}:
    os.system("cls||clear") # Vyčištění obazovky
    obrazek_start = 173 # Obrázek Cucu
    obrazek_stop = 218
    with open("ASCII_pictures.ans") as f:
        radky_obrazku = islice(f, obrazek_start, obrazek_stop)
        print("".join(radky_obrazku))
    live.pop()  # Mínus jeden život
    print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Lišta životů
    print("\033[32mCucumberto\033[0m: VSTÁVEJ TY JEDEN PITOMEJ LENOCHU!! To si mám snídani dělat sám?\nŽe já tě tehdy na té plantáži nenechal schnít! Jsi mi k ničemu.")
    input(">>>")
    os.system("cls||clear") # Vyčištění obazovky
    obrazek_start = 311 # Obrázek Pomelo de Tonto
    obrazek_stop = 356
    with open("ASCII_pictures.ans") as f:
        radky_obrazku = islice(f, obrazek_start, obrazek_stop)
        print("".join(radky_obrazku))
    print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Lišta životů
    print("\033[32mPomelo de Tonto\033[0m: OH! Co? Já zaspal?! Velice se omlouvám El Padrino. Nechápu co se to stalo. Hned jdu na to!")
    print("\033[32mCucumberto\033[0m: Tak už aby to sakra bylo! Ještě jednou a nechám tě vylisovat. To se mi snad zdá...")
    input(">>>")    
    os.system("cls||clear") # Vyčištění obazovky
    obrazek_start = 403 # Obrázek cucu palace
    obrazek_stop = 448
    with open("ASCII_pictures.ans") as f:
        radky_obrazku = islice(f, obrazek_start, obrazek_stop)
        print("".join(radky_obrazku))
    print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Lišta životů
    print("\033[32mPomelo de Tonto\033[0m: Ten má dnes zase náladu teda. Ale co nadělám El Padrino je hold El Padrino.\nKdybych tak jen veděl na co bude mít dnes zase chuť, když si ji včera tak znechutil zápasem.")
    print("Je mi na stopro jasné, že jak dojdu do kuchyně bude tam zase absolutní bordel a nic k nalezení, neboť včerejší zápas\nmezi Elta Bandoleros Citrutos proti La Samplíta Celeria byl dost divoký")
    print(".............")
    print("No to jsem si mohl myslet. Všude bordel, lednice prázdná, nikde žádné suroviny. Fakt paráda! Zase jen práce navíc...")
    print("""Nachystám mu jeho oblíbené nálevové Kesadillas a pak začnu raději zrovna uklízet a chystat věci na odpoledne nebo zase budu\nposlouchat jak jsem měl zhnít někde na plantáži nebo zplesnivět někde v nějaké díře.
    """)
    input(">>>")
elif odpoved == {'menu': 'Ano'}:
    os.system("cls||clear") # Vyčištění obazovky
    obrazek_start = 173 # Obrázek 
    obrazek_stop = 218
    with open("ASCII_pictures.ans") as f:
        radky_obrazku = islice(f, obrazek_start, obrazek_stop)
        print("".join(radky_obrazku))
        print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Lišta životů
    # elif odpoved pro ANO
    print("\033[32mPomelo de Tonto\033[0m: Ještě jednoou se omlouvám El Padrino! Vůbec nechápu jak se to mohlo stát, že jsem zaspal.")
    print("\033[32mCucumberto\033[0m: Ale já moc dobře vím jak se to mohlo stát! Do rána tady chlastat Coronu a požírat jablečné Tacos!\nA pak ráno makat to už moc nevoní, že ?!!")
    print("\033[32mPomelo de Tonto\033[0m: Omlouvám se ještě jednou pane, nemusíte ani nic říkat a jdu na to. K jídlu jako obvykle pane,že?!")
    print("..........El Padrino tiše a bez odpovědi odchází z místnosti..........")
    input(">>>")
# Pomelo nese jidlo a něco slyší
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 449 # Pomelo door
obrazek_stop = 494
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
print("\033[32mPomelo de Tonto\033[0m: Pane nesu Vám něco na uklid....... Co je? Otevřeno? A někdo tam je. Ne že bych byl zvědavej ale půjdu blíž že jo.")
input(">>>")
# Rozhovor Cucu a avocado
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 495 # Door
obrazek_stop = 540
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
print("\033[32mCucumberto\033[0m: Jak to vypadá s naším hnojivem? Pokračuje výroba dobře? Nerad bych nechal ovocňáky zbytečně čekat že jo? HAHAHAAA")
print("\033[32mNeznámý\033[0m: Jasně šéfe. Všechno podle plánu. Řeknu Vám ale že jste po čertech mazanej El Padrino. To se musí nechat!")
print("\033[32mCucumberto\033[0m: Jooo až budeš jednou taky pořádná okurka a ne jen blbý avokádo, tak třeba taky někdy něčeho dosáhneš.\nStejně nechápu že ty, jako ovocňák, jdeš proti vlastním.")
print("\033[32mNeznámý\033[0m:Aleee El Padrino. Kdo jiný než vy, by tomu měl rozumnět. Prachy jsou prachy. HAHAHAA a vy platíte královsky.")
print("\033[32mCucumberto\033[0m: Počkej ticho! Neslyšel jsi něco? Na chodbě. Někdo tam je! Běž to omrknout.")
input(">>>")
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 449 # Pomelo door
obrazek_stop = 494
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
print("\033[32mPomelo de Tonto\033[0m: A doprčic. Já zvědavej hlupák, že si nehledím svýho. Honem se schovám.")
otazka = [  # Pomelo se musí někam schovat
    inquirer.List("main_menu",
    message="Co teď?",
    choices=["Utéct", "Schovat do skříně", "Zůstat"],
    ),
]
odpoved = inquirer.prompt(otazka)

if odpoved == {'main_menu': 'Zůstat'}:
    os.system("cls||clear") # Vyčištění obazovky
    live.clear()
    obrazek_start = 679 # Game Over
    obrazek_stop = 724
    with open("ASCII_pictures.ans") as f:
        radky_obrazku = islice(f, obrazek_start, obrazek_stop)
        print("".join(radky_obrazku))
    print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
    print("\033[32mCucumberto\033[0m: Zase ty? Tak to už přestává všechno! Do odšťavňovače s ním!")
    input()
    pass
#elif odpoved == {'main_menu': 'Schovat do skříně'}:
