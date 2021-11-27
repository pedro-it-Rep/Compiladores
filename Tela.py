from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
#from Sintatico import Sintatico

class Tela:

    root = Tk()
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    button = Button(root, text="Compilar")
    text = Text(root, height=20)
    errLabel = LabelFrame(root, text="Errors")
    errText = Text(errLabel, height=10)

    arquivo = None

    def mainTela(self):

        self.root.resizable(False, False)
        self.root.title("Compilador")
        self.root.geometry("650x570")

        self.filemenu.add_command(label="Open", command=lambda : self.openFile(self))
        #self.filemenu.add_command(label="Save", command=lambda: self.saveFile(self))
        self.filemenu.add_command(label="Save as...", command=lambda : self.saveFileAs(self))

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.button.grid(row=1, column=0, sticky=E, padx=10, pady=10)
        self.button["command"]=lambda :self.compSint(self)

        self.text.grid(row=2, column=0, sticky=EW)

        self.errLabel.grid(row=3, column=0, sticky=EW)

        self.errText.pack()

        self.root.config(menu=self.menubar)
        self.root.mainloop()

    def openFile(self):
        self.text.delete("1.0",END)
        self.arquivo = askopenfile(mode="r", title="Select a file",
                              filetypes=(('All Files', '*.*'),("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py")))
        conteudo = self.arquivo.read()
        self.text.insert(END, conteudo)
        self.arquivo.close()

    #def saveFile(self):
        #text_file = open(self.arquivo, "w")
        #text_file.write(self.text.get(1.0,END))
        #text_file.close()

    def saveFileAs(self):
        self.arquivo = asksaveasfile(filetypes=(('All Files', '*.*'),("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py"))).name
        with open(self.arquivo, "w") as f:
            f.write(self.text.get("1.0",END))

    def compSint(self):
        if self.arquivo is None:
            print("Arquivo vazio")
        #Sintatico.Sintatico(Sintatico)

