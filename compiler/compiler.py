class Compiler:
    def __init__(self,file):
        self.code = Parser(file).parse()
