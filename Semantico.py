#                           Modulo Semantico
# Direitos reservados por Fabricio Silva Cardoso e Pedro Ignácio Trevisan
#
# Programa responsavel por analisar de forma semantica o arquivo recebido no modulo lexical.
#
# Este modulo é responsavel por atribuir significado as variaveis e expressões encontradas
# ao longo do programa, onde essa análise e feita utilizando as funções em seu formato
# pós ordem, onde essa conversão tambem é realizadas nesse arquivo
#
# Todos os simbolos estão disponiveis no arquivo Simbolos.py
# Todos os tipos estão disponiveis no arquivo Tipos.py
#
# O intuito do programa é fazer uma analise completa da linguagem proposta
# pelo professor a ponto de compor um sistema, sendo este o nosso compilador.


from Constants.Simbolos import Simbolos
from Models.TabelaSimbolos import TabelaDeSimbolos
from Constants.Tipos import Tipos
from Constants.Errors import Errors


class Semantico:
    prioridade = []
    posOrdemExpression = []
    termo = ""
    lexema = ""

    # Define a prioridade de como os simbolos devem ser tratados
    # Caso essa prioriade não seja respeitada, teremos um funcionamento incorreto do modulo
    # Ordem utilizada
    # Aritméticos: (+ positivo, - negativo) (*,div) (+,-)
    # Relacionais: (todos iguais)
    # Lógicos: (não) (e) (ou)
    def definePrioridades(self, prioridade):
        # Maior valor -> Tratado antes
        # Ex: 7 * 5 + 10 -> Primeiro trata a multiplicação (Valor 6) e depois a soma (Valor 5)
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

    # Verifica se nossa pilha está vazia
    def pilhaVazia(self, pilhain):
        if not pilhain:
            return True
        else:
            return False

    # Realiza a analise da nossa expressão pós ordem baseado nas prioridades
    def analisaExpressao(self, expressao, tipo):
        types = []
        # termo = expressão[i], onde i inicia em 0 e vai até o tamanho máximo de expressão
        # expressão = [lexema, simbolo], então termo = expressao[i][lexema, simbolo]
        for self.termo in expressao:
            # Verifica se é algum simbolo que deve ser inserido na pilha
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
                # A tratativa é realizada no sintatico, aqui apenas verificamos se foi inserido corretamente durante
                # a conversão do pós ordem
                if self.termo[1] == Simbolos.Nao or\
                        self.termo[1] == Simbolos.Positivo or\
                        self.termo[1] == Simbolos.Negativo:
                    pass
                if self.termo[1] == Simbolos.E or self.termo[1] == Simbolos.Ou:
                    if types[len(types) - 1] != Tipos.Boolean and types[len(types) - 2] != Tipos.Boolean:
                        Errors.conflictTypeBool(Errors)

                    # E ou OU realizam a comparação utilizando booleano e booleano e seu resultado é em booleano,
                    # então não precisamos manter os dois, apenas um.
                    x = types[len(types) - 1]
                    types.remove(x)

                if self.termo[1] == Simbolos.Maior or \
                        self.termo[1] == Simbolos.MaiorIgual or \
                        self.termo[1] == Simbolos.Menor or \
                        self.termo[1] == Simbolos.MenorIgual or \
                        self.termo[1] == Simbolos.Igual or \
                        self.termo[1] == Simbolos.Diferente:
                    if types[len(types) - 1] != Tipos.Inteiro and types[len(types) - 2] != Tipos.Inteiro:
                        Errors.conflictTypeInt(Errors)
                    # Verificamos se a conta foi realizada utilizando apenas inteiros.
                    # Caso tenha sido feita de forma correta, devemos trocar os dois inteiros por um booleano, pois é o
                    # tipo gerado pela operação relacional
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
                        Errors.aplicationType(Errors)
                    # Operadores aritméticos realizam a comparação utilizando inteiro e inteiro e seu
                    # resultado é em inteiro, então não precisamos manter os dois, apenas um.
                    x = types[len(types) - 1]
                    types.remove(x)

            else:
                # Caso não seja nenhum simbolo, devemos verificar se é algum identificador, numero ou verdadeiro/falso
                if self.termo[1] == Simbolos.Numero:
                    types.append(Tipos.Inteiro)
                if self.termo[1] == Simbolos.Identificador:
                    # Realiza a busca para saber qual o tipo do identificador declarado
                    aux = TabelaDeSimbolos.busca(TabelaDeSimbolos, self.termo[0])
                    if aux[1] == Tipos.Inteiro or aux[1] == Tipos.IntFunction:
                        types.append(Tipos.Inteiro)
                    elif aux[1] == Tipos.Boolean or aux[1] == Tipos.BoolFunction:
                        types.append(Tipos.Boolean)
                if self.termo[1] == Simbolos.Verdadeiro or self.termo[1] == Simbolos.Falso:
                    types.append(Tipos.Boolean)

        if tipo == Tipos.IntFunction or tipo == Tipos.Inteiro:
            if Tipos.Inteiro != types[0]:
                Errors.checkTypeInt(Errors)
        if tipo == Tipos.BoolFunction or tipo == Tipos.Boolean:
            if Tipos.Boolean != types[0]:
                Errors.checkTypeBool(Errors)

    # Realiza a conversão da nossa expressão em pós ordem
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

    # Remove as variaveis definidas no escopo com a ajuda da tabela de simbolos
    def removeSimbolo(self, variables):
        for i in variables:
            TabelaDeSimbolos.remove(TabelaDeSimbolos, i)
