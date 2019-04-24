# -*- coding: utf-8 -*-
"""
Created on Sun May  6 10:17:53 2018

@author: janvr
"""
import sys
from collections import deque

class Node:
    def __init__(self, num, color):
        self.num = num
        self.color = color
        self.neighbours = set()

class Graph:
    def __init__(self, nodes, base):
        self.nodes = nodes
        self.base = base
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
    N, E, C, S = [int(x) for x in f.readline().split()]
    colors = [int(x) for x in f.readline().split()]
    lines = f.readlines()
    edges = []
    for line in lines:
        edges.append([int(x) for x in line.split()])
    return(N, E, C, S, colors, edges)
    
def sys_read_in():
    N, E, C, S = [int(x) for x in sys.stdin.readline().split()]
    colors = [int(x) for x in sys.stdin.readline().split()]
    lines = sys.stdin.readlines()
    edges = []
    for line in lines:
        edges.append([int(x) for x in line.split()])
    return(N, E, C, S, colors, edges)
    
def make_graph(colors, edges, S):
    nodes = [Node(i, c) for i, c in enumerate(colors)]
    base = nodes[S]
    for edge in edges:
        nodes[edge[0]].neighbours.add(edge[1])
        nodes[edge[1]].neighbours.add(edge[0])
    graph = Graph(nodes, base)
    return(graph)
    
def find_triangles(edges, graph):
    triangles = set()
    for n1, n2 in edges:
        n1neighbours = graph.nodes[n1].neighbours
        n2neighbours = graph.nodes[n2].neighbours
        for x in n1neighbours:
            if x in n2neighbours:
                triangles.add(frozenset([n1, n2, x]))
    return(triangles)

def add_distances(tri, dist):
    distances = []
    for t in tri:
        distances.append(min([dist[i] for i in t]))
    return(distances)
    

def find_chromatic(tri, colors, d):            
    cnt = [0]*(max(d)+1)
    clrs = []
    for t in tri:
        clrs.append([colors[i] for i in t])
    for i, c in enumerate(clrs):
        if c[0]!=c[1] and c[1]!=c[2] and c[2]!=c[0]:
           cnt[d[i]]+=1 
    return(cnt, clrs)
        
def bfs(g):
    visited = [False]*g.size
    q = deque()
    dist = [999999999999999]*g.size
    q.append(g.base)
    visited[g.base.num] = True
    dist[g.base.num] = 0
    while q:
        node = q.popleft()
        for nbr in node.neighbours:
            if not(visited[g.nodes[nbr].num]):
                q.append(G.nodes[nbr])
                visited[nbr]=True
                dist[nbr] = dist[node.num]+1
    return(dist)
            
name = "datapub5/pub10.in"
N, E, C, S, colors, edges = read_in(name)
G = make_graph(colors, edges, S)
dist = bfs(G)
tri = find_triangles(edges, G)
distances = add_distances(tri, dist)

cnt, clrs = find_chromatic(tri, colors, distances)

for i, x in enumerate(cnt):
    if x!=0:
        print(i, x)