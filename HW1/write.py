import random as rnd

def construct(N):
	f = open('data2.txt', 'w')
	x = []
	for i in range(0, N):  #construct data
		row = []
		for j in range(0, N):
			row.append(rnd.randint(-9, 9))
		
		x.append(row)
	return(x)

N = int(input("Size: "))
data = construct(N)

def write(N, x):
	f = open("data2.txt", 'w')
	f.write(str(N) + "\n")

	for i in range(0, N):
		f.write(str(x[i]))
		f.write("\n")

write(N, data)