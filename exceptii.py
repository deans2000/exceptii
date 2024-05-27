#5. Scrieti o functie care citeste un string de la tastatura si afiseaza lungimea lui. Tratati cazul in care textul nu este string

def lungimeString():
    try:
        string=input('Introduceti text:')
        if string.isdigit():
            string=int(string)
        return len(string)
    except TypeError as TE:
        print(TE)
        print('Trebuie sa introduceti un text!')
# print(lungimeString())