#!/usr/bin/env python
from parser import Parser
from ops import Ops
import sys
class Compiler:
    def __init__(self,file):
        parser = Parser(file)
        self.filename = file
        parser.tokenize()
        parser.get_labels()
        parser.remove_label_defs()
        parser.find_jumps()
        #At this point, the code has been parsed, jumps have been calculated and the code inserted.
        self.code = parser.tokens
        self.ops = Ops()
        #print self.code

    def translate_to_opcodes(self):
        hexcode = []
        for i, item in enumerate(self.code):
            hexcode.append(self.ops.contains(item)) #If the item is one of the opcodes, return the opcode in hex. If it isnt, return the number in hex.
        #print hexcode
        print self.code
        print hexcode
        self.compiled = hexcode

    def write_to_file(self):
        file = open("bootloader.bin","wb")
        for op in self.compiled:
            print op
            file.write(op)
        file.close()

sys.dont_write_bytecode = True

compiler = Compiler("bootloader.p15")
compiler.translate_to_opcodes()
compiler.write_to_file()
