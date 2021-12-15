import os, re
import inquirer

input("Pro ideální zážitek ze hry prosím maximalizujte okno a stiskněte klávesu.")
# Logo hry
logo = open("logo.txt", "r")
file_contents = logo.read()
print(file_contents)
logo.close()
# Experient s menu
otazka = [
  inquirer.List("main_menu",
                message="VYBER SI",
                choices=["Nová hra", "Zavřít", "Kredit"],
            ),
]
odpoved = inquirer.prompt(otazka)
# Konec experimentu s menu
input("Pokračovat >>>")
os.system("cls||clear") # Vyčištění obazovky
print("-----------------MEZITÍM V MEXIKU-----------------")
input("Pokračovat >>>")
os.system("cls||clear") # Vyčištění obazovky
# Tv zprávy
tv = open("tv.txt", "r")
file_contents = tv.read()
print(file_contents)
tv.close()
print("KESADILLA TV: MIMOŘÁDNÉ ZPRAVODAJSTVÍ! POSLECHNĚTE SI NOVINKY Z VALE DE LA NACHOS!!")
input("Pokračovat >>>")
os.system('cls||clear') # Vyčištění obazovky
print("""\033[4mRamína Petrželková\033[0m,,...Děkuji za předání slova ze studia Alejandro. Tady Ramína Petrželková z ranního vysílání KesadillaTV!
Zrovna se nacházíme na jižní straně města del Nachos a to konkrétně v provincii El brote más Brillante, kde je spolu semnou místní hrdina, filantrop a zastánce chudých a muž jenž plní žaludky všech bez různých skrupulí seňor Cucumberto.
Tímhle Vás chci za celou naši televizi pozdravit a poděkovat, že jste přijal naše pozvání, ale zrovna k věci!
Chtěla bych Vás požádat, abyste nám takhle do úvodu našeho rozhovoru řekl pár slov.
Určitě mnoho našich diváků a také posluchačů zajímá právě důvod, který u Vás odstartoval tu myšlenku, která vedla k největšímu masovému celoplošnému hnojení v dějinách celého Mechika?
A proč zrovna přišel nápad vše vyzkoušet tady u nás ve Vale de la Nachos, když je veřejně známo, že do města jste přijel teprve nedávno a nemáte vůči němu žádné závazky ani jiný osobní vztah\".""")
input("Pokračovat >>>")