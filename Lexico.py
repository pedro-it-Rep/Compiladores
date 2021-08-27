from tkinter.filedialog import askopenfilename
from Constants.Simbolos import Simbolos


class Lexico:
    file_path = askopenfilename()
    print(file_path)
    file = open(file_path, "r")
    line = 0
    caracter = ""
    lexema = ""
    simbolo = -1

    def Lexico(self):
        source = self.file
        try:
            self.caracter = source.read(1)
            self.Token(self)
        except:
            print("error")

    def Token(self):
        while self.caracter == 10:
            self.caracter = self.file.read(1)
            self.line = self.line + 1
            print("while1 token")

        while self.caracter != -1 and (self.caracter == "{" or self.caracter == 8 or self.caracter == 9):
            # -1 -> Caracter invalido // 8 -> Escreva // 9 -> Leia
            if self.caracter == '{':  # Caso seja um comentario, apenas ignora
                while self.caracter != -1 and self.caracter != '}':
                    if self.caracter == 10:
                        self.line = self.line + 1
                    self.caracter = self.file.read(1)
                    print("while2 e 3 token")

                self.caracter = self.file.read(1)
                print(self.caracter)
                self.caracter = self.file.read(1)
                print(self.caracter)

            while self.caracter != -1 and (self.caracter == 8 or self.caracter == 9 or self.caracter == 10):
                if self.caracter == 10:
                    self.line = self.line + 1

                self.caracter = self.file.read(1)

        if self.caracter != -1:
            print("call pegatoken")
            return self.pegaToken(self)

        return None

    def pegaToken(self):
        print("caracter: ", self.caracter)
        if self.caracter.isdigit():
            print("isDigit")
            return self.trataDigito(self)
        elif self.caracter.isalpha():
            return self.trataIeP(self)
        elif self.caracter == "+" or self.caracter == "-" or self.caracter == "*":
            return self.trataOA(self)
        elif self.caracter == "<" or self.caracter == ">" or self.caracter == "=":
            return self.trataOR(self)
        elif self.caracter == ";" or self.caracter == ":" or self.caracter == "(" or self.caracter == ".":
            return self.trataPontuacao(self)
        else:
            print("Error de caracter")

    def trataDigito(self):

        num = self.caracter
        self.caracter = self.file.read(1)
        while self.caracter.isdigit():
            num = num + self.caracter
            self.caracter = self.file.read(1)
        self.lexema = num
        self.simbolo = Simbolos.Inteiro

        return self.lexema, self.simbolo

    def trataIeP(self):
        id = self.caracter
        print("ID: ", id)
        self.caracter = self.file.read(1)
        print("Caracter trataIeP: ", self.caracter)

        while (self.caracter.isalpha() or self.caracter.isdigit()) or self.caracter == "_":  # MORRENDO AQUI
            id = id + self.caracter
            self.caracter = self.file.read(1)

        if id == "programa":
            self.simbolo = Simbolos.Programa
            print("lexico: ", id + " simbolo: ", self.simbolo)
            return id, self.simbolo
        elif id == "se":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Se
            return id, self.simbolo
        elif id == "entao":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Entao
            return id, self.simbolo
        elif id == "senao":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Senao
            return id, self.simbolo
        elif id == "enquanto":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Enquanto
            return id, self.simbolo
        elif id == "faca":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Faca
            return id, self.simbolo
        elif id == "inicio":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Inicio
            return id, self.simbolo
        elif id == "fim":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Fim
            return id, self.simbolo
        elif id == "escreva":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Escreva
            return id, self.simbolo
        elif id == "leia":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Leia
            return id, self.simbolo
        elif id == "var":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Var
            return id, self.simbolo
        elif id == "inteiro":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Inteiro
            return id, self.simbolo
        elif id == "booleano":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Booleano
            return id, self.simbolo
        elif id == "verdadeiro":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Verdadeiro
            return id, self.simbolo
        elif id == "falso":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Negativo
            return id, self.simbolo
        elif id == "procedimento":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Procedimento
            return id, self.simbolo
        elif id == "funcao":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Funcao
            return id, self.simbolo
        elif id == "div":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Divisao
            return id, self.simbolo
        elif id == "e":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.E
            return id, self.simbolo
        elif id == "ou":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Ou
            return id, self.simbolo
        elif id == "nao":
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Nao
            return id, self.simbolo
        else:
            print("lexico: ", id + " simbolo: ", self.simbolo)
            self.simbolo = Simbolos.Identificador
            return id, self.simbolo

    def trataAtribuicao(self):
        id = self.caracter
        self.caracter = self.file.read(1)

        if self.caracter == "=":
            id = id + self.caracter
            self.simbolo = Simbolos.Atribuicao
            return id, self.simbolo
        else:
            self.simbolo = Simbolos.DoisPontos
            return id, self.simbolo

    def trataOA(self):
        self.lexema = self.caracter
        if self.caracter == "+":
            self.simbolo = Simbolos.Mais
            return self.lexema, self.simbolo
        elif self.caracter == "-":
            self.simbolo = Simbolos.Menos
            return self.lexema, self.simbolo
        else:
            self.simbolo = Simbolos.Multiplicacao
            return self.lexema, self.simbolo

    def trataOR(self):

        self.lexema = self.caracter

        if self.caracter == ">":
            self.simbolo = Simbolos.Maior
            return self.lexema, self.simbolo
        elif self.caracter == ">=":
            self.simbolo = Simbolos.MaiorIgual
            return self.lexema, self.simbolo
        elif self.caracter == "=":
            self.simbolo = Simbolos.Igual
            return self.lexema, self.simbolo
        elif self.caracter == "<":
            self.simbolo = Simbolos.Menor
            return self.lexema, self.simbolo
        elif self.caracter == "<=":
            self.simbolo = Simbolos.MenorIgual
            return self.lexema, self.simbolo
        else:
            self.simbolo = Simbolos.Diferente
            return self.lexema, self.simbolo

    def trataPontuacao(self):
        self.lexema = self.caracter

        if self.caracter == ";":
            self.simbolo = Simbolos.PontoVirgula
            return self.lexema, self.simbolo
        elif self.caracter == ",":
            self.simbolo = Simbolos.Virgula
            return self.lexema, self.simbolo
        elif self.caracter == "(":
            self.simbolo = Simbolos.AbreParenteses
            return self.lexema, self.simbolo
        elif self.caracter == ")":
            self.simbolo = Simbolos.FechaParenteses
            return self.lexema, self.simbolo
        else:
            self.simbolo = Simbolos.Ponto
            return self.lexema, self.simbolo
