#!/usr/bin/env python3

import os, sys
from collections import Counter
from pyhamtools import LookupLib, Callinfo

res_reporter = Counter()

res_maxdst = 0
res_reporter_most = None
res_most_distant = None

with open("../input/wsprspots.csv","rt") as f:
    lines=f.readlines()
    for l in lines[1:]:
        l=l.strip()
        reporter, sdistance, callsign, reporter_grid, grid = l.split(',')
        distance = int(sdistance)
        res_reporter[reporter] +=1
    res_reporter_most = res_reporter.most_common(1)[0][0]

    my_lookuplib = LookupLib(lookuptype="countryfile")
    cic = Callinfo(my_lookuplib)
    try:
        print("Reporter with the most reports located in: {}, {}".format(res_reporter_most, cic.get_country_name(res_reporter_most)))
    except:
        pass

    for l in lines[1:]:
        l=l.strip()
        reporter, sdistance, callsign, reporter_grid, grid = l.split(',')
        distance = int(sdistance)
        if reporter == res_reporter_most and distance>res_maxdst:
            res_maxdst = distance
            res_most_distant = callsign

    print("Country of origin of the most distant received messages: {}, {}, {}".format(res_most_distant, res_maxdst, cic.get_country_name(res_most_distant)))
