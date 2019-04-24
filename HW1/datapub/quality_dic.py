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


def field_quality(old_Q, old_i, old_j, old_k, i, j, k): # (i, j) = coordinates of upper left corner, k = size
	Q = old_Q
	col = [x[j+k-1] for x in data[i:i+k-1]]
	Q = Q + sum(col) + sum(data[i+k-1][j:(j+k)]) 
	return(Q)


def field_quality0(i, j):
	Q = data[i][j]
	return(Q)


def all_qualities():
	qualities = {}
	for i in range(0, N):
		for j in range(0, N):
			if i >= j:
				for k in range(1, N-i+1):
					if k == 1:
						qualities[i, j, k] = field_quality0(i, j)
						old_i = i
						old_j = j
						old_k = k
						old_Q = qualities[old_i, old_j, old_k]
					else:
						qualities[i, j, k] = field_quality(old_Q, old_i, old_j, old_k, i, j, k)
						old_i = i
						old_j = j
						old_k = k
						old_Q = qualities[old_i, old_j, old_k]

			if i <  j:
				for k in range(1, N-j+1):
					if k == 1:
						qualities[i, j, k] = field_quality0(i, j)
						old_i = i
						old_j = j
						old_k = k
						old_Q = qualities[old_i, old_j, old_k]
					else:
						qualities[i, j, k] = field_quality(old_Q, old_i, old_j, old_k, i, j, k)
						old_i = i
						old_j = j
						old_k = k
						old_Q = qualities[old_i, old_j, old_k]
	return(qualities)

def reduce(minQ, maxQ):
	vec = []
	for i in range(0, N):
		for j in range(0, N):
			if i >= j:
				for k in range(1, N-i+1):
					Q = qualities[i, j, k] 
					if minQ <= Q <= maxQ:
						vec.append([i, j, k])
					#else:
					#	del qualities[i, j, k]
			if i < j:
				for k in range(1, N-j+1):
					Q = qualities[i, j, k] 
					if minQ <= Q <= maxQ:
						vec.append([i, j, k])
					#else:
					#	del qualities[i, j, k]
	return(vec)

def find():
	bestQ1  = Qmin
	bestQ2  = Qmax
	min_dif = abs(bestQ1 - bestQ2)
	sum     = (2 * Qmin)-1
	x, y = 0, 0
	#qualities = all_qualities()
	#vec = reduce(minQ, maxQ)

	for i, j, k in vec:
		x = x + 1
		Q1 = qualities[i, j, k]
		for l, m, n in vec:
			y = y + 1 
			if ((l<i or l>=i+k) or (m<j or m>=j+k)):
				if ((l+n<i or l>=i+k) or (m+n<j or m>=j+k)):
					Q2 = qualities[l, m, n]
					dif = abs(Q1-Q2)
					if dif < min_dif:
						sum = Q1 + Q2
						min_dif = dif
						bestQ1 = Q1
						bestQ2 = Q2
					if dif == min_dif:
						Q12 = Q1+Q2
						if Q12 > sum:
							sum = Q12
							min_dif = dif
							bestQ1 = Q1
							bestQ2 = Q2

	if bestQ1 > bestQ2:
		bestQ1, bestQ2 = bestQ2, bestQ1
	print(x, y)
	return(bestQ1, bestQ2)

file = input("Enter name: ")

start = time.time()

N, Qmin, Qmax, data = import_data(file)
qualities = all_qualities()
vec = reduce(Qmin, Qmax)
print(len(vec))
bestQ1, bestQ2 = find()
print(bestQ1, bestQ2)

end = time.time()
print("Time taken: ", end-start)

out_str = str(bestQ1) + " " + str(bestQ2)
output = open("output.txt", "w")
output.write(out_str)
output.close()