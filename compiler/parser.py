import re
#MEMBERS:
#filename: the name of the input file
#filecontents: the contents of the file
#tokens: the tokenized code
class Parser:
    def __init__(self, filename):
        self.filename = filename
        with open('testing/test.p15', 'r') as file: #read the whole file
            self.file_contents = file.read()

    def tokenize(self):
        self.tokens = self.file_contents.split()    #split into tokens
        print self.tokens

    def get_labels(self):
        labels = []
        i = 0
        label_regex = re.compile('_\D+')
        while i < len(self.tokens) - 1:
            if re.search(label_regex, self.tokens[i]) and re.search("\d",self.tokens[i+1]): #regex for labels
                print "Found a label!"
            i += 1




p = Parser("testing/test.p15")
p.tokenize()
p.get_labels()
