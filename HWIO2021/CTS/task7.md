# Task 7

![text](img/cts_task7.png)

Open given pcap file in Wireshark:

![1](img/task7_1.png)

Filter shorts packets:

![1](img/task7_2.png)

Checking few packets found interesting file signature %))

![1](img/task7_3.png)

After I switched to console and extracted data from interested packets:

```
"C:\Program Files\Wireshark\tshark.exe" -r data.pcapng -T fields -e usb.capdata -Y usb.capdata > capdata.raw
```

After I run binwalk on capdata.raw with option -e (extract all data),

as result "telesignal_1msps.complex32" was extracted.

Opened in URH:

![1](img/task7_4.png)

Name of file (telesignal) and screenshot above gave me idea that it can be some TV signal ( image line by line ) but my knowledge of RF signals too small and I decided to switch to other task.

