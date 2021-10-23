import Constants.Errors as Error
from Constants.Simbolos import Simbolos
from Lexico import Lexico
from Models.TabelaSimbolos import TabelaDeSimbolos
from Semantico import *


class Sintatico:
    tipo = ""
    expressao = []
    aux = ""
    tabela = TabelaDeSimbolos.tabela

    def Sintatico(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Programa:
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                TabelaDeSimbolos.insere(self, Tipos.NomePrograma, True, None)
                Lexico.Token(Lexico)
                print(Lexico.simbolo)

                if Lexico.simbolo == Simbolos.PontoVirgula:
                    self.analisaBloco(self)
                    print("Antes do veifica ponto:", Lexico.lexema)
                    print("Antes do verifica ponto:", Lexico.simbolo)
                    variables = TabelaDeSimbolos.getVariables()
                    Semantico.removeSimbolo(variables)
                    # Limpa Escopo

                    if Lexico.simbolo == Simbolos.Ponto:
                        print("Entro depois do ponto:", Lexico.lexema)
                        Lexico.Token(Lexico)

                        if Lexico.caracter == "":
                            print("Sucesso")
                            return
                        else:
                            print("Error: ", Lexico.caracter)
                            print("Erros2:", Lexico.lexema)
                            Error.exceptionWrongSpace(Lexico.n_line)
                    else:
                        Error.exceptionMissingDot(Lexico.n_line)
                else:
                    Error.exceptionPontoVirgula(Lexico.n_line)
            else:
                Error.exceptionMissingIdentifier(Lexico.n_line)
        else:
            print("Inicio:", Lexico.lexema)
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
        nVars = 0
        while Lexico.simbolo != Simbolos.DoisPontos:

            if Lexico.simbolo == Simbolos.Identificador:
                if not TabelaDeSimbolos.isDeclaradoNoEscopo(Lexico.lexema):
                    TabelaDeSimbolos.insere(Lexico.lexema, Tipos.Variavel, False, False)
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
                    Error.exceptionDuplicateVariable(Lexico.n_line)
            else:
                Error.exceptionVaribleIdentifier(Lexico.n_line)

        Lexico.Token(Lexico)
        self.analisaTipo(self)

    def analisaTipo(self):
        if Lexico.simbolo != Simbolos.Inteiro and Lexico.simbolo != Simbolos.Booleano:
            Error.exceptionTypeInvalid(Lexico.n_line)

        if Lexico.simbolo == Simbolos.Inteiro:
            TabelaDeSimbolos.alteraTipo(Tipos.Inteiro)
        elif Lexico.simbolo == Simbolos.Booleano:
            TabelaDeSimbolos.alteraTipo(Tipos.Boolean)

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
            print("antes do token:", Lexico.lexema)
            print("Antes do token2:", Lexico.caracter)
            Lexico.Token(Lexico)
            print("Depois do token2:", Lexico.lexema)
        else:
            Error.exceptionMissingStart(Lexico.n_line)

    def analisaComandoSimples(self):
        if Lexico.simbolo == Simbolos.Identificador:
            if TabelaDeSimbolos.isDeclarado(Lexico.lexema):
                self.analisa_atrib_chprocedimento(self)
            else:
                Error.exceptionIdentifierNotDeclared(Lexico.n_line)
        else:
            if Lexico.simbolo == Simbolos.Se:
                print("Antes do Se", Lexico.simbolo)
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
        identificador = TabelaDeSimbolos.busca(Lexico.lexema)
        Lexico.Token(Lexico)

        if Lexico.simbolo == Simbolos.Atribuicao:
            self.analisaAtribuicao(self, identificador)
        else:
            self.chamadaProcedimento(self, identificador)

    def analisaLeia(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.AbreParenteses:
            Lexico.Token(Lexico)
            if Lexico.simbolo == Simbolos.Identificador:
                if TabelaDeSimbolos.isDeclarado(Lexico.lexema):
                    # id = TabelaDeSimbolos.busca(Lexico.lexema) -> GERADOR DE CODIGO
                    Lexico.Token(Lexico)

                    if Lexico.simbolo == Simbolos.FechaParenteses:
                        Lexico.Token(Lexico)
                    else:
                        Error.exceptionCloseParenteses(Lexico.n_line)
                else:
                    Error.exceptionIdentifierNotDeclared(Lexico.n_line)
            else:
                Error.exceptionMissingIdentifier(Lexico.n_line)
        else:
            Error.exceptionAbreParenteses(Lexico.n_line)

    def analisaEscreva(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.AbreParenteses:
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                if TabelaDeSimbolos.isDeclarado(Lexico.lexema):
                    tipo = TabelaDeSimbolos.busca(Lexico.lexema)
                    if tipo == Tipos.IntFunction:
                        self.chamadaFuncao(tipo)
                        # GERAÇÃO DE CODIGO
                    else:
                        pass  # GERAÇÃO DE CODIGO

                    Lexico.Token(Lexico)

                    if Lexico.simbolo == Simbolos.FechaParenteses:
                        Lexico.Token(Lexico)
                        print("Dentro do analisa Escreva:", Lexico.lexema)
                    else:
                        Error.exceptionCloseParenteses(Lexico.n_line)
                else:
                    Error.exceptionIdentifierNotDeclared(Lexico.n_line)
            else:
                Error.exceptionMissingIdentifier(Lexico.n_line)
        else:
            Error.exceptionAbreParenteses(Lexico.n_line)

    def analisaEnquanto(self):
        print("Enquanto:", Lexico.lexema)
        # Def auxrot1,auxrot2 inteiro
        # auxrot1:= rotulo
        # Gera(rotulo,NULL,´ ´,´ ´) {início do while}
        # rotulo:= rotulo+1
        Lexico.Token(Lexico)

        self.expressao = Lexico
        self.analisaExpressao(self)
        self.subUnarios(self)
        self.expressao = Semantico.posOrdem(self.expressao)
        self.geraExpressao(self)
        self.tipo = Tipos.Boolean
        Semantico.analisaExpressao(self, Sintatico)
        print("Depois do analisa expressa:", Lexico.lexema)
        print("Depois do analisa expre:", Lexico.simbolo)

        if Lexico.simbolo == Simbolos.Faca:
            Lexico.Token(Lexico)
            self.analisaComandoSimples(self)

        else:
            Error.exceptionMissingDo(Lexico.n_line)

    def analisaSe(self):
        print("Espaço?????:", Lexico.lexema)
        Lexico.Token(Lexico)
        self.expressao = Lexico
        print("Depois de entrar no Se:", Lexico.lexema)
        self.analisaExpressao(self)
        self.subUnarios(self)
        self.expressao = Semantico.posOrdem(self.expressao)
        self.geraExpressao(self)
        self.tipo = Tipos.Boolean
        Semantico.analisaExpressao(self, Sintatico)

        if Lexico.simbolo == Simbolos.Entao:
            Lexico.Token(Lexico)
            self.analisaComandoSimples(self)

            if Lexico.simbolo == Simbolos.Senao:
                Lexico.Token(Lexico)
                print("Dentro do senao:", Lexico.lexema)
                print("Dentro do senao:", Lexico.caracter)
                print("Dentro do senao:", Lexico.simbolo)
                self.analisaComandoSimples(self)
        else:
            Error.exceptionInvalidIfDo(Lexico.n_line)

    def analisaSubrotina(self):
        # Def. auxrot, flag inteiro
        # flag = 0
        # if (token.simbolo = sprocedimento) ou
        # (token.simbolo = sfunção)
        # então início
        # auxrot:= rotulo
        # GERA(´ ´,JMP,rotulo,´ ´) {Salta sub-rotinas}
        # rotulo:= rotulo + 1
        # flag = 1
        # fim
        while Lexico.simbolo == Simbolos.Procedimento or Lexico.simbolo == Simbolos.Funcao:
            if Lexico.simbolo == Simbolos.Procedimento:
                self.analisaDeclaracaoProc(self)
            else:
                self.analisaDeclaraFunc(self)

            if Lexico.simbolo == Simbolos.PontoVirgula:
                Lexico.Token(Lexico)
            else:
                Error.exceptionPontoVirgula(Lexico.n_line)
            # if flag = 1
            # então Gera(auxrot,NULL,´ ´,´ ´) {início do principal}
            # fim

    def analisaDeclaraFunc(self):
        Lexico.Token(Lexico)
        # nível := “L” (marca ou novo galho)
        if Lexico.simbolo == Simbolos.Identificador:
            if not TabelaDeSimbolos.isDeclarado(Lexico.lexema):
                TabelaDeSimbolos.insere(Lexico.lexema, Tipos.Function, True, False)
                s = TabelaDeSimbolos.busca(Lexico.lexema)
                Lexico.Token(Lexico)
                if Lexico.simbolo == Simbolos.DoisPontos:
                    Lexico.Token(Lexico)
                    if Lexico.simbolo == Simbolos.Inteiro or Lexico.simbolo == Simbolos.Booleano:
                        if Lexico.simbolo == Simbolos.Inteiro:
                            TabelaDeSimbolos.alteraTipo(Tipos.IntFunction)
                        else:
                            TabelaDeSimbolos.alteraTipo(Tipos.BoolFunction)
                        Lexico.Token(Lexico)
                        if Lexico.simbolo == Simbolos.PontoVirgula:
                            self.analisaBloco(self)
                            variables = TabelaDeSimbolos.getVariables(self)
                            TabelaDeSimbolos.remove(variables)
                            #LIMPA ESCOPO
                    else:
                        Error.exceptionTypeInvalid(Lexico.n_line)
                else:
                    Error.exceptionMissingPontos(Lexico.n_line)
            else:
                Error.exceptionDuplicateVariable(Lexico.n_line)
        else:
            Error.exceptionMissingIdentifier(Lexico.n_line)
        # Desempliha ou volta nivel

    def analisaDeclaracaoProc(self):
        Lexico.Token(Lexico)
        # nível := “L” (marca ou novo galho)
        if Lexico.simbolo == Simbolos.Identificador:
            if not TabelaDeSimbolos.isDeclarado(Lexico.lexema):
                TabelaDeSimbolos.insere(Lexico.lexema, Tipos.Procedimento, True, False)

                Lexico.Token(Lexico)
                if Lexico.simbolo == Simbolos.PontoVirgula:
                    self.analisaBloco(self)
                    self.analisaBloco(self)
                    variables = TabelaDeSimbolos.getVariables(self)
                    TabelaDeSimbolos.remove(variables)
                    # LIMPA ESCOPO
                else:
                    Error.exceptionPontoVirgula(Lexico.n_line)
            else:
                Error.exceptionDuplicateVariable(Lexico.n_line)
        else:
            Error.exceptionMissingIdentifier(Lexico.n_line)

    def analisaExpressao(self):
        print("Expressao:", Lexico.lexema)
        self.analisaExpressaoSimples(self)
        if Lexico.simbolo == Simbolos.Maior or Lexico.simbolo == Simbolos.MaiorIgual or \
                Lexico.simbolo == Simbolos.Igual or Lexico.simbolo == Simbolos.Menor or \
                Lexico.simbolo == Simbolos.MenorIgual or Lexico.simbolo == Simbolos.Diferente:
            print("Expressao antes:", Lexico.lexema)
            Lexico.Token(Lexico)
            print("Expressao depois:", Lexico.lexema)
            self.analisaExpressaoSimples(self)

    def analisaExpressaoSimples(self):
        print("Exp Simples:", Lexico.lexema)
        if Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos:
            self.expressao.append(Lexico)
            Lexico.Token(Lexico)
        self.analisaTermo(self)
        print("depois analisa exp simples:", Lexico.lexema)
        while Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos or Lexico.simbolo == Simbolos.Ou:
            self.expressao.append(Lexico)
            Lexico.Token(Lexico)
            self.analisaTermo(self)

    def analisaTermo(self):
        print("Analisa termo:", Lexico.lexema)
        self.analisaFator(self)
        print("Depois analisa Fator:", Lexico.lexema)
        while Lexico.simbolo == Simbolos.Multiplicacao or Lexico.simbolo == Simbolos.Divisao or Lexico.simbolo == Simbolos.E:
            self.expressao.append(Lexico)
            Lexico.Token(Lexico)
            self.analisaFator(self)

    def analisaFator(self):
        print("Entro no Fator: ", Lexico.lexema)
        if Lexico.simbolo == Simbolos.Identificador:
            if TabelaDeSimbolos.isDeclarado(Lexico.lexema):
                self.aux = TabelaDeSimbolos.busca(Lexico.lexema)
                if self.tipo == Tipos.IntFunction or self.tipo == Tipos.IntFunction:
                    self.chamadaFuncao(self)
                self.expressao.append(Lexico.tokens)
                Lexico.Token(Lexico)
            else:
                Error.exceptionIdentifierNotDeclared(Lexico.n_line)
        elif Lexico.simbolo == Simbolos.Numero:
            self.expressao.append(Lexico.tokens)
            Lexico.Token(Lexico)
            print("é o pontos?:", Lexico.lexema)
        elif Lexico.simbolo == Simbolos.Nao:
            self.expressao.append(Lexico.tokens)
            Lexico.Token(Lexico)
            self.analisaFator(self)
        elif Lexico.simbolo == Simbolos.AbreParenteses:
            self.expressao.append(Lexico.Token(Lexico))
            Lexico.Token(Lexico)
            self.analisaExpressao(self)
            if Lexico.simbolo == Simbolos.FechaParenteses:
                self.expressao.append(Lexico.tokens)
                Lexico.Token(Lexico)
                print("Depois fecha parenteses:", Lexico.caracter)
                print("Depois fecha parenteses2:", Lexico.lexema)
            else:
                print("Aqui", Lexico.simbolo)
                print("Aui", Lexico.lexema)
                print("Error aqui")
                Error.exceptionCloseParenteses(Lexico.n_line)
        elif Lexico.simbolo == Simbolos.Verdadeiro or Lexico.simbolo == Simbolos.Falso:
            self.expressao.append(Lexico.tokens)
            Lexico.Token(Lexico)
        else:
            print("Deu erro no else do Fator")
            Error.exceptionInvalidExpression(Lexico.n_line)

    def analisaAtribuicao(self, identificador):
        Lexico.Token(Lexico)
        self.analisaExpressao(self)
        self.subUnarios(self)
        self.expressao = Semantico.posOrdem(self.expressao)
        self.geraExpressao(self)
        Semantico.analisaExpressao(self, identificador)
        nVars = len(TabelaDeSimbolos.getVariables(self))

        if self.tipo == Tipos.Boolean or self.tipo == Tipos.IntFunction:
            pass
        else:
            pass

    def chamadaProcedimento(self, identificador):  # Gerador de codigo
        pass

    def chamadaFuncao(self):  # Gerador de codigo
        Lexico.Token(Lexico)

    def subUnarios(self):
        i = 0
        self.expressao = Lexico
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
        i = 0
        for i in self.expressao:
            if Lexico.simbolo == Simbolos.Identificador:
                if TabelaDeSimbolos.isDeclarado(Lexico.lexema):
                    self.tipo = TabelaDeSimbolos.busca(Lexico.lexema)
                    if self.tipo == Tipos.Inteiro or self.tipo == Tipos.Boolean:
                        pass
                else:
                    Error.exceptionIdentifierNotDeclared(Lexico.n_line)
