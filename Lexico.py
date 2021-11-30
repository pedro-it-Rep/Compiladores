#                           Modulo Lexical
# Direitos reservados por Fabricio Silva Cardoso e Pedro Ignácio Trevisan
#
# Programa responsavel por analisar de forma lexical um arquivo recebido, onde
# este tem como caracteristicas ser parecido com a linguagem Pascal.
#
# Este modulo é responsavel por identificar os caracteres lidos de um arquivo
# de entrada e transforma-los em simbolos, onde estes serão analisados nos outros
# modulos desenvolvidos (Semantico.py e Sintatico.py).
#
# Todos os simbolos estão disponiveis no arquivo Simbolos.py
#
# O intuito do programa é fazer uma analise completa da linguagem proposta
# pelo professor a ponto de compor um sistema, sendo este o nosso compilador.


from Constants.Simbolos import Simbolos
from Constants.Errors import Errors


# Definição da classe. Definido desta forma para facilitar na transmissão das informações entre os modulos
class Lexico:
    file_path = None
    file = None
    maxChar, i, n_line = 0, 0, 0
    caracter = ''
    lexema = ""
    simbolo = -1

    # Função principal, responsavel por iniciar o fluxo principal do programa
    def Token(self):
        while self.caracter == '{' or self.caracter.isspace() and self.caracter != '':
            if self.caracter == '{':  # Caso seja um comentario, apenas ignora
                while self.caracter != '}' and self.caracter != '':
                    # Ler o comentario por completo
                    self.caracter = self.file.read(1)
                    self.i = self.i + 1

                self.caracter = self.file.read(1)
                self.i = self.i + 1

            while self.caracter.isspace() and self.caracter != '':
                # Por alguns problemas durante o desenvolvimento, é necessário verificar quando temos que pular linha
                if self.caracter == '\n':
                    self.n_line += 1
                self.caracter = self.file.read(1)
                self.i = self.i + 1

        if self.caracter != -1 and self.caracter != '':
            # Self.tokens recebe os lexemas e os simbolos, ficando com a seguinte informação: [Lexema, Simbolo]
            self.tokens = self.pegaToken(self, self.i)
            self.lexema = self.tokens[0]
            self.simbolo = self.tokens[1]

        return None

    # Responsavel por verificar qual é o tipo do caracter lido
    def pegaToken(self, i):
        # Recebe o caracter do fluxo principal e verifica qual seu tipo e qual função deve ser chamada
        if self.caracter.isdigit():
            return self.trataDigito(self, i)
        elif self.caracter.isalpha():
            return self.trataIeP(self, i)
        elif self.caracter == ":":
            return self.trataAtribuicao(self, i)
        elif self.caracter == "+" or self.caracter == "-" or self.caracter == "*":
            return self.trataOA(self, i)
        elif self.caracter == '<' or self.caracter == ">" or self.caracter == "=" or self.caracter == "!":
            return self.trataOR(self, i)
        elif self.caracter == ";" or self.caracter == "," or self.caracter == "(" or self.caracter == ")" or self.caracter == ".":
            return self.trataPontuacao(self)
        else:
            Errors.checkCaracter(Errors, self.n_line, self.caracter)

    # Trata caso o caracter lido seja um digito
    def trataDigito(self, i):

        num = ""
        num = num + self.caracter
        self.caracter = self.file.read(1)
        i = i + 1
        # Podemos ter digitos com várias casas, então é necessario verificar isso
        while self.caracter.isdigit():
            num = num + self.caracter
            self.caracter = self.file.read(1)
            i = i + 1
        self.lexema = num
        self.simbolo = Simbolos.Numero

        # Retorna o numero lido e o seu simbolo correspondente
        return self.lexema, self.simbolo

    # IeP = Idenficador e Palavra Reservada
    # Função responsavel por verificar se alguma declaração feita durante o programa está utilizando alguma
    # palavra reservada, caso não esteja então temos a declaração de um Identificador (Váriavel).
    def trataIeP(self, i):
        id = ""

        while (self.caracter.isalpha() or self.caracter.isdigit()) or self.caracter == "_":
            id = id + self.caracter
            self.caracter = self.file.read(1)
            i = i + 1

        # Bonito? Não, porém a utilização de switch case não funcionou conforme esperado
        if id == "programa":
            self.simbolo = Simbolos.Programa
            return id, self.simbolo
        elif id == "se":
            self.simbolo = Simbolos.Se
            return id, self.simbolo
        elif id == "entao":
            self.simbolo = Simbolos.Entao
            return id, self.simbolo
        elif id == "senao":
            self.simbolo = Simbolos.Senao
            return id, self.simbolo
        elif id == "enquanto":
            self.simbolo = Simbolos.Enquanto
            return id, self.simbolo
        elif id == "faca":
            self.simbolo = Simbolos.Faca
            return id, self.simbolo
        elif id == "inicio":
            self.simbolo = Simbolos.Inicio
            return id, self.simbolo
        elif id == "fim":
            self.simbolo = Simbolos.Fim
            return id, self.simbolo
        elif id == "escreva":
            self.simbolo = Simbolos.Escreva
            return id, self.simbolo
        elif id == "leia":
            self.simbolo = Simbolos.Leia
            return id, self.simbolo
        elif id == "var":
            self.simbolo = Simbolos.Var
            return id, self.simbolo
        elif id == "inteiro":
            self.simbolo = Simbolos.Inteiro
            return id, self.simbolo
        elif id == "booleano":
            self.simbolo = Simbolos.Booleano
            return id, self.simbolo
        elif id == "verdadeiro":
            self.simbolo = Simbolos.Verdadeiro
            return id, self.simbolo
        elif id == "falso":
            self.simbolo = Simbolos.Negativo
            return id, self.simbolo
        elif id == "procedimento":
            self.simbolo = Simbolos.Procedimento
            return id, self.simbolo
        elif id == "funcao":
            self.simbolo = Simbolos.Funcao
            return id, self.simbolo
        elif id == "div":
            self.simbolo = Simbolos.Divisao
            return id, self.simbolo
        elif id == "e":
            self.simbolo = Simbolos.E
            return id, self.simbolo
        elif id == "ou":
            self.simbolo = Simbolos.Ou
            return id, self.simbolo
        elif id == "nao":
            self.simbolo = Simbolos.Nao
            return id, self.simbolo
        else:
            self.simbolo = Simbolos.Identificador
            return id, self.simbolo

    # Realiza a tratativa de uma atribuição a um identificador
    def trataAtribuicao(self, i):
        id = ""
        id = id + self.caracter
        self.caracter = self.file.read(1)
        i = i + 1

        # Atribuição é identificada com ':=', então é necessario verificar se a ordem está sendo seguida
        if self.caracter != '=':
            self.simbolo = Simbolos.DoisPontos
            return id, self.simbolo
        else:
            id = id + self.caracter
            self.caracter = self.file.read(1)
            i = i + 1
            self.simbolo = Simbolos.Atribuicao
            return id, self.simbolo

    # OA = Operador Aritmético
    # Trata os simbolos aritméticos.
    # OBS: O simbolo de divisão é identificado por DIVI, por isso não tratamos ele aqui
    def trataOA(self, i):
        op = ""
        op = op + self.caracter

        if self.caracter == "+":
            self.simbolo = Simbolos.Mais
            self.caracter = self.file.read(1)
            i = i + 1
            return op, self.simbolo
        elif self.caracter == "-":
            self.simbolo = Simbolos.Menos
            self.caracter = self.file.read(1)
            i = i + 1
            return op, self.simbolo
        else:
            self.simbolo = Simbolos.Multiplicacao
            self.caracter = self.file.read(1)
            i = i + 1
            return op, self.simbolo

    # OR = Operador Relacional
    # Verifica se os operadores estão escritos de maneira correta
    def trataOR(self, i):
        operadorRelacional = ""
        operadorRelacional = operadorRelacional + self.caracter
        self.caracter = self.file.read(1)
        i = i + 1

        # Podemos ter !=, <=, <, >=, ==
        # Durante o desenvolvido, foi feita a verificação na ordem acima
        if operadorRelacional == '!':

            # !=
            if self.caracter == '=':
                operadorRelacional = operadorRelacional + self.caracter
                self.caracter = self.file.read(1)
                i = i + 1
                self.simbolo = Simbolos.Diferente
                return operadorRelacional, self.simbolo
            else:
                Errors.checkCaracter(Errors, self.n_line, self.caracter)
        # =
        elif operadorRelacional == '=':
            self.simbolo = Simbolos.Igual
            return operadorRelacional, self.simbolo

        elif operadorRelacional == "<":

            # <=
            if self.caracter == "=":
                operadorRelacional = operadorRelacional + self.caracter
                self.caracter = self.file.read(1)
                i = i + 1
                self.simbolo = Simbolos.MenorIgual
                return operadorRelacional, self.simbolo
            # <
            else:
                self.simbolo = Simbolos.Menor
                return operadorRelacional, self.simbolo
        else:
            # >=
            if self.caracter == '=':
                operadorRelacional = operadorRelacional + self.caracter
                self.caracter = self.file.read(1)
                i = i + 1
                self.simbolo = Simbolos.MaiorIgual
                return operadorRelacional, self.simbolo
            # >
            else:
                self.simbolo = Simbolos.Maior
                return operadorRelacional, self.simbolo

    # Trata os tipos de pontuação disponiveis no programa
    # OBS: As chaves ({ }) indicam comentário, então são tratadas no corpo principal do programa e não nessa função
    def trataPontuacao(self):
        pontuacao = ""
        pontuacao = pontuacao + self.caracter
        self.caracter = self.file.read(1)

        if pontuacao == ";":
            self.simbolo = Simbolos.PontoVirgula
            return pontuacao, self.simbolo
        elif pontuacao == ",":
            self.simbolo = Simbolos.Virgula
            return pontuacao, self.simbolo
        elif pontuacao == "(":
            self.simbolo = Simbolos.AbreParenteses
            return pontuacao, self.simbolo
        elif pontuacao == ")":
            self.simbolo = Simbolos.FechaParenteses
            return pontuacao, self.simbolo
        else:
            self.simbolo = Simbolos.Ponto
            return pontuacao, self.simbolo

    # Função utilizada para ler o arquivo de entrada
    def readfile(self):
        self.file = self.file_path
        for line in self.file:
            self.maxChar += len(line)
        self.file.seek(0, 0)
        self.caracter = self.file.read(1)