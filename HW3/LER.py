# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:37:49 2018

@author: janvr
"""
class Node():
    def __init__(self, color, key):
        self.left   = None
        self.right  = None
        self.key    = key
        self.color  = color
        self.parent = None
        self.b      = 0
        self.bb     = 0
        self.w      = 0
        self.ww     = 0


def read_in(fname):
    file = open(fname)
    nodes = []
    N = int(file.readline())
    colors = file.readline().split()

    for i, color in enumerate(colors):
        nodes.append(Node(int(color), i))
        
    for i in range(1, N):
        linex = file.readline().split()
        a, b, c = [int(y) for y in linex]
        if c == 0: 
            nodes[a].left = nodes[b]
            nodes[b].parent = nodes[a]
        else:
            nodes[a].right = nodes[b]
            nodes[b].parent = nodes[a]
    return(N, nodes)


def postorder(node, fun):
    last = None
    node = node
    nxt = None
    out = [0, 0, 0]

    while node:
        if not last or last.left == node or last.right == node:
            if node.left:
                nxt = node.left
            elif node.right:
                nxt = node.right
            else:
                out = fun(node, out)
                nxt = node.parent
        elif node.left == last:
            if node.right:
                nxt = node.right
            else:
                out = fun(node, out)
                nxt = node.parent
        else:
            out = fun(node, out)
            nxt = node.parent
            
        last = node
        node = nxt
    
    return(out[0], out[1], out[2])
            
def blackandwhite(node, out):
    if node.parent:
        if node == node.parent.left:
            node.parent.w = node.w + node.ww
            node.parent.b = node.b + node.bb
            if node.color == 0: node.parent.w += 1
            if node.color == 1: node.parent.b += 1
        if node == node.parent.right:
            node.parent.ww = node.w + node.ww
            node.parent.bb = node.b + node.bb
            if node.color == 0: node.parent.ww += 1
            if node.color == 1: node.parent.bb += 1

    if node.bb > 0 and node.b > 0 and node.w > 0 and node.ww > 0:
        if node.w/node.b >  node.ww/node.bb: out[0] += 1
        if node.w/node.b == node.ww/node.bb: out[1] += 1
        if node.w/node.b <  node.ww/node.bb: out[2] += 1
    return(out)            
            
fname = "pub10.in"
N, nodes = read_in(fname)
L, E, R = postorder(nodes[0], blackandwhite)
print(L, E, R)



