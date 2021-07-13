# Task 1

![text](img/cts_task1.png)

First we have to tune 454MHz and grab the signal (I reading recorded signal from 127.0.0.1, during real CTF use remote IP of server instead 127.0.0.1 ):

```bash
./rx_to_file.py --server-ip 127.0.0.1 --rx-frequency=454000000
```

![RX to File](img/task1_1.png)

Switching to waterfall we will something interesting:

![RX to File](img/task1_2.png)

Check in inpsectrum:

![RX to File](img/task1_inspectrum.png)

Check in GQRX:
```
file=/home/vvs/cts.raw,freq=454e6,rate=192000,repeat=true,throttle=true
```

![RX to File](img/task1_gqrx_1.png)

![RX to File](img/task1_gqrx_2.png)

Check in URH:

![RX to File](img/task1_urh.png)

**Welcome To HWIO2021 Listen@212MHz**

Let's go to 212MHz %)

[Task 2](task2.md)