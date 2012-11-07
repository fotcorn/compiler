	.file	"variables.c"
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
	mov	DWORD PTR [rbp-20], 11
	mov	DWORD PTR [rbp-16], 22
	mov	DWORD PTR [rbp-12], 33
	mov	DWORD PTR [rbp-8], 44
	mov	eax, DWORD PTR [rbp-8]
	add	eax, 31
	mov	edx, eax
	sal	edx, 5
	mov	eax, DWORD PTR [rbp-20]
	add	eax, 12
	imul	eax, edx
	mov	edx, eax
	add	edx, DWORD PTR [rbp-12]
	mov	eax, edx
	sal	eax, 5
	add	edx, eax
	mov	eax, DWORD PTR [rbp-16]
	add	eax, 15
	imul	eax, edx
	add	eax, DWORD PTR [rbp-16]
	add	eax, eax
	mov	edx, eax
	sal	edx, 4
	add	edx, eax
	mov	eax, DWORD PTR [rbp-12]
	add	eax, 23
	imul	eax, edx
	add	eax, DWORD PTR [rbp-20]
	mov	DWORD PTR [rbp-4], eax
	mov	eax, DWORD PTR [rbp-4]
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.6.1-9ubuntu3) 4.6.1"
	.section	.note.GNU-stack,"",@progbits
