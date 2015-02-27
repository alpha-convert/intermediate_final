from memory import Memory
from cpu import CPU
class VM:
    def __init__(self):
        self.memory = Memory(0xFF)
        self.cpu = CPU()
        #print self.memory._all()

    def load_file(self, addr, filename):
        file = open(filename, "rb")
        filecontents = file.read()
        file_bin = list(filecontents) #we now have our bootloader in memory format. Let's iterate through and write to memory
        file.close()
        #print file_bin
        for i in range(addr,addr + len(file_bin)):
            self.memory.mem[i] = ord(file_bin[i])
            self.cpu.registers["%MP"] = hex(i)

    def run(self):


    def PSH(val):
        if isinstance(val,str):
            self.memory.set(self.cpu.registers["%SP"],self.cpu.registers[val])  #If is string, push into value of sp, value in reg


    #DEBUG CODE
    def print_memory_segment(self,start_addr,end_addr):
        for i in range(start_addr,end_addr):
            print self.memory.get(i)

vm = VM()   #Create new
#Bootload. This will do all the necciary operations
vm.load_file(0x00,"software/bootloader.bin")
print vm.memory._all()
#while True:
#    vm.cpu.cycle()
