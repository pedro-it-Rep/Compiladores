#                           Modulo Sintático
# Direitos reservados por Fabricio Silva Cardoso e Pedro Ignácio Trevisan
#
# Programa responsavel por analisar de forma semantica o arquivo recebido no modulo lexical.
#
# Este módulo é o corpo principal do compilador, onde chama todas as funções dos outros arquivos,
# direcionando para o fim do arquivo lide e criando o compilador e seu código de máquina. Ele trabalha
# com a chamada do lexico, onde gera tokens para ser analisado pelo sintatico e redirecionar cada token
# para seu devido lugar, chamando os outros arquivos.
#
# Todos os simbolos estão disponiveis no arquivo Simbolos.py
# Todos os tipos estão disponiveis no arquivo Tipos.py
# Todos os comando estão disponíveis no arquivo Comandos.py
#
# O intuito do programa é fazer uma analise completa da linguagem proposta
# pelo professor a ponto de compor um sistema, sendo este o nosso compilador.

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

    # Inicializa a leitura do arquivo, recebendo o token ["nomedoprograma", "sprograma"] de inicio.
    # Declara na pilha o endereço 0 para retorno de função.
    # Executa o corpo do arquivo.
    # Declara a desalocação do valor de retorno da função.
    def Sintatico(self):
        GeradorDeCodigo.isCreated(GeradorDeCodigo)
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Programa:
            GeradorDeCodigo.geraComando(GeradorDeCodigo, Comandos.Start)
            #Aloca as váriaveis por linha
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
                    # Desaloca todas as variáveis declaradas
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
    # Decide qual o próximo passo
    def analisaBloco(self):
        Lexico.Token(Lexico)
        self.analisa_et_variaveis(self)
        self.analisaSubrotina(self)
        self.analisaComandos(self)

    # Verica se é variável.
    # Termina quando le um ";"
    def analisa_et_variaveis(self):
        #Token ["var", "svar"]
        if Lexico.simbolo == Simbolos.Var:
            Lexico.Token(Lexico)

            if Lexico.simbolo == Simbolos.Identificador:
                while Lexico.simbolo == Simbolos.Identificador:
                    # Recebe o nome da variável e faz a leitura de todas as variáveis
                    # Até encontrar ":"
                    self.analisaVariaveis(self)
                    if Lexico.simbolo == Simbolos.PontoVirgula:
                        Lexico.Token(Lexico)
                    else:
                        Errors.exceptionInvalidExpression(Errors, Lexico.n_line)
            else:
                Errors.exceptionMissingIdentifier(Errors, Lexico.n_line)

    #Declara a varriável.
    #Verfica se já foi declarado a variável.
    # Atribui o tipo para as variáveis
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

    #Atribui os tipos para as variáveis e reserva na Tabela de Símbolos
    def analisaTipo(self):
        if Lexico.simbolo != Simbolos.Inteiro and Lexico.simbolo != Simbolos.Booleano:
            Errors.exceptionTypeInvalid(Errors, Lexico.n_line)

        if Lexico.simbolo == Simbolos.Inteiro:
            TabelaDeSimbolos.alteraTipo(TabelaDeSimbolos, Tipos.Inteiro)
        elif Lexico.simbolo == Simbolos.Booleano:
            TabelaDeSimbolos.alteraTipo(TabelaDeSimbolos, Tipos.Boolean)

        Lexico.Token(Lexico)
        self.nVars = 0

    # Faz a leitura do corpo do código
    # Faz a leitura até encontrar um "fim"
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

    # Verifica se o símbolo é um procedimento ou alguma variável
    # Caso não seja, verifica se é uma condição ou ação
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

    # Verfica se o indentificador lido foi uma variável ou procedimento.
    # Guarda a váriavel para usar na atribuição.
    def analisa_atrib_chprocedimento(self):
        self.identificador = []
        self.identificador = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
        Lexico.Token(Lexico)

        if Lexico.simbolo == Simbolos.Atribuicao:
            self.analisaAtribuicao(self)
        else:
            self.chamadaProcedimento(self)

    # Caso seja ação "ler", verifica se o indetificador dentro do parametro é válido
    # Token ["leia", "sleia"]
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

    # Caso seja ação "escrever", verifica se o indetificador dentro do parametro é função ou variável, e se é válido
    # Token ["escreve", "sescreve"]
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

    # Analisa a expressão da condição.
    # Gera os códigos da máquina.
    # Analisa o corpo da condição.
    # Token ["enquanto", "senquanto"]
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

    # Analisa a expressão da condição.
    # Gera os códigos da máquina.
    # Analisa o corpo da condição.
    # Token ["se", "sse"]
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

    # Verficai se é função ou procedimento
    def analisaSubrotina(self):
        self.nVars = 0
        #Flag para controlar quando deve printa o NULL
        #Printa caso o simbolo seja um procedimento ou função
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

    # Analisa as variáveis, os procedimentos e o corpo da função.
    def analisaDeclaraFunc(self):
        Lexico.Token(Lexico)
        if Lexico.simbolo == Simbolos.Identificador:
            # Verifica se o indentificador já foi criado
            if not TabelaDeSimbolos.isDeclaradoNoEscopo(TabelaDeSimbolos, Lexico.lexema):
                TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.Function, True, None)
                # Pega todas as informações contidas nesse procedimento
                # self.found["nomedoidentificador","símbolodoidentifcador","layer","posiçãodamemória"]
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
            # Verifica se o indentificador já foi criado
            if not TabelaDeSimbolos.isDeclaradoNoEscopo(TabelaDeSimbolos, Lexico.lexema):
                TabelaDeSimbolos.insereTabela(TabelaDeSimbolos, Lexico.lexema, Tipos.Procedimento, True, None)
                GeradorDeCodigo.geraRotulo(GeradorDeCodigo, self.proxRotulo)
                # Pega todas as informações contidas nesse procedimento
                #self.found["nomedoidentificador","símbolodoidentifcador","layer","posiçãodamemória"]
                self.found = TabelaDeSimbolos.busca(TabelaDeSimbolos, Lexico.lexema)
                self.found[3] = self.proxRotulo
                self.proxRotulo += 1

                Lexico.Token(Lexico)
                if Lexico.simbolo == Simbolos.PontoVirgula:
                    self.analisaBloco(self)
                    variables = TabelaDeSimbolos.getVariables(TabelaDeSimbolos)
                    #Caso não tem variável para ser declarada, não precisa dar dalloc
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

    # Analisa a expressão seguida da condição
    def analisaExpressao(self):
        self.analisaExpressaoSimples(self)
        if Lexico.simbolo == Simbolos.Maior or Lexico.simbolo == Simbolos.MaiorIgual or \
                Lexico.simbolo == Simbolos.Igual or Lexico.simbolo == Simbolos.Menor or \
                Lexico.simbolo == Simbolos.MenorIgual or Lexico.simbolo == Simbolos.Diferente:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
            self.analisaExpressaoSimples(self)

    # Verifica qual é o sinal da variável e qual é o simbolo lógico
    def analisaExpressaoSimples(self):
        if Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
        self.analisaTermo(self)
        while Lexico.simbolo == Simbolos.Mais or Lexico.simbolo == Simbolos.Menos or Lexico.simbolo == Simbolos.Ou:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
            self.analisaTermo(self)

    # Verifica qual é o operador ou qual é o simbolo lógico
    def analisaTermo(self):
        self.analisaFator(self)
        while Lexico.simbolo == Simbolos.Multiplicacao or Lexico.simbolo == Simbolos.Divisao or Lexico.simbolo == Simbolos.E:
            self.expressao.append([Lexico.lexema, Lexico.simbolo])
            Lexico.Token(Lexico)
            self.analisaFator(self)

    #Verifica se o símbolo é um identificador, número, um sabre ou fecha parenteses, uma negação ou se é verdadeiro ou falso
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

    # Analisa a expressão seguida do sinal de recebe ":=", se ela é válida
    # E verifica se a atribuição é válida também
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
            #Faz a subtração de -4, pois é para remover da contagem o end de retorno da função
            #
            #
            GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Store, (self.proxEnd - self.nVars - 4))
        else:
            GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Store, self.identificador[3])

    def chamadaProcedimento(self):  # Gerador de codigo
        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Call, self.identificador[3])

    def chamadaFuncao(self):  # Gerador de codigo

        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.Call, self.found[3])
        GeradorDeCodigo.geraComando1Var(GeradorDeCodigo, Comandos.LoadValue, 0)

    # Com a expressao gerado pelo analisa expressao, receberemos a expressão como um vetor, antes de passar pra pós-ordem
    # Passaremos por cada posição do vetor verficando se o que vem antes de um número ou identificador
    # Pode estar relacionado ao sinal do núemro ou identificador
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

    # Após ter gerado a expressão e colocado ela em pós-ordem
    # Agora analisamos em forma de pós-ordem e geramos seu cógigo para máquina virtual
    # De cada elemento do vetor
    def geraExpressao(self):
        for i in self.expressao:
            # self.expressao com todos os lexemas e simbolos necessários
            # Para criar o código de máquina
            # i[lexema][simbolo]
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