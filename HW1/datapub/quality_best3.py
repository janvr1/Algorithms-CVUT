import time as time

def start_timer():
	start = time.time()
	return(start)

def input_num(num):
	file_num = num #input("Enter number: ")
	file =  "pub" + file_num + ".in"
	return (file, file_num)

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

def field_quality(i, j, k, data, old_Q): # (i, j) = coordinates of upper left corner, k = size
	Q   = old_Q
	col = [x[j+k-1] for x in data[i:i+k-1]]
	row = data[i+k-1][j:(j+k)]
	Q   = Q + sum(col) + sum(row) 
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

def reduce(minQ, maxQ, N, qualities):
	vec = []
	for i in range(0, N):
		for j in range(0, N):
			if i >= j:
				for k in range(1, N-i+1):
					Q = qualities[i, j, k]
					if minQ <= Q <= maxQ:
						vec.append([i, j, k])
					else:
						del qualities[i, j, k]
			if i < j:
				for k in range(1, N-j+1):
					Q = qualities[i, j, k] 
					if minQ <= Q <= maxQ:
						vec.append([i, j, k])
					else:
						del qualities[i, j, k]
	vec_sorted = sorted(qualities, key = qualities.get, reverse = True)
	return(vec_sorted, qualities)

def find(vec, Qmin, Qmax, qualities):
	bestQ1  = Qmin
	bestQ2  = Qmax
	min_dif = abs(bestQ1 - bestQ2)
	cnt = 0

	for x in range(0, len(vec)-1):
		i, j, k = vec[x]
		Q1 = qualities[i, j, k]
		for y in range(x+1, len(vec)):
			l, m, n = vec[y]
			cnt = cnt+1
			if ((l<i or l>=i+k) or (m<j or m>=j+k)):
				if ((l+n<=i or l>=i+k) or (m+n<=j or m>=j+k)):
					Q2 = qualities[l, m, n]
					dif = abs(Q1-Q2)
					if dif < min_dif:
						min_dif = dif
						bestQ1 = Q1
						bestQ2 = Q2
					break

	if bestQ1 > bestQ2:
		bestQ1, bestQ2 = bestQ2, bestQ1
	print(cnt)
	return(bestQ1, bestQ2)

def check_out(bestQ1, bestQ2, file):
	out = open(file[0:6]+"out", "r")
	result = out.readline()
	out.close()
	out_str = str(bestQ1) + " " + str(bestQ2) + "\n"

	if result == out_str:
		print("Correct")
	else:
		print("Wrong")

def write_out(file_num, bestQ1, bestQ2):
	out_str = str(bestQ1) + " " + str(bestQ2) + "\n"
	output = open("out" + file_num + ".jan", "w")
	output.write(out_str)
	output.close()

def end_timer(start):
	end = time.time()
	print("Time taken: ", end-start)

def doIt(num):	
	start = start_timer()
	file, file_num = input_num(num)
	N, Qmin, Qmax, data = import_data(file)
	qualities = all_qualities(N, data)
	vec, qualities = reduce(Qmin, Qmax, N, qualities)
	bestQ1, bestQ2 = find(vec, Qmin, Qmax, qualities)
	print(bestQ1, bestQ2)
	check_out(bestQ1, bestQ2, file)
	write_out(file_num, bestQ1, bestQ2)
	end_timer(start)
	return(qualities, data)