from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from Sintatico import Sintatico

class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title("Compiler")
        self.nossaTela.geometry('520x250')
        self.barra_menu = tk.Menu(self.nossaTela)
        self.nossaTela.config(menu=self.barra_menu)
        self.txtArea = Text(self.nossaTela, height=12)
        self.txtArea.grid(column=0, row=0, sticky='nsew')
        self.barra_menu.add_command(label="Open File", command=self.readFile)
        self.btn = ttk.Button(self.nossaTela, text="Compiler")
        self.btn.grid(column=0, row=1, sticky='w', padx=10, pady=10)



    def readFile(self):
        self.arquivo = filedialog.askopenfile(mode="r", title="Select a file",
                                              filetypes=(("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py")))
        self.conteudo = self.arquivo.read()
        self.txtArea.insert(tk.INSERT, self.conteudo)
        self.txtArea.insert('1.0', self.conteudo)


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
