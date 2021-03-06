import time as time

def import_data(name):
	f = open(name, 'r')
	txt = f.readlines()
	N = int(txt[0])
	
	x = []
	for i in range(1, N+1):
		x.append(txt[i].split())
	
	dat = []
	for j in range(0, N):
		y = []
		for k in x[j][0:N]:
			y.append(int(k))
		dat.append(y)

	minmax_str = []
	minmax_str.append(txt[N+1].split())
	minmax = []
	for k in range(0, 2):
		minmax.append(int(minmax_str[0][k]))
	min, max = minmax


	return(N, min, max, dat)

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

def find(minQ, maxQ):
	bestQ1  = minQ
	bestQ2  = maxQ
	min_dif = abs(bestQ1 - bestQ2)
	sum     = 2 * minQ-1
	#qualities = all_qualities()

	for i in range(0, N):
		for j in range(0, N):
			if i >= j:
				for k in range(1, N-i+1):
					Q1 = field_quality(i, j, k)
					
					if minQ <= Q1 <= maxQ:
						for l in range(0, N):
							for m in range(0, N):
								if ((l<i or l>=i+k) or (m<j or m>=j+k)):
									if l >= m:
										for n in range(1, N-l+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):
												Q2 = field_quality(l, m, n)

												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)

													if dif < min_dif:
														sum = Q1 + Q2
														min_dif = dif
														bestQ1 = Q1
														bestQ2 = Q2

													if dif == min_dif:
														if (Q1+Q2) > sum:
															sum = Q1 + Q2
															min_dif = dif
															bestQ1 = Q1
															bestQ2 = Q2

												


									if l < m:
										for n in range(1, N-m+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):
												Q2 = field_quality(l, m, n)

												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)

													if dif < min_dif:
														sum = Q1 + Q2
														min_dif = dif
														bestQ1 = Q1
														bestQ2 = Q2

													if dif == min_dif:
														if (Q1+Q2) > sum:
															sum = Q1 + Q2
															min_dif = dif
															bestQ1 = Q1
															bestQ2 = Q2
			if i < j:
				for k in range(1, N-j+1):
					Q1 = field_quality(i, j, k)

					if minQ <= Q1 <= maxQ:	
						for l in range(0, N):
							for m in range(0, N):
								if ((l<i or l>=i+k) or (m<j or m>=j+k)):
									if l >= m:
										for n in range(1, N-l+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):
												Q2 = field_quality(l, m, n)
												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)

													if dif < min_dif:
														sum = Q1 + Q2
														min_dif = dif
														bestQ1 = Q1
														bestQ2 = Q2
													if dif == min_dif:
														if (Q1+Q2) > sum:
															sum = Q1 + Q2
															min_dif = dif
															bestQ1 = Q1
															bestQ2 = Q2

									if l < m:
										for n in range(1, N-m+1):
											if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):	
												Q2 = field_quality(l, m, n)
												if minQ <= Q2 <= maxQ:
													dif = abs(Q1-Q2)
													if dif < min_dif:
														sum = Q1 + Q2
														min_dif = dif
														bestQ1  = Q1
														bestQ2  = Q2

													if dif == min_dif:
														if (Q1+Q2) > sum:
															sum = Q1 + Q2
															min_dif = dif
															bestQ1  = Q1
															bestQ2  = Q2
	return(bestQ1, bestQ2)

file = input("Enter name: ")

start = time.time()

N, Qmin, Qmax, data = import_data(file)
bestQ1, bestQ2 = find(Qmin, Qmax)
print(bestQ1, bestQ2)

end = time.time()
print("Time taken: ", end - start)

string = str(bestQ1) + str(bestQ2)
output = open("output.txt", "w")
output.write(string)
output.close()