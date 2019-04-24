# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:28:31 2018

@author: janvr
"""

from sys import stdin
from collections import deque

class Node:
    def __init__(self, num, color):
        self.num = num
        self.color = color
        self.neighbours = set()

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.size = len(nodes)
        
    def gprint(self):
        for node in self.nodes:
            print("Node {0}: {1}".format(node.num, [x.num for x in node.neighbours]))
        
def read_in(name):
    f = open(name, 'r')
    N, E, C = [int(x) for x in f.readline().split()]
    colors = [int(x) for x in f.readline().split()]
    lines = f.readlines()
    edges = []
    for line in lines:
        edges.append([int(x) for x in line.split()])
    return N, E, C, colors, edges

def sys_read_in():
    N, E, C = [int(x) for x in stdin.readline().split()]
    colors = [int(x) for x in stdin.readline().split()]
    lines = stdin.readlines()
    edges = []
    for line in lines:
        edges.append([int(x) for x in line.split()])
    return N, E, C, colors, edges
    
    
def make_graph(colors, edges):
    nodes = [Node(i, c) for i, c in enumerate(colors)]
    for edge in edges:
        nodes[edge[0]].neighbours.add(edge[1])
        nodes[edge[1]].neighbours.add(edge[0])
    graph = Graph(nodes)
    return graph
        
def mono(g, start, visited):
    q = deque()
    q.append(g.nodes[start])
    color = g.nodes[start].color
    visited[g.nodes[start].num] = True
    cnt=0
    while q:
        node = q.popleft()
        cnt+=1
        for nbr in node.neighbours:
            if G.nodes[nbr].color==color and visited[nbr]==False:
                q.append(G.nodes[nbr])
                visited[nbr]=True
    return cnt, visited

def can_i_pls_get_an_A(g):
    out = dict()
    visited = [False]*g.size
    for node in g.nodes:
        if visited[node.num]==True: continue
        cnt, visited = mono(g, node.num, visited)
        #print(node.num)
        try: out[cnt]+=1
        except: out[cnt]=1
    return out

def jprint(out):
    vec = sorted(out)
    for i in vec:
        if out[i]!=0:
            print(i, out[i])


name = "datapub/pub10.in"
N, E, C, colors, edges = sys_read_in()
G = make_graph(colors, edges)
out = can_i_pls_get_an_A(G)
jprint(out)