# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 14:14:40 2018

@author: janvr
"""

def num_leaves(node):
	lfs = 0
	if node.left: lfs += num_leaves(node.left)
	if node.right: lfs += num_leaves(node.right)
	if node.left == None and node.right == None:	lfs += 1
	return(lfs)
	
	
def howmany(fllnodes, pathlist):
	fullness = []
	for j in range(C):
		fullness.append(False)
	
	cnt = 0
	for path in pathlist:
		for i in range(len(fllnodes)):
			for node in fllnodes[i]:
				if node in path:
					fullness[i] = True
					break
				else:
					fullness[i] = False
			if fullness[i] == False:
				break
			
			#if all(fullness) == True:
			#	break
		if all(fullness) == True:
				cnt += 1
	print(cnt)
	return(cnt)

def search(node, C, D):
	count = [0]*C	
	if node.left:
		count2 = search (node.left, C , D)
		count = [count[i] + count2[i]  for i in range(C)]
	if node.right:
		count2 = search(node.right, C, D)
		count = [count[i] + count2[i] for i in range(C)]
		
	count[node.key] += 1
	for i in range(C):
		if count[i] == D:
			fllnodes[i].append(node.num)
	
	return(count)
	
def paths(node, path = [], pathlist = []):
	path.append(node.num)
	if node.left: pathlist = paths(node.left, path, pathlist)
	if node.right: pathlist = paths(node.right, path, pathlist)
	if node.left == None and node.right == None:	
		pathlist.append(set(path))
	path.remove(node.num)
	return(pathlist)