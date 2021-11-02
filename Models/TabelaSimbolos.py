from Lexico import Lexico
from Constants.Tipos import Tipos


class TabelaDeSimbolos:
    tabela = []
    simbolo = ""
    lexema = ""
    tipo = ""

    def insere(self, tipo, escopo, end_mem):
        self.tabela.append([self.lexema, tipo, escopo, end_mem])

    def remove(self):
        self.tabela.remove(self.simbolo)

    def searchIndex(self):
        # Passa por todos os elementos do vetor -> for (x : tabela)
        for self.simbolo in self.tabela:
            self.lexema = self.tabela
            if Lexico.lexema == self.lexema:
                return self.tabela.index(self.simbolo)
        return -1

    def busca(self):
        self.simbolo = self.searchIndex(self.lexema)
        if self.simbolo is not None:
            return self.simbolo
        else:
            return None

    def alteraTipo(self):
        for self.simbolo in self.tabela:
            self.simbolo = self.tabela
            if self.simbolo == Tipos.Variavel and (self.tipo == Tipos.Inteiro or self.tipo == Tipos.Boolean):
                # setTipo
                pass
            if self.simbolo == Tipos.Function and (self.tipo == Tipos.IntFunction or self.tipo == Tipos.BoolFunction):
                # setTipo
                pass

    def clearScopo(self):
        i = len(self.tabela) - 1
        while i > 0:  # and not novo escopo
            i -= 1
            # novo escopo = false

    def getVariables(self):
        variables = []
        i = len(self.tabela) - 1
        while i > 0:  # and is novo escopo
            if self.tabela[i] == Tipos.Inteiro or self.tabela[i] == Tipos.Boolean:
                variables.append(self.tabela[i])
            i -= 1
        return variables

    def isDeclaradoNoEscopo(self):
        i = len(self.tabela) - 1
        while i > 0:  # and not novo escopo
            if self.tabela[i] == self.lexema:
                return True
        return False

    def isDeclarado(self):
        for self.simbolo in self.tabela:
            self.simbolo = self.tabela
            if self.simbolo == self.lexema:  # REVER
                return True
        return False