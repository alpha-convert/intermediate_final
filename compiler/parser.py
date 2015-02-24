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
        label_regex = re.compile('_\D+')    #regex for label
        for cur_token in range(0,len(self.tokens)): #go over entire set of tokens
            if re.search(label_regex, self.tokens[cur_token]):  #if it's a label def
                label_entry = []
                label_length = int(self.tokens[cur_token+1])
                for label_op in range(cur_token + 1, cur_token + label_length + 2):
                    #print self.tokens[label_op]
                    label_entry.append(self.tokens[label_op])
                #print "\n"
                #print label_entry
                labels.update({self.tokens[cur_token]:label_entry})
        self.labels = labels

    #def update_with_labels(self):








p = Parser("testing/test.p15")
p.tokenize()
p.get_labels()
p.update_with_labels()
