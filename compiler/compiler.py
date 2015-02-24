#!/usr/bin/env python
from parser import Parser
class Compiler:
    def __init__(self,file):
        self.code = Parser(file)
        self.code.tokenize()
        self.code.get_labels()
