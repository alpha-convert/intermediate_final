class Memory:
    def __init__(self, size):
        self.mem = [[None]]*10

    def get(self, index):
        return self.mem[index]

    def set(self, index, val):
        self.mem[index] = val

    def _all(self)
        return self.mem
