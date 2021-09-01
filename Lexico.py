from tkinter.filedialog import askopenfilename
from Constants.Simbolos import Simbolos


class Lexico:
    file_path = askopenfilename()
    maxChar, i = 0, 0
    file = open(file_path, "r")
    for line in file:
        #line = line.strip("\n")
        maxChar += len(line)
    print("Max: ", maxChar)
    file.seek(0, 0)
    print(file_path)
    caracter = ""
    lexema = ""
    simbolo = -1
    aux = []

    def Lexico(self):
        source = self.file
        self.caracter = source.read(1)
        self.Token(self)

    def Token(self):
        while self.i != self.maxChar:
            while self.caracter == '{' or self.caracter.isspace():
                if self.caracter == '{':  # Caso seja um comentario, apenas ignora
                    while self.caracter != '}':
                        # Ler o comentario por completo
                        self.caracter = self.file.read(1)
                        self.i = self.i + 1
                        if self.i == self.maxChar:
                            exit("EOF")

                    self.caracter = self.file.read(1)
                    self.i = self.i + 1

                while self.caracter.isspace():
                    self.caracter = self.file.read(1)
                    self.i = self.i + 1

            if self.caracter != -1:
                self.aux.append(self.pegaToken(self, self.i))
        print("Print Vet: ", self.aux)
        exit("Deu ruim")

    def pegaToken(self, i):
        print("caracter: ", self.caracter)
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
            print(self.aux)
            exit("Erro de caracter")

    def trataDigito(self, i):

        num = ""
        self.caracter = self.file.read(1)
        i = i + 1
        while self.caracter.isdigit():
            num = num + self.caracter
            self.caracter = self.file.read(1)
            i = i + 1
        self.lexema = num
        self.simbolo = Simbolos.Inteiro

        return self.lexema, self.simbolo

    def trataIeP(self, i):
        id = ""
        print("ID: ", id)
        # self.caracter = self.file.read(1)
        print("Caracter trataIeP: ", self.caracter)

        while (self.caracter.isalpha() or self.caracter.isdigit()) or self.caracter == "_":
            id = id + self.caracter
            print("ID2: ", id)
            self.caracter = self.file.read(1)
            i = i + 1

        if id == "programa":
            self.simbolo = Simbolos.Programa
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "se":
            self.simbolo = Simbolos.Se
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "entao":
            self.simbolo = Simbolos.Entao
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "senao":
            self.simbolo = Simbolos.Senao
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "enquanto":
            self.simbolo = Simbolos.Enquanto
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "faca":
            self.simbolo = Simbolos.Faca
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "inicio":
            self.simbolo = Simbolos.Inicio
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "fim":
            self.simbolo = Simbolos.Fim
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "escreva":
            self.simbolo = Simbolos.Escreva
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "leia":
            self.simbolo = Simbolos.Leia
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "var":
            self.simbolo = Simbolos.Var
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "inteiro":
            self.simbolo = Simbolos.Inteiro
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "booleano":
            self.simbolo = Simbolos.Booleano
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "verdadeiro":
            self.simbolo = Simbolos.Verdadeiro
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "falso":
            self.simbolo = Simbolos.Negativo
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "procedimento":
            self.simbolo = Simbolos.Procedimento
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "funcao":
            self.simbolo = Simbolos.Funcao
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "div":
            self.simbolo = Simbolos.Divisao
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "e":
            self.simbolo = Simbolos.E
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "ou":
            self.simbolo = Simbolos.Ou
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "nao":
            self.simbolo = Simbolos.Nao
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        else:
            self.simbolo = Simbolos.Identificador
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo

    def trataAtribuicao(self, i):
        id = ""
        id = id + self.caracter
        self.caracter = self.file.read(1)
        i = i + 1

        if self.caracter != '=':
            self.simbolo = Simbolos.DoisPontos
            return id, self.simbolo
        else:
            id = id + self.caracter
            self.caracter = self.file.read(1)
            i = i + 1
            self.simbolo = Simbolos.Atribuicao
            return id, self.simbolo

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

    def trataOR(self, i):
        operadorRelacional = ""
        operadorRelacional = operadorRelacional + self.caracter
        self.caracter = self.file.read(1)
        i = i + 1

        if operadorRelacional == '!':

            if self.caracter == '=':
                operadorRelacional = operadorRelacional + self.caracter
                self.caracter = self.file.read(1)
                i = i + 1
                self.simbolo = Simbolos.Diferente
                return operadorRelacional, self.simbolo
            else:
                exit("Caracter Invalido")
        elif operadorRelacional == '=':
            self.simbolo = Simbolos.Igual
            return operadorRelacional, self.simbolo

        elif operadorRelacional == "<":

            if self.caracter == "=":
                operadorRelacional = operadorRelacional + self.caracter
                self.caracter = self.file.read(1)
                i = i + 1
                self.simbolo = Simbolos.MenorIgual
                return operadorRelacional, self.simbolo
            else:
                self.simbolo = Simbolos.Menor
                return operadorRelacional, self.simbolo
        else:
            if self.caracter == '=':
                operadorRelacional = operadorRelacional + self.caracter
                self.caracter = self.file.read(1)
                i = i + 1
                self.simbolo = Simbolos.MaiorIgual
                return operadorRelacional, self.simbolo
            else:
                self.simbolo = Simbolos.Maior
                return operadorRelacional, self.simbolo

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
