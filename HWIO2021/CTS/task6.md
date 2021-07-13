# Task 6

(0 solves)

![text](img/cts_task6.png)

Read signal:

![Read](img/task6_rx2file.png)

Signal consists of two parts repeated one by one with big pauses:

![URH](img/task6_1.png)

I split them and analysed separetly.

Surprise:

![Part1](img/task6_2.png)

At the top the part from signal 6, at the bottom - signal from... task4 %)))

Part 2:

![Part1](img/task6_3.png)

![Part1](img/task6_4.png)

![Part1](img/task6_5.png)

At this point I stopped due to time over.

Current idea is:
* 1's are stop bits between symbols
* each symbol is the number of 0's between two consecutive 1's
* each such symbol corresponds to some char, for exampling adding some constant to get ASCII code

![Part1](img/task6_6.png)