# Defuse

Open in Cutter:

![](img/defuse_main_asm.png)

Decompile it:

![](img/defuse_main_dec.png) 

Main points we see are:
- strange 20 numbers
- validation of input string len = must be also 20 (it is pure coincidence? I don't think...)
- together with size validation the other function is called. After I renamed it to islowerascii():

![](img/defuse_isalowerascii.png)

I.e. defuse sequence must be 20 chars string of lower ASCII.

Inside loop we see two things happenn:
- called some function (I renamed it to decode_char() later)
- result if compared with strange 20 numbers

Check decoding function:
![](img/defuse_decode.png)

Check 
![](img/defuse_validation.png)

bVar1 = (bool)(bVar1 & iVar2 == *(int32_t *)((int64_t)&var_60h + (int64_t)(var_6ch._4_4_ + -1) * 4));

