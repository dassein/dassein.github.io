	.file	"note02_21_assembly.c"
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
    mov ebp, esp; for correct debugging
    mov rbp, rsp; for correct debugging
    mov ebp, esp; for correct debugging
    movq %rsp, %rbp #for correct debugging
    movl %esp, %ebp #for correct debugging
.LFB2:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movl	%edi, -20(%rbp)
	movq	%rsi, -32(%rbp)
	movl	$8, %edi
	call	malloc@PLT
	movq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	addq	$4, %rax
	movl	$100, (%rax)
	movq	-8(%rbp), %rax
	movl	$0, (%rax)
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$0, %eax
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
