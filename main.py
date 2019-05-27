import numpy as np

productii = {}

with open("input.txt") as input:

	cuvant = str(input.readline())

	numar_simboluri_neterminale = int(input.readline().split()[0])
	simboluri_neterminale = input.readline().split(' ')

	numar_simboluri_terminale = int(input.readline().split()[0])
	simboluri_terminale = str(input.readline().split(' '))

	numar_productii = int(input.readline().split()[0])

	data = input.readlines()

	for line in data:
		line = line.split(' ')
		start = line[0]
		line = line[2:]
		for destination in line:
			if destination != '->' and destination != '|':
				try:
					if '\n' in destination:
						destination = destination.split('\n')[0]
					productii[start].append(destination)
				except:

					if '\n' in destination:
						destination = destination.split('\n')[0]
					productii[start] = list()
					productii[start].append(destination)


	P = np.zeros((len(cuvant) + 1, len(cuvant) + 1, numar_simboluri_neterminale))

	nr = 0
	n = len(cuvant)

	for i in range(1, len(cuvant)+1):
		for simbol_neterminal in productii.keys():
			if cuvant[i-1] in productii[(simbol_neterminal)]:
				cnt = int(0)
				for aux in productii.keys():
					if aux == simbol_neterminal:
						nr = cnt
					cnt += 1
				P[1][i][nr] = 1

	for l in range(2, n+1):
		for s in range(1, n-l+2):
			for p in range(1, l):
				for a, neterminal in zip(range(0, numar_simboluri_neterminale), productii.keys()):
					for b, element1 in zip(range(0, numar_simboluri_neterminale), productii.keys()):
						for c, element2 in zip(range(0, numar_simboluri_neterminale), productii.keys()):
							if (element1 in productii[neterminal] and element2 in productii[neterminal]) or ((element1+element2 in productii[neterminal]) or (element2+element1 in productii[neterminal])):
								if P[p][s][b]==1 and P[l-p][s+p][c]==1:
									P[l][s][a]=1
	
	if P[len(cuvant)-1][1][0] == 1:
		print("Cuvantul este membru al limbajului!")
	else:
		print("Cuvantul nu este membru al limbajului!")

	print(P)
