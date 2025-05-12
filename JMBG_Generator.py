from tkinter import *
import random
import csv

# Učitaj podatke iz CSV fajla (ime, prezime, pol)
osobe = []
with open('imena_prezimena.csv', 'r', encoding='utf-8') as fajl:
    fajl.readline()  # preskoči header
    for red in fajl:
        podaci = red.strip().split(',')
        if len(podaci) == 3:
            ime = podaci[0]
            prezime = podaci[1]
            pol = podaci[2].strip().lower()
            osobe.append((ime, prezime, pol))

# Pomoćne liste
mesta = ["Beograd", "Novi Sad", "Niš", "Kragujevac", "Subotica", "Zrenjanin", "Čačak", "Valjevo",
         "Kraljevo", "Šabac", "Aleksinac", "Sremski Karlovci", "Sombor"]
ime_roditelja = ['Zoran', 'Dragan', 'Bojana', 'Milena', 'Dragica', 'Milun', 'Milutin', 'Dragutin',
                 'Stojan', 'Bojan', 'Miloš', 'Dejan', 'Borislav', 'Jovan', 'Stanoje']

# --- GUI deo ---
prozor = Tk()
prozor.title("Random JMBG generator")
prozor.geometry("800x400")

Label(prozor, text="Serbian person generator", font='italic').pack(side='top', fill='x', pady=10)

ime_label = Label(prozor, text="Ime: ")
ime_label.pack(pady=5, anchor='w')

prezime_label = Label(prozor, text="Prezime: ")
prezime_label.pack(pady=5, anchor='w')

datum_rodjenja_label = Label(prozor, text="Datum rođenja: ")
datum_rodjenja_label.pack(pady=5, anchor='w')

mesto_rodjenja_label = Label(prozor, text="Mesto rođenja: ")
mesto_rodjenja_label.pack(pady=5, anchor='w')

ime_roditelja_label = Label(prozor, text="Ime roditelja: (opciono)")
ime_roditelja_label.pack(pady=5, anchor='w')

pol_label = Label(prozor, text="Pol: ")
pol_label.pack(pady=5, anchor='w')

jmbg_naslov = Label(prozor, text="JMBG:", font=("Arial", 12, "bold"))
jmbg_naslov.pack(pady=(10, 0), anchor='w')

jmbg_label = Entry(prozor, width=30, font=("Arial", 14), state='readonly', readonlybackground='white')
jmbg_label.pack(pady=5, anchor='w')

# --- Funkcija za generaciju osobe ---
def generisi_osobu():
    ime, prezime, pol = random.choice(osobe)
    ime_label.config(text=f"Ime: {ime}")
    prezime_label.config(text=f"Prezime: {prezime}")
    pol_label.config(text=f"Pol: {pol}")

    dan = random.randint(1, 28)
    mesec = random.randint(1, 12)
    godina = random.randint(1950, 2005)
    datum_rodjenja_label.config(text=f"Datum rođenja: {dan:02d}.{mesec:02d}.{godina}.")

    mesto = random.choice(mesta)
    mesto_rodjenja_label.config(text=f"Mesto rođenja: {mesto}")

    roditelj = random.choice(ime_roditelja)
    ime_roditelja_label.config(text=f"Ime roditelja: {roditelj}")

    region = 70
    rrr = f"{region:03d}"
    bbb = random.randint(0, 499) if pol == 'muški' else random.randint(500, 999)
    bbb_str = f"{bbb:03d}"

    dd = f"{dan:02d}"
    mm = f"{mesec:02d}"
    gg = f"{godina % 100:02d}"
    jmbg12 = dd + mm + gg + rrr + bbb_str

    a = [int(c) for c in jmbg12]
    k = 11 - ((7 * (a[0] + a[6]) + 6 * (a[1] + a[7]) + 5 * (a[2] + a[8]) +
               4 * (a[3] + a[9]) + 3 * (a[4] + a[10]) + 2 * (a[5] + a[11])) % 11)
    if k > 9:
        k = 0

    jmbg = jmbg12 + str(k)
    jmbg_label.config(state='normal')
    jmbg_label.delete(0, END)
    jmbg_label.insert(0, jmbg)
    jmbg_label.config(state='readonly')

# Dugme za generaciju
Button(prozor, text='Generiši JMBG', command=generisi_osobu).pack(side=RIGHT)

# Start aplikacije
prozor.mainloop()
