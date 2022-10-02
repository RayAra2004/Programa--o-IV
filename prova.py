from funProva import *

def main():
	arqPessoas = open(input(), "r")
	dicPessoas = f_le(arqPessoas)
	arqPessoas.close()
	dicPar = f_par(dicPessoas)
	arqPar = open(input(), "w")
	f_imprimi(dicPar, dicPessoas,arqPar)
	arqPar.close()
	return 0
if __name__ == '__main__': main()

