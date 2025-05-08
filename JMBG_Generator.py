from tkinter import *
import random

#verzija 1.2 vezba git-a
def random_jmbg():
    dan = random.randint(1, 31)
    mesec = random.randint(1, 12)
    godina = random.randint(1910, 2024)
    




prozor = Tk()
prozor.title("Random JMBG generator")
prozor.geometry("800x400")

Label(prozor, text = "Serbian person generator", font='italic').pack(pady='1')
Label(prozor, text = "Name").pack(pady='10', anchor='w')
Label(prozor, text = "Lastname").pack(pady='10', anchor='w')
Label(prozor, text="JMBG").pack(pady = '10', anchor = 'w')

#komentar koji treba da commitujem na git







prozor.mainloop()