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
    
    def incmp(self):
        self.cpu.registers["%MP"] += 1
            
    def bootload(self):
        self.cpu.registers["%MP"] = 0x00  #clear mem pointer to 0
        
        while self.cpu.registers["%MP"] < 0x20: #length of bootloader
            op = self.memory.get(self.cpu.registers["%MP"])	#find current op from memory by mem ptr
            
            if self.is_an_op(op):  #if It's an op...
                print "Found an op! (%s)" % hex(op)#print the op in hex for readability
                self.process_op(op)
                
            self.cpu.registers["%MP"] += 1 #Remove this once all are implimented
           	

    def process_op(self,op):
        #return 0
	if op is 0x00: #Nop! Does nothing, so we just inc mp and return
	   self.incmp()
	   return 0
	if op is 0x01: #Add [mp + 1] to [m + 2], push to stack pointer + 1
	    a = self.memory.get(self.cpu.registers["%MP"] + 1) #first number will be directly after the op in memory
	    b = self.memory.get(self.cpu.registers["%MP"] + 2) #second will be just after that
	    self.cpu.registers["%"]
	    
	
	          #self.cpu.registers["%MP"] += 1 #nop does not require any jumps			

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
