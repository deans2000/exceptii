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

#6. Fiind dat un dictionar {"a":1,"b":2,"c":3} scrieti o functie care primeste ca parametru cheia si returneaza valoarea

def dictionar(cheie):
    try:
        dict={
            'a':1,
            'b':2,
            'c':3
        }
        return dict[cheie]
    except KeyError as KE:
        print(KE)
        print('Cheia transmisa nu exista!')
# print(dictionar(2))
