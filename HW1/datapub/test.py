def field_quality(i, j, k, data, old_Q): # (i, j) = coordinates of upper left corner, k = size
	Q   = old_Q
	col = [x[j+k-1] for x in data[i:i+k-1]]
	row = data[i+k-1][j:(j+k)]
	Q   = Q + sum(col) + sum(row) 
	return(Q)

def field_quality2(i, j, k, data): # (i, j) = coordinates of upper left corner, k = size
	Q = 0
	for r in range(i, i+k):
		Q = Q + sum(data[r][j:(j+k)])
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
					oldQ = qualities[i, j, k]
			if i <  j:
				for k in range(1, N-j+1):
					qualities[i, j, k] = field_quality(i, j, k, data, oldQ)
					oldQ = qualities[i, j, k]
	return(qualities)

def all_qualities2(N, data):
	qualities = {}
	for i in range(0, N):
		for j in range(0, N):
			oldQ = 0
			if i >= j:
				for k in range(1, N-i+1):
					qualities[i, j, k] = field_quality2(i, j, k, data)
					oldQ = qualities[i, j, k]
			if i <  j:
				for k in range(1, N-j+1):
					qualities[i, j, k] = field_quality2(i, j, k, data)
					oldQ = qualities[i, j, k]
	return(qualities)

def import_data(name):
	f   = open(name, 'r')
	txt = f.readlines()
	N   = int(txt[0])
	
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

N, Qmin, Qmax, data = import_data("pub01.in")

