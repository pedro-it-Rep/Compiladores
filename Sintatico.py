from Constants.Errors import Errors
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
    proxEnd = 1
    End = 0
    proxRotulo = 1
    rótulo = 0
    expressao = []
    posexpressao = []
    identificador = []
    nVars = 0
    tela1 = None
    Errors.sla = tela1

    def Sintatico(self):
        GeradorDeCodigo.isCreated(GeradorDeCodigo)
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Programa:
            GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Start)
            GeradorDeCodigo.geraComando2Var(GeradorDeCodigo, Comandos.Allocate, self.End, self.proxEnd)
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.NomePrograma, True, None)
                Lexico.Token(Lexico)

                if Lexico.simbolo == Simbolos.PontoVirgula:
                    self.analisaBloco(self)
                    variables = TabelaDeSimbolos.getVariables(TabelaDeSimbolos)
                    GeradorDeCodigo.geraComando2Var(GeradorDeCodigo, Comandos.Deallocate,
                                                    (self.proxEnd - len(variables)), len(variables))
                    GeradorDeCodigo.geraComando2Var(GeradorDeCodigo, Comandos.Deallocate, self.End,
                                                    self.proxEnd - len(variables))
                    Semantico.removeSimbolo(Semantico, variables)
                    TabelaDeSimbolos.removeEscopo(TabelaDeSimbolos)
                    self.proxEnd -= len(variables)

                    if Lexico.simbolo == Simbolos.Ponto:
                        GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Halt)
                        GeradorDeCodigo.closeFile(GeradorDeCodigo)
                        Lexico.Token(Lexico)

                        if Lexico.caracter == "":
                            print("Sucesso")
                            return
                        else:
                            Errors.exceptionWrongSpace(Errors, Lexico.n_line)
                    else:
                        Errors.exceptionMissingDot(Errors, Lexico.n_line)
                else:
                    Errors.exceptionPontoVirgula(Errors, Lexico.n_line)
            else:
                Errors.exceptionMissingIdentifier(Errors, Lexico.n_line)
        else:
            Errors.exceptionMissingPrograma(Errors, Lexico.n_line)

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
                        Errors.exceptionInvalidExpression(Errors, Lexico.n_line)
            else:
                Errors.exceptionMissingIdentifier(Errors, Lexico.n_line)

    def analisaVariaveis(self):
        self.nVars = 0
        while Lexico.simbolo != Simbolos.DoisPontos:
            if Lexico.simbolo == Simbolos.Identificador:
                if not TabelaDeSimbolos.isDeclaradoNoEscopo(TabelaDeSimbolos, Lexico.lexema):
                    TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.Variavel, False,
                                                  self.proxEnd + self.nVars)
                    self.nVars += 1
                    Lexico.Token(Lexico)
                    if Lexico.simbolo == Simbolos.Virgula or Lexico.simbolo == Simbolos.DoisPontos:

                        if Lexico.simbolo == Simbolos.Virgula:
                            Lexico.Token(Lexico)

                            if Lexico.simbolo == Simbolos.DoisPontos:
                                Errors.exceptionWrongPontos(Errors, Lexico.n_line)
                    else:
                        Errors.exceptionMissingPontos(Errors,Lexico.n_line)
                else:
                    Errors.semanticoVariable(Errors, Lexico.n_line)
            else:
                Errors.exceptionVaribleIdentifier(Errors, Lexico.n_line)

        GeradorDeCodigo.geraComando2Var(GeradorDeCodigo, Comandos.Allocate, self.proxEnd, self.nVars)
        self.proxEnd += self.nVars

        Lexico.Token(Lexico)
        self.analisaTipo(self)

    def analisaTipo(self):
        if Lexico.simbolo != Simbolos.Inteiro and Lexico.simbolo != Simbolos.Booleano:
            Errors.exceptionTypeInvalid(Errors, Lexico.n_line)

        if Lexico.simbolo == Simbolos.Inteiro:
            TabelaDeSimbolos.alteraTipo(TabelaDeSimbolos, Tipos.Inteiro)
        elif Lexico.simbolo == Simbolos.Booleano:
            TabelaDeSimbolos.alteraTipo(TabelaDeSimbolos, Tipos.Boolean)

        Lexico.Token(Lexico)
        self.nVars = 0

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
                    Errors.exceptionPontoVirgula(Errors, Lexico.n_line)
            Lexico.Token(Lexico)
        else:
            Errors.exceptionMissingStart(Errors, Lexico.n_line)

    def analisaComandoSimples(self):
        if Lexico.simbolo == Simbolos.Identificador:
            if TabelaDeSimbolos.isDeclarado(TabelaDeSimbolos, Lexico.lexema):
                self.analisa_atrib_chprocedimento(self)
            else:
                Errors.exceptionIdentifierNotDeclared(Errors, Lexico.n_line)
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

        self.identificador = []
        self.identificador = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
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
                        Errors.exceptionCloseParenteses(Errors, Lexico.n_line)
                else:
                    Errors.exceptionMissingIdentifier(Errors, Lexico.n_line)
            else:
                Errors.exceptionMissingIdentifier(Errors, Lexico.n_line)
        else:
            Errors.exceptionAbreParenteses(Errors, Lexico.n_line)

    def analisaEscreva(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.AbreParenteses:
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                if TabelaDeSimbolos.isDeclarado(TabelaDeSimbolos, Lexico.lexema):
                    self.found = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
                    if self.found[1] == Tipos.IntFunction:
                        self.chamadaFuncao(self)
                        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadValue, self.proxEnd - 1)
                    else:
                        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadValue, self.found[3])

                    GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Print)
                    Lexico.Token(Lexico)

                    if Lexico.simbolo == Simbolos.FechaParenteses:
                        Lexico.Token(Lexico)
                    else:
                        Errors.exceptionCloseParenteses(Errors, Lexico.n_line)
                else:
                    Errors.exceptionMissingIdentifier(Errors, Lexico.n_line)
            else:
                Errors.exceptionMissingIdentifier(Errors, Lexico.n_line)
        else:
            Errors.exceptionAbreParenteses(Errors, Lexico.n_line)

    def analisaEnquanto(self):
        aux = self.proxRotulo
        self.proxRotulo += 1

        Lexico.Token(Lexico)
        self.expressao = []
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
            Errors.exceptionMissingDo(Errors, Lexico.n_line)

        GeradorDeCodigo.geraRotulo(GeradorDeCodigo, aux2)

    def analisaSe(self):

        Lexico.Token(Lexico)
        self.expressao = []
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
            if Lexico.simbolo != Simbolos.PontoVirgula:
                GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Jump, self.proxRotulo)
            aux2 = self.proxRotulo
            self.proxRotulo += 1
            GeradorDeCodigo.geraRotulo(GeradorDeCodigo, aux)

            if Lexico.simbolo == Simbolos.Senao:
                Lexico.Token(Lexico)
                self.analisaComandoSimples(self)
                GeradorDeCodigo.geraRotulo(GeradorDeCodigo, aux2)
        else:
            Errors.exceptionInvalidIfDo(Errors, Lexico.n_line)

    def analisaSubrotina(self):
        self.nVars = 0
        flag = 0
        if Lexico.simbolo == Simbolos.Procedimento or Lexico.simbolo == Simbolos.Funcao:
            GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Jump, self.proxRotulo)
            aux = self.proxRotulo
            self.proxRotulo += 1
            flag = 1
        while Lexico.simbolo == Simbolos.Procedimento or Lexico.simbolo == Simbolos.Funcao:
            if Lexico.simbolo == Simbolos.Procedimento:
                self.analisaDeclaracaoProc(self)
            else:
                self.analisaDeclaraFunc(self)

            if Lexico.simbolo == Simbolos.PontoVirgula:
                Lexico.Token(Lexico)
            else:
                Errors.exceptionPontoVirgula(Errors, Lexico.n_line)
        if flag == 1:
            GeradorDeCodigo.geraRotulo(GeradorDeCodigo, aux)

    def analisaDeclaraFunc(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Identificador:
            if not TabelaDeSimbolos.isDeclaradoNoEscopo(TabelaDeSimbolos, Lexico.lexema):
                TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.Function, True, None)
                GeradorDeCodigo.geraRotulo(GeradorDeCodigo, self.proxRotulo)
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
                            GeradorDeCodigo.geraComando2Var(GeradorDeCodigo, Comandos.Deallocate,
                                                            self.proxEnd - len(variables), len(variables))
                            Semantico.removeSimbolo(Semantico, variables)
                            TabelaDeSimbolos.removeEscopo(TabelaDeSimbolos)
                            self.proxEnd -= len(variables)
                            GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Return)
                    else:
                        Errors.exceptionTypeInvalid(Errors, Lexico.n_line)
                else:
                    Errors.exceptionMissingPontos(Errors, Lexico.n_line)
            else:
                Errors.nomeFunc(Errors, Lexico.n_line)
        else:
            Errors.exceptionMissingIdentifier(Errors, Lexico.n_line)
        TabelaDeSimbolos.removeEscopo(TabelaDeSimbolos)

    def analisaDeclaracaoProc(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Identificador:
            if not TabelaDeSimbolos.isDeclaradoNoEscopo(TabelaDeSimbolos, Lexico.lexema):
                TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.Procedimento, True, None)
                GeradorDeCodigo.geraRotulo(GeradorDeCodigo, self.proxRotulo)
                self.found = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
                self.found[3] = self.proxRotulo
                self.proxRotulo += 1

                Lexico.Token(Lexico)
                if Lexico.simbolo == Simbolos.PontoVirgula:
                    self.analisaBloco(self)
                    variables = TabelaDeSimbolos.getVariables(TabelaDeSimbolos)
                    if len(variables) == 0:
                        pass
                    else:
                        GeradorDeCodigo.geraComando2Var(GeradorDeCodigo, Comandos.Deallocate,
                                                        self.proxEnd - len(variables),
                                                        len(variables))
                    Semantico.removeSimbolo(Semantico, variables)
                    TabelaDeSimbolos.removeEscopo(TabelaDeSimbolos)
                    self.proxEnd -= len(variables)
                    GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Return)
                else:
                    Errors.exceptionPontoVirgula(Errors, Lexico.n_line)
            else:
                Errors.nomeProc(Errors, Lexico.n_line)
        else:
            Errors.exceptionMissingIdentifier(Errors, Lexico.n_line)

    def analisaExpressao(self):
        self.analisaExpressaoSimples(self)
        if Lexico.simbolo == Simbolos.Maior or Lexico.simbolo == Simbolos.MaiorIgual or \
                Lexico.simbolo == Simbolos.Igual or Lexico.simbolo == Simbolos.Menor or \
                Lexico.simbolo == Simbolos.MenorIgual or Lexico.simbolo == Simbolos.Diferente:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
            self.analisaExpressaoSimples(self)

    def analisaExpressaoSimples(self):
        if Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
        self.analisaTermo(self)
        while Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos or Lexico.simbolo == Simbolos.Ou:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
            self.analisaTermo(self)

    def analisaTermo(self):
        self.analisaFator(self)
        while Lexico.simbolo == Simbolos.Multiplicacao or Lexico.simbolo == Simbolos.Divisao or Lexico.simbolo == Simbolos.E:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
            self.analisaFator(self)

    def analisaFator(self):
        if Lexico.simbolo == Simbolos.Identificador:
            if TabelaDeSimbolos.isDeclarado(TabelaDeSimbolos, Lexico.lexema):
                self.found = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
                if self.found[1] == Tipos.IntFunction or self.found[1] == Tipos.BoolFunction:
                    self.chamadaFuncao(self)
                self.expressao.append([Lexico.lexema, Lexico.simbolo])
                Lexico.Token(Lexico)
            else:
                Errors.exceptionIdentifierNotDeclared(Errors, Lexico.n_line)
        elif Lexico.simbolo == Simbolos.Numero:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
        elif Lexico.simbolo == Simbolos.Nao:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
            self.analisaFator(self)
        elif Lexico.simbolo == Simbolos.AbreParenteses:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
            self.analisaExpressao(self)
            if Lexico.simbolo == Simbolos.FechaParenteses:
                self.expressao.append([Lexico.lexema, Lexico.simbolo])
                Lexico.Token(Lexico)
            else:
                Errors.exceptionCloseParenteses(Errors, Lexico.n_line)
        elif Lexico.simbolo == Simbolos.Verdadeiro or Lexico.simbolo == Simbolos.Falso:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
        else:
            Errors.exceptionInvalidExpression(Errors, Lexico.n_line)

    def analisaAtribuicao(self):
        Lexico.Token(Lexico)

        self.expressao = []
        self.analisaExpressao(self)
        self.subUnarios(self)
        self.expressao = Semantico.posOrdem(Semantico, self.expressao)
        self.geraExpressao(self)
        self.tipo = Tipos.Inteiro
        Semantico.analisaExpressao(Semantico, self.expressao, self.tipo)
        self.nVars = len(TabelaDeSimbolos.getVariables(TabelaDeSimbolos))

        if self.identificador[1] == Tipos.Boolean or self.identificador[1] == Tipos.IntFunction:
            GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Store, (self.proxEnd - self.nVars - 4))
        else:
            GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Store, self.identificador[3])

    def chamadaProcedimento(self):  # Gerador de codigo
        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Call, self.identificador[3])

    def chamadaFuncao(self):  # Gerador de codigo

        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Call, self.found[3])
        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadValue, 0)

    def subUnarios(self):
        i = 0
        while i < len(self.expressao):
            if self.expressao[i][1] == Simbolos.Mais or self.expressao[i][1] == Simbolos.Menos:
                if (i - 1) == -1 or self.expressao[i - 1][1] == Simbolos.AbreParenteses or \
                        self.expressao[i - 1][1] == Simbolos.Ou or self.expressao[i - 1][1] == Simbolos.E or \
                        self.expressao[i - 1][1] == Simbolos.Nao or self.expressao[
                    i - 1][1] == Simbolos.Maior or \
                        self.expressao[i - 1][1] == Simbolos.MaiorIgual or self.expressao[
                    i - 1][1] == Simbolos.Menor or \
                        self.expressao[i - 1][1] == Simbolos.MenorIgual or self.expressao[
                    i - 1][1] == Simbolos.Igual or \
                        self.expressao[i - 1][1] == Simbolos.Diferente or self.expressao[
                    i - 1][1] == Simbolos.Mais or \
                        self.expressao[i - 1][1] == Simbolos.Menos or self.expressao[
                    i - 1][1] == Simbolos.Multiplicacao or \
                        self.expressao[i - 1][1] == Simbolos.Divisao or self.expressao[
                    i - 1][1] == Simbolos.Positivo or \
                        self.expressao[i - 1][1] == Simbolos.Negativo:
                    if self.expressao[i][1] == Simbolos.Mais:
                        self.expressao[i][1] = Simbolos.Positivo
                    else:
                        self.expressao[i][1] = Simbolos.Negativo
            i += 1

    def geraExpressao(self):
        for i in self.expressao:
            if i[1] == Simbolos.Identificador:
                if TabelaDeSimbolos.isDeclarado(TabelaDeSimbolos, i[0]):
                    self.found = TabelaDeSimbolos.busca(TabelaDeSimbolos, i[0])
                    if self.found[1] == Tipos.Inteiro or self.found[1] == Tipos.Boolean:
                        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadValue, self.found[3])
                else:
                    Errors.exceptionIdentifierNotDeclared(Errors, Lexico.n_line)
            elif i[1] == Simbolos.Numero:
                GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadConst, i[0])
            elif i[1] == Simbolos.Verdadeiro:
                GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadConst, 1)
            elif i[1] == Simbolos.Falso:
                GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadConst, 0)
            elif i[1] == Simbolos.Ou:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Or)
            elif i[1] == Simbolos.E:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.And)
            elif i[1] == Simbolos.Nao:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Negate)
            elif i[1] == Simbolos.Menor:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpLower)
            elif i[1] == Simbolos.MenorIgual:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpLowerEqual)
            elif i[1] == Simbolos.Maior:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpHigher)
            elif i[1] == Simbolos.MaiorIgual:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpHigherEqual)
            elif i[1] == Simbolos.Igual:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpEqual)
            elif i[1] == Simbolos.Diferente:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.CmpDifferent)
            elif i[1] == Simbolos.Negativo:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Invert)
            elif i[1] == Simbolos.Mais:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Add)
            elif i[1] == Simbolos.Menos:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Subtract)
            elif i[1] == Simbolos.Multiplicacao:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Multiply)
            elif i[1] == Simbolos.Divisao:
                GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Divide)