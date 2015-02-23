
#p15 Architecture Notes
##CPU
###Registers
Name|Description|HexName|
---|---|---
SP|Stack pointer|`0xF1`
MP|Memory (current op/value) pointer|`0xF2`
CL|Clock|`0xF3`
AR|Arethmatical uses|`0xF4`
GP1-GP8|General purpose registers|`0xF5`-`0xFC`
SY1|1st argument in syscalls|`0xFD`
SY2|2nd argument in syscalls|`0xFE`
SY3|3rd argument in syscalls|`0xFF`
###Notes
- *Every clock cycle:*
    - MP increments

##Memory
**32 bit address space** (`0x0000` - `0xFFFF`)

**Stack:** `null` - `0x0BA2` (1/16 of total memory space)

**Video memory:** `0x0BA3` - `0x3FFF`

**General purpouse** `0x4000`-`0xFFFF`

#p15 Assembly Language Docs
###Instruction Set
Instruction|OpCode|Args|Description
---|:---:|---|---
NOP|`0x00`|null|Does nothing. Absolutely useless, but standard in most assembly languages.
ADD|`0x01`|a,b|Add a and b, push answer to stack
SUB|`0x02`|a,b|Subtract a from b, push answer to stack
MUL|`0x02`|a,b|Multiply a and b, push answer to stack
DIV|`0x03`|a,b|Divide a by b, push answer to stack
AND|`0x04`|a,b|Binary AND a and b. Push answer to stack
OR|`0x05`|a,b|Binary OR a and b. Push answer to stack
NOT|`0x06`|a|Flip Bits
XOR|`0x07`|a,b|Binary XOR a and b. Push answer to stack
LSH|`0x08`|a,b|Left shift a by b
RSH|`0x09`|a,b|Right shift a by b
MOV|`0x0A`|r,v|Moves value V into register R
PSH|`0x0B`|v|Pushes value V onto the stack
POP|`0x0C`|null|Pop off the top of the stack
SYS|`0x0D`|null|Syscall, based on registers
HLT|`0x0E`|null|Halts execution

###Syscalls:
```mem_write(unsigned int addr, int value)```

```mem_read(unsigned int addr,unsigned int reg)``` - Reads memory from address `addr` into register `reg`.
###Syntax
**No-arg operations:** `OP`

**N-arg operations:** `OP arg1,arg2...,argN`
