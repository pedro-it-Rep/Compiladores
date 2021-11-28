from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from Sintatico import Sintatico
from Lexico import Lexico
from Constants.Errors import Errors

class Tela:

    root = Tk()
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    text = Text(root, height=20)
    errLabel = LabelFrame(root, text="Errors")
    errText = Text(errLabel, height=10)

    def mainTela(self):

        self.root.resizable(False, False)
        self.root.title("Compilador")
        self.root.geometry("650x570")

        self.filemenu.add_command(label="Open", command=lambda : self.openFile(self))
        self.filemenu.add_command(label="Save as...", command=lambda : self.saveFileAs(self))

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        button = Button(self.root, text="Compilar",command=lambda :self.compSint(self))
        button.grid(row=1, column=0, sticky=E, padx=10, pady=10)

        self.text.grid(row=2, column=0, sticky=EW)

        self.errLabel.grid(row=3, column=0, sticky=EW)
        self.errText.pack()
        Errors.sla = self.errText

        self.root.config(menu=self.menubar)
        self.root.mainloop()

    def openFile(self):
        self.text.delete("1.0",END)
        self.arquivo = askopenfile(mode="r", title="Select a file",
                              filetypes=(('All Files', '*.*'),("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py")))
        Lexico.file_path = self.arquivo
        conteudo = self.arquivo.read()
        self.text.insert(END, conteudo)
        Lexico.readfile(Lexico)

    def saveFileAs(self):

        self.arquivo = asksaveasfile(filetypes=(('All Files', '*.*'),("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py"))).name
        with open(self.arquivo, "w") as f:
            f.write(self.text.get("1.0",END))

    def compSint(self):
        if self.arquivo is not None:
            self.errText.delete(1.0,END)
            Sintatico.Sintatico(Sintatico)