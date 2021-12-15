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
