
class Exec:

    i = -1
    operation = ""
    attr1 = ""
    attr2 = ""
    description = ""
    pilha = []
    saida = []

    def exec(self):
        if self.operation == "LDC":
            # S := s + 1; M[s]: = k
            self.pilha.append([len(self.pilha), self.attr1])

        elif self.operation == "LDV":
            # S := s + 1; M[s] := M[n]
            addr = int(self.attr1)
            aux = self.pilha[addr]
            self.pilha.append([len(self.pilha), aux])

        elif self.operation == "ADD":
            # M[s - 1] := M[s - 1] + M[s]; s := s - 1
            soma = self.pilha[len(self.pilha) - 2] + self.pilha[len(self.pilha) - 1]
            self.pilha[len(self.pilha) - 2] = soma
            self.pilha.pop()

        elif self.operation == "SUB":
            # M[s - 1] := M[s - 1] - M[s]; s := s - 1
            sub = self.pilha[len(self.pilha) - 2] - self.pilha[len(self.pilha) - 1]
            self.pilha[len(self.pilha) - 2] = sub
            self.pilha.pop()

        elif self.operation == "MULT":
            # M[s - 1] := M[s - 1] * M[s]; s := s - 1
            mult = self.pilha[len(self.pilha) - 2] * self.pilha[len(self.pilha) - 1]
            self.pilha[len(self.pilha) - 2] = mult
            self.pilha.pop()

        elif self.operation == "DIVI":
            # M[s - 1] := M[s - 1] div M[s]; s := s - 1
            divi = self.pilha[len(self.pilha) - 2] / self.pilha[len(self.pilha) - 1]
            self.pilha[len(self.pilha) - 2] = divi
            self.pilha.pop()

        elif self.operation == "INV":
            # M[s] := -M[s]
            inv = -self.pilha[len(self.pilha) - 1]
            self.pilha[len(self.pilha) - 1] = inv

        elif self.operation == "AND":
            # se M[s - 1] = 1 e M[s] = 1 então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
            if self.pilha[len(self.pilha) - 2] == 1 and self.pilha[len(self.pilha) - 1] == 1:
                self.pilha[len(self.pilha) - 2] = 1
            else:
                self.pilha[len(self.pilha) - 2] = 0
            self.pilha.pop()

        elif self.operation == "OR":
            # se M[s - 1] = 1 ou M[s] = 1 então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
            if self.pilha[len(self.pilha) - 2] == 1 or self.pilha[len(self.pilha) - 1] == 1:
                self.pilha[len(self.pilha) - 2] = 1
            else:
                self.pilha[len(self.pilha) - 2] = 0
            self.pilha.pop()

        elif self.operation == "NEG":
            # M[s] := 1 - M[s]
            neg = 1 - self.pilha[len(self.pilha) - 1]
            self.pilha[len(self.pilha) - 1] = neg

        elif self.operation == "CME":
            # se M[s - 1] < M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
            if self.pilha[len(self.pilha) - 2] < self.pilha[len(self.pilha) - 1]:
                self.pilha[len(self.pilha) - 2] = 1
            else:
                self.pilha[len(self.pilha) - 2] = 0
            self.pilha.pop()

        elif self.operation == "CMA":
            # se M[s - 1] > M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
            if self.pilha[len(self.pilha) - 2] > self.pilha[len(self.pilha) - 1]:
                self.pilha[len(self.pilha) - 2] = 1
            else:
                self.pilha[len(self.pilha) - 2] = 0
            self.pilha.pop()

        elif self.operation == "CEQ":
            # se M[s - 1] = M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
            if self.pilha[len(self.pilha) - 2] == self.pilha[len(self.pilha) - 1]:
                self.pilha[len(self.pilha) - 2] = 1
            else:
                self.pilha[len(self.pilha) - 2] = 0
            self.pilha.pop()

        elif self.operation == "CDIF":
            # se M[s - 1] != M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
            if self.pilha[len(self.pilha) - 2] != self.pilha[len(self.pilha) - 1]:
                self.pilha[len(self.pilha) - 2] = 1
            else:
                self.pilha[len(self.pilha) - 2] = 0
            self.pilha.pop()

        elif self.operation == "CMEQ":
            # se M[s - 1] <= M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
            if self.pilha[len(self.pilha) - 2] <= self.pilha[len(self.pilha) - 1]:
                self.pilha[len(self.pilha) - 2] = 1
            else:
                self.pilha[len(self.pilha) - 2] = 0
            self.pilha.pop()

        elif self.operation == "CMAQ":
            # se M[s - 1] >= M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1
            if self.pilha[len(self.pilha) - 2] >= self.pilha[len(self.pilha) - 1]:
                self.pilha[len(self.pilha) - 2] = 1
            else:
                self.pilha[len(self.pilha) - 2] = 0
            self.pilha.pop()

        elif self.operation == "START":
            # S := -1
            self.pilha = []

        elif self.operation == "HLT":
            # Button == False
            pass

        elif self.operation == "STR":
            # M[n] := M[s]; s;=s - 1;
            addr = int(self.attr1)
            self.pilha[addr] = self.pilha[len(self.pilha) - 1]
            self.pilha.pop()

        elif self.operation == "JMP":
            self.i = int(self.attr1)

        elif self.operation == "JMPF":
            # se M[s] = 0, entao i := att1, senao i := i + 1
            zero = self.pilha[len(self.pilha) - 1]
            if zero == 0:
                self.i = int(self.attr1)
            self.pilha.pop()

        elif self.operation == "NULL":
            pass

        elif self.operation == "RD":
            # S := s + 1; M[s] := proxima entra
            # READ Variable
            #entrada = ""
            self.pilha.append(len(self.pilha)), #entrada)

        elif self.operation == "PRN":
            # M[s]; s := s - 1;
            self.saida.append(self.pilha[len(self.pilha)] - 1)
            self.pilha.pop()

        elif self.operation == "ALLOC":
            # ALLOC m, n
            # Para k := 0 até n - 1 faça
            # {s := s + 1; M[s] := M[m + k]}
            aux1 = int(self.attr1)
            aux2 = int(self.attr2)
            k = 0
            for k in range(k < int(aux2-1)):
                self.pilha.append([len(self.pilha),  0])
                self.pilha[len(self.pilha) - 1] = self.pilha[aux1 + k]
                k += 1

        elif self.operation == "DALLOC":
            # ALLOC m, n
            # Para k := n - 1 até 0 faça
            # {M[m+k]:=M[s]; s:=s - 1}
            aux1 = int(self.attr1)
            aux2 = int(self.attr2)
            k = aux2 - 1
            while k > 0:
                self.pilha[aux1 + k] = self.pilha[len(self.pilha) - 1]
                self.pilha.pop()
                k -= 1

        elif self.operation == "CALL":
            self.pilha.append([len(self.pilha), self.i+1])
            self.i = int(self.attr1)

        elif self.operation == "RETURN":
            self.i = self.pilha[len(self.pilha) - 1] - 1
            self.pilha.pop()

