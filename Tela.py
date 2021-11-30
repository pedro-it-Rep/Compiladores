#                           Modulo Tela
# Direitos reservados por Fabricio Silva Cardoso e Pedro Ignácio Trevisan
#
# Programa responsavel por criar uma interface para o usuário.
#
# Este módulo é responsável por criar um interface, onde o usuário possa interagir com o programa
# com mais facilidade e sabe qual será o resultado da sua compilação.
#
#
# O intuito do programa é fazer uma analise completa da linguagem proposta
# pelo professor a ponto de compor um sistema, sendo este o nosso compilador.



from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from Sintatico import Sintatico
from Lexico import Lexico
from Constants.Errors import Errors

class Tela:

    # Declara todos os widgets que serão usados
    # Raiz, barra de menu, tela de texto para colocar o algoritmo e tela de erro para colocar os erros
    root = Tk()
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    text = Text(root, height=20)
    errLabel = LabelFrame(root, text="Errors")
    errText = Text(errLabel, height=10)

    # Tela principal
    def mainTela(self):

        # Configura como vai ser a raiz da tela
        self.root.resizable(False, False)
        self.root.title("Compilador")
        self.root.geometry("650x570")

        # Criar as opçòes do menu e o que fazem

        self.filemenu.add_command(label="Open", command=lambda : self.openFile(self))
        self.filemenu.add_command(label="Save as...", command=lambda : self.saveFileAs(self))

        #Junta as opções do Menu
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        #Dá funcionalidade para o botão compilar
        button = Button(self.root, text="Compilar",command=lambda :self.compSint(self))
        #Configura o botão
        button.grid(row=1, column=0, sticky=E, padx=10, pady=10)
        #configura a tela do algoritmo
        self.text.grid(row=2, column=0, sticky=EW)
        #Configura a tela de erro
        self.errLabel.grid(row=3, column=0, sticky=EW)
        self.errText.pack()
        Errors.sla = self.errText

        self.root.config(menu=self.menubar)
        self.root.mainloop()

    #Abre arquivo
    def openFile(self):
        self.text.delete("1.0",END)
        self.arquivo = askopenfile(mode="r", title="Select a file",
                              filetypes=(('All Files', '*.*'),("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py")))
        Lexico.file_path = self.arquivo
        conteudo = self.arquivo.read()
        self.text.insert(END, conteudo)
        Lexico.readfile(Lexico)

    #Salva arquivo com o tipo desejado
    def saveFileAs(self):

        self.arquivo = asksaveasfile(filetypes=(('All Files', '*.*'),("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py"))).name
        with open(self.arquivo, "w") as f:
            f.write(self.text.get("1.0",END))
    #Funcão para compilar o arquivo
    def compSint(self):
        if self.arquivo is not None:
            self.errText.delete(1.0,END)
            Sintatico.Sintatico(Sintatico)