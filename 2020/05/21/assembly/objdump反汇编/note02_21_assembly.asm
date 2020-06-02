	.file	"note02_21_assembly.c"
	.intel_syntax noprefix
	.globl	global
	.data
	.align 4
	.type	global, @object
	.size	global, 4
global:
	.long	100
	.section	.rodata
.LC0:
	.string	"Good"
	.text
	.globl	main
	.type	main, @function
main:
.LFB2:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	sub	rsp, 32
	mov	DWORD PTR -20[rbp], edi
	mov	QWORD PTR -32[rbp], rsi
	mov	edi, 8
	call	malloc@PLT
	mov	QWORD PTR -8[rbp], rax
	mov	rax, QWORD PTR -8[rbp]
	add	rax, 4
	mov	DWORD PTR [rax], 100
	mov	rax, QWORD PTR -8[rbp]
	mov	DWORD PTR [rax], 0
	lea	rdi, .LC0[rip]
	mov	eax, 0
	call	printf@PLT
	mov	eax, 0
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	main, .-main
	.data
	.align 4
	.type	BSS.2711, @object
	.size	BSS.2711, 4
BSS.2711:
	.long	100
	.ident	"GCC: (Ubuntu 6.2.0-5ubuntu12) 6.2.0 20161005"
	.section	.note.GNU-stack,"",@progbits
