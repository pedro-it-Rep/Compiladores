from Constants.Tipos import Tipos


class TabelaDeSimbolos:
    tabela = []
    simbolo = ""
    lexema = ""
    mem = 0
    id = []

    def insereTabela(self, nome, tipo, escopo, mem):
        self.tabela.append([nome, tipo, escopo, mem])

    def remove(self, variable):
        self.tabela.remove(variable)

    def buscaIdex(self, lexema):
        for i in self.tabela:
            if i[0] == lexema:
                return self.tabela.index(i)
        return -1

    def busca(self, lexema):
        Index = self.buscaIdex(self, lexema)
        funcLexema = self.tabela[Index]
        if funcLexema is not None:
            return funcLexema
        else:
            return None

    def alteraTipo(self, tipo):
        for i in self.tabela:
            if i[1] == Tipos.Variavel and (tipo == Tipos.Inteiro or tipo == Tipos.Boolean):
                i[1] = tipo
            if i[1] == Tipos.Function and (tipo == Tipos.IntFunction or tipo == Tipos.BoolFunction):
                i[1] = tipo

    def removeEscopo(self):
        i = len(self.tabela) - 1
        while i > 0 and self.tabela[i][2] is not True:
            i -= 1
        self.tabela[i][2] = False

    def getVariables(self):
        variables = []
        i = len(self.tabela) - 1
        while i > 0 and self.tabela[i][2] is not True:
            if self.tabela[i][1] == Tipos.Inteiro or self.tabela[i][1] == Tipos.Boolean:
                variables.append(self.tabela[i])
            i -= 1
        return variables

    def isDeclaradoNoEscopo(self, lexema):
        i = len(self.tabela) - 1
        while i > 0 and self.tabela[i][2] is not True:
            if self.tabela[i][0] == lexema:
                return True
            i -= 1
        return False

    def isDeclarado(self, lexema):
        for i in self.tabela:
            if i[0] == lexema:
                return True
        return False
