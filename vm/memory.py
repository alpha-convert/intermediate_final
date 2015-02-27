class Memory:
    def __init__(self, size):
        self.size = size
        self.mem = [0x00]*self.size

    def get(self, index):
        if not (index > self.size or index < self.size):
            return self.mem[index]
        else:
            print "Segmentation fault: %i" % hex(index)

    def set(self, index, val):
        if not (index > self.size or index < self.size):
            self.mem[index] = val
        else:
            print "Segmentation fault: %i" % hex(index)

    def _all(self):
        return list(self.mem)
