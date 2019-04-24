# -*- coding: utf-8 -*-
"""
Created on Sat May 12 12:06:55 2018

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
    dist = [None]*g.size
    q = deque()
    q.append(g.nodes[start])
    visited[g.nodes[start].num] = True
    dist[g.nodes[start].num] = 0
    while q:
        node = q.popleft()
        for nbr in node.neighbours:
            if not(visited[g.nodes[nbr].num]):
                q.append(G.nodes[nbr])
                visited[nbr]=True
                dist[nbr] = dist[node.num]+1
    return(dist)
    
def distances_dict(g, start):
    visited = [False]*g.size
    dist = {}
    q = deque()
    q.append(g.nodes[start])
    visited[g.nodes[start].num] = True
    dist[g.nodes[start].num] = 0
    while q:
        node = q.popleft()
        for nbr in node.neighbours:
            if not(visited[g.nodes[nbr].num]):
                q.append(G.nodes[nbr])
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
        for edge1 in edges:
            for edge2 in edges:
                e_dist.append(edge_distance(edge1, edge2, node_dist))
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

name = "datapub/pub01.in"
N, E, C, colors, edges = read_in(name)
G = make_graph(colors, edges)
node_dist = node_distances(G)
edgetypes = edge_types(edges, colors)
diams = diameters(edgetypes, node_dist)
jprint(diams)