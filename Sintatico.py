from Lexico import Lexico
from Constants.Simbolos import Simbolos


class Sintatico:
    tokenReturn = []
    lexico = Lexico
    endFile = ""

    def Sintatico(self):

        self.tokenReturn = Lexico.Token(self.lexico)
        if self.tokenReturn.simbolo == Simbolos.Programa:
            self.tokenReturn = Lexico.Token(self.lexico)

            if self.tokenReturn.simbolo == Simbolos.Identificador:
                # insere_tabela(token.lexema, "nomedoprograma","","")
                self.tokenReturn = Lexico.Token(self.lexico)

                if self.tokenReturn.simbolo == Simbolos.PontoVirgula:
                    self.analisaBloco(self)

                    if self.tokenReturn.simbolo == Simbolos.Ponto:
                        self.tokenReturn = Lexico.Token(self.lexico)

                        if self.tokenReturn is None:
                            print("Sucesso")
                            return
                        else:
                            exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "código após finalização do programa.")
                    else:
                        exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token '.' esperado.")
                else:
                    exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token ';' esperado.")
            else:
                exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token identificador esperado.")
        else:
            exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "programa deve iniciar com o token 'programa'.")

    def analisaBloco(self):
        self.tokenReturn = Lexico.Token(self.lexico)
        self.analisa_et_variaveis(self)
        self.analisaSubrotina(self)
        self.analisaComandos(self)

    def analisa_et_variaveis(self, tokenReturn):
        if Lexico.simbolo == Simbolos.Var:
            self.tokenReturn = Lexico.Token(self.lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                while Lexico.simbolo == Simbolos.Identificador:
                    self.analisaVariaveis(self)
                    if Lexico.simbolo == Simbolos.PontoVirgula:
                        self.tokenReturn = Lexico.Token(self.lexico)
                    else:
                        exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token ';' esperado.")
            else:
                exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token identificador esperado.")

    def analisaVariaveis(self):
        while Lexico.simbolo != Simbolos.DoisPontos:

            if self.tokenReturn == Simbolos.Identificador:
                # Pesquisa_duplicvar_tabela(token.lexema)
                # se nao encontrou duplicidade
                # entao inicio
                # insere_tablea(tokenReturn, "variavel")
                self.tokenReturn = Lexico.Token(self.lexico)
                if self.tokenReturn == Simbolos.Virgula or self.tokenReturn == Simbolos.DoisPontos:

                    if self.tokenReturn == Simbolos.Virgula:
                        self.tokenReturn = Lexico.Token(self.lexico)

                        if self.tokenReturn == Simbolos.DoisPontos:
                            exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token invalido ':' apos ','.")
                else:
                    exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token ',' ou ':' esperado.")
            else:
                exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "nome de variavel, token identificador esperado.")

        self.tokenReturn = Lexico.Token(self.lexico)
        self.analisaTipo(self)

    def analisaTipo(self):
        if self.tokenReturn != Simbolos.Inteiro and self.tokenReturn != Simbolos.Booleano:
            exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "tipo de variavel invalido.")

        self.tokenReturn = Lexico.Token(self.lexico)

    def analisaComandos(self):
        if Lexico.simbolo == Simbolos.Inicio:
            self.tokenReturn = Lexico.Token(self.lexico)
            self.analisaComandoSimples(self)

            while Lexico.simbolo != Simbolos.Fim:
                if Lexico.simbolo == Simbolos.PontoVirgula:
                    self.tokenReturn = Lexico.Token(self.lexico)

                    if Lexico.simbolo != Simbolos.Fim:
                        self.analisaComandosSimples(self)
                elif Lexico.simbolo != Simbolos.Fim:
                    exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token ';' esperado.")

            self.tokenReturn = Lexico.Token(self.lexico)
        else:
            exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token 'inicio' esperado.")

    def analisaComandoSimples(self):
        if Lexico.simbolo == Simbolos.Identificador:
            self.analisa_atrib_chprocedimento(self)
        else:
            if Lexico.simbolo == Simbolos.Se:
                self.analisaSe(self)
            elif Lexico.simbolo == Simbolos.Enquanto:
                self.analiasaEnquanto(self)
            elif Lexico.simbolo == Simbolos.Leia:
                self.analisaLeia(self)
            elif Lexico.simbolo == Simbolos.Escreva:
                self.analisaEscreva(self)
            else:
                self.analisaComando(self)

    def analisa_atrib_chprocedimento(self):
        self.tokenReturn = Lexico.Token(self.lexico)

        if Lexico.simbolo == Simbolos.Atribuicao:
            self.analisaAtribuicao(self)
        else:
            self.chamadaProcedimento(self)

    def analisaLeia(self):
        self.tokenReturn = Lexico.Token(self.lexico)
        if Lexico.simbolo == Simbolos.AbreParenteses:
            self.tokenReturn = Lexico.Token(self.lexico)
            if Lexico.simbolo == Simbolos.Identificador:
                # se pesquisa_decvar_tabela(tokenRetun.lexema)
                # entao inicio (pesquisa em toda a tabela)
                self.tokenReturn = Lexico.Token(self.lexico)

                if Lexico.simbolo == Simbolos.FechaParenteses:
                    self.tokenReturn = Lexico.Token(self.lexico)
                else:
                    exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token ')' esperado.")
            else:
                exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token identificador esperado.")
        else:
            exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token '(' esperado.")

    def analisaEscreva(self):
        self.tokenReturn = Lexico.Token(self.lexico)
        if Lexico.simbolo == Simbolos.AbreParenteses:
            self.tokenReturn = Lexico.Token(self.lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                # se pesquisa_decvarfunc_tabela(token.lexema)
                self.tokenReturn = Lexico.Token(self.lexico)

                if Lexico.simbolo == Simbolos.FechaParenteses:
                    self.tokenReturn = Lexico.Token(self.lexico)
                else:
                    exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token ')' esperado.")
            else:
                exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token identificador esperado.")
        else:
            exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token '(' esperado.")

    def analisaEnquanto(self):
        # Def auxrot1,auxrot2 inteiro
        # auxrot1:= rotulo
        # Gera(rotulo,NULL,´ ´,´ ´) {início do while}
        # rotulo:= rotulo+1
        self.tokenReturn = Lexico.Token(self.lexico)
        self.analisaExpressao(self)

        if self.tokenReturn == Simbolos.Faca:
            self.tokenReturn = Lexico.Token(self.lexico)
            self.analisaComandoSimples(self)

        else:
            exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "comando enquanto, 'faca' esperado.")

    def analisaSe(self):
        self.tokenReturn = Lexico.Token(self.lexico)
        self.analisaExpressao(self)

        if Lexico.simbolo == Simbolos.Entao:
            self.tokenReturn = Lexico.Token(self.lexico)
            self.analisaComandoSimples(self)

            if Lexico.simbolo == Simbolos.Senao:
                self.tokenReturn = Lexico.Token(self.lexico)
                self.analisaComandoSimples(self)
        else:
            exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "comando se, 'entao' esperado.")

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
                self.analisaDeclaracaoFunc(self)

            if Lexico.simbolo == Simbolos.PontoVirgula:
                self.tokenReturn = Lexico.Token(self.lexico)
            else:
                exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token ';' esperado.")
            # if flag = 1
            # então Gera(auxrot,NULL,´ ´,´ ´) {início do principal}
            # fim

    def analisaDeclaracaoProc(self):
        self.tokenReturn = Lexico.Token(self.lexico)
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
            if Lexico.simbolo == Simbolos.PontoVirgula:
                self.analisaBloco(self)
            else:
                exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token ';' esperado.")
        else:
            exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "nome de procedimento, identificador esperado.")

    def analisaExpressao(self):
        self.analisaExpressaoSimples(self)
        if Lexico.simbolo == Simbolos.Maior or Lexico.simbolo == Simbolos.MaiorIgual or \
                Lexico.simbolo == Simbolos.Igual or Lexico.simbolo == Simbolos.Menor or \
                Lexico.simbolo == Simbolos.MenorIgual or Lexico.simbolo == Simbolos.Diferente:
            self.tokenReturn = Lexico.Token(self.lexico)
            self.analisaExpressaoSimples(self)

    def analisaExpressaoSimples(self):
        if Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos:
            self.tokenReturn = Lexico.Token(self.lexico)
        self.analisaTermo(self)
        while Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos or Lexico.simbolo == Simbolos.Ou:
            self.tokenReturn = Lexico.Token(self.lexico)
            self.analisaTermo(self)

    def analisaTermo(self):
        self.analisaFator(self)
        while Lexico.simbolo == Simbolos.Multiplicacao or Lexico.simbolo == Simbolos.Divisao or Lexico.simbolo == Simbolos.E:
            self.tokenReturn = Lexico.Token(self.lexico)
            self.analisaFator(self)

    def analisaFator(self):
        if Lexico.simbolo == Simbolos.Identificador:
            pass
            # Se pesquisa_tabela(token.lexema,nível,ind)
            # Então Se (TabSimb[ind].tipo = “função inteiro”) ou
            # (TabSimb[ind].tipo = “função booleano”)
            # Então
            # self.analisaFuncao(self)
            # Senão Léxico(token)
            # Senão ERRO
            # Fim
        elif Lexico.simbolo == Simbolos.Numero:
            self.tokenReturn = Lexico.Token(self.lexico)
        elif Lexico.simbolo == Simbolos.Nao:
            self.tokenReturn = Lexico.Token(self.lexico)
            self.analisaFator(self)
        elif Lexico.simbolo == Simbolos.AbreParenteses:
            self.tokenReturn = Lexico.Token(self.lexico)
            self.analisaExpressao(self)
            if Lexico.simbolo == Simbolos.FechaParenteses:
                self.tokenReturn = Lexico.Token(self.lexico)
            else:
                exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "token ')' esperado.")
        elif Lexico.simbolo == Simbolos.Verdadeiro or self.tokenReturn.simbolo == Simbolos.Falso:
            self.tokenReturn = Lexico.Token(self.lexico)
        else:
            exit("Analisador Sintatico -> Linha : " + (Lexico.n_line + 1) + "invalido na expressao.")

    def chamadaProcedimento(self): # Gerador de codigo
        pass

    def analisaFuncao(self): # Gerador de codigo
        pass
