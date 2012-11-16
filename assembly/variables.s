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
	mov	DWORD PTR [rbp-24], 55
	mov	DWORD PTR [rbp-20], 44
	mov	DWORD PTR [rbp-16], 33
	mov	DWORD PTR [rbp-12], 22
	mov	DWORD PTR [rbp-8], 11
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-8]
	mov	ecx, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-12]
	mov	esi, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-16]
	mov	edi, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-20]
	mov	r8d, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-24]
	imul	eax, r8d
	imul	eax, edi
	imul	eax, esi
	imul	eax, ecx
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
