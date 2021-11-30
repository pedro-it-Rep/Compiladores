#                           Modulo Tabela de Símbolos
# Direitos reservados por Fabricio Silva Cardoso e Pedro Ignácio Trevisan
#
# Programa responsavel por guardar as informações e os indetificadores..
#
# Este módulo serve para verificar, armazaenar e buscar os identificadores.
#
# Todos os tipos estão disponiveis no arquivo Tipos.py
#
# O intuito do programa é fazer uma analise completa da linguagem proposta
# pelo professor a ponto de compor um sistema, sendo este o nosso compilador.

from Constants.Tipos import Tipos

class TabelaDeSimbolos:
    tabela = []
    simbolo = ""
    lexema = ""
    mem = 0
    id = []

    # Insere em uma lista ligada os identificadores
    def insereTabela(self, nome, tipo, escopo, mem):
        self.tabela.append([nome, tipo, escopo, mem])

    #Remove o identificador
    def remove(self, variable):
        self.tabela.remove(variable)

    #Busca qual posicão da tabela de simbolos agente quer
    def buscaIdex(self, lexema):
        i = len(self.tabela) - 1
        while i > 0:
            if self.tabela[i][0] == lexema:
                return i
            i -= 1
        return -1

    #Busca quem a gente quer na tabela de símbolos
    def busca(self, lexema):
        Index = self.buscaIdex(self, lexema)
        funcLexema = self.tabela[Index]
        if funcLexema is not None:
            return funcLexema
        else:
            return None

    def alteraTipo(self, tipo):
        for i in self.tabela:
            #i["nomdedoidentificador","tipodoidentifcador","layer,"mem"]
            if i[1] == Tipos.Variavel and (tipo == Tipos.Inteiro or tipo == Tipos.Boolean):
                i[1] = tipo
            if i[1] == Tipos.Function and (tipo == Tipos.IntFunction or tipo == Tipos.BoolFunction):
                i[1] = tipo

    #Deleta tudo até o layer e depois tira o layer
    def removeEscopo(self):
        i = len(self.tabela) - 1
        while i > 0 and self.tabela[i][2] is not True:
            i -= 1
        self.tabela[i][2] = False

    # Recebe todas as variaveis daquele escopo
    def getVariables(self):
        variables = []
        i = len(self.tabela) - 1
        while i > 0 and self.tabela[i][2] is not True:
            if self.tabela[i][1] == Tipos.Inteiro or self.tabela[i][1] == Tipos.Boolean:
                variables.append(self.tabela[i])
            i -= 1
        return variables

    #Verfica na tabela inteira se já foi declarado no layer/escopo
    def isDeclaradoNoEscopo(self, lexema):
        i = len(self.tabela) - 1
        while i > 0 and self.tabela[i][2] is not True:
            if self.tabela[i][0] == lexema:
                return True
            i -= 1
        return False

    #Verfica se já foi declarado na tabela inteira
    def isDeclarado(self, lexema):
        for i in self.tabela:
            # i recebe tudo da tabela
            # i["nomdedoidentificador","tipodoidentifcador","layer,"mem"]
            if i[0] == lexema:
                return True
        return False