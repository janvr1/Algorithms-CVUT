# -*- coding: utf-8 -*-
"""
Created on Sun May  6 11:09:07 2018

@author: janvr
"""

class Node:
    def __init__(self, num, c):
        self.nbrs = set()
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
        self.nodes[N].nbrs.add(M)
        self.nodes[M].nbrs.add(N)
        
    def gprint(self):
        for node in self.nodes:
            x = [nd.num for nd in node.nbrs]
            print("Node number/color: {0}/{1}".format(node.num, node.color))
            print("Node neighbours: {}".format(x))
            print("------------------------------")
       
def import_data(name):
    f = open(name, 'r')
    line1 = f.readline()
    N, E, C = [int(x) for x in line1.split()]
    line2 = f.readline()
    clrs = [int(x) for x in line2.split()]
    edges = []
    lines = f.readlines()
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
        OK1 = False
        OK2 = False
        c1 = G.nodes[m1].color
        c2 = G.nodes[n2].color
        m1neighbours = set([x for x in G.nodes[m1].nbrs if x!=n2])
        n2neighbours = set([x for x in G.nodes[n2].nbrs if x!=m1])
        n2c = set([G.nodes[x].color for x in n2neighbours])
        m1c = set([G.nodes[x].color for x in m1neighbours])
        if (m1 in n2c) or (n2 in m1c): continue
        if (m1 not in n2c) and (n2 not in n2c) and (m1 not in m1c) and (n2 not in m1c): cnt+=1
        else:
            sos11 = set([G.nodes[x].num for x in m1neighbours if G.nodes[x].color == c1])
            sos22 = set([G.nodes[x].num for x in n2neighbours if G.nodes[x].color == c2])
            for y in sos11:
                sos111 = set([G.nodes[x].color for x in G.nodes[y].nbrs if x!=m1])
                if c2 not in sos111: OK1 = True
                else:
                    OK1 = False
                    break
            
            for z in sos22:
                sos222 = set([G.nodes[x].color for x in G.nodes[z].nbrs if x!=n2])
                if c1 not in sos222: OK2 = True
                else:
                    OK2 = False
                    break
            if OK1 and OK2: cnt+=1
        
    return(cnt)
    
    
    
    
    
name = "datapub/pub10.in"
N, E, C, clrs, edges = import_data(name)
G = create_graph(N, clrs, edges)
print(find(edges, G))