#from Tela import Tela
from tkinter import *

class Errors:

    sla = None
    content = ""
    linha = "Linha"

    def exceptionMissingPrograma(self, line_no):
        self.content = "Erro Sintático. O programa de iniciar com o token 'programa'."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "."+ " " + self.content))

    def exceptionCloseParenteses(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, missing ')' ".format((line_no + 1)))
        self.content = "Erro Sintático. Missing ')'."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionPontoVirgula(self,line_no):
        #exit("Analisador Sintatico -> Linha : {}, token ';' esperado.".format((line_no + 1)))
        self.content = "Erro Sintático. Token ';' esperado."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))

    def exceptionInvalidExpression(self, line_no):
        #exit("Analisador Sintatico -> Linha : expressao invalida.".format((line_no + 1)))
        self.content = "Erro Sintático. Expressão invalida."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionInvalidProcIndentifier(self, line_no):
        #exit("Analisador Sintatico -> Linha : {} nome de procedimento, identificador esperado.".format(
        #    (line_no + 1)))
        self.content = "Erro Sintático. Nome de procedimento, identificador esperado."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionInvalidIfDo(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, comando se, 'entao' esperado.".format((line_no + 1)))
        self.content = "Erro Sintático. Erro no 'se', 'entao esperado'."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionMissingDo(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, comando enquanto, 'faca' esperado.".format((line_no + 1)))
        self.content = "Erro Sintático. Comando 'enquanto', 'faca' esperado."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionAbreParenteses(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, token '(' esperado.".format((line_no + 1)))
        self.content = "Erro Sintático. Token '(' esperado."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionMissingIdentifier(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, token identificador esperado.".format((line_no + 1)))
        self.content = "Erro Sintático. Token identificador esperado."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionTypeInvalid(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, tipo de variavel invalido.".format((line_no + 1)))
        self.content = "Erro Semantico. Tipo de variavel invalido."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionVaribleIdentifier(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, nome de variavel, token identificador esperado.".format(
        #    (line_no + 1)))
        self.content = "Erro Sintático. Nome de variavel, token identificador esperado."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionMissingPontos(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, token ',' ou ':' esperado.".format((line_no + 1)))
        self.content = "Erro Sintático. Token ',' ou ':' esperado."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionWrongPontos(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, token invalido ':' apos ','.".format((line_no + 1)))
        self.content = "Erro Sintático. Token invalido ':' após ',' ."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))

    def exceptionWrongSpace(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, código após finalização do programa.".format((line_no + 1)))
        self.content = "Erro Sintático. Código após finalização do programa."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionMissingDot(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, token '.' esperado.".format((line_no + 1)))
        self.content = "Erro Sintático. Token '.' esperado."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))


    def exceptionMissingStart(self, line_no):
        #exit("Analisador Sintatico -> Linha : {}, missing start.".format((line_no + 1)))
        self.content = "Erro Sintático. Faltando o 'inicio' ."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))

    def exceptionDuplicateVariable(self, line_no):
        #exit("Analisador Semantico -> Linha : {}, variavel já declarada no escopo.".format((line_no + 1)))
        self.content = "Erro Semantico. Variável já declarada no escopo."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))

    def exceptionIdentifierNotDeclared(self, line_no):
        #exit("Analisador Semantico -> Linha : {}, identificador não declarada.".format((line_no + 1)))
        self.content = "Erro Sintático. Identificador não declarado."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))

    def nameAlreadyUsed(self, line_no):
        #exit("Name in line already used")
        self.content = "Erro Sintático. Nome já usado."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))

    def doubleVariable(self, line_no):
        #exit("Nome de variavel ja usada")
        self.content = "Erro Semantico. Váriavel já declarada anteriormente."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))

    def semanticoVariable(self, line_no):
        #exit("Nome de variavel ja utilizada")
        self.content = "Erro Semantico. Nome de váriavel já foi usada, tente outro nome."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))

    def nomeProc(self, line_no):
        #exit("Nome de procimento já usado anteriormente")
        self.content = "Erro Semantico. Nome do procedimento já usado anteriormente."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))

    def nomeFunc(self, line_no):
        #exit("Nome de funçao usada anteriormente")
        self.content = "Erro Semantico. Nome de função usado anteriormente."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))

    def expressaoIncompativel(self, line_no):
        #exit("Expressao Incompativel:{}").format((line_no + 1))
        self.content = "Erro Semantico. Expressão Incompatível."
        self.sla.insert(END, (self.linha + " " + str(line_no) + "." + " " + self.content))

    def conflictTypeBool(self):
        self.content = "Erro Semantico. Erro de tipo bool com int ou tipo errado."
        self.sla.insert(END, self.content)

    def conflictTypeInt(self):
        self.content = "Erro Semantico. Erro de tipo int com bool ou tipo errado."
        self.sla.insert(END, self.content)

    def aplicationType(self):
        self.content = "Erro Semantico. Operador deve ser aplicado a um inteiro."
        self.sla.insert(END, self.content)

    def checkTypeInt(self):
        self.content = "Erro Semantico. Expressão não inteiro incompatível."
        self.sla.insert(END, self.content)

    def checkTypeBool(self):
        self.content = "Erro Semantico. Expressão não booleano incompatível."
        self.sla.insert(END, self.content)

    def checkCaracter(self,n_line,caracter):
        self.content = "Erro Léxico. Caracter "
        self.sla.insert(END, (self.linha + " " + str(n_line) + ". " + self.content  + caracter + " " + "inválido."))