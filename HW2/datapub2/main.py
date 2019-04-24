import sys

class Node():
	def __init__(self, key, full):
		self.left   = None
		self.right  = None
		self.full   = full
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
	return(C, D, colors, connections)
	
def make_tree(colors, connections, C):
	nodes = []
	full  = [0]*C
	for color in colors:
		nodes.append(Node(color, full[:]))
	for p, c in connections:
		if nodes[p].left == None: nodes[p].left = nodes[c]
		else: nodes[p].right = nodes[c]
	return(nodes)

def fullnodes(node, C, D):
	count = [0]*C
	if node.left:
		count = fullnodes(node.left, C, D)
	if node.right:
		count2 = fullnodes(node.right, C, D)
		count = [count[i] + x for i,x in enumerate(count2)]
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

C, D, colors, connections = sys_read_in()
nodes = make_tree(colors, connections, C)
startnode = nodes[0]
fullnodes(startnode, C, D)
fullness = [0]*C
paths = countpaths(startnode, fullness)
print(paths)