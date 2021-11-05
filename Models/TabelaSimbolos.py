from Constants.Tipos import Tipos

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

    def removeVar(self, variables):
        self.simbolo = variables
        self.tabela.remove(self.simbolo)

    def isDeclaradoNoEscopo(self, Lexema): #REVER LOGICA DO ESCOPO
        i = len(self.tabela) - 1
        while i > 0:  # and not novo escopo
            if self.tabela[i][0] == Lexema:
                return True
            i -= 1
        return False

    def search(self, Lexema):
        for self.lexema in self.tabela:
            if self.lexema == Lexema:
                return True
        return False

    def colocaTipo(self, tipo):
        self.i = len(self.tabela) - 1
        while self.tabela[self.i][1] != self.principal and self.i > 0:
            if self.tabela[self.i][1] == self.variavel:
                self.tabela[self.i][1] = tipo
            self.i -= 1


    def searchNameVariable(self, namevar):
        self.i = len(self.tabela) - 1
        while self.tabela[self.i][1] != self.principal:
            if self.tabela[self.i][0] == namevar:
                return True
            self.i -= 1
        return False


    def getVariables(self):
        variables = []
        i = len(self.tabela) - 1
        while i > 0:  # and is novo escopo
            if self.tabela[i] == Tipos.Inteiro or self.tabela[i] == Tipos.Boolean:
                variables.append(self.tabela[i])
            i -= 1
        return variables

    def searchNameFunc(self, namefunc):
        self.i = len(self.tabela) - 1
        while self.tabela[self.i][1] != self.principal:
            if self.tabela[self.i][1] == namefunc:
                return True
            self.i -= 1
        return False