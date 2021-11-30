#                           Modulo VMUI
# Direitos reservados por Fabricio Silva Cardoso e Pedro Ignácio Trevisan
#
# Programa responsável por mostrar o arquivo gerado pelo compilador, mostrar os valores da pilha e os valores.
#
# Este módulo é responsável por criar a interface da máquina virtual e ler o arquivo gerado pelo compilador.
#
#
# O intuito do programa é fazer uma analise completa da linguagem proposta
# pelo professor a ponto de compor um sistema, sendo este o nosso compilador.


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from MaquinaVirtual.VM import *
from MaquinaVirtual.Exec import Exec

class VMUI:

    # Declara a raiz da interface
    app = Tk()
    app.resizable(False, False)

    #Cria os títulos das áreas
    framepc = LabelFrame(app, text="Instruções", font=(20))
    frametv = LabelFrame(app, text="Código", font=(20))
    framestack = LabelFrame(app, text="Pilha", font=(20))
    frameoutput = LabelFrame(app, text="Dados", font=(20))

    #Criar as telas
    tv = ttk.Treeview(frametv, columns=('Linha', 'Instrução', 'Atributo 1', 'Atributo 2', 'Comentário'), show='headings',
                          height=20)
    tv2 = ttk.Treeview(framestack, columns=('Endereço', 'Valor'), show='headings', height=15)
    tv3 = ttk.Treeview(frameoutput, columns='Dados', show='headings')
    tv4 = ttk.Treeview(framepc, column=("Endereço","PC"), show="headings", heigh=2)

    #Cria o botão para compilar
    button = Button(app, text="Compilar", state="disabled")

    type_comp = -1

    def printVMUI(self):

        #Configura a raiz
        self.app.title("Máquina  Virtual")
        self.app.geometry("1000x900")
        self.app.configure(background="#dde")

        #Confira as áreas
        self.frametv.grid(row=1, column=0, sticky=W)
        self.framestack.grid(row=1, column=1, sticky=NE)
        self.framepc.grid(row=1,column=1, sticky=S)
        self.frameoutput.grid(row=2, column=0, sticky=W)

        #Cria um menu bar
        menubar = Menu(self.app)

        #Cria as opçoes do Menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open",command=lambda:self.lerArquivo(self))
        menubar.add_cascade(label="File", menu=filemenu)

        #Configura o botão
        self.button.grid(row=0, column=1, sticky=NE, padx=10, pady=10)
        self.button["command"]=lambda :self.comp(self)

        # Cria as colunas da tela "Código"
        self.tv.column('Linha', minwidth=0, width=90)
        self.tv.column('Instrução', minwidth=0, width=150)
        self.tv.column('Atributo 1', minwidth=0, width=100)
        self.tv.column('Atributo 2', minwidth=0, width=100)
        self.tv.column('Comentário', minwidth=0, width=250)
        self.tv.heading('Linha', text='LINHA')
        self.tv.heading('Instrução', text='INSTRUÇÃO')
        self.tv.heading('Atributo 1', text='ATRIBUTO 1')
        self.tv.heading('Atributo 2', text='ATRIBUTO 2')
        self.tv.heading('Comentário', text='COMENTÁRIO')
        self.tv.grid(row=1, column=0, sticky=W, pady=10, padx=20)

        # Cria as colunas da tela "Pilha"
        self.tv2.column('Endereço', minwidth=0, width=125)
        self.tv2.column('Valor', minwidth=0, width=125)
        self.tv2.heading('Endereço', text='Endereço')
        self.tv2.heading('Valor', text='Valor')
        self.tv2.grid(row=1, column=1, sticky=NE, pady=10, padx=3)

        # Cria as colunas da tela "Dados"
        self.tv3.column('Dados', minwidth=0, width=150)
        self.tv3.heading('Dados', text='Dados')
        self.tv3.grid(row=2, column=0, sticky=SW, padx=20, pady=15)

        # Cria as colunas da tela "Instruções"
        self.tv4.column("Endereço", minwidth=0, width=100)
        self.tv4.column("PC", minwidth=0, width=100)
        self.tv4.heading("Endereço", text="Endereço")
        self.tv4.heading("PC",text="PC")
        self.tv4.grid(column= 3, row= 3, sticky=S, padx=9, pady=5)

        # Cria o modo de compilar
        frameradio = LabelFrame(self.app, text="Modo de Compilar", font=(20))
        frameradio.grid(column=1, row=2, sticky=W)
        radioB1 = Radiobutton(frameradio, text="Default", command=lambda : self.printar(self,0))
        radioB1.grid(sticky=W)
        radioB2 = Radiobutton(frameradio, text='Rápido', command= lambda: self.printar(self,1))
        radioB2.grid(sticky=W)
        radioB3 = Radiobutton(frameradio, text='Passo-a-Passo', command=lambda: self.printar(self,2))
        radioB3.grid(sticky=W)

        self.app.config(menu=menubar)
        self.app.mainloop()


    #Le arquivo
    def lerArquivo(self):
        arquivo = filedialog.askopenfilename(title="Choose a file", filetypes=(("Obj File", "*.obj"),))
        VM.replace(VM, arquivo)
        VM.fileTolist(VM)
        VM.defineEnd(VM)
        VM.jmpEnd(VM)
        VM.newObjfile(VM, self.tv)

    # Função chamada na hora de compilar
    #Caso seja 1, executa o rápido, caso seja 2, executa o passo-a-passo, caso seja 0, não faz nada
    def comp(self):
        if self.type_comp == 1:
            #Envia o lugar aonde tem que imprimir as informações
            Exec.eitas = self.tv2
            Exec.eitas2 = self.app
            Exec.eitas4 = self.tv4
            Exec.exec2(Exec)
            VM.printOutput(VM, Exec.saida, self.tv3)
        elif self.type_comp == 2:
            Exec.eitas = self.tv2
            Exec.eitas4=self.tv4
            Exec.exec(Exec)
            if Exec.flag == 1:
                VM.printOutput(VM, Exec.saida, self.tv3)
                Exec.flag = 0
        else:
            pass

    #Cria o estilo do botão
    def printar(self,valor):
        if valor == 0:
            self.button["state"]="disabled"
            self.button["bg"]= "white"
        elif valor == 1:
            self.button["state"]="normal"
            self.button["bg"]="red"
            self.type_comp = valor
        else:
            self.button["state"]="normal"
            self.button["bg"]="blue"
            self.type_comp = valor