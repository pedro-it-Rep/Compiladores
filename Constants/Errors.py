from Lexico import Lexico

class Errors:

    def exceptionPontoVirgula(self):
        exit("Analisador Sintatico -> Linha : {}, token ';' esperado.".format((Lexico.n_line + 1)))

    def exceptionInvalidExpression(self):
        exit("Analisador Sintatico -> Linha : expressao invalida.".format((Lexico.n_line + 1)))

    def exceptionInvalidProcIndentifier(self):
        exit("Analisador Sintatico -> Linha : {} nome de procedimento, identificador esperado.".format(
            (Lexico.n_line + 1)))

    def exceptionInvalidIfDo(self):
        exit("Analisador Sintatico -> Linha : {}, comando se, 'entao' esperado.".format((Lexico.n_line + 1)))

    def exceptionMissingDo(self):
        exit("Analisador Sintatico -> Linha : {}, comando enquanto, 'faca' esperado.".format((Lexico.n_line + 1)))

    def exceptionAbreParenteses(self):
        exit("Analisador Sintatico -> Linha : {}, token '(' esperado.".format((Lexico.n_line + 1)))

    def exceptionMissingIdentifier(self):
        exit("Analisador Sintatico -> Linha : {}, token identificador esperado.".format((Lexico.n_line + 1)))

    def exceptionTypeInvalid(self):
        exit("Analisador Sintatico -> Linha : {}, tipo de variavel invalido.".format((Lexico.n_line + 1)))

    def exceptionVaribleIdentifier(self):
        exit("Analisador Sintatico -> Linha : {}, nome de variavel, token identificador esperado.".format(
            (Lexico.n_line + 1)))

    def exceptionMissingPontos(self):
        exit("Analisador Sintatico -> Linha : {}, token ',' ou ':' esperado.".format((Lexico.n_line + 1)))

    def exceptionWrongPontos(self):
        exit("Analisador Sintatico -> Linha : {}, token invalido ':' apos ','.".format((Lexico.n_line + 1)))

    def exceptionMissingPrograma(self):
        exit("Analisador Sintatico -> Linha : {}, programa deve iniciar com o token 'programa'.".format((Lexico.n_line + 1)))

    def exceptionMissingDot(self):
        exit("Analisador Sintatico -> Linha : {}, token '.' esperado.".format((Lexico.n_line + 1)))

    def exceptionWrongSpace(self):
        exit("Analisador Sintatico -> Linha : {}, código após finalização do programa.".format((Lexico.n_line + 1)))

    def exceptionMissingStart(self):
        exit("Analisador Sintatico -> Linha : {}, missing start.".format((Lexico.n_line + 1)))

    def exceptionCloseParenteses(self):
        exit("Analisador Sintatico -> Linha : {}, missing '}' ".format((Lexico.n_line + 1)))
