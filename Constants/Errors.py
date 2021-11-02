def exceptionCloseParenteses(line_no):
    exit("Analisador Sintatico -> Linha : {}, missing ')' ".format((line_no + 1)))


def exceptionPontoVirgula(line_no):
    exit("Analisador Sintatico -> Linha : {}, token ';' esperado.".format((line_no + 1)))


def exceptionInvalidExpression(line_no):
    exit("Analisador Sintatico -> Linha : expressao invalida.".format((line_no + 1)))


def exceptionInvalidProcIndentifier(line_no):
    exit("Analisador Sintatico -> Linha : {} nome de procedimento, identificador esperado.".format(
        (line_no + 1)))


def exceptionInvalidIfDo(line_no):
    exit("Analisador Sintatico -> Linha : {}, comando se, 'entao' esperado.".format((line_no + 1)))


def exceptionMissingDo(line_no):
    exit("Analisador Sintatico -> Linha : {}, comando enquanto, 'faca' esperado.".format((line_no + 1)))


def exceptionAbreParenteses(line_no):
    exit("Analisador Sintatico -> Linha : {}, token '(' esperado.".format((line_no + 1)))


def exceptionMissingIdentifier(line_no):
    exit("Analisador Sintatico -> Linha : {}, token identificador esperado.".format((line_no + 1)))


def exceptionTypeInvalid(line_no):
    exit("Analisador Sintatico -> Linha : {}, tipo de variavel invalido.".format((line_no + 1)))


def exceptionVaribleIdentifier(line_no):
    exit("Analisador Sintatico -> Linha : {}, nome de variavel, token identificador esperado.".format(
        (line_no + 1)))


def exceptionMissingPontos(line_no):
    exit("Analisador Sintatico -> Linha : {}, token ',' ou ':' esperado.".format((line_no + 1)))


def exceptionWrongPontos(line_no):
    exit("Analisador Sintatico -> Linha : {}, token invalido ':' apos ','.".format((line_no + 1)))


def exceptionMissingPrograma(line_no):
    exit("Analisador Sintatico -> Linha : {}, programa deve iniciar com o token 'programa'.".format(
        (line_no + 1)))


def exceptionWrongSpace(line_no):
    exit("Analisador Sintatico -> Linha : {}, código após finalização do programa.".format((line_no + 1)))


def exceptionMissingDot(line_no):
    exit("Analisador Sintatico -> Linha : {}, token '.' esperado.".format((line_no + 1)))


def exceptionMissingStart(line_no):
    exit("Analisador Sintatico -> Linha : {}, missing start.".format((line_no + 1)))

def nameAlreadyUsed(line_no):
    exit("Name in line already used")

def doubleVariable(line_no):
    exit("Nome de variavel ja usada")

def semanticoVariable():
    exit("Nome de variavel ja utilizada")

def nomeProc():
    exit("Nome de procimento já usado anteriormente")

def nomeFunc():
    exit("Nome de funçao usada anteriormente")

def notNome():
    exit("Nome não declarado")

def expressaoIncompativel(line_no):
    exit("Expressao Incompativel:{}").format((line_no + 1))
