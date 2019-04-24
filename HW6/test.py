# -*- coding: utf-8 -*-
"""
Created on Thu May 10 20:32:29 2018

@author: janvr
"""
import networkx as nx

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
        edges.append(tuple([int(x) for x in line.split()]))
    return(N, E, C, colors, edges)
    
def make_graph(colors, edges):
    nodes = [Node(i, c) for i, c in enumerate(colors)]
    for edge in edges:
        nodes[edge[0]].neighbours.add(edge[1])
        nodes[edge[1]].neighbours.add(edge[0])
    graph = Graph(nodes)
    return(graph) 
        
def distances(g, start):
    visited = [False]*g.size
    q = Queue(g.size)
    dist = [999999999999999]*g.size
    q.enqueue(g.nodes[start])
    visited[g.nodes[start].num] = True
    dist[g.nodes[start].num] = 0
    while not(q.isempty()):
        node = q.dequeue()
        #print(node.num, end=" ")
        for nbr in node.neighbours:
            if not(visited[g.nodes[nbr].num]):
                q.enqueue(G.nodes[nbr])
                visited[nbr]=True
                dist[nbr] = dist[node.num]+1
    return(dist)
    
def node_distances(g):
    all_dist=dict()
    for i in range(g.size):
        all_dist[i]=distances(g, i)
    return(all_dist)
    
def edge_distance(edge1, edge2, n_dist):
    dst = []
    for i in edge1:
        for j in edge2:
            dst.append(n_dist[i][j])
    dist = min(dst)
    return(dist)
        
        
def edge_types(edges, colors):
    edgetypes = [tuple(sorted([colors[i], colors[j]])) for i, j in edges]    
    types = dict()
    for x in edgetypes:
        types[x] = []
    for i, x in enumerate(edges):
        types[edgetypes[i]].append(x)
    return(types)
    
def diameters(types, node_dist):
    diams = dict.fromkeys(types.keys())
    for x in diams:
        edges = types[x]
        e_dist = []
        for i, edge1 in enumerate(edges):
            for edge2 in edges[i:]:
                d = edge_distance(edge1, edge2, node_dist)
                e_dist.append(d)
                if d == 9 and x==(8,8): print(edge1, edge2)
        diameter = max(e_dist)
        diams[x]=diameter
    return(diams)
    
def jprint(diams):
    y = sorted(list(diams.keys()))
    for x in y:
        if diams[x]!=0: 
            a, b = x
            c = diams[x]
            print(a, b, c)
            


name = "datapub/pub05.in"
N, E, C, colors, edges = read_in(name)
G = make_graph(colors, edges)
dist = distances(G, 0)
node_dist = node_distances(G)
edgetypes = edge_types(edges, colors)
diams = diameters(edgetypes, node_dist)
jprint(diams)


X = nx.Graph()
X.add_edges_from(edges)

nxdist = sorted(list(nx.shortest_path_length(X)))
nx.draw_networkx(X)