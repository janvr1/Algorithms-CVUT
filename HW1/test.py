import random as rnd

def construct(N):
	x = []
	for i in range(0, N):  #construct data
		row = []
		for j in range(0, N):
			row.append(rnd.randint(-10, 10))
		
		x.append(row)
	return(x)

N = 120
data = construct(N)






def field_quality(i, j, k, data, old_Q): # (i, j) = coordinates of upper left corner, k = size
	Q   = old_Q
	col = [x[j+k-1] for x in data[i:i+k-1]]
	row = data[i+k-1][j:(j+k)]
	Q   = Q + sum(col) + sum(row) 
	return(Q)

def field_quality0(i, j, data):
	Q = data[i][j]
	return(Q)

def all_qualities(N, data):
	qualities = {}
	for i in range(0, N):
		for j in range(0, N):
			oldQ = 0
			if i >= j:
				for k in range(1, N-i+1):
					qualities[i, j, k] = field_quality(i, j, k, data, oldQ)
					old_Q = qualities[i, j, k]

			if i <  j:
				for k in range(1, N-j+1):
					if k > 1:
						qualities[i, j, k] = field_quality(i, j, k, data, oldQ)
						old_Q = qualities[i, j, k]
	return(qualities)


def field_quality2(i, j, k): # (i, j) = coordinates of upper left corner, k = size
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

def all_qualities2():
	qualities = make_array()
	for i in range(0, N):
		for j in range(0, N):
			if i >= j:
				for k in range(1, N-i+1):
					qualities[i][j][k-1] = field_quality2(i, j, k)
			if i <  j:
				for k in range(1, N-j+1):
					qualities[i][j][k-1] = field_quality2(i, j, k)
	return(qualities)