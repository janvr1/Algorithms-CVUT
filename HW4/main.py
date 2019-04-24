# -*- coding: utf-8 -*-
"""
Created on Thu May  3 18:50:28 2018

@author: janvr
"""
import sys
class Node:
    def __init__(self, num, c):
        self.nbrs = []
        self.num  = num
        self.color = c
        
    def nprint(self):
        print("Node number: {}".format(self.num))
        print("Node neighbours: {}".format([x.num for x in self.nbrs]))
        
class Graph:
    def __init__(self, N, colors):
        self.size = N
        self.nodes = [Node(x, c) for x, c in enumerate(colors)]
        
    def newedge(self, N, M):
        self.nodes[N].nbrs.append(self.nodes[M])
        self.nodes[M].nbrs.append(self.nodes[N])
        
    def gprint(self):
        for node in self.nodes:
            x = [nd.num for nd in node.nbrs]
            print("Node number/color: {0}/{1}".format(node.num, node.color))
            print("Node neighbours: {}".format(x))
            print("------------------------------")
        
def import_data():
    line1 = sys.stdin.readline()
    N, E, C = [int(x) for x in line1.split()]
    line2 = sys.stdin.readline()
    clrs = [int(x) for x in line2.split()]
    edges = []
    lines = sys.stdin.readlines()
    for line in lines:
        edge = [int(x) for x in line.split()]
        edges.append(edge)
    return(N, E, C, clrs, edges)
    
def create_graph(N, colors, edges):
    G = Graph(N, colors)
    for m, n in edges:
        G.newedge(m, n)
    return(G)

def find(edges, G):
    cnt=0

    for m1, n2 in edges:
        OK1 = True
        OK2 = True
        c1 = G.nodes[m1].color
        c2 = G.nodes[n2].color
        sos_m1 = [x for x in G.nodes[m1].nbrs if x.num!=n2]
        sos_n2 = [x for x in G.nodes[n2].nbrs if x.num!=m1]
        sos_m1c = [x.color for x in sos_m1]
        sos_n2c = [x.color for x in sos_n2]
        if any(x==c1 for x in sos_n2c):
            continue
        if any(x==c2 for x in sos_m1c):
            continue
        if all((x!=c1 and x!=c2) for x in sos_m1c) and all((x!=c1 and x!=c2) for x in sos_n2c):
            cnt+=1
        else:
            sos11 = [x for x in sos_m1 if x.color == c1]
            sos22 = [x for x in sos_n2 if x.color == c2]
            for y in sos11:
                sos111 = [x.color for x in y.nbrs if x.num!=m1]
                if all(x!=c2 for x in sos111): OK1 = True
                else:
                    OK1 = False
                    break
            
            for z in sos22:
                sos222 = [x.color for x in z.nbrs if x.num!=n2]  
                if all(x!=c1 for x in sos222): OK2 = True
                else:
                    OK2 = False
                    break
            if OK1 and OK2: cnt+=1
    return(cnt)

    
def isolated(node1, node2):
    nbrs = node1.nbrs
    nbrs_col = [x.color for x in nbrs if x.num!=node2.num]
    OK = False
    for i in nbrs_col:
        if (i!=node1.color and i!=node2.color): OK = True
        else: OK = False
    
    if OK==True: return(True)
    else:
        same_nbrs = [x for x in nbrs if x.color==node1.color]
        for n in same_nbrs:
            n_nbrs = [x.color for x in n.nbrs]
            for j in n_nbrs:
                if j!=node2.color: OK=True
                else: OK=False
    return(OK)
    
    
    
    
    
N, E, C, clrs, edges = import_data()
G = create_graph(N, clrs, edges)
print(find(edges, G))
