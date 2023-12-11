import re
import w
import sys
import subprocess

if len(sys.argv) < 2:
    print("Usage: python x.py <file_path>")
    sys.exit(1)

fpath = sys.argv[1] # compile this file

# c like iota function
iotac = 0 
def iota():
    global iotac
    iotac = iotac + 1
    return iotac

# instruction sets
PUSH = iota()
POP = iota()
ADD = iota()
SUB = iota()
DUMP = iota()
EQUAL = iota()
GREATER_THAN = iota()
SMALLER_THAN = iota()
GREATER_THAN_EQUAL = iota()
SMALLER_THAN_EQUAL = iota()
NOT_EQUAL = iota()
IFF = iota()
ELSEF = iota()
FI = iota()
OUTS = iota()
NOP = iota()
INS = iota()

def push(value):
    return (PUSH, value)

def add():
    return (ADD, 0 )

def sub():
    return (SUB, 0 )

def dump():
    return (DUMP, 0 )

def equals():
    return (EQUAL, 0)

def greater_than():
    return (GREATER_THAN, 0)

def greater_then_equal():
    return  (GREATER_THAN_EQUAL, 0)

def smaller_then():
    return (SMALLER_THAN, 0)

def smaller_then_equal():
    return  (SMALLER_THAN_EQUAL, 0)

def not_equal():
    return (NOT_EQUAL, 0)

def iff():
    return (IFF, 0)

def elsef():
    return (ELSEF, 0)

def fi():
    return (FI, 0)

def outs(value):
    return (OUTS, value)

def nop():
    return (NOP, 0)

def ins():
    return (INS, 0)

programcode = ""

newfile = w.process_file(fpath)
with open(newfile) as source:
    for line in source:
        programcode = programcode + line.split("##")[0]

programcode = programcode.strip()
programcode = re.sub(r'\s+', ' ', programcode)
program = []
stack_cross_reference = []
else_cross_reference = []
outs_strs = []

finalcode = ""

def append(data2):
    global finalcode
    finalcode = finalcode + data2 + "\n"

def create_string(varname,value):
    global finalcode
    finalcode = finalcode.replace(
            ";---- ELEMENT DATA ----",
            varname + " db '" + value.replace("&nbsp;", " ") +"',0xA\n" + varname + "_len equ $ - " + varname + "\n;---- ELEMENT DATA ----")



for c in range(len(programcode.split(" "))):
    word = programcode.split(" ")[c]
    if word == "+":
        program.append(add())
    elif word == "-":
        program.append(sub())
    elif word == ".":
        program.append(dump())
    elif word == "=":
        program.append(equals())
    elif word == ">":
        program.append(greater_than())
    elif word == "<":
        program.append(smaller_then())
    elif word == ">=":
        program.append(greater_then_equal())
    elif word == "<=":
        program.append(smaller_then_equal())
    elif word == "!=":
        program.append(not_equal())
    elif word == "if":
        program.append(iff())
        stack_cross_reference.append(len(program) - 1)
    elif word == "fi":
        program.append(fi())
        elem = stack_cross_reference.pop()
        if program[elem][1] == 0:
            program[elem] = (IFF, c)
        slem = else_cross_reference.pop()
        program[slem] = (ELSEF, c)
    elif word == "else":
        program.append(elsef())
        elem = stack_cross_reference.pop()
        program[elem] = (IFF, c)
        stack_cross_reference.append(elem)
        else_cross_reference.append(len(program) - 1)
    elif word.startswith("\"") and word.endswith("\""):
        outs_strs.append(word)
        program.append(nop())
    elif word == "outs":
        program.append(outs(outs_strs.pop()))
    elif word == "in":
        program.append(ins())
    else:
        # word is push
        program.append(push(int(word)))

append("section .data")
append('    format db "%d", 0')
append(";---- ELEMENT DATA ----")
append("section .bss")
append(" num resb 10     ; Buffer to store user input")
append("section .text")
append("dump:")
append("    mov     r9, -3689348814741910323")
append("    sub     rsp, 40")
append("    mov     BYTE [rsp+31], 10")
append("    lea     rcx, [rsp+30]")
append(".L2:")
append("    mov     rax, rdi")
append("    lea     r8, [rsp+32]")
append("    mul     r9")
append("    mov     rax, rdi")
append("    sub     r8, rcx")
append("    shr     rdx, 3")
append("    lea     rsi, [rdx+rdx*4]")
append("    add     rsi, rsi")
append("    sub     rax, rsi")
append("    add     eax, 48")
append("    mov     BYTE [rcx], al")
append("    mov     rax, rdi")
append("    mov     rdi, rdx")
append("    mov     rdx, rcx")
append("    sub     rcx, 1")
append("    cmp     rax, 9")
append("    ja      .L2")
append("    lea     rax, [rsp+32]")
append("    mov     edi, 1")
append("    sub     rdx, rax")
append("    xor     eax, eax")
append("    lea     rsi, [rsp+32+rdx]")
append("    mov     rdx, r8")
append("    mov     rax, 1")
append("    syscall")
append("    add     rsp, 40")
append("    ret")
append("; Get input and push to stack")
append("get_input_and_push:")
append("    ; Input: RDI - Pointer to the prompt string")
append("    ; Output: The entered number pushed onto the stack")
append("")
append("    ; Read input")
append("    mov rax, 0        ; System call number: sys_read")
append("    mov rdi, 0        ; File descriptor: STDIN")
append("    mov rsi, num      ; Pointer to the buffer")
append("    mov rdx, 10       ; Maximum number of bytes to read")
append("    syscall")
append("")
append("    ; Convert the input to an integer")
append("    mov rdi, num      ; Pointer to the buffer")
append("    mov rax, 0        ; Clear RAX for conversion")
append("    call str2int")
append("")
append("    ; Push the number onto the stack")
append("    mov rdi, rax      ; Move the integer to RDI")
append("    mov rax, 0        ; Clear RAX for syscall")
append("")
append("    ret")
append("; Function to convert string to integer")
append("str2int:")
append("    xor rax, rax      ; Clear RAX for result")
append("    xor rcx, rcx      ; Clear RCX for loop counter")
append("")
append(".next_digit:")
append("    movzx rdx, byte [rdi + rcx] ; Load the next character into RDX")
append("    cmp rdx, 0        ; Check if it is the null terminator")
append("    je .found_null     ; If yes, terminate the loop")
append("")
append("    sub rdx, '0'      ; Convert ASCII character to integer")
append("    imul rax, 10      ; Multiply the current result by 10")
append("    add rax, rdx      ; Add the new digit")
append("    inc rcx           ; Move to the next character")
append("    jmp .next_digit   ; Repeat the process")
append("")
append(".found_null:")
append("    ret")

