	.file	"scope.c"
	.intel_syntax noprefix
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	mov	DWORD PTR [rbp-12], 0
	mov	DWORD PTR [rbp-8], 0
	jmp	.L2
.L3:
	mov	eax, DWORD PTR [rbp-12]
	xor	eax, 2
	mov	DWORD PTR [rbp-4], eax
	mov	eax, DWORD PTR [rbp-4]
	add	DWORD PTR [rbp-8], eax
	add	DWORD PTR [rbp-12], 1
.L2:
	cmp	DWORD PTR [rbp-12], 9
	jle	.L3
	mov	eax, DWORD PTR [rbp-8]
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.6.1-9ubuntu3) 4.6.1"
	.section	.note.GNU-stack,"",@progbits
