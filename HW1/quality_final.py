

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

	minmax_str = txt[Ni+1]
	minmax = []
	for k in range(0, 2):
		minmax.append(txt[k])


	return(Ni, min, max, dat)

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

def find2(minQ, maxQ):
	cnt     = 0
	cnt1    = 0
	cnt2 	= 0
	bestQ1  = minQ
	bestQ2  = maxQ
	min_dif = abs(bestQ1 - bestQ2)
	success = False
	sum     = 0

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

#bestQ1, bestQ2, min_dif, i, j, k, l, m, n, cnt = find(10, 25)