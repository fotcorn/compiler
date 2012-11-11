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
	mov	DWORD PTR [rbp-28], 66
	mov	DWORD PTR [rbp-24], 55
	mov	DWORD PTR [rbp-20], 44
	mov	DWORD PTR [rbp-16], 33
	mov	DWORD PTR [rbp-12], 22
	mov	DWORD PTR [rbp-8], 11
	mov	eax, DWORD PTR [rbp-12]
	mov	edx, DWORD PTR [rbp-8]
	add	eax, edx
	mov	edx, eax
	add	edx, DWORD PTR [rbp-16]
	mov	eax, DWORD PTR [rbp-24]
	mov	ecx, DWORD PTR [rbp-20]
	add	eax, ecx
	add	eax, DWORD PTR [rbp-28]
	imul	edx, eax
	mov	eax, DWORD PTR [rbp-12]
	mov	ecx, DWORD PTR [rbp-8]
	add	eax, ecx
	add	eax, DWORD PTR [rbp-16]
	imul	eax, edx
	mov	DWORD PTR [rbp-4], eax
	mov	eax, DWORD PTR [rbp-4]
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3"
	.section	.note.GNU-stack,"",@progbits
