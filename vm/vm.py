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

    #def run(self):


    def PSH(self,val):
        if isinstance(val,str):
            self.memory.set(self.cpu.registers["%SP"],self.cpu.registers[val])  #If is string, push into value of sp, value in reg
        else:
            self.memory.set(self.cpu.registers["%SP"],val)
        self.cpu.registers["%SP"] += 1

    #DEBUG CODE
    def print_memory_segment(self,start_addr,end_addr):
        for i in range(start_addr,end_addr):
            print self.memory.get(i)

    def stacktrace(self):
        self.print_memory_segment(0x21,0x61)

    def print_register(self,reg):
        print "Value of {0} is: {1} ({2}).".format(reg, self.cpu.registers[reg], hex(self.cpu.registers[reg]))

vm = VM()   #Create new
#Bootload. This will do all the necciary operations
vm.load_file(0x00,"software/bootloader.bin")
vm.PSH(20)
vm.cpu.MOV("%SP",33)
vm.PSH(0xFF)
print vm.memory._all()
vm.print_register("%SP")

#while True:
#    vm.cpu.cycle()
