class Ops:
    def __init__(self):
        self.ops = {
            #REGISTERS
            "%SP":"\xF1",
            "%MP":"\xF2",
            "%CL":"\xF3",
            "%AL":"\xF4",
            "%GP1":"\xF5",
            "%GP2":"\xF6",
            "%GP3":"\xF7",
            "%GP4":"\xF8",
            "%GP5":"\xF9",
            "%GP6":"\xFA",
            "%GP7":"\xFB",
            "%GP8":"\xFC",
            "%SY1":"\xFD",
            "%SY2":"\xFE",
            "%SY3":"\xFF",

            #ARITHMATIC OPERATIONS
            "NOP":"\x00",
            "ADD":"\x01",
            "SUB":"\x02",
            "MUL":"\x03",
            "DIV":"\x04",
            "AND":"\x05",
            "OR":"\x06",
            "NOT":"\x07",
            "XOR":"\x08",
            "LSF":"\x09",
            "RSF":"\x0A",

            #REGISTER/MEMORY OPS
            "MOV":"\x0B",
            "PSH":"\x0C",
            "POP":"\x0D",
            "SYS":"\x0E",
            "JMP":"\x0F",
            "CMP":"\x11",
            "HLT":"\x12"
        }

    def contains(self,str):
        if str in self.ops:
            #print str
            return self.ops[str]
        else:
            #print chr(int(str))
            return chr(int(str))
