# Task 5

![text](img/cts_task5.png)

Wav file given.

## Part 1. Morze
Listening it I recognized morze code at the beginning, later DTMF, and later some additional noise.

Decoding Morze (I cut part with Morze code, applied low-band filter and used online Morze decoder ), beginning was recognized good but final part looked broken.
I manually decoded last word and got:

```SOS-STEGHIDE-TOOL-F1N1CKY5HUT```

## Part 2. DTMF

Did the same, tried few also mobile phone, but best result got using http://dialabc.com/sound/detect/index.html

It gives 
```
05208407203506707206507803507008207907703507606907008403508308907806703505065
```

I look close we will saw that it is groups of 3 digits, looks like ASCCII codes:

https://www.dcode.fr/ascii-code

=>


```
DEC /3

4TH#CHAN#FROM#LEFT#SYNC#2A
```

## Part 3. Steg-hide
Hinf from part 1 says that it could steghide coded data with password "F1N1CKY5HUT"

```bash
>steghide --extract -sf track.wav -p F1N1CKY5HUT
wrote extracted data to "iq-data.cfile".
```

Opening in URH and checking spectre gives as clue taht there 6 channels of OOK coded data:

![Spectre](img/task5_part3_spectre.png)

We need "4th from left", it seems to be left is the toward 0 Hz %) i.e. counted from bottom in URH

Width of each band is ~15kHz

