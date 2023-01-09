class selectionsort:
	def __init__(self,arr):
		self.arr = arr
	def selectionsort(self):
		n = len(self.arr)
		for i in range(n):
			minm = i
			for j in range(i+1,n):
				if(self.arr[j]<self.arr[minm]):
					minm = j
			self.arr[minm],self.arr[i] = self.arr[i],self.arr[minm]
		print(self.arr)


