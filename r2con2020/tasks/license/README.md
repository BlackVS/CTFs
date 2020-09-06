# Radare License Checker

## First run

![](img/first_run.png)

We need to know correct size first.

Open binary in Cutter to check.

## Get correct size

Locate incorrect size warning in the Strings:

![](img/err_wrong_size_1.png)

Go to the needed string:

![](img/err_wrong_size_2.png) 

Locate X-Ref to it:

![](img/err_wrong_size_3.png) 

Due to Cutter didn't show jumps (I don'd know why) I checked X-Refs to 
![](img/strlen_0.png)

![](img/strlen_1.png)

![](img/strlen_2.png)

## Second run

![](img/second_run.png)

## remove anti-bruteforce defence

![](img/sleep.png)

## time to script

```python
#!/usr/bin/env python

import os, sys
from py_execute.process_executor import execute
from mock import Mock

cmd = "radarelicensechecker_patched.exe "
key_pre = "r2con{"
key_sfx = "}"
key_mid = [' '] * (34 - len(key_pre) - len(key_sfx))

i=0
while i<len(key_mid):
    key = "\""+key_pre + "".join(key_mid) + key_sfx + "\""
    ret = execute(cmd+key, ui=Mock())
    msg = "ERROR: decryption error in block "
    if  msg not in ret[1]:
        print(key)
        break
    pos1 = ret[1].find(msg) + len(msg)
    pos2 = ret[1].find("!", pos1)
    blk = int( ret[1][pos1:pos2].strip())
    if blk == i+len(key_pre):
        key_mid[i] = chr( ord(key_mid[i]) + 1)
        if key_mid[i]=="\"":
            key_mid[i] = chr( ord(key_mid[i]) + 1)
    else:
        i+=1
        print(key)
        continue
```

![](img/script.png)
