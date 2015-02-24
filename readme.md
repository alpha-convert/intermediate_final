
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

**Bootloader** `0x4000`-`0x4FFF`

**General** `0x5000` - `0xFFFF`

#p15 Assembly Language Docs
###Instruction Set
Instruction|OpCode|Args|Description
---|:---:|---|---
NOP|`0x00`|null|Does nothing. Absolutely useless, but standard in most assembly languages.
ADD|`0x01 A B`|a,b|Add a and b, push answer to stack
SUB|`0x02 A B`|a,b|Subtract a from b, push answer to stack
MUL|`0x03 A B`|a,b|Multiply a and b, push answer to stack
DIV|`0x04 A B`|a,b|Divide a by b, push answer to stack
AND|`0x05 A B`|a,b|Binary AND a and b. Push answer to stack
OR|`0x06 A B`|a,b|Binary OR a and b. Push answer to stack
NOT|`0x07 A B`|a|Flip Bits
XOR|`0x08 A B`|a,b|Binary XOR a and b. Push answer to stack
LSH|`0x09 A B`|a,b|Left shift a by b
RSH|`0x0A A B`|a,b|Right shift a by b
MOV|`0x0B R V`|r,v|Moves value V into register R
PSH|`0x0C V`|v|Pushes value V onto the stack
POP|`0x0D`|null|Pop off the top of the stack
SYS|`0x0E`|null|Syscall, based on registers
JMP|`0x0F 0xOFFSET`|label|Jumps to a Label with offset.
CMP|`0x11 A B`|a,b|Compares a,b, increases the mem-read pointer by 2 instead of 1 iff `a < b`
HLT|`0x12`|null|Halts excecution

###Syscalls:
```mem_write(unsigned int addr, int value)```

```mem_read(unsigned int addr,unsigned int reg)``` - Reads memory from address `addr` into register `reg`.
###Syntax
**No-arg operations:** `OP`

**N-arg operations:** `OP arg1,arg2...,argN`

**Labels** Labels can act as an external function. The first line must be the label name, and the length of the function it contains, in bytes. Ex:
```
_dostuff 7
ADD 1,2
OR %SP,13
POP
```

This works because the total number of bytes in the compiled machine code is 7.
```
0x01 0x01 0x02
0x06 0xF1 0x0D
0x0D
```

**Jumps: `JMP _label`**. `_<labelname>` is a reserved word. eg: `_variable` is illegal

**Register use syntax:** registers will be referenced starting with a "%". Ex: `MOV 123 %GP1`
