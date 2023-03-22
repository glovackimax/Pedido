import tkinter as tk
import random

root = tk.Tk()
root.geometry('900x900')

def hover(event):
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    nao.place(x=x, y=y)

def mensagem():
    mensage = tk.Label(root, text= "Oi meu bem eu te amo")
    mensage.place(x=70, y=120, relx=0, rely=0)

pergunta = tk.Label(root, text="Quer namorar comigo???????????")
pergunta.pack(anchor="n", padx=20)

nao = tk.Button(root, text="Não", height= 3, width=15)
nao.place(x=140, y=80)
nao.bind("<Enter>", hover)


sim = tk.Button(root, text="Sim", height= 3, width=15)
sim.place(x=25, y=80, relx=0, rely=0)

root.mainloop()