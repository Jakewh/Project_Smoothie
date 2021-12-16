from itertools import islice

obrazek_start = 2
obrazek_stop = 47
with open("ASCII_pictures.ans") as f:
    radky_obrazku = islice(f, obrazek_start, obrazek_stop)
    print("".join(radky_obrazku))
