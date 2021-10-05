# Task 8

![text](img/desc.png)

## Input file:

[signal8.iqdata](input/signal8.iqdata)

## Solution:

As base I used Drake's Signal 5 [write-up](https://batchdrake.github.io/ctsII/).

First I tried solve it using URH:

![sig00](img/sig00.png)

![sig01](img/sig01.png)

![sig02](img/sig02.png)

![sig03](img/sig03.png)

![sig04](img/sig04.png)


and try decode demodulated bitstream (4FSK) but failed.

Finally I switched to SigDigger due to it allow more accurate timespace operations:

![sd00](img/sd00.png)

![sd01](img/sd01.png)

![sd02](img/sd02.png)

![sd03](img/sd03.png)

![sd04](img/sd04.png)

![sd05](img/sd05.png)

![sd06](img/sd06.png)

Demodulated data were decoded using [C++ programm](script/check1.cpp).



