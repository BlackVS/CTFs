# eXit

set disable-randomization off
e asm.emu=1
pdd 30 @main

db 0x562c080e7783
rdi = input

db 0x562c080e74dd
db 0x560d7d1803a9

dc

[0x560d7d1803a9]> x 16 @rdi
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x560d7e71cac0  5465 7374 0a00 0000 0000 0000 0000 0000  Test............
[0x560d7d1803a9]> x 16 @rsi
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x560d7d18107b  97cd d2d6 c0c7 cd84 ec91 ad62 f5f1 6522  ...........b..e"
[0x560d7d1803a9]> x 32 @rsi
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x560d7d18107b  97cd d2d6 c0c7 cd84 ec91 ad62 f5f1 6522  ...........b..e"
0x560d7d18108b  5882 b137 613e 5d2b 144c 0000 000a 596f  X..7a>]+.L....Yo

rsi=coded_key1=param_1

        if ((uint8_t)((*(uint8_t *)(param_1 + i) ^ *(uint8_t *)((int64_t)&var_60h + (int64_t)i)) +
                     *(char *)((int64_t)&var_40h + (int64_t)i)) != *(char *)(param_2 + i)) {
            uVar2 = 0;
            goto code_r0x000014a7;
        }






db 0x562c080e758b

https://en.wikipedia.org/wiki/X86_calling_conventions
RDI, RSI, RDX, RCX, R8, R9,
