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
hra = ["Kámen", "Nůžky", "Papír"]

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
pokracujici_text("""-----------------\033[32;1mMEZITÍM V MEXIKU\033[0m-----------------



LOADING...
""")

os.system("cls||clear") # Vyčištění obazovky

# Tv zprávy a rozhovor z Cucu
obrazek_start = 127
obrazek_stop = 172
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
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
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
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
pokracujici_text("""-----------------\033[32;1mO NĚJAKÝ ČAS POZDĚJI\033[0m-----------------



LOADING...
""")
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
    live.clear()    # Životy pryč - konec
    obrazek_start = 679 # Game Over
    obrazek_stop = 724
    with open("ASCII_pictures.ans") as f:
        radky_obrazku = islice(f, obrazek_start, obrazek_stop)
        print("".join(radky_obrazku))
    print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
    print("\033[32mCucumberto\033[0m: Zase ty? Tak to už přestává všechno! Do odšťavňovače s ním! Beztak tady jenom čmucháš.")
    input()
    exit()
elif odpoved == {'main_menu': 'Schovat do skříně'}:
    os.system("cls||clear") # Vyčištění obazovky
    live.pop()
    obrazek_start = 311 # Pomelo
    obrazek_stop = 356
    with open("ASCII_pictures.ans") as f:
        radky_obrazku = islice(f, obrazek_start, obrazek_stop)
        print("".join(radky_obrazku))
    print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
    print("\033[32mPomelo de Tonto\033[0m: Hehe tady jsem v pohodě. Ve filmech se do skříně schovávají běžně a vždycky jim to projde")
    print("\033[32mCucumberto\033[0m: Hele koukni do té skříně. To je jak z filmu co? Tam by se stejně mohl schovat jenom debil")
    print("\033[32mPomelo de Tonto\033[0m: Hups")
    print("\033[32mCucumberto\033[0m: To snad... Já se tě dneska nezbavím? Co tady vůbec hledáš?\nPadej zpátky do kuchyně. To si ještě vyřídíme!")
    input(">>>")
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 587 # Avocado
obrazek_stop = 632
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
print("\033[32mNeznámý\033[0m: Šéfe nikdo tu není. Asi nějaká ratas nebo jiná havěť. S Vaším dovolením El Padrino už půjdu.\nMusím nám dohlídnout na výrobu té dobroty. Mrk mrk")
print("\033[32mCucumberto\033[0m: Jasná věc. Ať všichni dělají na 120%. Musíme toho mít co nejvíc, a pak to konečně ukončíme.")
input(">>>")
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 541 # Avocado a Pomelo
obrazek_stop = 586
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
print("\033[32mPomelo de Tonto\033[0m: Moment. Já ho přece znám. No jistě, dneska o něm zrovna vyšel článek v LA PERSONAS.\nKde to jenom mám...")
input(">>>")
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 633 # Avocado a Pomelo
obrazek_stop = 678
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
print("""\033[32mPomelo de Tonto\033[0m: No jistě. Tady je to. \033[35mMístní podnikatel Avocado Piedra Grande náhle zbohatnul po té, co začal výrábět syntetické hnojivo
pro seňora Cucumberta. Policie ho podezírá z různých daňových úniků a jiným defraudacím. Také je v podezření, že ovládá gang avokád zvaný El Sombreros.
Ti terorizují celou městkou čtvrť Gheto del Rata.\033[0m
Tady něco nehraje. Vypadá to, že náš El Padrino seňor Cucumberto nebude takový samaritánec, za kterého se vydává. Musím si dávat pozor!
""")
input(">>>")
# Rozhovor Cucu a Mrkvos
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 173 # Cucu
obrazek_stop = 218
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
print("""\033[32mCucumberto\033[0m: Tohle nějak smrdí. Pozoruju delší dobu jak se tady ten malej kulatej neřád potuluje. Beztak tady jen slídí, a to by ještě tak hrálo aby na něco přišel.
Myslím že není důvod k čekání a zbytečně riskovat. Tohle se musí vyřídit jednou pro vždy. Nemám rád překvapení. Vždy je lepší jim předcházet. To je práce pro moji pravou ruku.
Los Mrkvosi! Kde jsi příteli?!
""")
input(">>>")
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 725 # Mrkvos
obrazek_stop = 770
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
print("\033[32mLos Mrkvos\033[0m: Tady El Padrino. Vždy pár kroků za vámi a připraven s čímkoliv pomoci.")
print("""\033[32mCucumberto\033[0m: Ano můj příteli, já vím. Zrovna teď bych něco potřeboval, a s touto prosbou se mohu obrátit pouze na tebe.
Pořád se tady motá ten Pomelo. Nemám z něj vůbec dobrej pocit. Myslím že je čas se jej zbavit a musí to vypadat jako nehoda...
""")
print("\033[32mLos Mrkvos\033[0m: Ale seňore, proč zrovna já? Vždyť přeci víte že je to....")
print("""\033[32mCucumberto\033[0m: Ano vím příteli. A věř mi, že kdybych měl jinou možnost, nežádal bych to zrovna po tobě. Vždyť jen kvůli tobě je
tady u mne v domě. Chtít to někdo jiný, odmítl bych.""")
print("..........Los Mrkvos si povzdechne..........")
print("\033[32mLos Mrkvos\033[0m: Rozumím pane. Udělám co je třeba a nezklamu Vás.")
print("\033[32mCucumberto\033[0m: Já vám příteli. Já vím...")
input(">>>")
# Předěl
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 219 # Čas
obrazek_stop = 264
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
pokracujici_text("""-----------------\033[32;1mO UBĚHNE PÁR DNÍ A POMELO SE VEČER VRACÍ Z MĚSTA\033[0m-----------------



LOADING...
""")
# Pomelo, nehoda a cizinec
os.system("cls||clear") # Vyčištění obazovky
obrazek_start = 311 # Pomelo
obrazek_stop = 356
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
print("""\033[32mPomelo de Tonto\033[0m: To se nám ta párty protáhla. Hlavně ráno nezaspat. Podruhé v tomhle měsící by mi to už El Padrino neodpustil, zase bych musel čistit záchody.
Brrr ještě teď je mi zle když si vzpomenu na posledně. Musím si pospíšit, ať jsem co nejdříve v posteli. Možná bych to mohl vzít tady tou uličkou.
""")
otazka = [
    inquirer.List("main_menu",
    message="Kudy?",
    choices=["Pokračovat normálně po cestě dál", "Zkrátit si cestu tmavou uličkou"],
    ),
]
odpoved = inquirer.prompt(otazka)

