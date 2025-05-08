from tkinter import *
import random
import csv
from datetime import datetime



osobe = []
with open('imena_prezimena.csv', 'r', encoding='utf-8') as fajl:
    naslov = fajl.readline()
    for red in fajl:
        podaci = red.strip().split(',')
        if len(podaci) == 2:
            ime = podaci[0]
            prezime = podaci[1]
            osobe.append((ime, prezime)) 

def random_num():
    num = random.randint(10**12, 10**13 - 1)
    jmbg_label.config(text=f"JMBG: {num}")
    ime, prezime = random.choice(osobe)
    ime_label.config(text=f"Ime: {ime}")
    prezime_label.config(text=f"Prezime: {prezime}")

prozor = Tk()
Label(prozor, text = "Serbian person generator", font='italic').pack(side='top', fill='x', pady=10)
prozor.title("Random JMBG generator")
prozor.geometry("800x400")


Button(prozor, text='Pritisni ovde', command=random_num).pack(side=RIGHT)



ime_label = Label(prozor, text="Ime: ")
ime_label.pack(pady=10, anchor='w')

prezime_label = Label(prozor, text="Prezime: ")
prezime_label.pack(pady=10, anchor='w')

datum_rodjenja_label = Label(prozor, text = 'Datum rođenja: ')
datum_rodjenja_label.pack(pady=10, anchor='w')

mesto_rodjenja_label = Label(prozor, text='Mesto rođenjа: ')
mesto_rodjenja_label.pack(pady=10, anchor='w')

ime_roditelja_label = Label(prozor, text='Ime roditelja: ')
ime_roditelja_label.pack(pady=10, anchor='w')

pol_label = Label(prozor, text='Pol: ')
pol_label.pack(pady=10, anchor='w')





print(osobe[:5])






jmbg_label = Label(prozor, text='JMBG: ')
jmbg_label.pack(pady=10, anchor='w')

prozor.mainloop()