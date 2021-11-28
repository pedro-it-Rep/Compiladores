from Constants.Simbolos import Simbolos
from Models.TabelaSimbolos import TabelaDeSimbolos
from Constants.Tipos import Tipos
from Constants.Errors import Errors


class Semantico:
    prioridade = []
    posOrdemExpression = []
    termo = ""
    lexema = ""

    def definePrioridades(self, prioridade):
        if prioridade == Simbolos.Ou:
            return 1
        elif prioridade == Simbolos.E:
            return 2
        elif prioridade == Simbolos.Nao:
            return 3
        elif prioridade == Simbolos.Maior:
            return 4
        elif prioridade == Simbolos.MaiorIgual:
            return 4
        elif prioridade == Simbolos.Menor:
            return 4
        elif prioridade == Simbolos.MenorIgual:
            return 4
        elif prioridade == Simbolos.Diferente:
            return 4
        elif prioridade == Simbolos.Menos:
            return 5
        elif prioridade == Simbolos.Mais:
            return 5
        elif prioridade == Simbolos.Divisao:
            return 6
        elif prioridade == Simbolos.Multiplicacao:
            return 6
        elif prioridade == Simbolos.Negativo:
            return 7
        elif prioridade == Simbolos.Positivo:
            return 7
        elif prioridade == Simbolos.AbreParenteses:
            return 0
        else:
            return -1

    def pilhaVazia(self, pilhain):
        if not pilhain:
            return True
        else:
            return False

    def analisaExpressao(self, expressao, tipo):
        types = []
        for self.termo in expressao:
            print(self.termo)
            if self.termo[1] == Simbolos.Ou or \
                    self.termo[1] == Simbolos.E or \
                    self.termo[1] == Simbolos.Nao or \
                    self.termo[1] == Simbolos.Maior or \
                    self.termo[1] == Simbolos.MaiorIgual or \
                    self.termo[1] == Simbolos.Menor or \
                    self.termo[1] == Simbolos.MenorIgual or \
                    self.termo[1] == Simbolos.Igual or \
                    self.termo[1] == Simbolos.Diferente or \
                    self.termo[1] == Simbolos.Mais or \
                    self.termo[1] == Simbolos.Menos or \
                    self.termo[1] == Simbolos.Multiplicacao or \
                    self.termo[1] == Simbolos.Divisao or \
                    self.termo[1] == Simbolos.Positivo or \
                    self.termo[1] == Simbolos.Negativo:
                if self.termo[1] == Simbolos.Nao or\
                        self.termo[1] == Simbolos.Positivo or\
                        self.termo[1] == Simbolos.Negativo:
                    pass
                if self.termo[1] == Simbolos.E or self.termo[1] == Simbolos.Ou:
                    if types[len(types) - 1] != Tipos.Boolean and types[len(types) - 2] != Tipos.Boolean:
                        #exit("Erro de tipo bool com int, ou tipo errado")
                        Errors.conflictTypeBool(Errors)

                    x = types[len(types) - 1]
                    types.remove(x)

                if self.termo[1] == Simbolos.Maior or \
                        self.termo[1] == Simbolos.MaiorIgual or \
                        self.termo[1] == Simbolos.Menor or \
                        self.termo[1] == Simbolos.MenorIgual or \
                        self.termo[1] == Simbolos.Igual or \
                        self.termo[1] == Simbolos.Diferente:
                    if types[len(types) - 1] != Tipos.Inteiro and types[len(types) - 2] != Tipos.Inteiro:
                        #exit("Erro de tipos")
                        Errors.conflictTypeInt(Errors)
                    x = types[len(types) - 1]
                    types.remove(x)
                    x = types[len(types) - 1]
                    types.remove(x)
                    types.append(Tipos.Boolean)

                if self.termo[1] == Simbolos.Mais or \
                        self.termo[1] == Simbolos.Menos or \
                        self.termo[1] == Simbolos.Multiplicacao or \
                        self.termo[1] == Simbolos.Divisao:
                    if types[len(types) - 1] != Tipos.Inteiro and types[len(types) - 2] != Tipos.Inteiro:
                        #exit("ERRO: Operador deve ser aplicado a um inteiro")
                        Errors.aplicationType(Errors)
                    x = types[len(types) - 1]
                    types.remove(x)

            else:
                if self.termo[1] == Simbolos.Numero:
                    types.append(Tipos.Inteiro)
                if self.termo[1] == Simbolos.Identificador:
                    aux = TabelaDeSimbolos.busca(TabelaDeSimbolos, self.termo[0])
                    if aux[1] == Tipos.Inteiro or aux[1] == Tipos.IntFunction:
                        types.append(Tipos.Inteiro)
                    elif aux[1] == Tipos.Boolean or aux[1] == Tipos.BoolFunction:
                        types.append(Tipos.Boolean)
                if self.termo[1] == Simbolos.Verdadeiro or self.termo[1] == Simbolos.Falso:
                    types.append(Tipos.Boolean)

        if tipo == Tipos.IntFunction or tipo == Tipos.Inteiro:
            if Tipos.Inteiro != types[0]:
                #exit("Expressao Incompativel")
                Errors.checkTypeInt(Errors)
        if tipo == Tipos.BoolFunction or tipo == Tipos.Boolean:
            if Tipos.Boolean != types[0]:
                #exit("Expressao booleano incompativel")
                Errors.checkTypeBool(Errors)

    def posOrdem(self, expressaoin):
        pilha = []
        i = 0
        self.posOrdemExpression = []
        for i in range(len(expressaoin)):
            self.termo = expressaoin[i]
            if self.termo[1] == Simbolos.Identificador or \
                    self.termo[1] == Simbolos.Numero or \
                    self.termo[1] == Simbolos.Positivo or \
                    self.termo[1] == Simbolos.Negativo:
                self.posOrdemExpression.append(self.termo)
            elif self.termo[1] == Simbolos.Ou or \
                    self.termo[1] == Simbolos.E or \
                    self.termo[1] == Simbolos.Nao or \
                    self.termo[1] == Simbolos.Maior or \
                    self.termo[1] == Simbolos.MaiorIgual or \
                    self.termo[1] == Simbolos.Menor or \
                    self.termo[1] == Simbolos.MenorIgual or \
                    self.termo[1] == Simbolos.Igual or \
                    self.termo[1] == Simbolos.Diferente or \
                    self.termo[1] == Simbolos.Mais or \
                    self.termo[1] == Simbolos.Menos or \
                    self.termo[1] == Simbolos.Multiplicacao or \
                    self.termo[1] == Simbolos.Divisao or \
                    self.termo[1] == Simbolos.Positivo or \
                    self.termo[1] == Simbolos.Negativo:
                while self.pilhaVazia(self, pilha) is False and\
                        self.definePrioridades(self, pilha[-1][1]) >= self.definePrioridades(self, self.termo[1]):
                    self.posOrdemExpression.append(pilha.pop())
                pilha.append(self.termo)
            elif self.termo[1] == Simbolos.AbreParenteses:
                pilha.append(self.termo)
            elif self.termo[1] == Simbolos.FechaParenteses:
                while pilha[-1][1] != Simbolos.AbreParenteses:
                    self.posOrdemExpression.append(pilha.pop())
                pilha.pop()
        while self.pilhaVazia(self, pilha) is False:
            self.posOrdemExpression.append(pilha.pop())
        return self.posOrdemExpression

    def removeSimbolo(self, variables):
        for i in variables:
            TabelaDeSimbolos.remove(TabelaDeSimbolos, i)
