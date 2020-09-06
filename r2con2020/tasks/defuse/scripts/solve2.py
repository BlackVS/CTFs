#!/usr/bin/env python3
import os,sys
from itertools import *

#for p in product( 'prxz', 'su', 'ln', 'ce', 'prxz', 'aio', 'ln', 'ce', 'km', 'aio', 'prxz', 'ce', 'tv', 'aio', 'km', 'ce' ):
#for p in product( 'prxz', 'su', 'ln', 'ce', 'prxz', 'aio' ):
#for p in product( ['rule'], 'prxz', 'aio', 'ln', 'ce', 'km', 'aio', 'prxz', 'ce', 'tv', 'aio', 'km', 'ce' ):
#for p in product( 'prxz', 'ce', 'tv', 'aio', 'km', 'ce' ):
#for p in product( ['rule'], 'prxz', 'aio', 'ln', 'ce', 'km', 'aio', 'prxz', 'ce', ['take','time','tome']):
#for p in product( ['rule'], 'prxz', 'aio', 'ln', 'ce', 'km', 'aio', 'prxz', 'ce', ['time']):
for p in product( ['rule'], 'prxz', 'aio', 'ln', 'ce', ['more'], ['time']):
    print("esil"+"".join(p))

esilrulezonemoretime