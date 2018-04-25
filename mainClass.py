import math

items = ['jablko','banan','pomarancza','winogrona','brzoskwinia','truskawka','jagoda','kiwi','mango','gruszka']
attributes = ['Czy zazwyczaj jest okragle/koliste?',
'Czy zazwyczaj jest podluznego krztaltu?',
'Czy gdy jest dojrzałe ma pomarańczową skórkę?',
'Czy może mieć zieloną skórkę?',
'Czy gdy jest dojrzałe może mieć czerwona skórkę?',
'Czy zazwyczaj jest malych rozmiarow?',
'Czy może być granatowe?',
'Czy jest gladkie?',
'Czy gdy jest dojrzałe może być wielokolorowe?',
'Czy rośnie na drzewach?',
'Czy rośnie na krzakach?',
'Czy rosnie w Polsce?',
'Czy ma chropowatą skórkę?',
'Czy może być zielone?']

merged = [[1,0,0,1,1,0,0,1,1,1,0,1,0,1],
[0,1,0,1,0,0,0,1,0,1,0,0,0,1],
[1,0,1,0,0,0,0,0,0,1,0,0,1,0],
[1,0,0,1,0,1,1,1,0,1,0,0,0,1],
[1,0,1,0,0,0,0,0,1,1,0,1,1,0],
[0,1,0,1,1,1,0,0,0,0,1,1,1,1],
[1,0,0,0,0,1,1,1,0,0,1,1,0,1],
[1,0,0,1,0,0,0,0,0,1,0,0,1,1],
[1,0,1,1,1,0,0,1,1,1,0,0,0,1],
[0,1,0,1,0,0,0,1,1,1,0,1,0,1]]

class countStrengthclass:
	def __init__(self, tab):
		self.tab = tab
		self.attributes = attributes
		self.items = items

	def countStrength(self):
		#count strength of all attributes
		maxHeight = len(self.tab)
		maxLength = len(self.tab[0])
		avg = maxHeight/2.0
		#r#esult = 0
		index_value = 0
		index_strength = 0;
		for y in range(0,maxLength):
			tempResult = 0
			for x in range(0,maxHeight):
				if self.tab[x][y] == 1:
					tempResult = tempResult + 1
			if math.fabs(avg - tempResult) < math.fabs(avg - index_strength ):
				index_strength = tempResult
				index_value = y

		#return index of attribute, whose strength is the nearest to average
		return (index_strength, index_value)
		
	
	def createNewMatrix (self, ans):
		# matrix = [[0 for x in range(width)] for y in range(height)]
		
		(str, value) = self.countStrength() # zwraca strukture .strength i .value(nr cechy)
		self.sortBy(value)
		
		if (ans=="n"):
			size = len(self.tab) - str
			newitems = [0 for x in range (size)]
			newmatrix = [[0 for x in range(len(self.tab[0]))] for x in range(size)] #lista pustych list
			for i in range (0, size):
				newitems[i] = self.items[i]
				for j in range(0, len(self.tab[0])):
					newmatrix[i][j] = self.tab[i][j]
		elif (ans == "y"):
			size = str
			newitems = [0 for x in range (size)]
			newmatrix = [[0 for x in range(len(self.tab[0]))] for x in range(size)]
			for i in range (0, size):
				newitems[i] = self.items[len(self.tab) - size + i]
				for j in range(0, len(self.tab[0])):
					newmatrix[i][j] = self.tab[len(self.tab) - size + i][j]
		
		self.tab, self.items = newmatrix, newitems
		return
		
		
	def sortBy(self, attribute):
		
		height = len(self.tab)
		#for i in range(0,height-5):#height-1)):
		i = 0
		
		while (i<height-1):
			j = 0
			#for j in range (i,height-2-i):
			while(j<height-1):
				#print(j, i)
				if (self.tab[j][attribute]>self.tab[j+1][attribute]):
					#print(j)
					#print (self.items[j], self.items[j+1])
					temp = self.tab[j]
					self.tab[j] = self.tab[j+1]
					self.tab[j+1] = temp
					temp = self.items[j+1]
					self.items[j+1] = self.items[j]
					self.items[j] = temp
					#self.swapElements(self.tab[j], self.tab[j+1])
					#self.swapElements(self.items[j], self.items[j+1])
				j = j+1
			i=i+1
		#print(attribute)
		#print(self.tab)
		#return self

	def swapElements(self,a, b):
		temp = a
		a = b
		b = temp
			

cs = countStrengthclass(merged)


while (len(cs.items) >1):
	x,numer_cechy = cs.countStrength()
	print(attributes[numer_cechy])
	odpowiedz = input()
	cs.createNewMatrix(odpowiedz)
	
print (cs.items)