# AESTHETIC

## recon

First open in radare2 or Cutter and check main:

![](img/main.png)

Let's go deeper, to aes_128_table_encrypt .. awful:

![](img/aes_128_table_encrypt.png)

Let's check exports...

![](img/exports.png)

and google for AES, SBox, TyiBoxes, TyiTables.
Very soon you will get this links:

https://en.wikipedia.org/wiki/Rijndael_S-box

https://github.com/Gr1zz/WhiteBoxAES

Now we know our opponent - WhiteBOX AES %) 

Let's check found sources and... we are lucky!!! -> our program is about 100% is https://github.com/Gr1zz/WhiteBoxAES/blob/master/aes_table.c


![](img/tboxes-hex.png)

![](img/sbox-hex.png)

![](img/subbytes.png)

![](img/sbox-gdb.png)

## analisys


## pwn



