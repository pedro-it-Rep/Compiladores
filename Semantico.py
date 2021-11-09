from Constants.Simbolos import Simbolos
from Models.TabelaSimbolos import TabelaDeSimbolos
from Constants.Tipos import Tipos


class Semantico:
    prioridade = []
    posOrdemExpression = []
    termo = ""
    simbolo = ""

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

    def defineSimbolo(self, simbolo):
        if simbolo == "ou":
            return Simbolos.Ou
        elif simbolo == "e":
            return Simbolos.E
        elif simbolo == "nao":
            return Simbolos.Nao
        elif simbolo == ">":
            return Simbolos.Menor
        elif simbolo == ">=":
            return Simbolos.MaiorIgual
        elif simbolo == "<":
            return Simbolos.Menor
        elif simbolo == "<=":
            return Simbolos.MenorIgual
        elif simbolo == "!=":
            return Simbolos.Diferente
        elif simbolo == "-":
            return Simbolos.Menos
        elif simbolo == "+":
            return Simbolos.Mais
        elif simbolo == "div":
            return Simbolos.Divisao
        elif simbolo == "*":
            return Simbolos.Multiplicacao
        elif simbolo == "-u":
            return Simbolos.Negativo
        elif simbolo == "+u":
            return Simbolos.Positivo
        elif simbolo == ")":
            return Simbolos.FechaParenteses
        elif simbolo == "(":
            return Simbolos.AbreParenteses
        else:
            x = simbolo.isdigit()
            if x is True:
                return Simbolos.Numero
            else:
                return Simbolos.Identificador

    def pilhaVazia(self, pilhain):
        if not pilhain:
            return True
        else:
            return False

    def analisaExpressao(self, expressao, expreanterior):
        types = []
        i = 0
        for i in range(len(expressao)):
            token = expressao[i]
            self.termo = self.defineSimbolo(self, token)
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
                elif self.termo == Simbolos.E or self.termo == Simbolos.Ou:
                    if types[-1] != Tipos.Booleano and types[-2] != Tipos.Booleano:
                        exit("Erro de tipo bool com int, ou tipo errado")
                    types.pop()

                if self.termo == Simbolos.Maior or \
                        self.termo == Simbolos.MaiorIgual or \
                        self.termo == Simbolos.Menor or \
                        self.termo == Simbolos.MenorIgual or \
                        self.termo == Simbolos.Igual or \
                        self.termo == Simbolos.Diferente:
                    if types[-1] != Tipos.Inteiro and types[-2] != Tipos.Inteiro:
                        exit("Erro de tipos")
                    types.pop()
                    types.pop()
                    types.append(Tipos.Booleano)

                if self.termo == Simbolos.Mais or \
                        self.termo == Simbolos.Menos or \
                        self.termo == Simbolos.Multiplicacao or \
                        self.termo == Simbolos.Divisao:
                    if types[-1] != Tipos.Inteiro and types[-2] != Tipos.Inteiro:
                        types.pop()

            else:
                if self.termo == Simbolos.Numero:
                    types.append(Tipos.Inteiro)
                elif self.termo == Simbolos.Identificador:
                    TabelaDeSimbolos.search(TabelaDeSimbolos, token)
                    if TabelaDeSimbolos.id[1] == Tipos.Inteiro or TabelaDeSimbolos.id[1] == Tipos.IntFunction:
                        types.append(Tipos.Inteiro)
                    elif TabelaDeSimbolos.id[1] == Tipos.Booleano or TabelaDeSimbolos.id[1] == Tipos.BoolFunction:
                        types.append(Tipos.Booleano)
                elif token == Simbolos.Verdadeiro or token == Simbolos.Falso:
                    types.append(Tipos.Booleano)
        if expreanterior == Tipos.IntFunction or expreanterior == Tipos.Inteiro:
            if Tipos.Inteiro != types[0]:
                exit("Expressao Incompativel")
        if expreanterior == Tipos.BoolFunction or expreanterior == Tipos.Booleano:
            if Tipos.Booleano != types[0]:
                exit("Expressao booleano incompativel")

    def posOrdem(self, expressaoin):
        pilha = []
        i = 0
        self.posOrdemExpression = []
        for i in range(len(expressaoin)):
            sla = expressaoin[i]
            self.termo = self.defineSimbolo(self, sla)

            if self.termo == Simbolos.Identificador or \
                    self.termo == Simbolos.Numero or \
                    self.termo == Simbolos.Positivo or \
                    self.termo == Simbolos.Negativo:
                self.posOrdemExpression.append(sla)
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
                while self.pilhaVazia(self, pilha) is False and self.definePrioridades(self, pilha[-1]) >= self.definePrioridades(self, self.termo):
                    self.posOrdemExpression.append(pilha.pop())
                pilha.append(sla)
            elif self.termo == Simbolos.AbreParenteses:
                pilha.append(expressaoin[i])
            elif self.termo == Simbolos.FechaParenteses:
                aux = pilha[-1]
                aux_simbolo = self.defineSimbolo(self, aux)
                while aux_simbolo != Simbolos.AbreParenteses:
                    self.posOrdemExpression.append(pilha.pop())
                    aux = pilha[-1]
                    aux_simbolo = self.defineSimbolo(self, aux)
        while pilha:
            self.posOrdemExpression.append(pilha.pop())
        return self.posOrdemExpression

    def removeSimbolo(self, variables):
        for i in variables:
            TabelaDeSimbolos.remove(TabelaDeSimbolos, i)
