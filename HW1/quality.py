import random as rnd
import timeit as tmt


def construct(N):
	x = []
	for i in range(0, N):  #construct data
		row = []
		for j in range(0, N):
			row.append(rnd.randint(-10, 10))
		
		x.append(row)
	return(x)

N = 200
#data = [[-4, -1, 9, 3, -7, -9], [10, -5, 3, -4, -4, -9], [5, 3, 7, 9, 0, 7], [5, 10, -9, 7, 2, 9], [-9, -9, -10, -2, -5, -8], [-1, 1, -9, -9, 4, -6]]

#N = int(input("Enter size: "))
data = construct(N)

def field_quality_slow(i, j, k): # (i, j) = coordinates of upper left corner, k = size
	Q = 0
	for r in range(i, i+k):
		for c in range(j, j+k):
			Q = Q + data[r][c]
	return(Q)

def field_quality(i, j, k): # (i, j) = coordinates of upper left corner, k = size
	Q = 0
	for r in range(i, i+k):
		Q = Q + sum(data[r][j:(j+k)])
	return(Q)
	
def make_array():
	qualities = []
	for i in range(0, N):
		zy_axis = []
		for j in range(0, N):
			z_axis = []
			if i >= j:
				for k in range(1, N-i+1):
					z_axis.append([i, j, k])
			if i < j:
				for k in range(1, N-j+1):
					z_axis.append([i, j, k])
			zy_axis.append(z_axis)
		qualities.append(zy_axis)
	return(qualities)

def all_qualities():
	qualities = make_array()
	for i in range(0, N):
		for j in range(0, N):
			if i >= j:
				for k in range(1, N-i+1):
					qualities[i][j][k-1] = field_quality(i, j, k)
			if i <  j:
				for k in range(1, N-j+1):
					qualities[i][j][k-1] = field_quality(i, j, k)
	return(qualities)

def all_qualities2():
	qualities2 = []
	for i in range(0, N):
		for j in range(0, N):
			if i >= j:
				for k in range(1, N-i+1):
					qualities2.append(field_quality(i, j, k))
			if i < j:
				for k in range(1, N-j+1):
					qualities2.append(field_quality(i, j, k))
	return(qualities2)

#print(tmt.repeat("all_qualities()", "from __main__ import data, field_quality, make_array, all_qualities", repeat=1, number=1))
#print(len(all_qualities2()))

qualities = all_qualities()

def find(minQ, maxQ):
	cnt     = 0
	bestQ1  = minQ
	bestQ2  = maxQ
	min_dif = abs(bestQ1 - bestQ2)

	for i in range(0, N):
		for j in range(0, N):
			if i >= j:
				for k in range(1, N-i+1):
					Q1 = qualities[i][j][k-1]
					
					if minQ < Q1 < maxQ:
						for l in range(0, N):
							for m in range(0, N):
								if ((l<i or l>=i+k) or (m<j or m>=j+k)):
									if l >= m:
										for n in range(1, N-l+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):
												Q2 = qualities[l][m][n-1]
												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)
													cnt = cnt + 1
													if dif < min_dif:
														min_dif = dif
														bestQ1 = Q1
														bestQ2 = Q2
														if min_dif == 0:
															return(bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt)

									if l < m:
										for n in range(1, N-m+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):
												Q2 = qualities[l][m][n-1]
												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)
													cnt = cnt + 1
													if dif < min_dif:
														min_dif = dif
														bestQ1 = Q1
														bestQ2 = Q2
														if min_dif == 0:
															return(bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt)
			
			if i < j:
				for k in range(1, N-j+1):
					Q1 = qualities[i][j][k-1]

					if minQ < Q1 < maxQ:	
						for l in range(0, N):
							for m in range(0, N):
								if ((l<i or l>=i+k) or (m<j or m>=j+k)):
									if l >= m:
										for n in range(1, N-l+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):
												Q2 = qualities[l][m][n-1]
												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)
													cnt = cnt + 1
													if dif < min_dif:
														min_dif = dif
														bestQ1 = Q1
														bestQ2 = Q2
														if min_dif == 0:
															return(bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt)
									if l < m:
										for n in range(1, N-m+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):	
												Q2 = qualities[l][m][n-1]
												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)
													cnt = cnt + 1
													if dif < min_dif:
														min_dif = dif
														bestQ1 = Q1
														bestQ2 = Q2
														if min_dif == 0:
															return(bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt)
	return(bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt)

bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt = find(10, 25)

#print("Data:")
#for z in range(0, N):
#	print(data[z][:])

print("\nQ1: ", bestQ1, "\nQ2: ", bestQ2, "\ndiff: ", min_dif, "\nQ1 coor: ", (i, j, k), "\nQ2 coor: ", (l, m, n), "\ncnt: ", cnt)
#	
#print("\nField 1:")
#for x in range(i, i+k):
#	print(data[x][j:j+k])
#	
#print("\nField 2:")
#for y in range(l, l+n):
#   print(data[y][m:m+n])

#print(tmt.repeat("all_qualities()", "from __main__ import data, field_quality, make_array, all_qualities", repeat=1, number=1))
#print(tmt.repeat("find(10, 25)", "from __main__ import data, field_quality, make_array, all_qualities, find", repeat=1, number=1))