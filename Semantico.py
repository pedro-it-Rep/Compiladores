from Models.TabelaSimbolos import TabelaDeSimbolos
from Constants.Simbolos import Simbolos

class Semantico:
    tabela = []
    prioridade = []
    lexema = ""

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

