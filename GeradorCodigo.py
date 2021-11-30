#                         Modulo Gerador De Codigo
# Direitos reservados por Fabricio Silva Cardoso e Pedro Ignácio Trevisan
#
# Programa responsavel por criar os comando para a máquina virtual.
#
# Este módulo é responsável por gerar os códigos da máquina virtual de forma que
# possa ser feita a leitura dessa arquivo pela máquina.
# As informações iniciais estão separadas por "\t" e o resto das informações
# separadas por " ", para facilitar o tratamento na máquina virtual
#
#
# O intuito do programa é fazer uma analise completa da linguagem proposta
# pelo professor a ponto de compor um sistema, sendo este o nosso compilador.

import os


# Inicializa o arquivo com um nome padrão
class GeradorDeCodigo:
    arquivo = "geral1.obj"
    f1 = arquivo

    # Verfica se o arquivo já foi criado
    # Caso positivo, sobrescreve, caso negativo, cria
    def isCreated(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "w+") as self.f1:
                pass
        else:
            with open(self.arquivo, "w") as self.f1:
                pass

    # Gera o comando NULL no nosso arquivo
    def geraRotulo(self, n):
        with open(self.arquivo, "a+") as self.f1:
            self.f1.write("{} \t{} \n".format(n, "NULL"))

    # Usado para comando com 0 argumentos.EX:.  RDN
    def geraComando(self, comando):
        with open(self.arquivo, "a+") as self.f1:
            self.f1.write("\t{} \n".format(comando))

    # Usado para comando com 1 argumentos.EX:. JMPF 1
    def geraComando1Var(self, comando, arg):
        with open(self.arquivo, "a+") as self.f1:
            self.f1.write("\t{} {} \n".format(comando, arg))

    # Usado para comando com 2 argumentos.EX:. ALLOC 0 1
    def geraComando2Var(self, comando, arg, arg2):
        with open(self.arquivo, "a+") as self.f1:
            self.f1.write("\t{} {} {} \n".format(comando, arg, arg2))

    def closeFile(self):
        self.f1.close()

