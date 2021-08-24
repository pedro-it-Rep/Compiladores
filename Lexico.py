from tkinter.filedialog import askopenfilename


class Lexico:

    file_path = askopenfilename()
    file = file_path
    line = 0
    caracter = ""

    def Lexico(self, source):
        source = self.file
        self.caracter = source.read(1)
        #Fazer tratamento de erros


    def Token(self):
        while self.caracter == 10:
            self.caracter = self.file.read(1)
            self.line = self.line + 1

        while self.caracter != -1 and (self.caracter == '{' or self.caracter == 8 or self.caracter == 9):
            #-1 -> Caracter invalido // 8 -> Escreva // 9 -> Leia
            if self.caracter == '{':
                while self.caracter != -1 and self.caracter != '}':
                    if self.caracter == 10:
                        self.line = self.line + 1
                    self.caracter = self.file.read(1)

                self.caracter = self.file.read(1)

                while self.caracter != -1 and (self.caracter == 8 or self.caracter == 9 or self.caracter == 10):
                    if self.caracter == 10:
                        self.line = self.line + 1

        if self.caracter != -1:
            #pegatoken()
            #return tk

        return None