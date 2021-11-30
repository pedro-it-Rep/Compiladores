#                           Modulo VM
# Direitos reservados por Fabricio Silva Cardoso e Pedro Ignácio Trevisan
#
# Programa responsável por analisar o arquivo gerado pelo compilador, modificar o arquivo e
# separar as intruções.
#
# Este módulo é responsável por gerar fazer formatação do arquivo e separar os comando e colocá-los em
# um vetor para fazer os futuros comandos.
#
#
# O intuito do programa é fazer uma analise completa da linguagem proposta
# pelo professor a ponto de compor um sistema, sendo este o nosso compilador.

class VM:
    endereco = 0
    funcao = ""
    numero1 = 0
    numero2 = 0
    comando = []
    lista = []
    i = 0
    k = 0
    l = 0
    maxSize = 0
    indexSize = 0
    caracter = ""
    instru = ""
    geral = []
    geralzao = []
    jmpPos = []
    lines = []
    auxprint = []

    #Função para chamar todas as funções que formatam o arquivo
    def main(self):
        self.replace(self)
        self.fileTolist(self)

        self.defineEnd(self)

        self.jmpEnd(self)
        self.newObjfile(self)

    #Substitui os "\t" por nada, os "\n" por  nada e os " " por "-", para separar cada endereço, intrução e parametros
    def replace(self, path):
        file = path
        with open(file) as f:
            line = f.readline().replace('\t', '').replace('\n', '').replace(' ', '-')
            self.lista.append(line)
            while line:
                line = f.readline().replace('\t', '').replace('\n', '').replace(' ', '-')
                self.lista.append(line)

    #Pega o endereço, intrução e parametros
    def fileTolist(self):
        self.maxSize = len(self.lista)
        #Faz até o final da lista
        #["START-"]["ALLOC-0-1-"]...
        for self.i in range(self.maxSize):
            self.k = 0
            # Tamanho do elemento do vetor
            self.indexSize = len(self.lista[self.i])
            self.instru = ''
            #Faz até o final de um determinado valor do vetor
            for self.k in range(self.indexSize):
                self.caracter = self.lista[self.i][self.k]
                if self.caracter != "-":
                    if self.caracter.isalpha():
                        #Forma a intrução
                        self.instru = self.instru + self.caracter
                    else:
                        #Forma o numero
                        self.instru = self.instru + self.caracter
                else:
                    # Gera o elemento do vetor separado
                    self.geral.append(self.instru)
                    self.instru = ''
            # Coloca o elemento do vetor separado em um vetor que vai guardar todas as instruções formatadas
            self.geralzao.append(self.geral)
            self.geral = []
        #Remove a ultima posição vazia do vetor
        self.geralzao.pop()

    #Após a formatação do arquivo e separado no vetor, é responsável por atribuir os endereços corretos
    def defineEnd(self):
        self.maxSize = len(self.geralzao)
        self.l = 0
        while self.l < self.maxSize:
            if self.geralzao[self.l][0] == "START":
                #Coloca o endereço antes de tudo
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "ALLOC":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "DALLOC":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "HLT":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "LDC":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "LDV":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "ADD":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "SUB":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "MULT":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "DIVI":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "INV":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "AND":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "OR":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "NEG":
                self.geralzao[self.l].insert(0, self.endereco)
                self.l += 1
            elif self.geralzao[self.l][0] == "CME":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "CMA":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "CEQ":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "CDIF":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "CMEQ":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "CMAQ":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "STR":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "JMP":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "JMPF":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "RETURN":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "RD":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "PRN":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            elif self.geralzao[self.l][0] == "CALL":
                self.geralzao[self.l].insert(0, self.endereco)
                self.endereco += 1
                self.l += 1
            else:
                # Guarda em um vetor os valores endereços dos NULLs e seus respectivos endereços
                self.jmpPos.append([self.geralzao[self.l][0], self.endereco])
                self.geralzao[self.l][0] = self.endereco
                self.endereco += 1
                self.l += 1

    # Verifica quais são os valores que o JMP, JMPF e CALL carregam e substituí pelos valores corretos
    def jmpEnd(self):
        self.i = 0
        while self.i < self.maxSize:
            if self.geralzao[self.i][1] == "JMP" or self.geralzao[self.i][1] == "JMPF" or self.geralzao[self.i][1] == "CALL":
                for k in range(len(self.jmpPos)):
                    if self.jmpPos[k][0] == self.geralzao[self.i][2]:
                        self.geralzao[self.i][2] = self.jmpPos[k][1]
            self.i += 1

    # Exibe os elementos desses vetores na tela para o usuário
    def newObjfile(self,tv):
        #tv é a tela principal
        self.maxSize = len(self.geralzao)
        self.l = 0
        while self.l < self.maxSize:
            if self.geralzao[self.l][1] == "START":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "ALLOC":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], self.geralzao[self.l][2], self.geralzao[self.l][3], ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "DALLOC":
                tv.insert('', 'end', values=(self.geralzao[self.l][0],self.geralzao[self.l][1], self.geralzao[self.l][2], self.geralzao[self.l][3],''))
                self.l += 1
            elif self.geralzao[self.l][1] == "HLT":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "LDC":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], self.geralzao[self.l][2], '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "LDV":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], self.geralzao[self.l][2], '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "ADD":
                self.l += 1
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
            elif self.geralzao[self.l][1] == "SUB":
                self.l += 1
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
            elif self.geralzao[self.l][1] == "MULT":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "DIVI":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "INV":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "AND":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "OR":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "NEG":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "CME":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "CMA":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "CEQ":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "CDIF":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "CMEQ":
                self.l += 1
            elif self.geralzao[self.l][1] == "CMAQ":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "STR":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], self.geralzao[self.l][2], '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "JMP":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], self.geralzao[self.l][2], '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "JMPF":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], self.geralzao[self.l][2], '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "NULL":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "RD":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "PRN":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1
            elif self.geralzao[self.l][1] == "CALL":
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], self.geralzao[self.l][2], '', ''))
                self.l += 1
            else:
                tv.insert('', 'end', values=(self.geralzao[self.l][0], self.geralzao[self.l][1], '', '', ''))
                self.l += 1

    # Mostra na tela os valores que foram pedidos para serem printados
    def printOutput(self, output, tv3):
        for i in output:
            tv3.insert('','end',values=i[1])