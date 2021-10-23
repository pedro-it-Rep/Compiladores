from Constants.Tipos import Tipos
from Sintatico import *


class Semantico:
    expressao = []
    prioridade = []
    lexema = ""
    simbolo = -1
    line = 0

    def Semantico(self):
        self.definePrioridades()

    def definePrioridades(self):
        self.prioridade.append([Simbolos.Ou, 1])
        self.prioridade.append([Simbolos.E, 2])
        self.prioridade.append([Simbolos.Nao, 3])
        self.prioridade.append([Simbolos.Maior, 4])
        self.prioridade.append([Simbolos.MaiorIgual, 4])
        self.prioridade.append([Simbolos.Menor, 4])
        self.prioridade.append([Simbolos.MenorIgual, 4])
        self.prioridade.append([Simbolos.Diferente, 4])
        self.prioridade.append([Simbolos.Menos, 5])
        self.prioridade.append([Simbolos.Mais, 5])
        self.prioridade.append([Simbolos.Divisao, 6])
        self.prioridade.append([Simbolos.Multiplicacao, 6])
        self.prioridade.append([Simbolos.Negativo, 7])
        self.prioridade.append([Simbolos.Positivo, 7])
        self.prioridade.append([Simbolos.AbreParenteses, 0])

    def analisaExpressao(self, sin):

        types = []

        for i in self.expressao:
            self.simbolo = Lexico.simbolo
            if self.simbolo == Simbolos.Ou or self.simbolo == Simbolos.E or self.simbolo == Simbolos.Nao or \
                    self.simbolo == Simbolos.Maior or self.simbolo == Simbolos.MaiorIgual or \
                    self.simbolo == Simbolos.Menor or self.simbolo == Simbolos.MenorIgual or \
                    self.simbolo == Simbolos.Igual or self.simbolo == Simbolos.Diferente or \
                    self.simbolo == Simbolos.Mais or self.simbolo == Simbolos.Menos or \
                    self.simbolo == Simbolos.Multiplicacao or self.simbolo == Simbolos.Divisao or \
                    self.simbolo == Simbolos.Positivo or self.simbolo == Simbolos.Negativo:
                if self.simbolo == Simbolos.Positivo or self.simbolo == Simbolos.Negativo:
                    pass

                if self.simbolo == Simbolos.Divisao or self.simbolo == Simbolos.Multiplicacao or Simbolos.Mais or Simbolos.Menos:
                    if types[len(types) - 1] != Tipos.Inteiro and types[len(types) - 2] != Tipos.Inteiro:
                        exit("Operador deve ser aplicado a um Inteiro")

                    types.pop(len[types] - 1)

                if self.simbolo == Simbolos.Maior or self.simbolo == Simbolos.MaiorIgual or \
                        self.simbolo == Simbolos.Menor or self.simbolo == Simbolos.MenorIgual or \
                        self.simbolo == Simbolos.Igual or self.simbolo == Simbolos.Diferente:
                    if types[len(types) - 1] != Tipos.Inteiro and types[len(types) - 2] != Tipos.Inteiro:
                        exit("Operador deve ser aplicado a um Inteiro")

                    types.pop(len[types] - 1)
                    types.pop(len[types] - 1)
                    types.append(Tipos.Boolean)

                if self.simbolo == Simbolos.Nao or self.simbolo == Simbolos.E or self.simbolo == Simbolos.Ou:
                    if types[len(types) - 1] != Tipos.Boolean and types[len(types) - 2] != Tipos.Boolean:
                        exit("Operador deve ser aplicado a um Booleano")

                    types.pop(len[types] - 1)

            else:
                if self.simbolo == Simbolos.Numero:
                    types.append(Tipos.Inteiro)
                if self.simbolo == Simbolos.Identificador:
                    self.lexema = Lexico.lexema
                    TabelaDeSimbolos.busca(self.lexema)
                    if Sintatico.tipo == Tipos.IntFunction or Sintatico.tipo == Tipos.Inteiro:
                        types.append(Tipos.Inteiro)
                    elif Sintatico.tipo == Tipos.BoolFunction or Sintatico.tipo == Tipos.Boolean:
                        types.append(Tipos.Boolean)

                if Sintatico.tipo == Simbolos.Verdadeiro or Sintatico.tipo == Simbolos.Falso:
                    types.append(Tipos.Boolean)

        if sin.tipo == Tipos.IntFunction or sin.tipo == Tipos.Inteiro:
            if types[0] != Tipos.Inteiro:
                exit("Expressao de tipo incompativel")
        if sin.tipo == Tipos.BoolFunction or sin.tipo == Tipos.Boolean:
            if types[0] != Tipos.Boolean:
                exit("Expressao de tipo incompativel")

    def posOrdem(self):
        posOrdemExpression = []
        pilha = []

        for i in len(self.expressao):
            termo = self.expressao[i]

            if termo == Simbolos.Identificador or termo == Simbolos.Numero or termo == Simbolos.Verdadeiro or \
                    termo == Simbolos.Falso:
                posOrdemExpression.append(self.expressao[i])

            elif self.simbolo == Simbolos.Ou or self.simbolo == Simbolos.E or self.simbolo == Simbolos.Nao or \
                    self.simbolo == Simbolos.Maior or self.simbolo == Simbolos.MaiorIgual or \
                    self.simbolo == Simbolos.Menor or self.simbolo == Simbolos.MenorIgual or \
                    self.simbolo == Simbolos.Igual or self.simbolo == Simbolos.Diferente or \
                    self.simbolo == Simbolos.Mais or self.simbolo == Simbolos.Menos or \
                    self.simbolo == Simbolos.Multiplicacao or self.simbolo == Simbolos.Divisao or \
                    self.simbolo == Simbolos.Positivo or self.simbolo == Simbolos.Negativo:
                while pilha is not None and self.prioridade[pilha[-1]] >= self.prioriade[termo]:
                    posOrdemExpression.append(pilha.pop())
                pilha.append(self.expressao[i])
            elif termo == Simbolos.AbreParenteses:
                pilha.append(self.expressao[i])
            elif termo == Simbolos.FechaParenteses:
                while pilha[-1] != Simbolos.AbreParenteses:
                    posOrdemExpression.append(pilha.pop())
                pilha.pop()
            i += 1
        while pilha is not None:
            posOrdemExpression.append(pilha.pop())

        return posOrdemExpression

    def removeSimbolo(self, vars):
        i = 0
        for self.simbolo in vars[i]:
            self.simbolo = vars[i]
            TabelaDeSimbolos.tabela.remove(self.simbolo)

