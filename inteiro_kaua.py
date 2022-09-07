def C_Dic(nome):
  with open(nome) as arq:
    dic = dict()
    conteudo = list()
    conteudo = arq.readline().split(';')
    #while conteudo != ['']:
    for i in range(12):
      print(conteudo)
      dic[conteudo[0]] = conteudo[1:-1]
      dic[conteudo[0]].append(conteudo[-1][:-1])
      conteudo = arq.readline().split(';')
    return dic
def C_csv(dicio):
  conteudo = str()
  for k in dicio.keys():
    conteudo += f'{k};{str(dicio[k])}\n'
  conteudo = conteudo[:-1]
  #with open('resultados.csv','w') as Saida:
    #Saida.write(conteudo)
def main():
  dicMatch = dict()
  dicResKeys = list()
  dicPes = C_Dic(input())
  dicRes = C_Dic(input())
  for chave in dicRes.keys():
    dicResKeys.append(chave)
  aux = 0
  for i in dicResKeys[:-1]:
    aux += 1
    for j in dicResKeys[aux:]:
      dicMatch[i,j] = 0
      for NResposta in range(len(dicRes[i])):
        if dicRes[i][NResposta] == 'I' or dicRes[j][NResposta] == 'I':
          dicMatch[i,j] += 1
        elif dicRes[i][NResposta] == dicRes[j][NResposta]:
          dicMatch[i,j] += 2
  C_csv(dicMatch)
  print(dicMatch)
if __name__ == '__main__':main()