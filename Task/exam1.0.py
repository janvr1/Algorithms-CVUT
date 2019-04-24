# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:22:27 2018

@author: janvr
"""
from sys import stdin
from collections import deque

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
    
name = "datapub/pub01.in"
N, E, C, clrs, edges = import_data(name)
G = create_graph(N, clrs, edges)