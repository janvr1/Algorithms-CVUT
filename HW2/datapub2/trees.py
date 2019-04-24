import time
import sys

start = time.time()

class Node():
	def __init__(self, key, num):
		self.left   = None
		self.right  = None
		self.parent = None
		self.num    = num
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
		nodes.append(Node(colors[i], i))
	return(nodes)
	
def make_edges(nodes, connections):
	for p, c in connections:
		nodes[c].parent = nodes[p]
		if nodes[p].left == None:
			nodes[p].left = nodes[c]
		elif nodes[p].right == None:
			nodes[p].right = nodes[c]

def fullnodes(C):
	fll = []
	for i in range(C):
		fll.append([])
	return(fll)

def search(node, path = [], pathlist = []):
	count = [0]*C	
	path.append(node.num)
	
	if node.left:
		count2, pathlist = search (node.left)
		count = [count[i] + count2[i]  for i in range(C)]
	if node.right:
		count2, pathlist = search(node.right)
		count = [count[i] + count2[i] for i in range(C)]
	if node.left == None and node.right == None:	
		pathlist.append(set(path))
		
	count[node.key] += 1
	for i in range(C):
		if count[i] == D:
			fllnodes[i].append(node.num)
	
	path.remove(node.num)
	
	return(count, pathlist)
	
def howmany(fllnodes, pathlist):
	cnt = 0
	for path in pathlist:
		i = 0
		fullness = [False]*C
		for color in fllnodes:
			for node in color:
				if node in path:
					fullness[i] = True
					break
			if fullness[i] == False:
				break
			i+=1
			
		if all(fullness) == True:
				cnt += 1
	return(cnt)
	
	
def InOrder2(node):
	if node == None:
		return
	InOrder2(node.left)
	print(node.key, end = " ")
	InOrder2(node.right)

def PostOrder2(node):
	if node.left: PostOrder2(node.left)
	if node.right: PostOrder2(node.right)
	#print(node.key, end = " ")
	
def PreOrder2(node):
	if node == None:
		return
	print(node.key, end = " ")
	PreOrder2(node.left)
	PreOrder2(node.right)	




fname = "pub09.in"
N, C, D, colors, connections = read_in(fname)   #text file input
#N, C, D, colors, connections = sys_read_in()    #console input
nodes = make_nodes(colors)
make_edges(nodes, connections)
fllnodes = fullnodes(C)
start2 = time.time()
useless_variable, pathlist = search(nodes[0])
print("Search took:", time.time()-start2)
start3 = time.time()
cnt = howmany(fllnodes, pathlist)
print("Howmany took:", time.time()-start3)
print(fname)
print(cnt)
print("Time taken: ", time.time()-start)


