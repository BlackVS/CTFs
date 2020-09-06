# Hellcode

[200~92      push    0x7361655f ; '_eas' ; rsp=0x177ff0
0x10000197      push    0x30735f74 ; 't_s0' ; rsp=0x177fe8
0x1000019c      push    0x306e7b6e ; 'n{n0' ; rsp=0x177fe0
0x100001a1      push    0x6f633272 ; 'r2co' ; rsp=0x177fd8
0x100001a6      push    0x20736920 ; ' is ' ; rsp=0x177fd0
0x100001ab      push    0x67616c66 ; 'flag' ; rsp=0x177fc8 rsi
0x100001b0      push    0x20656854 ; 'The ' ; rsp=0x177fc0


The flag is r2con{n0t_s0_easy}



https://filippo.io/linux-syscall-table/

34	pause	sys_pause	kernel/signal.c

radiff2 binary0 binary0_patched 
0x00001004 48c7c0220000000f05 => 909090909090909090 0x00001004
0x0000105e 48c7c0220000000f05 => 909090909090909090 0x0000105e
0x00001073 48c7c0220000000f05 => 909090909090909090 0x00001073
0x0000108c 48c7c0220000000f05 => 909090909090909090 0x0000108c
0x000010b1 48c7c0220000000f05 => 909090909090909090 0x000010b1
0x000010bd 48c7c0220000000f05 => 909090909090909090 0x000010bd
0x000010cb 48c7c0220000000f05 => 909090909090909090 0x000010cb
0x00001166 48c7c0220000000f05 => 909090909090909090 0x00001166

0x100000ba      80ea53                 sub     dl, 0x53 ; 83 ; dl=0xffffffffffffffad ; of=0x0 ; sf=0x1 ; zf=0x0 ; pf=0x0 ; cf=0x1
0x100000bd      90                     nop
0x100000be      90                     nop
0x100000bf      90                     nop
0x100000c0      90                     nop
0x100000c1      90                     nop
0x100000c2      90                     nop
0x100000c3      90                     nop
0x100000c4      90                     nop
0x100000c5      90                     nop
0x100000c6      4831c9                 xor     rcx, rcx ; rcx=0x0 ; zf=0x1 ; pf=0x1 ; sf=0x0 ; cf=0x0 ; of=0x0
0x100000c9      759c                   jne     trolololololololo ; unlikely
0x100000cb      90                     nop
0x100000cc      90                     nop
0x100000cd      90                     nop
0x100000ce      90                     nop
0x100000cf      90                     nop
0x100000d0      90                     nop
0x100000d1      90                     nop
0x100000d2      90                     nop
0x100000d3      90                     nop
0x100000d4      80faff                 cmp     dl, 0xff ; 255 ; zf=0x0 ; cf=0x1 ; pf=0x0 ; sf=0x1 ; of=0x0
0x100000d7      7558                   jne     error ; rip=0x10000131 -> 0x20646268 loc.error ; likely


input-0x53==0xff => input = (0x53+0xff) % 256 = 0x52, 'R'