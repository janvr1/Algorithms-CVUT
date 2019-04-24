# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:51:32 2018

@author: janvr
"""


def rec(cnt=[]):
	if len(cnt) == 10: return
	cnt = cnt[:]+[1]
	rec(cnt)
	print(cnt)
	
rec()