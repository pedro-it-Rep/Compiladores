from Lexico import Lexico
from Constants.Simbolos import Simbolos
from Constants.Errors import Errors
#from Models.TabelaSimbolos import TabelaDeSimbolos


class Sintatico:

    def Sintatico(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Programa:
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                # insere_tabela(token.lexema, "nomedoprograma","","")
                Lexico.Token(Lexico)
                print(Lexico.simbolo)

                if Lexico.simbolo == Simbolos.PontoVirgula:
                    self.analisaBloco(self)

                    if Lexico.simbolo == Simbolos.Ponto:
                        Lexico.Token(Lexico)

                        if Lexico.i == Lexico.maxChar:
                            print("Sucesso")
                            return
                        else:
                            Errors.exceptionWrongSpace(Errors)
                    else:
                        Errors.exceptionMissingDot(Errors)
                else:
                    Errors.exceptionPontoVirgula(Errors)
            else:
                Errors.exceptionMissingIdentifier(Errors)
        else:
            Errors.exceptionMissingPrograma(Errors)

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
                        Errors.ex(Errors)
            else:
                Errors.exceptionMissingIdentifier(Errors)

    def analisaVariaveis(self):
        while Lexico.simbolo != Simbolos.DoisPontos:

            if Lexico.simbolo == Simbolos.Identificador:
                # Pesquisa_duplicvar_tabela(token.lexema)
                # se nao encontrou duplicidade
                # entao inicio
                # insere_tablea(tokenReturn, "variavel")
                Lexico.Token(Lexico)
                if Lexico.simbolo == Simbolos.Virgula or Lexico.simbolo == Simbolos.DoisPontos:

                    if Lexico.simbolo == Simbolos.Virgula:
                        Lexico.Token(Lexico)

                        if Lexico.simbolo == Simbolos.DoisPontos:
                            Errors.exceptionWrongPontos(Errors)
                else:
                    Errors.exceptionMissingPontos(Errors)
            else:
                Errors.exceptionVaribleIdentifier(Errors)

        Lexico.Token(Lexico)
        self.analisaTipo(self)

    def analisaTipo(self):
        if Lexico.simbolo != Simbolos.Inteiro and Lexico.simbolo != Simbolos.Booleano:
            Errors.exceptionTypeInvalid(Errors)

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
                elif Lexico.simbolo != Simbolos.Fim:
                    Errors.exceptionPontoVirgula(Errors)

            Lexico.Token(Lexico)
        else:
            Errors.exceptionMissingStart(Errors)

    def analisaComandoSimples(self):
        if Lexico.simbolo == Simbolos.Identificador:
            #print("Comando Simples:", Lexico.simbolo)
            self.analisa_atrib_chprocedimento(self)
        else:
            if Lexico.simbolo == Simbolos.Se:
                print("Antes do Se",Lexico.simbolo)
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
        Lexico.Token(Lexico)
        #print("Chamada de Procedimento:", Lexico.simbolo)

        if Lexico.simbolo == Simbolos.Atribuicao:
            self.analisaAtribuicao(self)
        else:
            self.chamadaProcedimento(self)

    def analisaLeia(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.AbreParenteses:
            Lexico.Token(Lexico)
            if Lexico.simbolo == Simbolos.Identificador:
                # se pesquisa_decvar_tabela(tokenRetun.lexema)
                # entao inicio (pesquisa em toda a tabela)
                Lexico.Token(Lexico)

                if Lexico.simbolo == Simbolos.FechaParenteses:
                    Lexico.Token(Lexico)
                else:
                    Errors.exceptionCloseParenteses(Errors)
            else:
                Errors.exceptionMissingIdentifier(Errors)
        else:
            Errors.exceptionAbreParenteses(Errors)

    def analisaEscreva(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.AbreParenteses:
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                # se pesquisa_decvarfunc_tabela(token.lexema)
                Lexico.Token(Lexico)

                if Lexico.simbolo == Simbolos.FechaParenteses:
                    Lexico.Token(Lexico)
                else:
                    Errors.exceptionFechaParenteses(Errors)
            else:
                Errors.exceptionMissingIdentifier(Errors)
        else:
            Errors.exceptionAbreParenteses(Errors)

    def analisaEnquanto(self):
        # Def auxrot1,auxrot2 inteiro
        # auxrot1:= rotulo
        # Gera(rotulo,NULL,´ ´,´ ´) {início do while}
        # rotulo:= rotulo+1
        Lexico.Token(Lexico)
        self.analisaExpressao(self)

        if Lexico.simbolo == Simbolos.Faca:
            Lexico.Token(Lexico)
            self.analisaComandoSimples(self)

        else:
            Errors.exceptionMissingDo(Errors)

    def analisaSe(self):
        print("Espaço?????:", Lexico.lexema)
        Lexico.Token(Lexico)
        print("Depois de entrar no Se:", Lexico.lexema)
        self.analisaExpressao(self)

        if Lexico.simbolo == Simbolos.Entao:
            Lexico.Token(Lexico)
            self.analisaComandoSimples(self)

            if Lexico.simbolo == Simbolos.Senao:
                Lexico.Token(Lexico)
                self.analisaComandoSimples(self)
        else:
            Errors.exceptionInvalidIfDo(Errors)

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
                Errors.exceptionPontoVirgula(Errors)
            # if flag = 1
            # então Gera(auxrot,NULL,´ ´,´ ´) {início do principal}
            # fim

    def analisaDeclaraFunc(self):
        Lexico.Token(Lexico)
        # nível := “L” (marca ou novo galho)
        if Lexico.simbolo == Simbolos.Identificador:
            #pesquisa_declfunc_tabela(token.lexema)
            #se não encontrou
            #então início
            #Insere_tabela(token.lexema,””,nível,rótulo)
            Lexico.Token(Lexico)
            if Lexico.simbolo == Simbolos.DoisPontos:
                Lexico.Token(Lexico)
                if Lexico.simbolo == Simbolos.Inteiro or Lexico.simbolo == Simbolos.Booleano:
                    #se(token.símbolo = Sinteger)
                        #então TABSIMB[pc].tipo :=“função inteiro”
                    #senão TABSIMB[pc].tipo :=“função boolean”
                    Lexico.Token(Lexico)
                    if Lexico.simbolo == Simbolos.PontoVirgula:
                        self.analisaBloco(self)
                Errors.exceptionTypeInvalid(Errors)
            Errors.exceptionMissingPontos(Errors)
            #senao
        Errors.exceptionMissingIdentifier(Errors)
        #Desempliha ou volta nivel

    def analisaDeclaracaoProc(self):
        Lexico.Token(Lexico)
        # nível := “L” (marca ou novo galho)
        if Lexico.simbolo == Simbolos.Identificador:
            # pesquisa_declproc_tabela(token.lexema)
            # se não encontrou
            # então início
            # Insere_tabela(token.lexema,”procedimento”,nível, rótulo)
            # {guarda na TabSimb}
            # Gera(rotulo,NULL,´ ´,´ ´)
            # {CALL irá buscar este rótulo na TabSimb}
            # rotulo:= rotulo+1
            # self.tokenReturn = Lexico(self)
            Lexico.Token(Lexico)
            if Lexico.simbolo == Simbolos.PontoVirgula:
                self.analisaBloco(self)
            else:
                #print("Deu ruim aqui")
                Errors.exceptionPontoVirgula(Errors)
        else:
            Errors.exceptionMissingIdentifier(Errors)

    def analisaExpressao(self):
        #print("Entro Analisa Expressão:", Lexico.lexema)
        self.analisaExpressaoSimples(self)
        if Lexico.simbolo == Simbolos.Maior or Lexico.simbolo == Simbolos.MaiorIgual or \
                Lexico.simbolo == Simbolos.Igual or Lexico.simbolo == Simbolos.Menor or \
                Lexico.simbolo == Simbolos.MenorIgual or Lexico.simbolo == Simbolos.Diferente:
            #print("Entra Expressao2:", Lexico.lexema)
            #print("Lexico caracter:", Lexico.caracter)
            Lexico.Token(Lexico)
            #print("Entra Expressao2:", Lexico.lexema)
            #print("Entes do Expressao Simples", Lexico.lexema)
            self.analisaExpressaoSimples(self)


    def analisaExpressaoSimples(self):
        if Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos:
            Lexico.Token(Lexico)
        self.analisaTermo(self)
        while Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos or Lexico.simbolo == Simbolos.Ou:
            #print("While do Expressao Simples")
            Lexico.Token(Lexico)
            self.analisaTermo(self)


    def analisaTermo(self):
        self.analisaFator(self)
        while Lexico.simbolo == Simbolos.Multiplicacao or Lexico.simbolo == Simbolos.Divisao or Lexico.simbolo == Simbolos.E:
            Lexico.Token(Lexico)
            self.analisaFator(self)


    def analisaFator(self):
        if Lexico.simbolo == Simbolos.Identificador:
            Lexico.Token(Lexico)
            # Se pesquisa_tabela(token.lexema,nível,ind)
            # Então Se (TabSimb[ind].tipo = “função inteiro”) ou
            # (TabSimb[ind].tipo = “função booleano”)
            # Então
            # self.analisaFuncao(self)
            # Senão Léxico(token)
            # Senão ERRO
            # Fim
        elif Lexico.simbolo == Simbolos.Numero:
            #print("Entro no analisaFator -> Numero:", Lexico.lexema)
            Lexico.Token(Lexico)
        elif Lexico.simbolo == Simbolos.Nao:
            Lexico.Token(Lexico)
            self.analisaFator(self)
        elif Lexico.simbolo == Simbolos.AbreParenteses:
            Lexico.Token(Lexico)
            self.analisaExpressao(self)
            if Lexico.simbolo == Simbolos.FechaParenteses:
                Lexico.Token(Lexico)
            else:
                Errors.exceptionCloseParenteses(Errors)
        elif Lexico.simbolo == Simbolos.Verdadeiro or Lexico.simbolo == Simbolos.Falso:
            Lexico.Token(Lexico)
        else:
            Errors.exceptionInvalidExpression(Errors)

    def analisaAtribuicao(self):
        Lexico.Token(Lexico)
        self.analisaExpressao(self)

    def chamadaProcedimento(self): # Gerador de codigo
        pass

    def analisaFuncao(self): # Gerador de codigo
        Lexico.Token(Lexico)