from memory import Memory
from cpu import CPU
class VM:
    def __init__(self):
        self.memory = Memory(0xFF)
        self.cpu = CPU()
        #print self.memory._all()

    def load_file_to_mem(self, addr, filename):
        file = open(filename, "r")
        filecontents = file.read()
        bootloader = list(filecontents) #we now have our bootloader in memory format. Let's iterate through and write to memory
        file.close()

        for i in range(addr,addr + len(bootloader)):
            self.memory.mem[i] = bootloader[i]


vm = VM()
vm.load_file_to_mem(0x00,"software/bootloader.bin")
print vm.memory._all()
#while True:
#    vm.cpu.cycle()
