	.file	"test.c"
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
	push	r15
	push	r14
	push	r13
	push	r12
	push	rbx
	sub	rsp, 8
	mov	DWORD PTR [rbp-144], 25
	mov	DWORD PTR [rbp-140], 24
	mov	DWORD PTR [rbp-136], 23
	mov	DWORD PTR [rbp-132], 22
	mov	DWORD PTR [rbp-128], 21
	mov	DWORD PTR [rbp-124], 20
	mov	DWORD PTR [rbp-120], 19
	mov	DWORD PTR [rbp-116], 18
	mov	DWORD PTR [rbp-112], 17
	mov	DWORD PTR [rbp-108], 16
	mov	DWORD PTR [rbp-104], 15
	mov	DWORD PTR [rbp-100], 14
	mov	DWORD PTR [rbp-96], 13
	mov	DWORD PTR [rbp-92], 12
	mov	DWORD PTR [rbp-88], 11
	mov	DWORD PTR [rbp-84], 10
	mov	DWORD PTR [rbp-80], 9
	mov	DWORD PTR [rbp-76], 8
	mov	DWORD PTR [rbp-72], 7
	mov	DWORD PTR [rbp-68], 6
	mov	DWORD PTR [rbp-64], 5
	mov	DWORD PTR [rbp-60], 4
	mov	DWORD PTR [rbp-56], 3
	mov	DWORD PTR [rbp-52], 2
	mov	DWORD PTR [rbp-48], 1
	mov	DWORD PTR [rbp-44], 0
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-44]
	mov	edi, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-48]
	mov	r8d, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-52]
	mov	r9d, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-56]
	mov	r10d, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-60]
	mov	r11d, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-64]
	mov	ebx, eax
	.cfi_offset 3, -56
	.cfi_offset 12, -48
	.cfi_offset 13, -40
	.cfi_offset 14, -32
	.cfi_offset 15, -24
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-68]
	mov	r12d, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-72]
	mov	r13d, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-76]
	mov	r14d, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-80]
	mov	r15d, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-84]
	mov	DWORD PTR [rbp-156], eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-88]
	mov	DWORD PTR [rbp-160], eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-92]
	mov	DWORD PTR [rbp-164], eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-96]
	mov	esi, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-100]
	mov	ecx, eax
	mov	eax, 29
	mov	edx, eax
	sar	edx, 31
	idiv	DWORD PTR [rbp-104]
	imul	eax, ecx
	imul	eax, esi
	imul	eax, DWORD PTR [rbp-164]
	imul	eax, DWORD PTR [rbp-160]
	imul	eax, DWORD PTR [rbp-156]
	imul	eax, r15d
	imul	eax, r14d
	imul	eax, r13d
	imul	eax, r12d
	imul	eax, ebx
	imul	eax, r11d
	imul	eax, r10d
	imul	eax, r9d
	imul	eax, r8d
	imul	eax, edi
	add	rsp, 8
	pop	rbx
	pop	r12
	pop	r13
	pop	r14
	pop	r15
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.6.1-9ubuntu3) 4.6.1"
	.section	.note.GNU-stack,"",@progbits
