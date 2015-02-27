from memory import Memory
class CPU:
    def __init__(self):
        self.registers = {
            "%SP":0x00,
            "%MP":0x00,
            "%CL":0x00,
            "%AR":0x00,
            "%GP1":0x00,
            "%GP2":0x00,
            "%GP3":0x00,
            "%GP4":0x00,
            "%GP5":0x00,
            "%GP6":0x00,
            "%GP7":0x00,
            "%GP8":0x00,
            "%SY1":0x00,
            "%SY2":0x00,
            "%SY3":0x00
        }

    def cycle(self):
        self.registers["%CL"] += 1

    def INC(self,register, times = 1):
        for i in xrange(times):
            self.registers[register] += 1

    def ADD(self,a,b):
        return a + b

    def SUB(self,a,b):
        return a - b

    def MUL(self,a,b):
        return a * b

    def DIV(self,a,b):
        return a / b

    def AND(self,a,b):
        return a & b

    def OR(self,a,b):
        return a | b

    def NOT(self,a):
        return ~a

    def XOR(self,a,b):
        return a ^ b

    def LSF(self,a,b):
        return a << b

    def RSF(self,a,b):
        return a >> b

    def MOV(self,register,value):
        self.registers[register] = value
