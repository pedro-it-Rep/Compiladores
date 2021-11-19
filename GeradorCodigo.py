import os


class GeradorDeCodigo:
    arquivo = "geral1.obj"
    f1 = arquivo

    def isCreated(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "w+") as self.f1:
                pass
        else:
            with open(self.arquivo, "w") as self.f1:
                pass

    def geraRotulo(self, n):
        with open(self.arquivo, "a+") as self.f1:
            self.f1.write("{}\t{}\n".format(n, "NULL"))

    def geraComando(self, comando):
        with open(self.arquivo, "a+") as self.f1:
            self.f1.write("\t{} \n".format(comando))

    def geraComando1Var(self, comando, arg):
        with open(self.arquivo, "a+") as self.f1:
            self.f1.write("\t{}\t{} \n".format(comando, arg))

    def geraComando2Var(self, comando, arg, arg2):
        with open(self.arquivo, "a+") as self.f1:
            self.f1.write("\t{}\t{}\t{} \n".format(comando, arg, arg2))

    def closeFile(self):
        self.f1.close()
