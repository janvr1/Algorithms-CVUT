import time
import sys

start = time.time()

class Node():
	def __init__(self, key, num, C):
		self.left   = None
		self.right  = None
		self.parent = None
		self.num    = num
		self.full   = [0]*C
		self.key    = key

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
	
def make_nodes(colors):
	nodes = []
	for i in range(0, len(colors)):
		nodes.append(Node(colors[i], i, C))
	return(nodes)
	
def make_edges(nodes, connections):
	for p, c in connections:
		nodes[c].parent = nodes[p]
		if nodes[p].left == None:
			nodes[p].left = nodes[c]
		elif nodes[p].right == None:
			nodes[p].right = nodes[c]

def fullnodes(node):
	count = [0]*C
	if node.left:
		count2 = fullnodes(node.left)
		count = [count[i] + count2[i]  for i in range(C)]
	if node.right:
		count2 = fullnodes(node.right)
		count = [count[i] + count2[i] for i in range(C)]		
	count[node.key] += 1
	for i in range(C):
		if count[i] == D:
			node.full[i] = 1
	return(count)
	
def countpaths(node, fullness, pths=0):
	
	fullness = [fullness[i] + node.full[i]  for i in range(C)]
	
	if node.left:  pths = countpaths(node.left, fullness, pths)
	if node.right: pths = countpaths(node.right, fullness, pths)
	if node.left == None and node.right == None:
		if all(fullness) > 0:
			pths+=1
	return(pths)
	

fname = "pub10.in"
start1 = time.time()
N, C, D, colors, connections = read_in(fname)   #text file input
#N, C, D, colors, connections = sys_read_in()    #console input
print("Input took:", time.time()-start1)
start2 = time.time()
nodes = make_nodes(colors)
make_edges(nodes, connections)
print("Making a tree took:", time.time()-start2)
start3 = time.time()
fullnodes(nodes[0])
print("fullnodes took:", time.time()-start3)
fullness = [0]*C
start4  = time.time()
pths = countpaths(nodes[0], fullness)
print("countpaths took:", time.time()-start4)
print("Paths:", pths)
print("Total time:", time.time()-start)

out = open(fname[0:6]+ "out", "r")
output = int(out.readline())
if output == pths:
	print("Correct")
else:
	print("Wrong")
