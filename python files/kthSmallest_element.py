# Python implementation of the above approach. 
import math 
import random 

# Function to return the 
# sign of the number 
def sign(x): 
	if x>0: 
		return 1
	elif x<0: 
		return -1
	return 0

# Function to swap two 
# numbers in an array 
def swap(arr, i, j): 
	temp = arr[i] 
	arr[i] = arr[j] 
	arr[j] = temp 

# Function to return kth smallest number 
def select(arr: list, left: int, 
right: int, k: int): 
	while right>left: 

		# Choosing a small subarray 
		# S based on sampling. 
		# 600, 0.5 and 0.5 are 
		# arbitrary constants 
		if right-left > 600: 
			n = right - left + 1
			i = k - left + 1
			z = math.log(n) 
			s = 0.5 * math.exp(2 * z / 3) 
			sd = 0.5 * math.sqrt(z * s * (n-s)/n) * sign(i-n / 2) 
			newLeft = int(max(left, k-i * s / n + sd)) 
			newRight = int(min(right, k + (n - i) * s / n + sd)) 
			select(arr, newLeft, newRight, k) 
		t = arr[k] 
		i = left 
		j = right 
		swap(arr, left, k) 
		if arr[right] > t: 
			swap(arr, left, right) 
		while i<j: 
			swap(arr, i, j) 
			i = i + 1
			j = j-1
			while arr[i]<t: 
				i = i + 1
			while arr[j] >t: 
				j = j-1

		if arr[left] == t: 
			swap(arr, left, j) 
		else: 
			j = j + 1
			swap(arr, right, j) 

		# Updating the left and right indices 
		# depending on position of k-th element 
		if j<= k: 
			left = j + 1
		if k<= j: 
			right = j-1
	return arr[k] 


arr = [7, 3, 4, 0, 1, 6] 
# k-th smallest element. 
# In this the 2nd smallest element is returned. 
k = 2
res = select(arr, 0, len(arr)-1, k-1) 
print('The {}-th smallest element is {}'.format(k, res)) 

"""
O algoritmo Floyd-Rivest é um algoritmo de seleção usado para encontrar 
o k-ésimo menor elemento em uma matriz de elementos distintos. 
É semelhante ao algoritmo QuickSelect, mas tem melhor tempo de execução na prática.
Como o QuickSelect, o algoritmo trabalha com a ideia de particionamento. 
Depois de particionar uma matriz, o elemento de partição termina na posição de classificação corrigida.
Se a matriz tiver todos os elementos distintos, recuperar o (k + 1) o menor elemento é o mesmo que recuperar o (k + 1)
o elemento após a classificação. 
Como uma classificação completa é cara (leva O (N log N) para computar), 
o algoritmo Floyd-Rivest aproveita o particionamento para realizar o mesmo em tempo O (N).

Algoritmo:
Se o tamanho do array S considerado é pequeno o suficiente, o algoritmo QuickSelect é aplicado diretamente
 para obter o K-ésimo menor elemento. Esse tamanho é uma constante arbitrária do algoritmo, que os autores escolheram como 600.
Caso contrário, 2 pivôs são escolhidos - newLeftIndex e newRightIndex usando amostragem aleatória de forma 
que eles tenham a maior probabilidade de conter o maior elemento K-th. Em seguida, a função é chamada recursivamente 
com os limites esquerdo e direito da matriz agora definidos como newLeftIndex e newRightIndex.
Como QuickSelect, depois de particionar o subarray, os limites esquerdo e direito precisam ser 
definidos de forma que contenham o elemento K maior.
Depois de particionar o array em torno de K, o elemento K-th está em sua posição classificada correta. 
Portanto, os limites esquerdo e direito são definidos de forma que o subarray considerado contém o array [k]
"""