Carros = []
#criando lista com append
Carros.append('Marea') #colocar na lista
Carros.append('Fusca')
Carros.append(10)
#criando no momento que cria ela
Filmes = ['A bruxa', 'os suspeitos', 'corra']
Filmes.append('Seven')
Filmes.insert(1, 'Lego') #inserindo onde eu quisr
Filmes.pop() #deleta o ultimo
del Filmes[1] #remove o que voce quiser
Carros.remove(10) #baseado em valor
Filmes.append('A bruxa')
print(Filmes.count('A bruxa'))
Filmes.reverse()
Filmes.sort()
print(Filmes)
print(Carros)