import Constants.Errors as Error
from Constants.Simbolos import Simbolos
from Lexico import Lexico
from Models.TabelaSimbolos import TabelaDeSimbolos
from Constants.Tipos import Tipos
from Semantico import Semantico


class Sintatico:

    found = None
    rótulo = 0 # Delcarado aqui parar lembrar de mudar no futuro
    nível = "X"
    expressao = []
    posexpressao = []
    indentificador = []

    def Sintatico(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Programa:
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.NomedoPrograma, self.nível, 0)
                Lexico.Token(Lexico)

                if Lexico.simbolo == Simbolos.PontoVirgula:
                    self.analisaBloco(self)

                    if Lexico.simbolo == Simbolos.Ponto:
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

            if Lexico.simbolo == Simbolos.Identificador:
                print(TabelaDeSimbolos.tabela)
                self.found = TabelaDeSimbolos.PesquisaDuplicVarTabela(TabelaDeSimbolos, Lexico.lexema)
                if self.found is False:
                    TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.Variavel, "", 0)
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

        Lexico.Token(Lexico)
        self.analisaTipo(self)

    def analisaTipo(self):
        if Lexico.simbolo != Simbolos.Inteiro and Lexico.simbolo != Simbolos.Booleano:
            Error.exceptionTypeInvalid(Lexico.n_line)
        TabelaDeSimbolos.colocaTipo(TabelaDeSimbolos, Lexico.lexema)
        Lexico.Token(Lexico)

    def analisaComandos(self):
        if Lexico.simbolo == Simbolos.Inicio:
            Lexico.Token(Lexico)
            self.analisaComandoSimples(self)

            while Lexico.simbolo != Simbolos.Fim:
                if Lexico.simbolo == Simbolos.PontoVirgula:
                    Lexico.Token(Lexico)

                    if Lexico.simbolo != Simbolos.Fim:
                        self.expressao = []
                        self.analisaComandoSimples(self)
                else:
                    Error.exceptionPontoVirgula(Lexico.n_line)
            Lexico.Token(Lexico)
        else:
            Error.exceptionMissingStart(Lexico.n_line)

    def analisaComandoSimples(self):
        if Lexico.simbolo == Simbolos.Identificador:
            self.analisa_atrib_chprocedimento(self)
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

        TabelaDeSimbolos.search(TabelaDeSimbolos, Lexico.lexema)
        self.indentificador = TabelaDeSimbolos.id
        Lexico.Token(Lexico)

        if Lexico.simbolo == Simbolos.Atribuicao:

            self.analisaAtribuicao(self)
        else:
            self.chamadaProcedimento(self)

    def analisaLeia(self):
        identificador = []
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.AbreParenteses:
            Lexico.Token(Lexico)
            if Lexico.simbolo == Simbolos.Identificador:
                self.found = TabelaDeSimbolos.searchNameVariable(TabelaDeSimbolos, Lexico.lexema)
                if self.found is True:
                    print("Leia", Lexico.lexema)
                    TabelaDeSimbolos.search(TabelaDeSimbolos, Lexico.lexema)
                    identificador = TabelaDeSimbolos.id
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
        identificador = []
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.AbreParenteses:
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                self.found = TabelaDeSimbolos.searchNameVariable(TabelaDeSimbolos, Lexico.lexema)
                if self.found is True:
                    TabelaDeSimbolos.search(TabelaDeSimbolos, Lexico.lexema)
                    indentificador = TabelaDeSimbolos.id
                    if indentificador[1] == Tipos.IntFunction:
                        print("Oiif")
                        #analisaChamadaFuncao
                        #codigoGera
                    else:
                        print("Entrouelse")
                        #codigogera
                        #codigogera
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
        idanterior = []
        print("Enquanto:", Lexico.lexema)
        # Def auxrot1,auxrot2 inteiro
        # auxrot1:= rotulo
        # Gera(rotulo,NULL,´ ´,´ ´) {início do while}
        # rotulo:= rotulo+1
        Lexico.Token(Lexico)
        self.analisaExpressao(self)
        self.posexpressao = Semantico.posOrdem(Semantico, self.expressao)
        idanterior = ["ENQUANTO", Tipos.Booleano, "", 0]
        Semantico.analisaExpressao(Semantico, self.posexpressao, idanterior)

        if Lexico.simbolo == Simbolos.Faca:
            self.expressao = []
            Lexico.Token(Lexico)
            self.analisaComandoSimples(self)

        else:
            Error.exceptionMissingDo(Lexico.n_line)

    def analisaSe(self):
        posExp = []
        idanterior = []
        Lexico.Token(Lexico)
        self.analisaExpressao(self)
        self.posexpressao = Semantico.posOrdem(Semantico, self.expressao)
        idanterior = ["SE", Tipos.Booleano, "", 0]
        Semantico.analisaExpressao(Semantico, self.posexpressao, idanterior)

        if Lexico.simbolo == Simbolos.Entao:
            self.expressao = []
            Lexico.Token(Lexico)
            self.analisaComandoSimples(self)

            if Lexico.simbolo == Simbolos.Senao:
                Lexico.Token(Lexico)
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
        if Lexico.simbolo == Simbolos.Identificador:
            self.found = TabelaDeSimbolos.searchNameFunc(Lexico.lexema)
            if self.found is False:
                TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, "", self.nível, self.rótulo) #token.lexema,””,nível,rótulo)
                Lexico.Token(Lexico)
                if Lexico.simbolo == Simbolos.DoisPontos:
                    Lexico.Token(Lexico)
                    i = len(TabelaDeSimbolos.tabela)
                    if Lexico.simbolo == Simbolos.Inteiro or Lexico.simbolo == Simbolos.Booleano:
                        if Lexico.simbolo == Simbolos.Inteiro:
                            TabelaDeSimbolos.tabela[i][1] = Tipos.IntFunction
                        else:
                            TabelaDeSimbolos.tabela[i][1] = Tipos.BoolFunction
                        Lexico.Token(Lexico)
                        if Lexico.simbolo == Simbolos.PontoVirgula:
                            self.analisaBloco(self)
                    else:
                        Error.exceptionTypeInvalid(Lexico.n_line)
                else:
                    Error.exceptionMissingPontos(Lexico.n_line)
            else:
                Error.nomeFunc(Lexico.n_line)
        else:
            Error.exceptionMissingIdentifier(Lexico.n_line)
        TabelaDeSimbolos.remove(TabelaDeSimbolos)

    def analisaDeclaracaoProc(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Identificador:
            self.found = TabelaDeSimbolos.searchNameProc(TabelaDeSimbolos, Lexico.lexema)
            if self.found is False:
                TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.Procedimento, self.nível, self.rótulo)
                # {guarda na TabSimb}
                # Gera(rotulo,NULL,´ ´,´ ´)
                # {CALL irá buscar este rótulo na TabSimb}
                # rotulo:= rotulo+1
                # self.tokenReturn = Lexico(self)
                Lexico.Token(Lexico)
                if Lexico.simbolo == Simbolos.PontoVirgula:
                    self.analisaBloco(self)
                else:
                    Error.exceptionPontoVirgula(Lexico.n_line)
            else:
                Error.nomeProc(Lexico.n_line)
        else:
            Error.exceptionMissingIdentifier(Lexico.n_line)
        TabelaDeSimbolos.remove(TabelaDeSimbolos)

    def analisaExpressao(self):
        self.analisaExpressaoSimples(self)
        if Lexico.simbolo == Simbolos.Maior or Lexico.simbolo == Simbolos.MaiorIgual or \
                Lexico.simbolo == Simbolos.Igual or Lexico.simbolo == Simbolos.Menor or \
                Lexico.simbolo == Simbolos.MenorIgual or Lexico.simbolo == Simbolos.Diferente:
            self.expressao.append(Lexico.lexema)
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
            self.expressao.append(Lexico.lexema)
            Lexico.Token(Lexico)
            self.analisaTermo(self)

    def analisaTermo(self):
        self.analisaFator(self)
        while Lexico.simbolo == Simbolos.Multiplicacao or Lexico.simbolo == Simbolos.Divisao or Lexico.simbolo == Simbolos.E:
            self.expressao.append(Lexico.lexema)
            Lexico.Token(Lexico)
            self.analisaFator(self)

    def analisaFator(self):
        if Lexico.simbolo == Simbolos.Identificador:
            self.found = TabelaDeSimbolos.search(TabelaDeSimbolos, Lexico.lexema)
            if self.found is True:
                if TabelaDeSimbolos.tabela[TabelaDeSimbolos.i][1] == Tipos.IntFunction or\
                        TabelaDeSimbolos.tabela[TabelaDeSimbolos.i][1] == Tipos.BoolFunction:
                    self.chamadaFuncao()
                else:
                    self.expressao.append(Lexico.lexema)
                    Lexico.Token(Lexico)
            # Senão Léxico(token)
            # Senão ERRO
            # Fim
            else:
                Error.notNome()
        elif Lexico.simbolo == Simbolos.Numero:
            print("Analisa Fator", self.expressao)
            self.expressao.append(Lexico.lexema)
            Lexico.Token(Lexico)
        elif Lexico.simbolo == Simbolos.Nao:
            self.expressao.append(Lexico.lexema)
            Lexico.Token(Lexico)
            self.analisaFator(self)
        elif Lexico.simbolo == Simbolos.AbreParenteses:
            self.expressao.append(Lexico.lexema)
            Lexico.Token(Lexico)
            self.analisaExpressao(self)
            if Lexico.simbolo == Simbolos.FechaParenteses:
                self.expressao.append(Lexico.lexema)
                Lexico.Token(Lexico)
            else:
                Error.exceptionCloseParenteses(Lexico.n_line)
        elif Lexico.simbolo == Simbolos.Verdadeiro or Lexico.simbolo == Simbolos.Falso:
            self.expressao.append(Lexico.lexema)
            Lexico.Token(Lexico)
        else:
            Error.exceptionInvalidExpression(Lexico.n_line)

    def analisaAtribuicao(self):
        Lexico.Token(Lexico)
        self.analisaExpressao(self)
        self.posexpressao = Semantico.posOrdem(Semantico, self.expressao)
        Semantico.analisaExpressao(Semantico, self.posexpressao, self.indentificador)

    def chamadaProcedimento(self):  # Gerador de codigo
        pass

    def chamadaFuncao(self):  # Gerador de codigo
        Lexico.Token(Lexico)