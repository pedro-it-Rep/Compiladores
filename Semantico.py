from Constants.Simbolos import Simbolos
from Models.TabelaSimbolos import TabelaDeSimbolos
from Constants.Tipos import Tipos


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

    def analisaExpressao(self, expressao, tipo, lexema):
        types = []
        for self.termo in expressao:
            if self.termo == Simbolos.Ou or \
                    self.termo == Simbolos.E or \
                    self.termo == Simbolos.Nao or \
                    self.termo == Simbolos.Maior or \
                    self.termo == Simbolos.MaiorIgual or \
                    self.termo == Simbolos.Menor or \
                    self.termo == Simbolos.MenorIgual or \
                    self.termo == Simbolos.Igual or \
                    self.termo == Simbolos.Diferente or \
                    self.termo == Simbolos.Mais or \
                    self.termo == Simbolos.Menos or \
                    self.termo == Simbolos.Multiplicacao or \
                    self.termo == Simbolos.Divisao or \
                    self.termo == Simbolos.Positivo or \
                    self.termo == Simbolos.Negativo:
                if self.termo == Simbolos.Nao or\
                        self.termo == Simbolos.Positivo or\
                        self.termo == Simbolos.Negativo:
                    pass
                if self.termo == Simbolos.E or self.termo == Simbolos.Ou:
                    if types[len(types) - 1] != Tipos.Booleano and types[len(types) - 2] != Tipos.Booleano:
                        exit("Erro de tipo bool com int, ou tipo errado")

                    x = types[len(types) - 1]
                    types.remove(x)
                    print(types)

                if self.termo == Simbolos.Maior or \
                        self.termo == Simbolos.MaiorIgual or \
                        self.termo == Simbolos.Menor or \
                        self.termo == Simbolos.MenorIgual or \
                        self.termo == Simbolos.Igual or \
                        self.termo == Simbolos.Diferente:
                    if types[len(types) - 1] != Tipos.Inteiro and types[len(types) - 2] != Tipos.Inteiro:
                        exit("Erro de tipos")
                    x = types[len(types) - 1]
                    types.remove(x)
                    x = types[len(types) - 1]
                    types.remove(x)
                    types.append(Tipos.Boolean)

                if self.termo == Simbolos.Mais or \
                        self.termo == Simbolos.Menos or \
                        self.termo == Simbolos.Multiplicacao or \
                        self.termo == Simbolos.Divisao:
                    if types[len(types) - 1] != Tipos.Inteiro and types[len(types) - 2] != Tipos.Inteiro:
                        exit("ERRO: Operador deve ser aplicado a um inteiro")
                    x = types[len(types) - 1]
                    types.remove(x)

            else:
                if self.termo == Simbolos.Numero:
                    types.append(Tipos.Inteiro)
                if self.termo == Simbolos.Identificador:
                    print(lexema)
                    aux = TabelaDeSimbolos.busca(TabelaDeSimbolos, lexema)
                    print(aux)
                    if aux[1] == Tipos.Inteiro or aux[1] == Tipos.IntFunction:
                        types.append(Tipos.Inteiro)
                    elif aux[1] == Tipos.Boolean or aux[1] == Tipos.BoolFunction:
                        types.append(Tipos.Boolean)
                if self.termo == Simbolos.Verdadeiro or self.termo == Simbolos.Falso:
                    types.append(Tipos.Boolean)
        if tipo == Tipos.IntFunction or tipo == Tipos.Inteiro:
            if Tipos.Inteiro != types[0]:
                exit("Expressao Incompativel")
        if tipo == Tipos.BoolFunction or tipo == Tipos.Boolean:
            if Tipos.Boolean != types[0]:
                exit("Expressao booleano incompativel")

    def posOrdem(self, expressaoin):
        pilha = []
        i = 0
        self.posOrdemExpression = []
        for i in range(len(expressaoin)):
            self.termo = expressaoin[i][1]
            if self.termo == Simbolos.Identificador or \
                    self.termo == Simbolos.Numero or \
                    self.termo == Simbolos.Positivo or \
                    self.termo == Simbolos.Negativo:
                self.posOrdemExpression.append(self.termo)
            elif self.termo == Simbolos.Ou or \
                    self.termo == Simbolos.E or \
                    self.termo == Simbolos.Nao or \
                    self.termo == Simbolos.Maior or \
                    self.termo == Simbolos.MaiorIgual or \
                    self.termo == Simbolos.Menor or \
                    self.termo == Simbolos.MenorIgual or \
                    self.termo == Simbolos.Igual or \
                    self.termo == Simbolos.Diferente or \
                    self.termo == Simbolos.Mais or \
                    self.termo == Simbolos.Menos or \
                    self.termo == Simbolos.Multiplicacao or \
                    self.termo == Simbolos.Divisao or \
                    self.termo == Simbolos.Positivo or \
                    self.termo == Simbolos.Negativo:
                while self.pilhaVazia(self, pilha) is False and self.definePrioridades(self, pilha[-1][1]) >= self.definePrioridades(self, self.termo[0][1]):
                    self.posOrdemExpression.append(pilha.pop())
                pilha.append(self.termo)
            elif self.termo == Simbolos.AbreParenteses:
                pilha.append(self.termo)
            elif self.termo == Simbolos.FechaParenteses:
                while pilha[-1][1] != Simbolos.AbreParenteses:
                    self.posOrdemExpression.append(pilha.pop())
                pilha.pop()
        while self.pilhaVazia(self, pilha) is False:
            self.posOrdemExpression.append(pilha.pop())
        return self.posOrdemExpression

    def removeSimbolo(self, variables):
        for i in variables:
            TabelaDeSimbolos.remove(TabelaDeSimbolos, i)
