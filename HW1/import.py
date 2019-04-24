
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

N, data = import_data()

print(N)
print(data)