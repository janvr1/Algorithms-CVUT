import time as time
import sys

def start_timer():
	start = time.time()
	return(start)

def import_data(name):           #import data from text file to a list of lists
    # ------------- CONSOLE INPUT
	# f   = open(name, 'r')
    # txt = f.readlines()
    txt = [];
    line = sys.stdin.readline()
    txt.append( line )
    nn = int( txt[0] )
    for i in range(nn+1):
        line = sys.stdin.readline()
        txt.append(line)
    # ------END OF CONSOLE INPUT

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


def partial_sums(data, data_T):
	row_sums = []
	col_sums = []
	for x in data:
		row = [0] + [sum(x[:i+1]) for i in range(0, len(x))]
		row_sums.append(row)
	for y in data_T:
		col = [0] + [sum(y[:j+1]) for j in range(0, len(y))]
		col_sums.append(col)
	return(row_sums, col_sums)

def field_quality(i, j, k, rows, cols, old_Q): # (i, j) = coordinates of upper left corner, k = size
	Q   = old_Q + rows[i+k-1][j+k] - rows[i+k-1][j] + cols[j+k-1][i+k-1] - cols[j+k-1][i] 
	return(Q)


def all_qualities(N, rows, cols):             #calculate all possible qualities and store them in a dictionary. Keys = coordinates, values = qualities
	qualities = {}
	for i in range(0, N):
		for j in range(0, N):
			oldQ = 0
			if i >= j:
				for k in range(1, N-i+1):
					qualities[i, j, k] = field_quality(i, j, k, rows, cols, oldQ)
					oldQ = qualities[i, j, k]
			if i <  j:
				for k in range(1, N-j+1):
					qualities[i, j, k] = field_quality(i, j, k, rows, cols, oldQ)
					oldQ = qualities[i, j, k]
	return(qualities)

def reduce(minQ, maxQ, N, qualities):      #remove all qualities that are not within the prescribed range
	qualities2 = {}
	for i in range(0, N):
		for j in range(0, N):
			if i >= j:
				for k in range(1, N-i+1):
					Q = qualities[i, j, k]
					if minQ <= Q <= maxQ:
						qualities2[i, j, k] = qualities[i, j, k]
			if i < j:
				for k in range(1, N-j+1):
					Q = qualities[i, j, k] 
					if minQ <= Q <= maxQ:
						qualities2[i, j, k] = qualities[i, j, k]

	vec_sorted = sorted(qualities2, key = qualities.get, reverse = True)    #sort qualities from high to low, vec_sorted = a list with sorted dictionary keys
	return(vec_sorted, qualities2)

def find(vec, Qmin, Qmax, qualities):            #
	bestQ1  = Qmin
	bestQ2  = Qmax
	min_dif = abs(bestQ1 - bestQ2)

	for x in range(0, len(vec)-1):                 #start with the highest quality field (in 2nd round 2nd highest, in 3rd round 3rd highest and so on until
		i, j, k = vec[x]						   #the second lowest quality
		Q1 = qualities[i, j, k]
		for y in range(x+1, len(vec)):             #pick the second highest quality field and check if it overlaps with the first field. If it overlaps try
			l, m, n = vec[y]					   #the next highest one (3rd, 4th, ... until the lowest one). If it does not overlap calculate difference then break the loop)
			if ((l<i or l>=i+k) or (m<j or m>=j+k)):              #check for field overlapping
				if ((l+n<=i or l>=i+k) or (m+n<=j or m>=j+k)):
					Q2 = qualities[l, m, n]
					dif = abs(Q1-Q2)
					if dif < min_dif:               #if difference is small than current minimum, write the new values for best Q1 and Q2
						min_dif = dif
						bestQ1 = Q1
						bestQ2 = Q2
					break                           #break the inner loop everytime after finding the first non overlapping candidate, return to the outer loop


	return(bestQ2, bestQ1)  


def write_out(bestQ1, bestQ2):                   #write output to a text file
	out_str = str(bestQ1) + " " + str(bestQ2)
	output = open("janvr.out", "w")
	output.write(out_str)
	output.close()

def end_timer(start):
	end = time.time()
	# print("Time taken: ", end-start)

def doIt(filename):
	start = start_timer()
	N, Qmin, Qmax, data = import_data(filename)
	data_T = list(zip(*data))
	rows, cols = partial_sums(data, data_T)
	qualities = all_qualities(N, rows, cols)
	vec, qualities = reduce(Qmin, Qmax, N, qualities)
	bestQ1, bestQ2 = find(vec, Qmin, Qmax, qualities)
	print(bestQ1, bestQ2)
	# write_out(bestQ1, bestQ2)
	end_timer(start)

file = "pub10.in"

doIt(file)