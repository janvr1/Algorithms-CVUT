# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:31:19 2018

@author: janvr
"""

import time
import sys

start = time.time()

class Node():
	def __init__(self, key, C):
		self.left   = None
		self.right  = None
		self.full   = [0]*C
		self.key    = key

def check_out(fname, paths):
	out = open(fname[0:6]+ "out", "r")
	output = int(out.readline())
	if output == paths: print("Correct")
	else: print("Wrong")

def sys_read_in():
	line1_str = sys.stdin.readline()
	N, C, D = line1_str.split()
	N = int(N)
	C = int(C)
	D = int(D)
	line2_str = sys.stdin.readline()
	colors_str = line2_str.split()
	colors = [int(x) for x in colors_str]
	connections = []
	for i in range(1, N):
		linex = sys.stdin.readline()
		a, b = [int(y) for y in linex.split()]
		connections.append([a, b])
	return(N, C, D, colors, connections)

def read_in(fname):
	file = open(fname)
	line1_str = file.readline()
	N, C, D = line1_str.split()
	N = int(N)
	C = int(C)
	D = int(D)
	line2_str = file.readline()
	colors_str = line2_str.split()
	colors = [int(x) for x in colors_str]
	connections = []
	for i in range(1, N):
		linex = file.readline()
		a, b = [int(y) for y in linex.split()]
		connections.append([a, b])
	return(N, C, D, colors, connections)
	
def make_tree(colors, connection):
	nodes = []
	for i in range(len(colors)):
		nodes.append(Node(colors[i], C))
	
	for p, c in connections:
		if nodes[p].left == None:
			nodes[p].left = nodes[c]
		else:
			nodes[p].right = nodes[c]
	return(nodes)

def fullnodes(node):
	count = [0]*C
	
	if node.left:
		count2 = fullnodes(node.left)
		count = [count[i] + count2[i]  for i in range(C)]
	
	if node.right:
		count2 = fullnodes(node.right)
		count = [count[i] + count2[i] for i in range(C)]		
	
	count[node.key] += 1
	
	for i, x in enumerate(count):
		if x == D: node.full[i] = 1
	
	return(count)
	
def countpaths(node, fullness, pths = 0):
	
	fullness = [fullness[i] + x  for i, x in enumerate(node.full)]

	if node.left:  pths = countpaths(node.left,  fullness, pths)
	if node.right: pths = countpaths(node.right, fullness, pths)
	if node.left == None and node.right == None:
		if all(fullness) > 0: pths+=1
	
	return(pths)

fname = "pub09.in"
start1 = time.time()
N, C, D, colors, connections = read_in(fname)   #text file input
#N, C, D, colors, connections = sys_read_in()    #console input
print("Input took:", time.time()-start1)
start2 = time.time()
nodes = make_tree(colors, connections)
print("Making a tree took:", time.time()-start2)
start3 = time.time()
startnode = nodes[0]
fullnodes(startnode)
print("fullnodes took:", time.time()-start3)
start4  = time.time()
fullness = [0]*C
paths = countpaths(startnode, fullness)
print("countpaths took:", time.time()-start4)
print("Paths:", paths)
print("Total time:", time.time()-start)
check_out(fname, paths)


