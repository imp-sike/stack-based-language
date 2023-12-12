section .data
    format db "%d", 0
str1 db 'Prints first 10 natural numbers',0xA
str1_len equ $ - str1
str13 db 'End of Program',0xA
str13_len equ $ - str13
str15 db '----------------------------',0xA
str15_len equ $ - str15
str17 db 'Prints first 10 even numbers',0xA
str17_len equ $ - str17
str30 db 'End of Program',0xA
str30_len equ $ - str30
;---- ELEMENT DATA ----
section .bss
 num resb 10     ; Buffer to store user input
section .text
dump:
    mov     r9, -3689348814741910323
    sub     rsp, 40
    mov     BYTE [rsp+31], 10
    lea     rcx, [rsp+30]
.L2:
    mov     rax, rdi
    lea     r8, [rsp+32]
    mul     r9
    mov     rax, rdi
    sub     r8, rcx
    shr     rdx, 3
    lea     rsi, [rdx+rdx*4]
    add     rsi, rsi
    sub     rax, rsi
    add     eax, 48
    mov     BYTE [rcx], al
    mov     rax, rdi
    mov     rdi, rdx
    mov     rdx, rcx
    sub     rcx, 1
    cmp     rax, 9
    ja      .L2
    lea     rax, [rsp+32]
    mov     edi, 1
    sub     rdx, rax
    xor     eax, eax
    lea     rsi, [rsp+32+rdx]
    mov     rdx, r8
    mov     rax, 1
    syscall
    add     rsp, 40
    ret
; Get input and push to stack
get_input_and_push:
    ; Input: RDI - Pointer to the prompt string
    ; Output: The entered number pushed onto the stack

    ; Read input
    mov rax, 0        ; System call number: sys_read
    mov rdi, 0        ; File descriptor: STDIN
    mov rsi, num      ; Pointer to the buffer
    mov rdx, 10       ; Maximum number of bytes to read
    syscall

    ; Convert the input to an integer
    mov rdi, num      ; Pointer to the buffer
    mov rax, 0        ; Clear RAX for conversion
    call str2int

    ; Push the number onto the stack
    mov rdi, rax      ; Move the integer to RDI
    mov rax, 0        ; Clear RAX for syscall

    ret
; Function to convert string to integer
str2int:
    xor rax, rax      ; Clear RAX for result
    xor rcx, rcx      ; Clear RCX for loop counter

.next_digit:
    movzx rdx, byte [rdi + rcx] ; Load the next character into RDX
    cmp rdx, 0        ; Check if it is the null terminator
    je .found_null     ; If yes, terminate the loop

    sub rdx, '0'      ; Convert ASCII character to integer
    imul rax, 10      ; Multiply the current result by 10
    add rax, rdx      ; Add the new digit
    inc rcx           ; Move to the next character
    jmp .next_digit   ; Repeat the process

.found_null:
    ret
     global _start
_start:
    ; nop

    ; outs the string
    mov rax, 1
    mov rdi, 1
    mov rsi, str1
    mov rdx, str1_len
    syscall

    ; Push element to stack
     mov rax,1
     push rax

    ; label
    labbelnatural:
    ; peek and print
    pop rdi
    push rdi
    call dump
    ; increment stack value
    pop rax
    inc rax
    push rax
    ; pop, push, push = dup
     pop rax
     push rax
     push rax
    ; Push element to stack
     mov rax,10
     push rax

    ; Greater Than or Equal
    pop rax
    pop rbx
    cmp rax, rbx
    ; setge is for greater than or equal 
    setge al            ; Set AL to 1 if greater than or equal, 0 otherwise 
    ; Push the result onto the stack
    push rax

   ; if statement starts 
   pop rax
   cmp rax, 1
   jne addr_11

    ; goto
    jmp labbelnatural
   ; End of if
   addr_11:
 
    ; nop

    ; outs the string
    mov rax, 1
    mov rdi, 1
    mov rsi, str13
    mov rdx, str13_len
    syscall

    ; nop

    ; outs the string
    mov rax, 1
    mov rdi, 1
    mov rsi, str15
    mov rdx, str15_len
    syscall

    ; nop

    ; outs the string
    mov rax, 1
    mov rdi, 1
    mov rsi, str17
    mov rdx, str17_len
    syscall

    ; Push element to stack
     mov rax,0
     push rax

    ; label
    labbeleven:
    ; peek and print
    pop rdi
    push rdi
    call dump
    ; Push element to stack
     mov rax,2
     push rax

    ; Pop 2 elements from stack, add them and push back to stack
    pop rax
    pop rbx
    add rax, rbx
    push rax

    ; pop, push, push = dup
     pop rax
     push rax
     push rax
    ; Push element to stack
     mov rax,10
     push rax

    ; Greater Than or Equal
    pop rax
    pop rbx
    cmp rax, rbx
    ; setge is for greater than or equal 
    setge al            ; Set AL to 1 if greater than or equal, 0 otherwise 
    ; Push the result onto the stack
    push rax

   ; if statement starts 
   pop rax
   cmp rax, 1
   jne addr_28

    ; goto
    jmp labbeleven
   ; End of if
   addr_28:
 
    ; nop

    ; outs the string
    mov rax, 1
    mov rdi, 1
    mov rsi, str30
    mov rdx, str30_len
    syscall

    ; Exit the program
     mov eax, 1        
    ; System call number for exit
     xor ebx, ebx       
    ; Exit code 0
    int 0x80
    ; Make system call
