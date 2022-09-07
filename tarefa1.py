from fun import f_cadHistorico, f_preenche, f_leAlu, f_leDis
def main():
	aluno = {}
	historico = {}
	lista = []

	arqDis = open(input(),"r")
	disciplina = f_leDis(arqDis)
	arqDis.close()

	arqAlu = open(input(),"r")
	aluno = f_leAlu(arqAlu)
	arqDis.close()

	print(disciplina)
	print(aluno)

	historico = f_cadHistorico(disciplina, aluno, historico)
	arqHis = open(input(), "w")
	f_preenche(historico, arqHis)
	arqHis.close()
	print(historico)

	return 0
if __name__=="__main__":
	main()
