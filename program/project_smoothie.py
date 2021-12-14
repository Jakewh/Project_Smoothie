input("Pro ideální zážitek ze hry prosím maximalizujte okno a stiskněte klávesu.")
# Logo hry
logo = open("logo.txt", "r")
file_contents = logo.read()
print(file_contents)
logo.close()

input("Pokračovat >>>")
# Tv zprávy
tv = open("tv.txt", "r")
file_contents = tv.read()
print(file_contents)
tv.close()
print("KESADILLA TV: MIMOŘÁDNÉ ZPRAVODAJSTVÍ! POSLECHNĚTE SI NOVINKY Z VALE DE LA NACHOS!!")
input("Pokračovat >>>")