def f_le(arq):
	dic = dict()
	texto = arq.readline()
	texto = texto[:-1]
	while texto != "":
		lista = texto.split(";")
		dic[lista[0]] = [lista[1],lista[2], int(lista[3])]
		texto = arq.readline()
	return dic

def f_par(dic):
	dicPar = dict()
	for i in dic.keys():
		for j in dic.keys():
			if(i != j and not((i,j) in dicPar.keys() or (j,i) in dicPar.keys())):
				if(dic[i][2] == dic[j][2]):
					dicPar[(i,j)] = [(dic[i][2]) * 2, f_soma(i), f_soma(j)]
	return dicPar

def f_soma(n):
	s = 0
	for i in n:
		s += int(i)
	return s

def f_imprimi(dicPar, dicPess,arq):
	for i,j in dicPar.items():
		print(f'Pessoa 1= {dicPess[i[0]][0]} Pessoa 2= {dicPess[i[1]][0]} {j[0]} {j[1]} {j[2]}')
		arq.write(f'Pessoa 1= {dicPess[i[0]][0]} Pessoa 2= {dicPess[i[1]][0]} {j[0]} {j[1]} {j[2]}\n')
