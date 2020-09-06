# Brute Searcher

Getting *mr.Bean Walker* flag we discovered remote firmware folder:

![alt text](img/blackvs.11.png "Firmware folder")

But may be https://spynet.techmaker.ua/ has more accessible folders?
Let's check

## dirb

Let's run *dirb* from **Kali** and ... voilà ::

![alt text](img/blackvs.00.png "dirb@Kali")

## dirsearch 

If you don't have Kali you can download [dirsearch](https://github.com/maurosoria/dirsearch) tool and run it everywhere where Python present ^) :

![alt text](img/blackvs.01.png "Dirsearch@powershell")

## dirbuster

If you don't like Python but happy of Java %) - you can use **dirbuster**. It is included in [Kali](https://kali.tools/?p=116) as well as can be used standalone everywhere Java is (see at [OWASP](https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)).

## Capturing Flag

We discovered few more remote folders:

```
+ https://spynet.techmaker.ua/admin (CODE:401|SIZE:0)                          
+ https://spynet.techmaker.ua/Admin (CODE:401|SIZE:0)                          
+ https://spynet.techmaker.ua/ADMIN (CODE:401|SIZE:0)                          
+ https://spynet.techmaker.ua/docs (CODE:200|SIZE:249)                         
+ https://spynet.techmaker.ua/favicon.ico (CODE:200|SIZE:15086)                
+ https://spynet.techmaker.ua/fw (CODE:301|SIZE:0)                             
+ https://spynet.techmaker.ua/index (CODE:200|SIZE:3586)                       
+ https://spynet.techmaker.ua/Index (CODE:200|SIZE:3585)                       
```
First will check folders with return code 200 (OK) i.e. public available folders. It seems to be we got next prize:

![alt text](img/blackvs.02.png "docs@ptechmaker")

Let's try download/open both discovered files (yep - *secret.txt* sounds very promising).

https://spynet.techmaker.ua/docs/secret.txt

![alt text](img/blackvs.04.png "Flag")

PS: if you see "*flag{wrong deviceid}*" instead or error like this:

![alt text](img/blackvs.06.png "DeviceID missing")

it means no DeviceID cookie present during download request. 

To fix this you can just login to your Badge page:

![alt text](img/blackvs.03.png "Flag")

But if you don't look for easy ways you can manually add needed cookie directly in request. Name and value of cookie can be spied from Badge page:

![alt text](img/blackvs.07.png "Cookie")

This can be very helpful expirience for fulfilling "*NoNameCon SpyNet*" tasks later %))

After getting flag just register it on your badge:


![alt text](img/blackvs.05.png "Cookie")

<div align="center">
![alt text](img/blackvs.08.png "Done")
</div>


