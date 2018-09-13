   1              		.file	"hello.cpp"
   2              		.text
   3              		.section	.rodata
   6              	_ZStL19piecewise_construct:
   7 0000 00       		.zero	1
   8              		.local	_ZStL8__ioinit
   9              		.comm	_ZStL8__ioinit,1,1
  10              	.LC0:
  11 0001 61726776 		.string	"argv[0] = "
  11      5B305D20 
  11      3D2000
  12              	.LC1:
  13 000c 612C2062 		.string	"a, b = "
  13      203D2000 
  14              	.LC2:
  15 0014 2C2000   		.string	", "
  16              	.LC3:
  17 0017 622B2B00 		.string	"b++"
  18              	.LC4:
  19 001b 622B3D61 		.string	"b+=a"
  19      00
  20              		.text
  21              		.globl	main
  23              	main:
  24              	.LFB1493:
  25              		.cfi_startproc
  26 0000 55       		pushq	%rbp
  27              		.cfi_def_cfa_offset 16
  28              		.cfi_offset 6, -16
  29 0001 4889E5   		movq	%rsp, %rbp
  30              		.cfi_def_cfa_register 6
  31 0004 4883EC20 		subq	$32, %rsp
  32 0008 897DEC   		movl	%edi, -20(%rbp)
  33 000b 488975E0 		movq	%rsi, -32(%rbp)
  34 000f 488B45E0 		movq	-32(%rbp), %rax
  35 0013 488B00   		movq	(%rax), %rax
  36 0016 0FB600   		movzbl	(%rax), %eax
  37 0019 0FBEC0   		movsbl	%al, %eax
  38 001c 8945F8   		movl	%eax, -8(%rbp)
  39 001f 488B45E0 		movq	-32(%rbp), %rax
  40 0023 488B00   		movq	(%rax), %rax
  41 0026 4883C001 		addq	$1, %rax
  42 002a 0FB600   		movzbl	(%rax), %eax
  43 002d 0FBEC0   		movsbl	%al, %eax
  44 0030 8945FC   		movl	%eax, -4(%rbp)
  45 0033 488D3500 		leaq	.LC0(%rip), %rsi
  45      000000
  46 003a 488D3D00 		leaq	_ZSt4cout(%rip), %rdi
  46      000000
  47 0041 E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
  47      00
  48 0046 4889C2   		movq	%rax, %rdx
  49 0049 488B45E0 		movq	-32(%rbp), %rax
  50 004d 488B00   		movq	(%rax), %rax
  51 0050 4889C6   		movq	%rax, %rsi
  52 0053 4889D7   		movq	%rdx, %rdi
  53 0056 E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
  53      00
  54 005b BE0A0000 		movl	$10, %esi
  54      00
  55 0060 4889C7   		movq	%rax, %rdi
  56 0063 E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c@PLT
  56      00
  57 0068 488D3500 		leaq	.LC1(%rip), %rsi
  57      000000
  58 006f 488D3D00 		leaq	_ZSt4cout(%rip), %rdi
  58      000000
  59 0076 E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
  59      00
  60 007b 4889C2   		movq	%rax, %rdx
  61 007e 8B45F8   		movl	-8(%rbp), %eax
  62 0081 89C6     		movl	%eax, %esi
  63 0083 4889D7   		movq	%rdx, %rdi
  64 0086 E8000000 		call	_ZNSolsEi@PLT
  64      00
  65 008b 488D3500 		leaq	.LC2(%rip), %rsi
  65      000000
  66 0092 4889C7   		movq	%rax, %rdi
  67 0095 E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
  67      00
  68 009a 4889C2   		movq	%rax, %rdx
  69 009d 8B45FC   		movl	-4(%rbp), %eax
  70 00a0 89C6     		movl	%eax, %esi
  71 00a2 4889D7   		movq	%rdx, %rdi
  72 00a5 E8000000 		call	_ZNSolsEi@PLT
  72      00
  73 00aa BE0A0000 		movl	$10, %esi
  73      00
  74 00af 4889C7   		movq	%rax, %rdi
  75 00b2 E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c@PLT
  75      00
  76 00b7 8345FC01 		addl	$1, -4(%rbp)
  77 00bb 488D3500 		leaq	.LC3(%rip), %rsi
  77      000000
  78 00c2 488D3D00 		leaq	_ZSt4cout(%rip), %rdi
  78      000000
  79 00c9 E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
  79      00
  80 00ce BE0A0000 		movl	$10, %esi
  80      00
  81 00d3 4889C7   		movq	%rax, %rdi
  82 00d6 E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c@PLT
  82      00
  83 00db 488D3500 		leaq	.LC1(%rip), %rsi
  83      000000
  84 00e2 488D3D00 		leaq	_ZSt4cout(%rip), %rdi
  84      000000
  85 00e9 E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
  85      00
  86 00ee 4889C2   		movq	%rax, %rdx
  87 00f1 8B45F8   		movl	-8(%rbp), %eax
  88 00f4 89C6     		movl	%eax, %esi
  89 00f6 4889D7   		movq	%rdx, %rdi
  90 00f9 E8000000 		call	_ZNSolsEi@PLT
  90      00
  91 00fe 488D3500 		leaq	.LC2(%rip), %rsi
  91      000000
  92 0105 4889C7   		movq	%rax, %rdi
  93 0108 E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
  93      00
  94 010d 4889C2   		movq	%rax, %rdx
  95 0110 8B45FC   		movl	-4(%rbp), %eax
  96 0113 89C6     		movl	%eax, %esi
  97 0115 4889D7   		movq	%rdx, %rdi
  98 0118 E8000000 		call	_ZNSolsEi@PLT
  98      00
  99 011d BE0A0000 		movl	$10, %esi
  99      00
 100 0122 4889C7   		movq	%rax, %rdi
 101 0125 E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c@PLT
 101      00
 102 012a 8B45F8   		movl	-8(%rbp), %eax
 103 012d 0145FC   		addl	%eax, -4(%rbp)
 104 0130 488D3500 		leaq	.LC4(%rip), %rsi
 104      000000
 105 0137 488D3D00 		leaq	_ZSt4cout(%rip), %rdi
 105      000000
 106 013e E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
 106      00
 107 0143 BE0A0000 		movl	$10, %esi
 107      00
 108 0148 4889C7   		movq	%rax, %rdi
 109 014b E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c@PLT
 109      00
 110 0150 488D3500 		leaq	.LC1(%rip), %rsi
 110      000000
 111 0157 488D3D00 		leaq	_ZSt4cout(%rip), %rdi
 111      000000
 112 015e E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
 112      00
 113 0163 4889C2   		movq	%rax, %rdx
 114 0166 8B45F8   		movl	-8(%rbp), %eax
 115 0169 89C6     		movl	%eax, %esi
 116 016b 4889D7   		movq	%rdx, %rdi
 117 016e E8000000 		call	_ZNSolsEi@PLT
 117      00
 118 0173 488D3500 		leaq	.LC2(%rip), %rsi
 118      000000
 119 017a 4889C7   		movq	%rax, %rdi
 120 017d E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@PLT
 120      00
 121 0182 4889C2   		movq	%rax, %rdx
 122 0185 8B45FC   		movl	-4(%rbp), %eax
 123 0188 89C6     		movl	%eax, %esi
 124 018a 4889D7   		movq	%rdx, %rdi
 125 018d E8000000 		call	_ZNSolsEi@PLT
 125      00
 126 0192 BE0A0000 		movl	$10, %esi
 126      00
 127 0197 4889C7   		movq	%rax, %rdi
 128 019a E8000000 		call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_c@PLT
 128      00
 129 019f B8000000 		movl	$0, %eax
 129      00
 130 01a4 C9       		leave
 131              		.cfi_def_cfa 7, 8
 132 01a5 C3       		ret
 133              		.cfi_endproc
 134              	.LFE1493:
 137              	_Z41__static_initialization_and_destruction_0ii:
 138              	.LFB1978:
 139              		.cfi_startproc
 140 01a6 55       		pushq	%rbp
 141              		.cfi_def_cfa_offset 16
 142              		.cfi_offset 6, -16
 143 01a7 4889E5   		movq	%rsp, %rbp
 144              		.cfi_def_cfa_register 6
 145 01aa 4883EC10 		subq	$16, %rsp
 146 01ae 897DFC   		movl	%edi, -4(%rbp)
 147 01b1 8975F8   		movl	%esi, -8(%rbp)
 148 01b4 837DFC01 		cmpl	$1, -4(%rbp)
 149 01b8 7532     		jne	.L5
 150 01ba 817DF8FF 		cmpl	$65535, -8(%rbp)
 150      FF0000
 151 01c1 7529     		jne	.L5
 152 01c3 488D3D00 		leaq	_ZStL8__ioinit(%rip), %rdi
 152      000000
 153 01ca E8000000 		call	_ZNSt8ios_base4InitC1Ev@PLT
 153      00
 154 01cf 488D1500 		leaq	__dso_handle(%rip), %rdx
 154      000000
 155 01d6 488D3500 		leaq	_ZStL8__ioinit(%rip), %rsi
 155      000000
 156 01dd 488B0500 		movq	_ZNSt8ios_base4InitD1Ev@GOTPCREL(%rip), %rax
 156      000000
 157 01e4 4889C7   		movq	%rax, %rdi
 158 01e7 E8000000 		call	__cxa_atexit@PLT
 158      00
 159              	.L5:
 160 01ec 90       		nop
 161 01ed C9       		leave
 162              		.cfi_def_cfa 7, 8
 163 01ee C3       		ret
 164              		.cfi_endproc
 165              	.LFE1978:
 168              	_GLOBAL__sub_I_main:
 169              	.LFB1979:
 170              		.cfi_startproc
 171 01ef 55       		pushq	%rbp
 172              		.cfi_def_cfa_offset 16
 173              		.cfi_offset 6, -16
 174 01f0 4889E5   		movq	%rsp, %rbp
 175              		.cfi_def_cfa_register 6
 176 01f3 BEFFFF00 		movl	$65535, %esi
 176      00
 177 01f8 BF010000 		movl	$1, %edi
 177      00
 178 01fd E8A4FFFF 		call	_Z41__static_initialization_and_destruction_0ii
 178      FF
 179 0202 5D       		popq	%rbp
 180              		.cfi_def_cfa 7, 8
 181 0203 C3       		ret
 182              		.cfi_endproc
 183              	.LFE1979:
 185              		.section	.init_array,"aw"
 186              		.align 8
 187 0000 00000000 		.quad	_GLOBAL__sub_I_main
 187      00000000 
 188              		.hidden	__dso_handle
 189              		.ident	"GCC: (Ubuntu 7.3.0-16ubuntu3) 7.3.0"
 190              		.section	.note.GNU-stack,"",@progbits
