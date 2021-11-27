from MaquinaVirtual.VM import VM
from tkinter import *

class Exec:
    eitas = None
    eitas2 = None
    eitas4= None
    flag = 0
    i = -1
    operation = ""
    attr1 = ""
    attr2 = ""
    description = ""
    pilha = []
    saida = []
    index = 0
    pc = 0
    auxGeralzao = []
    endFile = 0
    endProg = 0
    clearflag = 0
    createdButton = 0
    again = 0

    top = Toplevel()
    entry = Entry(top, width=20)
    number = IntVar()

    def exec(self):
        if self.endProg != 1:
            self.auxGeralzao = VM.geralzao
            self.operation = self.auxGeralzao[self.pc][1]
            if self.clearflag == 1:
                self.clearStack(self)
                self.clearInstru(self)
                self.clearflag = 0
            self.printInstru(self)
            self.clearflag = 1

            if self.operation == "LDC":
                # S := s + 1; M[s]: = k
                self.attr1 = int(self.auxGeralzao[self.pc][2])
                self.pilha.append([len(self.pilha), self.attr1])
                self.pc += 1
                self.printStack(self)

            elif self.operation == "LDV":
                # S := s + 1; M[s] := M[n]
                addr = int(self.auxGeralzao[self.pc][2])
                aux = self.pilha[addr][1]
                self.pilha.append([len(self.pilha), aux])
                self.pc += 1
                self.printStack(self)

            elif self.operation == "ADD":
                # M[s - 1] := M[s - 1] + M[s]; s := s - 1
                soma = self.pilha[len(self.pilha) - 2][1] + self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 2][1] = soma
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "SUB":
                # M[s - 1] := M[s - 1] - M[s]; s := s - 1
                sub = self.pilha[len(self.pilha) - 2][1] - self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 2][1] = sub
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "MULT":
                # M[s - 1] := M[s - 1] * M[s]; s := s - 1
                mult = self.pilha[len(self.pilha) - 2][1] * self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 2][1] = mult
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "DIVI":
                # M[s - 1] := M[s - 1] div M[s]; s := s - 1
                divi = self.pilha[len(self.pilha) - 2][1] / self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 2][1] = divi
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "INV":
                # M[s] := -M[s]
                inv = -self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 1][1] = inv
                self.pc += 1
                self.printStack(self)

            elif self.operation == "AND":
                # se M[s - 1] = 1 e M[s] = 1 então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] == 1 and self.pilha[len(self.pilha) - 1][1] == 1:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "OR":
                # se M[s - 1] = 1 ou M[s] = 1 então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] == 1 or self.pilha[len(self.pilha) - 1][1] == 1:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "NEG":
                # M[s] := 1 - M[s]
                neg = 1 - self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 1][1] = neg
                self.pc += 1
                self.printStack(self)

            elif self.operation == "CME":
                # se M[s - 1] < M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if int(self.pilha[len(self.pilha) - 2][1]) < int(self.pilha[len(self.pilha) - 1][1]):
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "CMA":
                # se M[s - 1] > M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] > self.pilha[len(self.pilha) - 1][1]:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "CEQ":
                # se M[s - 1] = M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] == self.pilha[len(self.pilha) - 1][1]:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "CDIF":
                # se M[s - 1] != M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] != self.pilha[len(self.pilha) - 1][1]:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "CMEQ":
                # se M[s - 1] <= M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] <= self.pilha[len(self.pilha) - 1][1]:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "CMAQ":
                # se M[s - 1] >= M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] >= self.pilha[len(self.pilha) - 1][1]:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "START":
                # S := -1
                self.pilha = []
                self.pc += 1
                self.printStack(self)

            elif self.operation == "HLT":
                # Button == False
                self.endProg = 1
                self.printStack(self)

            elif self.operation == "STR":
                # M[n] := M[s]; s:=s - 1;
                addr = int(self.auxGeralzao[self.pc][2])
                self.pilha[addr][1] = self.pilha[len(self.pilha) - 1][1]
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "JMP":
                self.pc = int(self.auxGeralzao[self.pc][2])
                self.printStack(self)

            elif self.operation == "JMPF":
                # se M[s] = 0, entao i := att1, senao i := i + 1
                zero = self.pilha[len(self.pilha) - 1][1]
                if zero == 0:
                    self.pc = int(self.auxGeralzao[self.pc][2])
                else:
                    self.pc += 1
                self.pilha.pop()
                self.printStack(self)

            elif self.operation == "NULL":
                self.pc += 1
                self.printStack(self)

            elif self.operation == "RD":
                # S := s + 1; M[s] := proxima entra
                # READ Variable
                if self.again == 0:
                    self.again = 1
                    self.top.title("Insira o numero")
                    self.top.geometry("300x200")
                    self.entry.pack()
                    if self.createdButton == 0:
                        button = Button(self.top, text="Insert", command=lambda: self.insertValue(self))
                        button.pack()
                        self.createdButton = 1
                    self.top.wait_variable(self.number)
                    self.pilha.append([len(self.pilha), self.number.get()])
                    self.pc += 1
                    self.printStack(self)
                    self.again = 0

            elif self.operation == "PRN":
                # M[s]; s := s - 1;
                self.saida.append(self.pilha[len(self.pilha) - 1])
                self.pilha.pop()
                self.pc += 1
                self.printStack(self)

            elif self.operation == "ALLOC":
                # ALLOC m, n
                # Para k := 0 até n - 1 faça
                # {s := s + 1; M[s] := M[m + k]}
                m = int(self.auxGeralzao[self.pc][2])
                n = int(self.auxGeralzao[self.pc][3])
                k = 0
                while k < n:
                    self.pilha.append([len(self.pilha), 0])
                    self.pilha[len(self.pilha) - 1][1] = self.pilha[m + k][1]
                    k += 1
                self.pc += 1
                self.printStack(self)

            elif self.operation == "DALLOC":
                # ALLOC m, n
                # Para k := n - 1 até 0 faça
                # {M[m+k]:=M[s]; s:=s - 1}
                m = int(self.auxGeralzao[self.pc][2])
                n = int(self.auxGeralzao[self.pc][3])
                k = n - 1
                while k >= 0:
                    self.pilha[m + k][1] = self.pilha[len(self.pilha) - 1][1]
                    self.pilha.pop()
                    k -= 1
                self.pc += 1
                self.printStack(self)

            elif self.operation == "CALL":
                self.pilha.append([len(self.pilha), self.pc + 1])
                self.pc = int(self.auxGeralzao[self.pc][2])
                self.printStack(self)

            elif self.operation == "RETURN":
                self.pc = int(self.pilha[len(self.pilha) - 1][1])
                self.pilha.pop()
                self.printStack(self)

    def exec2(self):
        self.auxGeralzao = VM.geralzao
        self.endFile = VM.maxSize
        while self.endProg != 1:
            self.operation = self.auxGeralzao[self.pc][1]
            if self.clearflag == 1:
                self.clearStack(self)
                self.clearInstru(self)
                self.clearflag = 0
            self.printInstru(self)
            self.clearflag = 1

            if self.operation == "LDC":
                # S := s + 1; M[s]: = k
                self.attr1 = int(self.auxGeralzao[self.pc][2])
                self.pilha.append([len(self.pilha), self.attr1])
                self.pc += 1

            elif self.operation == "LDV":
                # S := s + 1; M[s] := M[n]
                addr = int(self.auxGeralzao[self.pc][2])
                aux = self.pilha[addr][1]
                self.pilha.append([len(self.pilha), aux])
                self.pc += 1

            elif self.operation == "ADD":
                # M[s - 1] := M[s - 1] + M[s]; s := s - 1
                soma = self.pilha[len(self.pilha) - 2][1] + self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 2][1] = soma
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "SUB":
                # M[s - 1] := M[s - 1] - M[s]; s := s - 1
                sub = self.pilha[len(self.pilha) - 2][1] - self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 2][1] = sub
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "MULT":
                # M[s - 1] := M[s - 1] * M[s]; s := s - 1
                mult = self.pilha[len(self.pilha) - 2][1] * self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 2][1] = mult
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "DIVI":
                # M[s - 1] := M[s - 1] div M[s]; s := s - 1
                divi = self.pilha[len(self.pilha) - 2][1] / self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 2][1] = divi
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "INV":
                # M[s] := -M[s]
                inv = -self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 1][1] = inv
                self.pc += 1

            elif self.operation == "AND":
                # se M[s - 1] = 1 e M[s] = 1 então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] == 1 and self.pilha[len(self.pilha) - 1][1] == 1:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "OR":
                # se M[s - 1] = 1 ou M[s] = 1 então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] == 1 or self.pilha[len(self.pilha) - 1][1] == 1:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "NEG":
                # M[s] := 1 - M[s]
                neg = 1 - self.pilha[len(self.pilha) - 1][1]
                self.pilha[len(self.pilha) - 1][1] = neg
                self.pc += 1

            elif self.operation == "CME":
                # se M[s - 1] < M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if int(self.pilha[len(self.pilha) - 2][1]) < int(self.pilha[len(self.pilha) - 1][1]):
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "CMA":
                # se M[s - 1] > M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] > self.pilha[len(self.pilha) - 1][1]:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "CEQ":
                # se M[s - 1] = M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] == self.pilha[len(self.pilha) - 1][1]:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "CDIF":
                # se M[s - 1] != M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] != self.pilha[len(self.pilha) - 1][1]:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "CMEQ":
                # se M[s - 1] <= M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] <= self.pilha[len(self.pilha) - 1][1]:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "CMAQ":
                # se M[s - 1] >= M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
                if self.pilha[len(self.pilha) - 2][1] >= self.pilha[len(self.pilha) - 1][1]:
                    self.pilha[len(self.pilha) - 2][1] = 1
                else:
                    self.pilha[len(self.pilha) - 2][1] = 0
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "START":
                # S := -1
                self.pilha = []
                self.pc += 1

            elif self.operation == "HLT":
                # Button == False
                self.endProg = 1

            elif self.operation == "STR":
                # M[n] := M[s]; s:=s - 1;
                addr = int(self.auxGeralzao[self.pc][2])
                self.pilha[addr][1] = self.pilha[len(self.pilha) - 1][1]
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "JMP":
                self.pc = int(self.auxGeralzao[self.pc][2])

            elif self.operation == "JMPF":
                # se M[s] = 0, entao i := att1, senao i := i + 1
                zero = self.pilha[len(self.pilha) - 1][1]
                if zero == 0:
                    self.pc = int(self.auxGeralzao[self.pc][2])
                else:
                    self.pc += 1
                self.pilha.pop()

            elif self.operation == "NULL":
                self.pc += 1

            elif self.operation == "RD":
                # S := s + 1; M[s] := proxima entra
                # READ Variable
                self.printStack(self)
                self.top.title("Insira o numero")
                self.top.geometry("300x200")
                self.entry.pack()
                if self.createdButton == 0:
                    button = Button(self.top, text="Insert", command=lambda: self.insertValue(self))
                    button.pack()
                    self.createdButton = 1
                self.top.wait_variable(self.number)
                #button.destroy()
                self.pilha.append([len(self.pilha), self.number.get()])
                self.pc += 1

            elif self.operation == "PRN":
                # M[s]; s := s - 1;
                self.saida.append(self.pilha[len(self.pilha) - 1])
                self.pilha.pop()
                self.pc += 1

            elif self.operation == "ALLOC":
                # ALLOC m, n
                # Para k := 0 até n - 1 faça
                # {s := s + 1; M[s] := M[m + k]}
                m = int(self.auxGeralzao[self.pc][2])
                n = int(self.auxGeralzao[self.pc][3])
                k = 0
                while k < n:
                    self.pilha.append([len(self.pilha),  0])
                    self.pilha[len(self.pilha) - 1][1] = self.pilha[m + k][1]
                    k += 1
                self.pc += 1

            elif self.operation == "DALLOC":
                # ALLOC m, n
                # Para k := n - 1 até 0 faça
                # {M[m+k]:=M[s]; s:=s - 1}
                m = int(self.auxGeralzao[self.pc][2])
                n = int(self.auxGeralzao[self.pc][3])
                k = n - 1
                while k >= 0:
                    self.pilha[m + k][1] = self.pilha[len(self.pilha) - 1][1]
                    self.pilha.pop()
                    k -= 1
                self.pc += 1

            elif self.operation == "CALL":
                self.pilha.append([len(self.pilha), self.pc+1])
                self.pc = int(self.auxGeralzao[self.pc][2])

            elif self.operation == "RETURN":
                self.pc = int(self.pilha[len(self.pilha) - 1][1])
                self.pilha.pop()

    def printStack(self):
        for i in self.pilha:
            self.eitas.insert('','end',values=(i[0], i[1]))

    def clearStack(self):
        for i in self.eitas.get_children():
            self.eitas.delete(i)

    def printInstru(self):
        self.eitas4.insert('', 'end', values=(self.auxGeralzao[self.pc][0], self.auxGeralzao[self.pc][1]))

    def clearInstru(self):
        for i in self.eitas4.get_children():
            self.eitas4.delete(i)

    def insertValue(self):
        self.number.set(self.entry.get())
        #self.pilha.append([len(self.pilha), self.number])
        #self.pc += 1
