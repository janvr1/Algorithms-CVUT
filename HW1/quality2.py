import random as rnd
#import timeit as tmt
import time   as time

start = time.time()

def construct(N):
	x = []
	for i in range(0, N):  #construct data
		row = []
		for j in range(0, N):
			row.append(rnd.randint(-9, 9))
		
		x.append(row)
	return(x)

N = 200
#data = [[-4, -1, 9, 3, -7, -9], [10, -5, 3, -4, -4, -9], [5, 3, 7, 9, 0, 7], [5, 10, -9, 7, 2, 9], [-9, -9, -10, -2, -5, -8], [-1, 1, -9, -9, 4, -6]]

#N = int(input("Enter size: "))
data = construct(N)

def import_data():
	f = open("data.txt", 'r')
	Ns = f.read(1)
	Ni  = int(Ns)
	txt = f.readlines()
	
	x = []
	for i in range(1, Ni+1):
		x.append(txt[i].split())
	
	dat = []
	for j in range(0, Ni):
		y = []
		for k in x[j][0:Ni]:
			y.append(int(k))
		dat.append(y)
	return(Ni, dat)

#N, data = import_data()

def field_quality(i, j, k): # (i, j) = coordinates of upper left corner, k = size
	Q = 0
	for r in range(i, i+k):
		Q = Q + sum(data[r][j:(j+k)])
	return(Q)

def find(minQ, maxQ):
	cnt     = 0
	cnt1    = 0
	cnt2 	= 0
	bestQ1  = minQ
	bestQ2  = maxQ
	min_dif = abs(bestQ1 - bestQ2)
	success = False

	for i in range(0, N):
		for j in range(0, N):
			if i >= j:
				for k in range(1, N-i+1):
					Q1 = field_quality(i, j, k)
					cnt1 =  cnt1 + 1
					
					if minQ < Q1 < maxQ:
						for l in range(0, N):
							for m in range(0, N):
								if ((l<i or l>=i+k) or (m<j or m>=j+k)):
									if l >= m:
										for n in range(1, N-l+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):
												Q2 = field_quality(l, m, n)
												cnt2 = cnt2 + 1
												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)
													cnt = cnt + 1
													if dif < min_dif:
														min_dif = dif
														bestQ1 = Q1
														bestQ2 = Q2
														I, J, K, L, M, N2 = i, j, k, l, m, n
														success = True
														if min_dif == 0:
															print("\n***********************Solution found***********************")
															return(bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt, cnt1, cnt2)

									if l < m:
										for n in range(1, N-m+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):
												Q2 = field_quality(l, m, n)
												cnt2 = cnt2 + 1
												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)
													cnt = cnt + 1
													if dif < min_dif:
														min_dif = dif
														bestQ1 = Q1
														bestQ2 = Q2
														I, J, K, L, M, N2 = i, j, k, l, m, n
														success = True
														if min_dif == 0:
															print("\n***********************Solution found***********************")
															return(bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt, cnt1, cnt2)
			
			if i < j:
				for k in range(1, N-j+1):
					Q1 = field_quality(i, j, k)
					cnt1 = cnt1 + 1

					if minQ < Q1 < maxQ:	
						for l in range(0, N):
							for m in range(0, N):
								if ((l<i or l>=i+k) or (m<j or m>=j+k)):
									if l >= m:
										for n in range(1, N-l+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):
												Q2 = field_quality(l, m, n)
												cnt2 = cnt2 + 1
												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)
													cnt = cnt + 1
													if dif < min_dif:
														min_dif = dif
														bestQ1 = Q1
														bestQ2 = Q2
														I, J, K, L, M, N2 = i, j, k, l, m, n
														success = True
														if min_dif == 0:
															print("\n***********************Solution found***********************")
															return(bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt, cnt1, cnt2)
									if l < m:
										for n in range(1, N-m+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):	
												Q2 = field_quality(l, m, n)
												cnt2 = cnt2 + 1
												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)
													cnt = cnt + 1
													if dif < min_dif:
														min_dif = dif
														bestQ1 = Q1
														bestQ2 = Q2
														I, J, K, L, M, N2 = i, j, k, l, m, n
														success = True
														if min_dif == 0:
															print("\n***********************Solution found***********************")
															return(bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt, cnt1, cnt2)
	if success == True:
		print("\n***********************Solution found***********************")
		return(bestQ1, bestQ2, min_dif, I, J, K, L, M, N2, cnt, cnt1, cnt2)
	else:
		print("\n***********************Solution not found***********************")
		return(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

range1 = 10
range2 = 25

bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt, cnt1, cnt2 = find(range1, range2)

print("\nData:")
for z in range(0, N):
	print(data[z][:])

print("\nSize: ", N, "\nRange: ", range1, "-", range2, "\nQ1: ", bestQ1, "\nQ2: ", bestQ2, "\ndiff: ", min_dif,
	  "\nQ1 coor: ", (i, j, k), "\nQ2 coor: ", (l, m, n), "\ncnt: ", cnt, cnt1, cnt2)

print("\nField 1:")
for x in range(i, i+k):
	print(data[x][j:j+k])
	
print("\nField 2:")
for y in range(l, l+n):
   print(data[y][m:m+n])

end = time.time()
print("Time taken: ", (end - start))

#print(tmt.repeat("all_qualities()", "from __main__ import data, field_quality, make_array, all_qualities", repeat=1, number=1))
#print(tmt.repeat("find(10, 25)", "from __main__ import data, field_quality, make_array, all_qualities, find", repeat=1, number=1))