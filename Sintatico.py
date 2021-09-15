from Lexico import Lexico

class Sintatico:

    def __init__(self):
        self.tokenReturn = []

    def Sintatico(self):

        #Def rotulo inteiro
        #rotulo := 1
        self.tokenReturn = Lexico(self)
        endFile = Lexico.maxChar
        if self.tokenReturn.simbolo == "sprograma":
            #insere_tabela(token.lexema, "nomedoprograma","","")
            if self.tokenReturn.simbolo == "sponto_virgula":
                self.analisaBloco(self)
                if self.tokenReturn.simbolo == "sponto":
                    if endFile == endFile.maxChar:
                        print("Sucesso")
                    else:
                        print("Erro")
                        return
                else:
                    print("Error")
                    return
            else:
                print("Erro")
                return
        else:
            print("Erro")
            return

    def analisaBloco(self):
        self.tokenReturn = Lexico(self)
        self.analisa_et_variaveis(self)
        self.analisaSubrotina(self)
        self.analisaComandos(self)

    def analisa_et_variaveis(self, tokenReturn):
        if self.tokenReturn.simbolo == "svar":
            self.tokenReturn = Lexico(self)
            if self.tokenReturn.simbolo == "sidentificador":
                while tokenReturn.simbolo == "sidentificador":
                    self.analisaVariaveis(self)
                    if self.tokenReturn.simbolo == "sponto_virgula":
                        self.tokenReturn = Lexico(self)
                    else:
                        print("Erro")
                        return
            else:
                print("Erro")
                return
        return

    def analisaVariaveis(self):
        while self.tokenReturn.simbolo != "sdoispontos":
            if self.tokenReturn.simbolo == "sidentificador":
                #Pesquisa_duplicvar_tabela(token.lexema)
                #se nao encontrou duplicidade
                #entao inicio
                    #insere_tablea(tokenReturn, "variavel")
                    self.tokenReturn = Lexico(self)
                    if self.tokenReturn.simbolo == "svirgula" or self.tokenReturn.simbolo == "sdoispontos":
                        if self.tokenReturn.simbolo == "svirgula":
                            self.tokenReturn = Lexico(self)
                            if self.tokenReturn.simbolo == "sdoispontos":
                                print("Erro")
                                return
                        return
                    print("Erro")
                    return
            print("error")
        tokenReturn = Lexico(self)
        self.analisaTipo(self)
        return

    def analisaTipo(self):
        if self.tokenReturn.simbolo != "sinteiro" and self.tokenReturn.simbolo != "sbooleano":
            print("Erro")
            return
        else:
            #senao coloca_tipo_tabela(tokenReturn.lexema)
            return

    def analisaComandos(self):
        if self.tokenReturn.simbolo == "sinicio":
            self.tokenReturn = Lexico(self)
            self.analisaComandoSimples(self)
            while self.tokenReturn.simbolo != "sfim":
                if self.tokenReturn.simbolo == "sponto_virgula":
                    self.tokenReturn = Lexico(self)
                    if self.tokenReturn.simbolo != "sfim":
                        self.analisaComandosSimples(self)
                else:
                    print("Erro")
                    return
            self.tokenReturn = Lexico(self)
        else:
            print("Erro")
            return

    def analisaComandoSimples(self):
        if self.tokenReturn.simbolo == "sidentificador":
            self.analisa_atrib_chprocedimento(self)
        elif self.tokenReturn.simbolo == "sse":
            self.analisaSe(self)
        elif self.tokenReturn.simbolo == "senquanto":
            self.analiasaEnquanto(self)
        elif self.tokenReturn.simbolo == "sleia":
            self.analisaLeia(self)
        elif self.tokenReturn.simbolo == "sescreva":
            self.analisaEscreva(self)
        else:
            self.analisaComando(self)

    def analisa_atrib_chprocedimento(self):
        tokenReturn = Lexico(self)
        if tokenReturn.simbolo == "satribuicao":
            self.analisaAtribuicao(self)
        else:
            self.chamadaProcedimento(self)

    def analisaLeia(self):
        self.tokenReturn = Lexico(self)
        if self.tokenReturn.simbolo == "sabre_parenteses":
            self.tokenReturn = Lexico(self)
            if self.tokenReturn.simbolo == "sidentificador":
                #se pesquisa_decvar_tabela(tokenRetun.lexema)
                #entao inicio (pesquisa em toda a tabela)
                self.tokenReturn = Lexico(self)
                if self.tokenReturn.simbolo == "sfecha_parenteses":
                    self.tokenReturn = Lexico(self)
                else:
                    print("Erro")
                    return
                #senao Erro
            else:
                print("Erro")
                return
        else:
            print("Erro")
            return

    def analisaEscreva(self):
        self.tokenReturn = Lexico(self)
        if self.tokenReturn.simbolo == "sabre_parenteses":
            self.tokenReturn = Lexico(self)
            if self.tokenReturn.simbolo == "sidentificador":
                #se pesquisa_decvarfunc_tabela(token.lexema)
                    self.tokenReturn = Lexico(self)
                    if self.tokenReturn.simbolo == "sfecha_parenteses":
                        self.tokenReturn = Lexico(self)
                    else:
                        print("Erro")
                        return
                #senao Erro
            else:
                print("Erro")
                return
        else:
            print("Erro")
            return

    def analisaEnquanto(self):
        #Def auxrot1,auxrot2 inteiro
        #auxrot1:= rotulo
        #Gera(rotulo,NULL,´ ´,´ ´) {início do while}
        #rotulo:= rotulo+1
        self.tokenReturn = Lexico(self)
        self.analisaExpressao(self)
        if self.tokenReturn.simbolo == "sfaca":
            #auxrot2:= rotulo
            #Gera(´ ´,JMPF,rotulo,´ ´) {salta se falso}
            #rotulo:= rotulo+1
            self.tokenReturn = Lexico(self)
            self.analisaComandoSimples(self)
            #Gera(´ ´,JMP,auxrot1,´ ´) {retorna início loop}
            #Gera(auxrot2,NULL,´ ´,´ ´) {fim do while}
        else:
            print("Erro")
            return

    def analisaSe(self):
        self.tokenReturn = Lexico(self)
        self.analisaExpressao(self)
        if self.tokenReturn.simbolo == "sentao":
            self.tokenReturn = Lexico(self)
            self.analisaComandoSimples(self)
            if self.tokenReturn.simbolo == "ssenao":
                self.tokenReturn = Lexico(self)
                self.analisaComandoSimples(self)
        else:
            print("Erro")
            return

    def analisaSubrotina(self):
        #Def. auxrot, flag inteiro
        #flag = 0
        #if (token.simbolo = sprocedimento) ou
        #(token.simbolo = sfunção)
        #então início
        #auxrot:= rotulo
        #GERA(´ ´,JMP,rotulo,´ ´) {Salta sub-rotinas}
        #rotulo:= rotulo + 1
        #flag = 1
        #fim
        while self.tokenReturn.simbolo == "sprocedimento" or self.tokenReturn.simbolo == "sfuncao":
            if self.tokenReturn.simbolo == "sprocedimento":
                self.analisaDeclaracaoProc(self)
            else:
                self.analisaDeclaracaoFunc(self)
            if self.tokenReturn.simbolo == "sponto_virgula":
                self.tokenReturn = Lexico(self)
            else:
                print("Erro")
                return
            #if flag = 1
            #então Gera(auxrot,NULL,´ ´,´ ´) {início do principal}
            #fim

    def analisaDeclaracaoProc(self):
        self.tokenReturn = Lexico(self)
        #nível := “L” (marca ou novo galho)
        if self.tokenReturn.simbolo == "sidentificador":
            #pesquisa_declproc_tabela(token.lexema)
            #se não encontrou
            #então início
            #Insere_tabela(token.lexema,”procedimento”,nível, rótulo)
            #{guarda na TabSimb}
            #Gera(rotulo,NULL,´ ´,´ ´)
            #{CALL irá buscar este rótulo na TabSimb}
            #rotulo:= rotulo+1
            self.tokenReturn = Lexico(self)
            if self.tokenReturn.simbolo == "sponto_virgula":
                self.analisaBloco(self)
            else:
                print("Erro")
                return
            #fim
            #senão ERRO
        else:
            print("Erro")
            return
        #DESEMPILHA OU VOLTA NÍVEL

    def analisaExpressao(self):
        self.analisaExpressaoSimples(self)
        if self.tokenReturn.simbolo == "smaior" or self.tokenReturn.simbolo == "smaiorig" or self.tokenReturn.simbolo == "sig" or self.tokenReturn.simbolo == "smenor" or self.tokenReturn.simbolo == "smenorig" or self.tokenReturn.simbolo == "sdif":
            self.tokenReturn = Lexico(self)
            self.analisaExpressaoSimples(self)

    def analisaExpressaoSimples(self):
        if self.tokenReturn.simbolo == "smais" or  self.tokenReturn.simbolo == "smenos":
            self.tokenReturn = Lexico(self)
            self.analisaTermo(self)
            while self.tokenReturn.simbolo == "smais" or self.tokenReturn.simbolo == "smenor" or self.tokenReturn.simbolo == "sou":
                self.tokenReturn = Lexico(self)
                self.analisaTermo(self)

    def analisaTermo(self):
        self.analisaFator(self)
        while self.tokenReturn.simbolo == "smult" or self.tokenReturn.simbolo == "sdiv" or self.tokenReturn.simbo == "se":
            self.tokenReturn = Lexico(self)
            self.analisaFator(self)

    def analisaFator(self):
        if self.tokenReturn.simbolo == "sidentificador":
            #Se pesquisa_tabela(token.lexema,nível,ind)
            #Então Se (TabSimb[ind].tipo = “função inteiro”) ou
            #(TabSimb[ind].tipo = “função booleano”)
            #Então
            self.analisaFuncao(self)
            #Senão Léxico(token)
            #Senão ERRO
            #Fim
        else:
            if self.tokenReturn.simbolo == "snumero":
                self.tokenReturn = Lexico(self)
            else:
                if self.tokenReturn.simbolo == "snao":
                    self.tokenReturn = Lexico(self)
                    self.analisaFator(self)
                else:
                    if self.tokenReturn.simbolo == "sabre_parenteses":
                        self.tokenReturn = Lexico(self)
                        self.analisaExpressao(self)
                        if self.tokenReturn.simbolo == "sfecha_parentese":
                            self.tokenReturn.simbolo = Lexico(self)
                        else:
                            print("Erro")
                            return
                    else:
                        if self.tokenReturn.simbolo == "verdadeiro" or self.tokenReturn.simbolo == "falso": ##
                            self.tokenReturn = Lexico(self)
                        else:
                            print("Erro")
                            return

    def chamadaProcedimento(self):
        pass
    def analisaFuncao(self):
        pass









