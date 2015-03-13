from memory import Memory
from cpu import CPU
from vm_ops import Ops
class VM:
    def __init__(self):
        self.memory = Memory(0xFF)
        self.cpu = CPU()
        self.ops = Ops()
        #print self.memory._all()

    def load_file(self, addr, filename):
        file = open(filename, "rb")
        filecontents = file.read()
        file_bin = list(filecontents) #we now have our bootloader in memory format. Let's iterate through and write to memory
        file.close()
        #print file_bin
        for i in range(addr,addr + len(file_bin)):
            print hex(i)
            self.memory.mem[i] = ord(file_bin[i])
            self.cpu.registers["%MP"] = hex(i)

    def is_an_op(self,op):
        return self.ops.contains(op)

    def bootload(self):
         cur_op_ptr = 0x00  #start at 0
         while cur_op_ptr < 0x20: #length of bootloader
         	op = self.memory.get(cur_op_ptr)	#find current op from memory by ptr
            if self.is_an_op(op):  #if It's an op...
            	print "Found an op! (%s)" % hex(op)#print the op in hex for readability
				

    #Should be the ONLY VM-Level instruction...
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


vm = VM()   #Create new
#Load bootloader from file
vm.load_file(0x00,"software/bootloader.bin")
#print vm.memory._all()
vm.bootload()
