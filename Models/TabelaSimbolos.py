from Constants.Errors import nameAlreadyUsed


class TabelaDeSimbolos:
    tabela = []
    simbolo = ""
    lexema = ""
    marca = "X"
    principal = "main"
    variavel = "variable"
    procedimento = "procedimento"
    mem = 0
    i = 0
    id = []

    def insereTabela(self, nome, tipo, escopo, mem):
        self.tabela.append([nome, tipo, escopo, mem])

    def remove(self):
        self.i = len(self.tabela) - 1
        while self.tabela[self.i][2] != self.marca:
            self.tabela.pop()
            self.i -= 1
        self.tabela[self.i][2] = ""

    def PesquisaDuplicVarTabela(self, name):
        self.i = len(self.tabela) - 1
        print(self.i)
        print(self.tabela[self.i][1])
        while self.tabela[self.i][2] != self.marca:
            if self.tabela[self.i][0] == name and self.tabela[self.i][1] == self.variavel:
                exit("Existe variavel duplicada")
                return True
            self.i -= 1
        while self.tabela[self.i][1] != self.principal:
            if self.tabela[self.i][0] == name and self.tabela[self.i][1] == self.variavel:
                exit("Existe algum procedimento ou função com esse mesmo nome")
                return True
            self.i -= 1
        return False

    def colocaTipo(self, tipo):
        self.i = len(self.tabela) - 1
        print(self.i)
        while self.tabela[self.i][1] != self.principal and self.i > 0:
            if self.tabela[self.i][1] == self.variavel:
                self.tabela[self.i][1] = tipo
            self.i -= 1
            print(self.i)
            print(self.tabela)

    def searchNameVariable(self, namevar):
        self.i = len(self.tabela) - 1
        while self.tabela[self.i][1] != self.principal:
            if self.tabela[self.i][0] == namevar:
                return True
            self.i -= 1
        return False

    def searchNameProc(self, nameproc):
        self.i = len(self.tabela) - 1
        while self.tabela[self.i][1] != self.principal:
            if self.tabela[self.i][0] == nameproc and self.tabela[self.i][1] == self.procedimento:
                return True
            self.i -= 1
        return False

    def searchNameFunc(self, namefunc):
        self.i = len(self.tabela) - 1
        while self.tabela[self.i][1] != self.principal:
            if self.tabela[self.i][1] == namefunc:
                return True
            self.i -= 1
        return False

    def search(self, nome):
        self.i = len(self.tabela) - 1
        while self.tabela[self.i][1] != self.principal:
            if self.tabela[self.i][0] == nome and (self.tabela[self.i][1] == "inteiro" or self.tabela[self.i][1] == "booleano"):
                self.id = self.tabela[self.i]
                return True
            self.i -= 1
        print("Nome não existe")
        return False


