from Lexico import Lexico


def exceptionCloseParenteses():
    exit("Analisador Sintatico -> Linha : {}, missing '}' ".format((Lexico.n_line + 1)))


def exceptionPontoVirgula():
    exit("Analisador Sintatico -> Linha : {}, token ';' esperado.".format((Lexico.n_line + 1)))


def exceptionInvalidExpression():
    exit("Analisador Sintatico -> Linha : expressao invalida.".format((Lexico.n_line + 1)))


def exceptionInvalidProcIndentifier():
    exit("Analisador Sintatico -> Linha : {} nome de procedimento, identificador esperado.".format(
        (Lexico.n_line + 1)))


def exceptionInvalidIfDo():
    exit("Analisador Sintatico -> Linha : {}, comando 'entao' esperado.".format((Lexico.n_line + 1)))


def exceptionMissingDo():
    exit("Analisador Sintatico -> Linha : {}, comando 'faca' esperado.".format((Lexico.n_line + 1)))


def exceptionAbreParenteses():
    exit("Analisador Sintatico -> Linha : {}, token '(' esperado.".format((Lexico.n_line + 1)))


def exceptionMissingIdentifier():
    exit("Analisador Sintatico -> Linha : {}, token 'identificador' esperado.".format((Lexico.n_line + 1)))


def exceptionTypeInvalid():
    exit("Analisador Sintatico -> Linha : {}, tipo de variavel invalido, esperado 'boolean' ou 'inteiro'.".format((Lexico.n_line + 1)))


def exceptionVaribleIdentifier():
    exit("Analisador Sintatico -> Linha : {}, nome de variavel, token identificador esperado.".format(
        (Lexico.n_line + 1)))


def exceptionMissingPontos():
    exit("Analisador Sintatico -> Linha : {}, token ',' ou ':' esperado.".format((Lexico.n_line + 1)))

def exceptionMissingDoisPontos():
    exit("Analisador Sintatico -> Linha : {}, token ':' esperado.".format((Lexico.n_line + 1)))


def exceptionWrongPontos():
    exit("Analisador Sintatico -> Linha : {}, token invalido ':' apos ','.".format((Lexico.n_line + 1)))


def exceptionMissingPrograma():
    exit("Analisador Sintatico -> Linha : {}, programa deve iniciar com o token 'programa'.".format(
        (Lexico.n_line + 1)))


def exceptionWrongSpace():
    exit("Analisador Sintatico -> Linha : {}, código após finalização do programa.".format((Lexico.n_line + 1)))


def exceptionMissingDot():
    exit("Analisador Sintatico -> Linha : {}, token '.' esperado.".format((Lexico.n_line + 1)))


def exceptionMissingStart():
    exit("Analisador Sintatico -> Linha : {}, missing start.".format((Lexico.n_line + 1)))