from fun import f_csvPesTOdic, f_csvMaTOdic, f_matrizMatch, f_escreve
def main():
    arqPess = open(input(),"r")
    dicPess = f_csvPesTOdic(arqPess)
    arqPess.close()
    print(dicPess)
    arqMatch = open(input(),"r")
    dicMatch = f_csvMaTOdic(arqMatch)
    arqMatch.close()
    matriz = f_matrizMatch(dicMatch)

    arqMatriz = open(input(), "w")
    f_escreve(arqMatriz, matriz)
    arqMatriz.close() 
    return 0
if __name__=="__main__": main()