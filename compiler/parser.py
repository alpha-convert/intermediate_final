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
        #print self.tokens

    def get_labels(self):
        labels = {}
        i = 0
        label_regex = re.compile('_\D+')
        while self.tokens[i] != 'SECTION.START':
            if re.search(label_regex, self.tokens[i]) and re.search("\d",self.tokens[i+1]): #regex for labels
                method = []
                for j in range(i + 1, (i + 2) + int(self.tokens[i+1])):
                    method.append(self.tokens[j])
                labels.update({self.tokens[i]:method})
            #del self.tokens[i]
            i += 1 #Be sure to jump forward the right length. Soon we'll jump passed the body of the label
        #print self.tokens
        print labels




p = Parser("testing/test.p15")
p.tokenize()
p.get_labels()
