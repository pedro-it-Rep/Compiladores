import Constants.Errors as Error
from Constants.Simbolos import Simbolos
from Lexico import Lexico
from Models.TabelaSimbolos import TabelaDeSimbolos
from Constants.Tipos import Tipos
from Semantico import Semantico
from GeradorCodigo import GeradorDeCodigo
from Constants.Comandos import Comandos


class Sintatico:
    tipo = ""
    found = None
    proxEnd = 0
    proxRotulo = 1
    rótulo = 0  # Delcarado aqui parar lembrar de mudar no futuro
    nível = "X"
    expressao = []
    posexpressao = []
    indentificador = []

    def Sintatico(self):
        GeradorDeCodigo.isCreated(GeradorDeCodigo)
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Programa:
            GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Start)
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.NomePrograma, True, None)
                Lexico.Token(Lexico)

                if Lexico.simbolo == Simbolos.PontoVirgula:
                    self.analisaBloco(self)
                    variables = TabelaDeSimbolos.getVariables(TabelaDeSimbolos)
                    GeradorDeCodigo.geraComando2Var(GeradorDeCodigo, Comandos.Deallocate,
                                                    (self.proxEnd - len(variables)), len(variables))
                    Semantico.removeSimbolo(variables)
                    TabelaDeSimbolos.removeEscopo(TabelaDeSimbolos)
                    self.proxEnd -= len(variables)

                    if Lexico.simbolo == Simbolos.Ponto:
                        GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Halt)
                        GeradorDeCodigo.closeFile(GeradorDeCodigo)
                        Lexico.Token(Lexico)

                        if Lexico.caracter == "":
                            print("Sucesso")
                            print(TabelaDeSimbolos.tabela)
                            return
                        else:
                            Error.exceptionWrongSpace(Lexico.n_line)
                    else:
                        Error.exceptionMissingDot(Lexico.n_line)
                else:
                    Error.exceptionPontoVirgula(Lexico.n_line)
            else:
                Error.exceptionMissingIdentifier(Lexico.n_line)
        else:
            Error.exceptionMissingPrograma(Lexico.n_line)

    def analisaBloco(self):
        Lexico.Token(Lexico)
        self.analisa_et_variaveis(self)
        self.analisaSubrotina(self)
        self.analisaComandos(self)

    def analisa_et_variaveis(self):
        if Lexico.simbolo == Simbolos.Var:
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                while Lexico.simbolo == Simbolos.Identificador:
                    self.analisaVariaveis(self)
                    if Lexico.simbolo == Simbolos.PontoVirgula:
                        Lexico.Token(Lexico)
                    else:
                        Error.exceptionInvalidExpression(Lexico.n_line)
            else:
                Error.exceptionMissingIdentifier(Lexico.n_line)

    def analisaVariaveis(self):
        while Lexico.simbolo != Simbolos.DoisPontos:
            nVars = 0
            if Lexico.simbolo == Simbolos.Identificador:
                if not TabelaDeSimbolos.isDeclaradoNoEscopo(TabelaDeSimbolos, Lexico.lexema):
                    TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.Variavel, False,
                                                  self.proxEnd + nVars)
                    nVars += 1
                    Lexico.Token(Lexico)
                    if Lexico.simbolo == Simbolos.Virgula or Lexico.simbolo == Simbolos.DoisPontos:

                        if Lexico.simbolo == Simbolos.Virgula:
                            Lexico.Token(Lexico)

                            if Lexico.simbolo == Simbolos.DoisPontos:
                                Error.exceptionWrongPontos(Lexico.n_line)
                    else:
                        Error.exceptionMissingPontos(Lexico.n_line)
                else:
                    Error.semanticoVariable()
            else:
                Error.exceptionVaribleIdentifier(Lexico.n_line)

        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, self.proxEnd, nVars)
        self.proxEnd += nVars

        Lexico.Token(Lexico)
        self.analisaTipo(self)

    def analisaTipo(self):
        if Lexico.simbolo != Simbolos.Inteiro and Lexico.simbolo != Simbolos.Booleano:
            Error.exceptionTypeInvalid(Lexico.n_line)

        if Lexico.simbolo == Simbolos.Inteiro:
            TabelaDeSimbolos.alteraTipo(TabelaDeSimbolos, Tipos.Inteiro)
        elif Lexico.simbolo == Simbolos.Booleano:
            TabelaDeSimbolos.alteraTipo(TabelaDeSimbolos, Tipos.Boolean)

        Lexico.Token(Lexico)

    def analisaComandos(self):
        if Lexico.simbolo == Simbolos.Inicio:
            Lexico.Token(Lexico)
            self.analisaComandoSimples(self)

            while Lexico.simbolo != Simbolos.Fim:
                if Lexico.simbolo == Simbolos.PontoVirgula:
                    Lexico.Token(Lexico)

                    if Lexico.simbolo != Simbolos.Fim:
                        self.analisaComandoSimples(self)
                else:
                    Error.exceptionPontoVirgula(Lexico.n_line)
            Lexico.Token(Lexico)
        else:
            Error.exceptionMissingStart(Lexico.n_line)

    def analisaComandoSimples(self):
        if Lexico.simbolo == Simbolos.Identificador:
            if TabelaDeSimbolos.isDeclarado(TabelaDeSimbolos, Lexico.lexema):
                self.analisa_atrib_chprocedimento(self)
            else:
                Error.exceptionIdentifierNotDeclared(Lexico.n_line)
        else:
            if Lexico.simbolo == Simbolos.Se:
                self.analisaSe(self)
            elif Lexico.simbolo == Simbolos.Enquanto:
                self.analisaEnquanto(self)
            elif Lexico.simbolo == Simbolos.Leia:
                self.analisaLeia(self)
            elif Lexico.simbolo == Simbolos.Escreva:
                self.analisaEscreva(self)
            else:
                self.analisaComandos(self)

    def analisa_atrib_chprocedimento(self):

        self.indentificador = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
        Lexico.Token(Lexico)

        if Lexico.simbolo == Simbolos.Atribuicao:
            self.analisaAtribuicao(self)
        else:
            self.chamadaProcedimento(self)

    def analisaLeia(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.AbreParenteses:
            Lexico.Token(Lexico)
            if Lexico.simbolo == Simbolos.Identificador:
                if TabelaDeSimbolos.isDeclarado(TabelaDeSimbolos, Lexico.lexema):
                    self.found = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
                    GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Read)
                    GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Store, self.found[3])

                    Lexico.Token(Lexico)
                    if Lexico.simbolo == Simbolos.FechaParenteses:
                        Lexico.Token(Lexico)
                    else:
                        Error.exceptionCloseParenteses(Lexico.n_line)
                else:
                    Error.exceptionMissingIdentifier(Lexico.n_line)
            else:
                exit("Identificador esperado")
        else:
            Error.exceptionAbreParenteses(Lexico.n_line)

    def analisaEscreva(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.AbreParenteses:
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                if TabelaDeSimbolos.isDeclarado(TabelaDeSimbolos, Lexico.lexema):
                    self.found = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
                    if self.found[1] == Tipos.IntFunction:
                        self.chamadaFuncao(self.found)
                        GeradorDeCodigo.geraComando1Var(Comandos.LoadValue, self.proxEnd - 1)
                    else:
                        GeradorDeCodigo.geraComando1Var(Comandos.LoadValue, self.indentificador[3])

                    GeradorDeCodigo.geraComando(Comandos.Print)
                    Lexico.Token(Lexico)

                    if Lexico.simbolo == Simbolos.FechaParenteses:
                        Lexico.Token(Lexico)
                    else:
                        Error.exceptionCloseParenteses(Lexico.n_line)
                else:
                    Error.exceptionMissingIdentifier(Lexico.n_line)
            else:
                exit("Identificador faltante")
        else:
            Error.exceptionAbreParenteses(Lexico.n_line)

    def analisaEnquanto(self):
        aux = self.proxRotulo
        self.proxRotulo += 1

        Lexico.Token(Lexico)

        self.analisaExpressao(self)
        self.subUnarios(self)
        self.expressao = Semantico.posOrdem(Semantico, self.expressao)
        self.geraExpressao(self)
        self.tipo = Tipos.Boolean
        Semantico.analisaExpressao(Semantico, self.expressao, self.tipo)
        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.JumpIfFalse, self.proxRotulo)
        aux2 = self.proxRotulo

        if Lexico.simbolo == Simbolos.Faca:
            Lexico.Token(Lexico)
            self.analisaComandoSimples(self)
            GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Jump, aux)

        else:
            Error.exceptionMissingDo(Lexico.n_line)

        GeradorDeCodigo.geraRotulo(GeradorDeCodigo, aux2)

    def analisaSe(self):

        Lexico.Token(Lexico)
        self.analisaExpressao(self)
        self.subUnarios(self)
        self.expressao = Semantico.posOrdem(Semantico, self.expressao)
        self.geraExpressao(self)
        self.tipo = Tipos.Boolean
        Semantico.analisaExpressao(Semantico, self.expressao, self.tipo)
        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.JumpIfFalse, self.proxRotulo)
        aux = self.proxRotulo
        self.proxRotulo += 1

        if Lexico.simbolo == Simbolos.Entao:
            Lexico.Token(Lexico)
            self.analisaComandoSimples(self)

            GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Jump, self.proxRotulo)
            aux2 = self.proxRotulo
            self.proxRotulo += 1
            GeradorDeCodigo.geraRotulo(GeradorDeCodigo, aux)

            if Lexico.simbolo == Simbolos.Senao:
                Lexico.Token(Lexico)
                self.analisaComandoSimples(self)
            GeradorDeCodigo.geraRotulo(GeradorDeCodigo, aux2)
        else:
            Error.exceptionInvalidIfDo(Lexico.n_line)

    def analisaSubrotina(self):

        while Lexico.simbolo == Simbolos.Procedimento or Lexico.simbolo == Simbolos.Funcao:
            if Lexico.simbolo == Simbolos.Procedimento:
                self.analisaDeclaracaoProc(self)
            else:
                self.analisaDeclaraFunc(self)

            if Lexico.simbolo == Simbolos.PontoVirgula:
                Lexico.Token(Lexico)
            else:
                Error.exceptionPontoVirgula(Lexico.n_line)

    def analisaDeclaraFunc(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Identificador:
            if not TabelaDeSimbolos.isDeclaradoNoEscopo(TabelaDeSimbolos, Lexico.lexema):
                TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.Function, True, None)
                GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Jump, self.proxRotulo)
                aux = self.proxRotulo
                self.proxRotulo += 1
                GeradorDeCodigo.geraRotulo(GeradorDeCodigo, self.proxRotulo)
                self.proxEnd += 2
                self.found = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
                self.found[3] = self.proxRotulo
                self.proxRotulo += 1

                Lexico.Token(Lexico)
                if Lexico.simbolo == Simbolos.DoisPontos:
                    Lexico.Token(Lexico)
                    if Lexico.simbolo == Simbolos.Inteiro or Lexico.simbolo == Simbolos.Booleano:
                        if Lexico.simbolo == Simbolos.Inteiro:
                            TabelaDeSimbolos.alteraTipo(TabelaDeSimbolos, Tipos.IntFunction)
                        else:
                            TabelaDeSimbolos.alteraTipo(TabelaDeSimbolos, Tipos.BoolFunction)
                        Lexico.Token(Lexico)
                        if Lexico.simbolo == Simbolos.PontoVirgula:
                            self.analisaBloco(self)
                            variables = TabelaDeSimbolos.getVariables(TabelaDeSimbolos)
                            Semantico.removeSimbolo(Semantico, variables)
                            TabelaDeSimbolos.removeEscopo(TabelaDeSimbolos)
                            self.proxEnd -= len(variables)
                            GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Return)
                            self.proxEnd -= 2
                            GeradorDeCodigo.geraRotulo(aux)
                    else:
                        Error.exceptionTypeInvalid(Lexico.n_line)
                else:
                    Error.exceptionMissingPontos(Lexico.n_line)
            else:
                Error.nomeFunc(Lexico.n_line)
        else:
            Error.exceptionMissingIdentifier(Lexico.n_line)
        TabelaDeSimbolos.removeEscopo(TabelaDeSimbolos)

    def analisaDeclaracaoProc(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Identificador:
            if not TabelaDeSimbolos.isDeclaradoNoEscopo(TabelaDeSimbolos, Lexico.lexema):
                TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.Procedimento, True, None)
                GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Jump, self.proxRotulo)
                aux = self.proxRotulo
                self.proxRotulo += 1
                GeradorDeCodigo.geraRotulo(GeradorDeCodigo, self.proxRotulo)
                self.proxEnd += 1
                self.found = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
                self.found[3] = self.proxRotulo
                self.proxRotulo += 1

                Lexico.Token(Lexico)
                if Lexico.simbolo == Simbolos.PontoVirgula:
                    self.analisaBloco(self)
                    variables = TabelaDeSimbolos.getVariables(TabelaDeSimbolos)
                    GeradorDeCodigo.geraComando2Var(GeradorDeCodigo, Comandos.Deallocate, self.proxEnd - len(variables),
                                                    len(variables))
                    Semantico.removeSimbolo(Semantico, variables)
                    TabelaDeSimbolos.removeEscopo(TabelaDeSimbolos)
                    self.proxEnd -= len(variables)
                    GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Return)
                    self.proxEnd -= 1
                    GeradorDeCodigo.geraRotulo(aux)
                else:
                    Error.exceptionPontoVirgula(Lexico.n_line)
            else:
                Error.nomeProc(Lexico.n_line)
        else:
            Error.exceptionMissingIdentifier(Lexico.n_line)

    def analisaExpressao(self):
        self.analisaExpressaoSimples(self)
        if Lexico.simbolo == Simbolos.Maior or Lexico.simbolo == Simbolos.MaiorIgual or \
                Lexico.simbolo == Simbolos.Igual or Lexico.simbolo == Simbolos.Menor or \
                Lexico.simbolo == Simbolos.MenorIgual or Lexico.simbolo == Simbolos.Diferente:
            self.expressao.append(Lexico)
            Lexico.Token(Lexico)
            self.analisaExpressaoSimples(self)

    def analisaExpressaoSimples(self):
        if Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos:
            if Lexico.simbolo == Simbolos.Mais:
                TabelaDeSimbolos.tabela.append("+u")
            else:
                TabelaDeSimbolos.tabela.append("-u")
            Lexico.Token(Lexico)
        self.analisaTermo(self)
        while Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos or Lexico.simbolo == Simbolos.Ou:
            self.expressao.append(Lexico)
            Lexico.Token(Lexico)
            self.analisaTermo(self)

    def analisaTermo(self):
        self.analisaFator(self)
        while Lexico.simbolo == Simbolos.Multiplicacao or Lexico.simbolo == Simbolos.Divisao or Lexico.simbolo == Simbolos.E:
            self.expressao.append(Lexico)
            Lexico.Token(Lexico)
            self.analisaFator(self)

    def analisaFator(self):
        if Lexico.simbolo == Simbolos.Identificador:
            print(Lexico.lexema)
            if TabelaDeSimbolos.isDeclarado(TabelaDeSimbolos, Lexico.lexema):
                self.found = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
                if self.found[1] == Tipos.IntFunction or self.found[1] == Tipos.BoolFunction:
                    self.chamadaFuncao(self.found)
                self.expressao.append(Lexico)
                Lexico.Token(Lexico)
            else:
                Error.notNome()
        elif Lexico.simbolo == Simbolos.Numero:
            self.expressao.append(Lexico)
            Lexico.Token(Lexico)
        elif Lexico.simbolo == Simbolos.Nao:
            self.expressao.append(Lexico)
            Lexico.Token(Lexico)
            self.analisaFator(self)
        elif Lexico.simbolo == Simbolos.AbreParenteses:
            self.expressao.append(Lexico)
            Lexico.Token(Lexico)
            self.analisaExpressao(self)
            if Lexico.simbolo == Simbolos.FechaParenteses:
                self.expressao.append(Lexico)
                Lexico.Token(Lexico)
            else:
                Error.exceptionCloseParenteses(Lexico.n_line)
        elif Lexico.simbolo == Simbolos.Verdadeiro or Lexico.simbolo == Simbolos.Falso:
            self.expressao.append(Lexico)
            Lexico.Token(Lexico)
        else:
            Error.exceptionInvalidExpression(Lexico.n_line)

    def analisaAtribuicao(self):
        Lexico.Token(Lexico)
        self.analisaExpressao(self)
        self.subUnarios(self)
        self.expressao = Semantico.posOrdem(self.expressao)
        self.geraExpressao(self)
        Semantico.analisaExpressao(Semantico, self.expressao, self.indentificador)
        nVars = len(TabelaDeSimbolos.getVariables(TabelaDeSimbolos))

        if self.identificador[1] == Tipos.Boolean or self.identificador[1] == Tipos.IntFunction:
            GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Store, self.proxEnd - nVars - 2)
        else:
            GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Store, self.indentificador[3])

    def chamadaProcedimento(self):  # Gerador de codigo
        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Call, self.indentificador[3])

    def chamadaFuncao(self):  # Gerador de codigo
        Lexico.Token(Lexico)
        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadConst, 0)
        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Call, self.found[3])

    def subUnarios(self):
        i = 0
        while i < len(self.expressao):
            if self.expressao[i].simbolo == Simbolos.Mais or self.expressao[i].simbolo == Simbolos.Menos:
                if (i - 1) == -1 or self.expressao[i - 1].simbolo == Simbolos.AbreParenteses or \
                        self.expressao[i - 1].simbolo == Simbolos.Ou or self.expressao[i - 1].simbolo == Simbolos.E or \
                        self.expressao[i - 1].simbolo == Simbolos.Nao or self.expressao[
                    i - 1].simbolo == Simbolos.Maior or \
                        self.expressao[i - 1].simbolo == Simbolos.MaiorIgual or self.expressao[
                    i - 1].simbolo == Simbolos.Menor or \
                        self.expressao[i - 1].simbolo == Simbolos.MenorIgual or self.expressao[
                    i - 1].simbolo == Simbolos.Igual or \
                        self.expressao[i - 1].simbolo == Simbolos.Diferente or self.expressao[
                    i - 1].simbolo == Simbolos.Mais or \
                        self.expressao[i - 1].simbolo == Simbolos.Menos or self.expressao[
                    i - 1].simbolo == Simbolos.Multiplicacao or \
                        self.expressao[i - 1].simbolo == Simbolos.Divisao or self.expressao[
                    i - 1].simbolo == Simbolos.Positivo or \
                        self.expressao[i - 1].simbolo == Simbolos.Negativo:
                    if self.expressao[i].simbolo == Simbolos.Mais:
                        self.expressao[i].simbolo = Simbolos.Positivo
                    else:
                        self.expressao[i].simbolo = Simbolos.Negativo

    def geraExpressao(self):
        print(self.expressao)
        for i in self.expressao:
            if i[1] == Simbolos.Identificador:
                if TabelaDeSimbolos.isDeclarado(TabelaDeSimbolos, i[0]):
                    self.found = TabelaDeSimbolos.busca(TabelaDeSimbolos, i[0])
                    if self.found[1] == Tipos.Inteiro or self.found[1] == Tipos.Boolean:
                        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadValue, self.found[3])
                else:
                    Error.exceptionIdentifierNotDeclared(Lexico.n_line)
            elif Lexico.simbolo == Simbolos.Numero:
                GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadConst, Lexico.lexema)
            elif Lexico.simbolo == Simbolos.Verdadeiro:
                GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadConst, 1)
            elif Lexico.simbolo == Simbolos.Falso:
                GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadConst, 0)
            elif Lexico.simbolo == Simbolos.Ou:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Or)
            elif Lexico.simbolo == Simbolos.E:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.E)
            elif Lexico.simbolo == Simbolos.Nao:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Negate)
            elif Lexico.simbolo == Simbolos.Menor:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpLower)
            elif Lexico.simbolo == Simbolos.MenorIgual:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpLowerEqual)
            elif Lexico.simbolo == Simbolos.Maior:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpHigher)
            elif Lexico.simbolo == Simbolos.MaiorIgual:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpHigherEqual)
            elif Lexico.simbolo == Simbolos.Igual:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpEqual)
            elif Lexico.simbolo == Simbolos.Diferente:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpDifferent)
            elif Lexico.simbolo == Simbolos.Negativo:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Invert)
            elif Lexico.simbolo == Simbolos.Mais:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Add)
            elif Lexico.simbolo == Simbolos.Menos:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Subtract)
            elif Lexico.simbolo == Simbolos.Multiplicacao:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Multiply)
            elif Lexico.simbolo == Simbolos.Divisao:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Divide)
