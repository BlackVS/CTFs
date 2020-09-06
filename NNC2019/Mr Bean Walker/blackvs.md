# Intro. Mr. Bean Walker and .. Doom?

## 0. Turn badge on
First of all you have to attach your badge to computer and connect to it via terminal. 

Correspondent instructions can be found at official NonameCon Badge [page](https://nonamecon.org/badge).
After connecting first try 'help' - works :)

![alt text](img/blackvs.00.png "Help command")

![alt text](img/blackvs.01.png "Help command results")

Good. Next try all commands mentioned in the help output:

![alt text](img/blackvs.02.png "Rest of commands")

Not good - we need root to run most of them.

But it seems *restart* works:

![alt text](img/blackvs.03.png "Help command results")

We see a lot of very interesting information including hint at the end.

Ok, now we need find mentioned trailer. Badge trailer. Google will help to us ^)

It was found at the official NonameCon Youtube channel - here it is: [NoNameCon Badge Trailer](https://www.youtube.com/watch?v=chfoAWevHMs)

## 1. Watch and enjoy trailer at Youtube

![alt text](img/blackvs.04.png "Doom...")

Yep, interesting... but what it is????
Password?????
Yesssssss

## 2. Get root
Let's try 'iddqd' found in video in terminal:

![alt text](img/blackvs.05.png "Doom...")

Super:

![alt text](img/blackvs.08.jpg "Doom...")

(hands themselves type 'idkfa' %) Yep, it is not [Doom](http://lurkmore.to/IDDQD) :))

![alt text](img/blackvs.06.png "Doom...")

Let's try other commands, for example:

![alt text](img/blackvs.07.png "...")

Ok. We have root. Now we need flags %)

## 3. Get the first flag

Check rest commands like *dmsg*, *join* etc.
For example, try connect badge to Wi-Fi:

![alt text](img/blackvs.09.png "Wi-Fi...")

and... after some time we will see diagnostic message:

![alt text](img/blackvs.10.png "BIN")

Very interesting. Can we download firmware manually? Yes, we can %)
But let's check folder with binary:

![alt text](img/blackvs.11.png "ELF")

Ok, we have both **bin** and **ELF** images - very good. Let's analyze them.
First of all check for strings inside:

```
rabin2.exe -zz nn-badge195.bin
```

if you have **radare2** installed

or 

![alt text](img/blackvs.12.png "Strings")

if you have Kali.

I used... FAR %) :

![alt text](img/blackvs.13.png "FAR")

Ok, it seems to be found hard-coded flag - let's check it:

![alt text](img/blackvs.14.png "Mr. Bean")

Yehhho!!!

![alt text](img/blackvs.ff.gif "Success RuLeZ")
