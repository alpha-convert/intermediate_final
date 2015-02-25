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
        bytes_of_def = 0
        for cur_token in range(0,len(self.tokens)): #go over entire set of tokens
            if re.search(label_regex, self.tokens[cur_token]):  #if it's a label def
                label_entry = []
                label_length = int(self.tokens[cur_token+1])
                for label_op in range(cur_token + 1, cur_token + label_length + 2):
                    bytes_of_def += 1   #THere's another byte in there!
                    label_entry.append(self.tokens[label_op])
                #print "\n"
                #print label_entry
                labels.update({self.tokens[cur_token].lstrip("_"):label_entry})
        self.labels = labels
        self.bytes_of_def = bytes_of_def
        #NOTE: At this time, we have all of our methods captured in a dictionary.
        #      we know how many ops of the program are label defs. We will then delete them.

    def remove_label_defs(self):
        del self.tokens[0:self.bytes_of_def + len(self.labels)]

    def find_jumps(self):
        new_code = self.tokens
        for i, token in enumerate(self.tokens):
            if token == "JMP":
                needed_label = self.tokens[i+1].lstrip(".")
                del new_code[i]     #remove the token
                new_code[i:i + 1] = self.labels[needed_label]   #smush in the jump code.

        #print self.tokens
        new_code
        self.tokens = new_code #our arr of tokens is now the full code.










p = Parser("testing/test.p15")
p.tokenize()
p.get_labels()
p.remove_label_defs()
p.find_jumps()
#p.update_with_labels()