append("     global _start")
append("_start:")


for ip in range(len(program)):
    code = program[ip]
    instrn, value = code
    if instrn == PUSH:
        append("    ; Push element to stack")
        append("     mov rax," + str(value))
        append("     push rax")
        append("")
    elif instrn == ADD:
        append("    ; Pop 2 elements from stack, add them and push back to stack")
        append("    pop rax")
        append("    pop rbx")
        append("    add rax, rbx")
        append("    push rax")
        append("")
    elif instrn == DUMP:
        append("    ; DUMP")
        append("    pop rdi")
        append("    call dump")
        append("")
    elif instrn == EQUAL:
        append("    ; Equals")
        append("    pop rax")
        append("    pop rbx")
        append("    cmp rax, rbx")
        append("    ; sete is for equality ")
        append("    sete al            ; Set AL to 1 if equal, 0 otherwise ")
        append("    ; Push the result onto the stack")
        append("    push rax")
        append("")
    elif instrn == NOT_EQUAL:
        append("    ; Not Equals")
        append("    pop rax")
        append("    pop rbx")
        append("    cmp rax, rbx")
        append("    ; setne is for not equal ")
        append("    setne al            ; Set AL to 1 if not equal, 0 otherwise ")
        append("    ; Push the result onto the stack")
        append("    push rax")
        append("")
    elif instrn == GREATER_THAN:
        append("    ; Greater Than")
        append("    pop rax")
        append("    pop rbx")
        append("    cmp rax, rbx")
        append("    ; setg is for greater than ")
        append("    setg al            ; Set AL to 1 if greater than, 0 otherwise ")
        append("    ; Push the result onto the stack")
        append("    push rax")
        append("")
    elif instrn == SMALLER_THAN:
        append("    ; Smaller Than")
        append("    pop rax")
        append("    pop rbx")
        append("    cmp rax, rbx")
        append("    ; setl is for smaller than ")
        append("    setl al            ; Set AL to 1 if smaller than, 0 otherwise ")
        append("    ; Push the result onto the stack")
        append("    push rax")
        append("")

    elif instrn == GREATER_THAN_EQUAL:
        append("    ; Greater Than or Equal")
        append("    pop rax")
        append("    pop rbx")
        append("    cmp rax, rbx")
        append("    ; setge is for greater than or equal ")
        append("    setge al            ; Set AL to 1 if greater than or equal, 0 otherwise ")
        append("    ; Push the result onto the stack")
        append("    push rax")
        append("")

    elif instrn == SMALLER_THAN_EQUAL:
        append("    ; Smaller Than or Equal")
        append("    pop rax")
        append("    pop rbx")
        append("    cmp rax, rbx")
        append("    ; setle is for smaller than or equal ")
        append("    setle al            ; Set AL to 1 if smaller than or equal, 0 otherwise ")
        append("    ; Push the result onto the stack")
        append("    push rax")
        append("")

    elif instrn == IFF:
        append("   ; if statement starts ")
        append("   pop rax")
        append("   cmp rax, 1")
        append("   jne addr_"+str(value))
        append("")
    elif instrn == ELSEF:
        append("   jmp addr_" + str(value))
        append("    ; else block here")
        append("    addr_"+str(ip)+":")
        append(" ")
    elif instrn == FI:
        append("   ; End of if")
        append("   addr_" + str(ip) + ":")
        append(" ")
    elif instrn == OUTS:
        append("    ; outs the string")
        variab = "str" + str(ip)
        create_string(variab, value.replace("\"", ""))
        append("    mov rax, 1")
        append("    mov rdi, 1")
        append("    mov rsi, "+variab)
        append("    mov rdx, "+variab + "_len")
        append("    syscall")
        # print(";-----Here-----")
        append("")
    elif instrn == NOP:
        append("    ; nop")
        append("")
    elif instrn == INS:
        append("    ; input the data and push on stack")
        append("    call get_input_and_push")
        append("    push rdi          ; Push the integer onto the stack")



append("    ; Exit the program")
append("     mov eax, 1        ")
append("    ; System call number for exit")
append("     xor ebx, ebx       ")
append("    ; Exit code 0")
append("    int 0x80")
append("    ; Make system call")

outputFile = fpath.replace(".expr", ".asm")
basename = fpath.replace(".expr", "")
with open(outputFile, "w") as op:
    op.writelines(finalcode)
subprocess.call(["nasm", "-felf64",  outputFile])
subprocess.call(["ld", "-o", basename, basename + ".o"])
try:
    if(sys.argv[2] == "-d"):
     # debug
     pass
except:
    subprocess.call(["rm", basename + ".asm"])
    pass
subprocess.call(["rm", basename + ".expr.intermediate"])
subprocess.call(["rm", basename + ".o"])