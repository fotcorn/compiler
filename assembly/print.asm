extern printf
global main

SECTION .data

print_format_str: db "%d", 10, 0

SECTION .text

main:
    mov rdi, print_format_str
    mov rsi, 1234
    mov rax, 0
    call printf

    mov rax, 0
    ret

