section .data
    format db "%d", 0

section .bss
    num resb 10 ; Reserve space for a 10-digit number

section .text
    global _start

_start:
    call get_input
    push rdi          ; Push the integer onto the stack
    call get_input
    push rdi          ; Push the integer onto the stack


    ; Exit the program
    mov rax, 60       ; System call number: sys_exit
    xor rdi, rdi      ; Exit code 0
    syscall

get_input:
    ; Read input
    mov rdi, 0        ; File descriptor: STDIN
    mov rax, 0        ; System call number: sys_read
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
