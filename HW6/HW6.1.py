# -*- coding: utf-8 -*-
"""
Created on Thu May 10 22:21:52 2018

@author: janvr
"""
import sys

class Node:
    def __init__(self, color, num):
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

class Queue():
    def __init__(self, N):
        self.size = N
        self.contents = [None]*N
        self.front = 0
        self.tail = 0

    def isempty(self):
        return(self.tail == self.front)
        
    def enqueue(self, x):
        self.contents[self.tail] = x
        self.tail = (self.tail+1)%self.size

    def dequeue(self):
        x = self.contents[self.front]
        self.contents[self.front] = None
        self.front = (self.front+1)%self.size
        return(x)

    def get(self):
        return(self.dequeue())

    def push(self, element):
        self.enqueue(element)
        
    def qprint(self):
        print(self.contents)
        
def read_in(name):
    f = open(name, 'r')
    N, E, C = [int(x) for x in f.readline().split()]
    colors = [int(x) for x in f.readline().split()]
    lines = f.readlines()
    edges = []
    for line in lines:
        edges.append([int(x) for x in line.split()])
    return(N, E, C, colors, edges)
    
def sys_read_in():
    N, E, C = [int(x) for x in sys.stdin.readline().split()]
    colors = [int(x) for x in sys.stdin.readline().split()]
    lines = sys.stdin.readlines()
    edges = []
    for line in lines:
        edges.append([int(x) for x in line.split()])
    return(N, E, C, colors, edges)
    
def make_graph(colors, edges):
    nodes = [Node(c, i) for i, c in enumerate(colors)]
    for m, n in edges:
        nodes[m].neighbours.add(n)
        nodes[n].neighbours.add(m)
    graph = Graph(nodes)
    return(graph)
        
def distances(g, start):
    visited = [False]*g.size
    q = Queue(g.size)
    dist = [None]*g.size
    q.enqueue(g.nodes[start])
    visited[start] = True
    dist[start] = 0
    while not(q.isempty()):
        node = q.dequeue()
        for nbr in node.neighbours:
            if not(visited[nbr]):
                q.enqueue(G.nodes[nbr])
                visited[nbr]=True
                dist[nbr] = dist[node.num]+1
    return(dist)
                
def dist2(g, start):
    visited = [False]*g.size
    q = Queue(g.size)
    dist = dict.fromkeys(range(g.size))
    q.enqueue(g.nodes[start])
    visited[start] = True
    dist[start] = 0
    while not(q.isempty()):
        node = q.dequeue()
        for nbr in node.neighbours:
            if not(visited[nbr]):
                q.enqueue(G.nodes[nbr])
                visited[nbr]=True
                dist[nbr] = dist[node.num]+1
    return(dist)
      
def node_distances(g):
    all_dist=dict()
    for i in range(g.size):
        all_dist[i]=dist2(g, i)
    return(all_dist)
    
def edge_distance(edge1, edge2, n_dist):
    return(min([n_dist[i][j] for i in edge1 for j in edge2]))
        
def edge_types(edges, colors):
    edgetypes = [tuple(sorted([colors[i], colors[j]])) for i, j in edges]    
    types = dict()
    for x in edgetypes:
        types[x] = []
    for i, x in enumerate(edges):
        types[edgetypes[i]].append(x)
    return(types)
    
def diameters(types, n_dist):
    diams = dict.fromkeys(types.keys())
    for x in diams:
        edges = types[x]
        if len(edges)<2: diameter = 0
        else:
            diameter = max([edge_distance(e1, e2, n_dist) for i, e1 in enumerate(edges) for e2 in edges[i+1:]])
        diams[x]=diameter
    return(diams)
    
def jprint(diams):
    y = sorted(list(diams.keys()))
    for x in y:
        if diams[x]!=0: 
            a, b = x
            c = diams[x]
            print(a, b, c)

name = "datapub/pub10.in"
N, E, C, colors, edges = read_in(name)
G = make_graph(colors, edges)
node_dist = node_distances(G)
edgetypes = edge_types(edges, colors)
diams = diameters(edgetypes, node_dist)
jprint(diams)