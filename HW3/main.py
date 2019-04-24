# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:45:31 2018

@author: janvr
"""
import sys

class Node():
    def __init__(self, color):
        self.left   = None
        self.right  = None
        self.color  = color
        self.parent = None
        self.b      = 0
        self.bb     = 0
        self.w      = 0
        self.ww     = 0

def read_in():
    nodes = []
    N = int(sys.stdin.readline())
    colors = sys.stdin.readline().split()

    for color in colors:
        nodes.append(Node(int(color)))
        
    for i in range(1, N):
        linex = sys.stdin.readline().split()
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

    while node:
        if not last or last.left == node or last.right == node:
            if node.left:
                nxt = node.left
            elif node.right:
                nxt = node.right
            else:
                fun(node)
                nxt = node.parent
        elif node.left == last:
            if node.right:
                nxt = node.right
            else:
                fun(node)
                nxt = node.parent
        else:
            fun(node)
            nxt = node.parent
            
        last = node
        node = nxt
            
def blackandwhite(node):
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

    global out
    if node.bb > 0 and node.b > 0 and node.w > 0 and node.ww > 0:
        if node.w/node.b >  node.ww/node.bb: out[0] += 1
        if node.w/node.b == node.ww/node.bb: out[1] += 1
        if node.w/node.b <  node.ww/node.bb: out[2] += 1

out = [0, 0, 0]
N, nodes = read_in()
postorder(nodes[0], blackandwhite)
print(out[0], out[1], out[2])
