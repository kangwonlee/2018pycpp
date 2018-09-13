   1              		.file	"hello.cpp"
   2              		.text
   3              		.section	.rodata
   6              	_ZStL19piecewise_construct:
   7 0000 00       		.zero	1
   8              		.local	_ZStL8__ioinit
   9              		.comm	_ZStL8__ioinit,1,1
  10              	.LC0:
  11 0001 61726776 		.string	"argv[0] = %s\n"
  11      5B305D20 
  11      3D202573 
  11      0A00
  12              	.LC1:
  13 000f 612C2062 		.string	"a, b = %d, %d\n"
  13      203D2025 
  13      642C2025 
  13      640A00
  14              	.LC2:
  15 001e 622B2B0A 		.string	"b++\n"
  15      00
  16              	.LC3:
  17 0023 622B3D61 		.string	"b+=a\n"
  17      0A00
  18              		.text
  19              		.globl	main
  21              	main:
  22              	.LFB1493:
  23              		.cfi_startproc
  24 0000 55       		pushq	%rbp
  25              		.cfi_def_cfa_offset 16
  26              		.cfi_offset 6, -16
  27 0001 4889E5   		movq	%rsp, %rbp
  28              		.cfi_def_cfa_register 6
  29 0004 4883EC20 		subq	$32, %rsp
  30 0008 897DEC   		movl	%edi, -20(%rbp)
  31 000b 488975E0 		movq	%rsi, -32(%rbp)
  32 000f 488B45E0 		movq	-32(%rbp), %rax
  33 0013 488B00   		movq	(%rax), %rax
  34 0016 0FB600   		movzbl	(%rax), %eax
  35 0019 0FBEC0   		movsbl	%al, %eax
  36 001c 8945F8   		movl	%eax, -8(%rbp)
  37 001f 488B45E0 		movq	-32(%rbp), %rax
  38 0023 488B00   		movq	(%rax), %rax
  39 0026 4883C001 		addq	$1, %rax
  40 002a 0FB600   		movzbl	(%rax), %eax
  41 002d 0FBEC0   		movsbl	%al, %eax
  42 0030 8945FC   		movl	%eax, -4(%rbp)
  43 0033 488B45E0 		movq	-32(%rbp), %rax
  44 0037 488B00   		movq	(%rax), %rax
  45 003a 4889C6   		movq	%rax, %rsi
  46 003d 488D3D00 		leaq	.LC0(%rip), %rdi
  46      000000
  47 0044 B8000000 		movl	$0, %eax
  47      00
  48 0049 E8000000 		call	printf@PLT
  48      00
  49 004e 8B55FC   		movl	-4(%rbp), %edx
  50 0051 8B45F8   		movl	-8(%rbp), %eax
  51 0054 89C6     		movl	%eax, %esi
  52 0056 488D3D00 		leaq	.LC1(%rip), %rdi
  52      000000
  53 005d B8000000 		movl	$0, %eax
  53      00
  54 0062 E8000000 		call	printf@PLT
  54      00
  55 0067 8345FC01 		addl	$1, -4(%rbp)
  56 006b 488D3D00 		leaq	.LC2(%rip), %rdi
  56      000000
  57 0072 E8000000 		call	puts@PLT
  57      00
  58 0077 8B55FC   		movl	-4(%rbp), %edx
  59 007a 8B45F8   		movl	-8(%rbp), %eax
  60 007d 89C6     		movl	%eax, %esi
  61 007f 488D3D00 		leaq	.LC1(%rip), %rdi
  61      000000
  62 0086 B8000000 		movl	$0, %eax
  62      00
  63 008b E8000000 		call	printf@PLT
  63      00
  64 0090 8B45F8   		movl	-8(%rbp), %eax
  65 0093 0145FC   		addl	%eax, -4(%rbp)
  66 0096 488D3D00 		leaq	.LC3(%rip), %rdi
  66      000000
  67 009d E8000000 		call	puts@PLT
  67      00
  68 00a2 8B55FC   		movl	-4(%rbp), %edx
  69 00a5 8B45F8   		movl	-8(%rbp), %eax
  70 00a8 89C6     		movl	%eax, %esi
  71 00aa 488D3D00 		leaq	.LC1(%rip), %rdi
  71      000000
  72 00b1 B8000000 		movl	$0, %eax
  72      00
  73 00b6 E8000000 		call	printf@PLT
  73      00
  74 00bb 8B45F8   		movl	-8(%rbp), %eax
  75 00be 0145FC   		addl	%eax, -4(%rbp)
  76 00c1 488D3D00 		leaq	.LC3(%rip), %rdi
  76      000000
  77 00c8 E8000000 		call	puts@PLT
  77      00
  78 00cd 8B55FC   		movl	-4(%rbp), %edx
  79 00d0 8B45F8   		movl	-8(%rbp), %eax
  80 00d3 89C6     		movl	%eax, %esi
  81 00d5 488D3D00 		leaq	.LC1(%rip), %rdi
  81      000000
  82 00dc B8000000 		movl	$0, %eax
  82      00
  83 00e1 E8000000 		call	printf@PLT
  83      00
  84 00e6 B8000000 		movl	$0, %eax
  84      00
  85 00eb C9       		leave
  86              		.cfi_def_cfa 7, 8
  87 00ec C3       		ret
  88              		.cfi_endproc
  89              	.LFE1493:
  92              	_Z41__static_initialization_and_destruction_0ii:
  93              	.LFB1974:
  94              		.cfi_startproc
  95 00ed 55       		pushq	%rbp
  96              		.cfi_def_cfa_offset 16
  97              		.cfi_offset 6, -16
  98 00ee 4889E5   		movq	%rsp, %rbp
  99              		.cfi_def_cfa_register 6
 100 00f1 4883EC10 		subq	$16, %rsp
 101 00f5 897DFC   		movl	%edi, -4(%rbp)
 102 00f8 8975F8   		movl	%esi, -8(%rbp)
 103 00fb 837DFC01 		cmpl	$1, -4(%rbp)
 104 00ff 7532     		jne	.L5
 105 0101 817DF8FF 		cmpl	$65535, -8(%rbp)
 105      FF0000
 106 0108 7529     		jne	.L5
 107 010a 488D3D00 		leaq	_ZStL8__ioinit(%rip), %rdi
 107      000000
 108 0111 E8000000 		call	_ZNSt8ios_base4InitC1Ev@PLT
 108      00
 109 0116 488D1500 		leaq	__dso_handle(%rip), %rdx
 109      000000
 110 011d 488D3500 		leaq	_ZStL8__ioinit(%rip), %rsi
 110      000000
 111 0124 488B0500 		movq	_ZNSt8ios_base4InitD1Ev@GOTPCREL(%rip), %rax
 111      000000
 112 012b 4889C7   		movq	%rax, %rdi
 113 012e E8000000 		call	__cxa_atexit@PLT
 113      00
 114              	.L5:
 115 0133 90       		nop
 116 0134 C9       		leave
 117              		.cfi_def_cfa 7, 8
 118 0135 C3       		ret
 119              		.cfi_endproc
 120              	.LFE1974:
 123              	_GLOBAL__sub_I_main:
 124              	.LFB1975:
 125              		.cfi_startproc
 126 0136 55       		pushq	%rbp
 127              		.cfi_def_cfa_offset 16
 128              		.cfi_offset 6, -16
 129 0137 4889E5   		movq	%rsp, %rbp
 130              		.cfi_def_cfa_register 6
 131 013a BEFFFF00 		movl	$65535, %esi
 131      00
 132 013f BF010000 		movl	$1, %edi
 132      00
 133 0144 E8A4FFFF 		call	_Z41__static_initialization_and_destruction_0ii
 133      FF
 134 0149 5D       		popq	%rbp
 135              		.cfi_def_cfa 7, 8
 136 014a C3       		ret
 137              		.cfi_endproc
 138              	.LFE1975:
 140              		.section	.init_array,"aw"
 141              		.align 8
 142 0000 00000000 		.quad	_GLOBAL__sub_I_main
 142      00000000 
 143              		.hidden	__dso_handle
 144              		.ident	"GCC: (Ubuntu 7.3.0-16ubuntu3) 7.3.0"
 145              		.section	.note.GNU-stack,"",@progbits
