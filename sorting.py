class sorting():
    def __init__(self, arr):
        self.arr = arr

    def bubbleSort(self):
        n = len(self.arr)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.arr[j] > self.arr[j + 1]:
                    swapped = True
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
            if not swapped:
                return
        return self.arr

    def insertionSort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i-1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
        return self.arr

    def MergeSort(self):
        if len(self.arr) > 1:
            m = len(self.arr)//2
            left = self.arr[:m]
            right = self.arr[m:]
            leftsorter = sorting(left)
            leftsorter.MergeSort()
            rightsorter = sorting(right)
            rightsorter.MergeSort()
            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.arr[k] = left[i]
                    i += 1
                else:
                    self.arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                self.arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                self.arr[k] = right[j]
                j += 1
                k += 1
        return (self.arr)

    def selection(self):
        for i in range(len(self.arr)):
            min_idx = i
            for j in range(i+1, len(self.arr)):
                if self.arr[min_idx] > self.arr[j]:
                    min_idx = j
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
        return self.arr

    def partition(self, low, high):
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i = i + 1
                (self.arr[i], self.arr[j]) = (self.arr[j], self.arr[i])
        (self.arr[i + 1], self.arr[high]) = (self.arr[high], self.arr[i + 1])
        return i + 1
    
    def quick_sort(self):
        low = 0 
        high = len(self.arr)-1
        if low < high:
            pi = sorting.partition(self.arr, low, high)
            sorting.quick_sort(self.arr, low, pi - 1)
    
            # Recursive call on the right of pivot
            sorting.quick_sort(self.arr, pi + 1, high)
        return self.arr


if __name__ == "__main__":
    abcd = [6, 5, 4, 3, 2, 1]
    detector = sorting(abcd)
    print(detector.quick_sort())
