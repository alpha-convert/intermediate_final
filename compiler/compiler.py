#!/usr/bin/env python
from parser import Parser
class Compiler:
    def __init__(self,file):
        parser = Parser(file)
        parser.tokenize()
        parser.get_labels()
        parser.remove_label_defs()
        parser.find_jumps()
        #At this point, the code has been parsed, jumps have been calculated and the code inserted.
        self.code = parser.tokens
        #print self.code

    def translate_to_opcodes(self):
        

compiler = Compiler("testing/test.p15")