if odpoved == {'main_menu': 'Zkrátit si cestu tmavou uličkou'}:
    os.system("cls||clear") # Vyčištění obazovky
    obrazek_start = 495 # Door
    obrazek_stop = 540
    with open("ASCII_pictures.ans") as f:
        radky_obrazku = islice(f, obrazek_start, obrazek_stop)
        print("".join(radky_obrazku))
    print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
    print("V uličce na zemi sedí cizinec a upřímně na tebe kouká.")
    otazka = [
        inquirer.List("main_menu",
        message="Co teď?",
        choices=["Oslovit jej", "Zklopit oči a přejít jej"],
        ),
    ]
    odpoved = inquirer.prompt(otazka)
    if odpoved == {'main_menu': 'Oslovit jej'}:
        os.system("cls||clear") # Vyčištění obazovky
        obrazek_start = 817 # Cizinec
        obrazek_stop = 862
        with open("ASCII_pictures.ans") as f:
            radky_obrazku = islice(f, obrazek_start, obrazek_stop)
            print("".join(radky_obrazku))
        print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
        print("\033[32mCizinec\033[0m: Jáá zdravíííím tě Pomelo. Pojď blííííž. Něco mít pro tebe.")
        print("\033[32mPomelo de Tonto\033[0m: Jakto že víš jak se jmenuji?")
        print("\033[32mPCizinec\033[0m: Když ty mě obehrát, řeknu víc. Když ty vyhrát, já řeknu. Když ty prohrát, přijít o jeden život. Chtít hrát?")
        otazka = [
            inquirer.List("main_menu",
            message="Hrát?",
            choices=["Ano, zkusím to", "Raději ne"],
            ),
        ]
        odpoved = inquirer.prompt(otazka)

        if odpoved == {'main_menu': 'Ano, zkusím to'}:
            os.system("cls||clear") # Vyčištění obazovky
            obrazek_start = 817 # Cizinec
            obrazek_stop = 862
            with open("ASCII_pictures.ans") as f:
                radky_obrazku = islice(f, obrazek_start, obrazek_stop)
                print("".join(radky_obrazku))
        print(150*" ", "Životy ", "\033[31;1m", " ".join(live), "\033[0m")  # Životy
