def f_csvPesTOdic(arq):
    dic = {}
    texto = arq.readline()
    while(texto != ""):
        lista = texto.split(";")
        dic[lista[0]] = [lista[1], lista[2], int(lista[3])]
        texto = arq.readline()
    
    return dic

def f_csvMaTOdic(arq):
    dic = {}
    texto = arq.readline()
    while(texto != ""):
        texto = texto[:-1]
        lista = texto.split(";")
        dic[lista[0]] = lista[1:]
        texto = arq.readline()
    
    return dic

def f_matrizMatch(dicMatch):
    matrizMatch = {}
    for i in dicMatch.keys():
        for j in dicMatch.keys():
            if(i != j and not((i,j) in matrizMatch.keys() or (j,i) in matrizMatch.keys())):
                res = f_confere(dicMatch[i], dicMatch[j])
                matrizMatch[(i,j)] = res
    return matrizMatch

def f_confere(li, lj):
    res = 0
    for i in range(10):
        if(li[i] == "I" or lj[i] == "I"):
            res += 1
        elif(li[i] == lj[i]):
            res += 2
    return res

def f_escreve(arq, dic):
    for i, j in dic.items():
        arq.write('Match:' + i[0] + ';' + i[1] + ';' + 'Pontuacao:' + str(j) + '\n')