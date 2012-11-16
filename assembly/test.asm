extern printf
global main
SECTION .data
print_format_str: db "%d", 10, 0
SECTION .text
main:
mov rbx, 5
imul rbx
mov rcx, rax
mov rdi, print_format_str
mov rsi, rcx
mov rax, 0
call printf
mov rax, 0
ret


