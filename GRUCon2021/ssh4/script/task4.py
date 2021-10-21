#!/usr/bin/env python3

import os, sys
from collections import Counter
from types import DynamicClassAttribute
from collections import *
from itertools import *
#from pyhamtools import LookupLib, Callinfo


# For the file in Whisper 1, what percent of the other nodes are unreachable 
# regardless of hop count from "F5MAF"? 
# Assume any node that is visible to a reporter may be reached by the reporter. Round to two decimal places.

node2check = "IZ7BOJ"

# vertices have nums 0..N-1
class Graph(object):
    def __init__(self,n):
        self.VN=n
        self.G = [[] for _ in range(n)]
        # BFS
        self.V  = None # visited
        self.D  = None # min distance
        self.PR = None # parent


    def add_edge(self,x,y):
        self.G[x].append(y)
        #not directed:
        self.G[y].append(x)

    def BFS(self,root=0):
        N =self.VN
        P  = self.PR  = [None]*N
        D  = self.D   = [0]*N
        #PTH= self.PATH= [ [] for _ in range(N) ]

        G=self.G #no need to save G
        i=0
        v=root
        D[root]=1
        q=deque([root])
        while q:
            v=q.popleft()
            pv=P[v]
            dv=D[v]
            for w in G[v]:
                if w==pv: #not go back
                    continue
                if D[w]: 
                    continue #already visited and counted
                P[w]=v
                D[w]=dv+1
                q.append(w)

        print("reachable from root: {}".format( sum(map(lambda x: x>0, D))-1 )) # -1 to exclude myself
        print("farthest  distance : {}".format( max(D) ))

        
        # check avg path
        res = 0
        res_cnt = 0
        for i,d in enumerate(D):
            if d==0:
                continue
            if i==root:
                continue #not check myself
            assert(d>0)
            res += d  # hops includes source and dest
            res_cnt+=1

        return res/res_cnt


# vertices have nums 0..N-1
map_cs2num = dict()
map_num2cs = []
edges = set() 

# maps callsigns to numeric node ids
# nodes numbered 0..N-1 where N is a numberof distinct call signs
def get_cs_idx(cs):
    # try get numeric id of node
    n_cs =  map_cs2num.get(cs, None)
    if n_cs!=None:
        return n_cs #if found - return it
    #assign id to new node
    n_cs = len(map_cs2num)
    map_num2cs.append(cs)
    map_cs2num[cs]=n_cs
    return n_cs

# parse input file 
with open("../input/wsprspots.csv","rt") as f:
    lines=f.readlines()
    for l in lines[1:]:
        l=l.strip()
        reporter, sdistance, callsign, reporter_grid, grid = l.split(',')
        n_rep = get_cs_idx(reporter)
        n_cs  = get_cs_idx(callsign)
        edges.add( (n_rep, n_cs) )

# get a number of distinct nodes
nodes_cnt = len(map_num2cs)

graph = Graph(nodes_cnt)
for u,v in edges:
    graph.add_edge(v, u)

n_src = get_cs_idx(node2check)
print("{:.2f}".format(graph.BFS(n_src)))

