from Lexico import Lexico

class TabelaDeSimbolos:

    tabela = []
    simbolo = ""
    lexema = ""

    def insere(self, tipo, escopo, end_mem):
        self.tabela.append([tipo, Lexico.lexema, escopo, end_mem])

    def remove(self):
        self.tabela.remove(self.simbolo)

    def searchIndex(self):
        for self.simbolo in self.tabela:
            self.simbolo = self.tabela
            if(Lexico.lexema == self.lexema):
                return self.tabela.index(self.simbolo)

        return -1

    def busca(self):
        self.simbolo = self.searchIndex(self.lexema)
        if self.simbolo != None:
            return self.simbolo
        else:
            return None
