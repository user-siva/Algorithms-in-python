class Searching:
    res = False
    ans = None

    def __init__(self, arr, element):
        self.arr = arr
        self.element = element

    def linear_search(self):
        for i in range(len(self.arr)):
            if self.arr[i] == self.element:
                res = True
                ans = i
        if res:
            return ans
        else:
            return "The given element is not found in a array"   
        
    def BinarySearch(self):
        self.arr.sort()
        low = 0
        high = len(self.arr)-1
        found = False
        while low <= high and not found:
            mid=(low+high)//2
            if self.element == self.arr[mid]:
                found = True
            elif self.element > self.arr[mid]:
                low = mid+1
            else:
                high = mid-1
        if found == True:
            print(self.element, "is found in")
        else:
            print(self.element, "is not found") 


a = Searching([3, 4, 2, 32, 65, 54, 6, 26], 54)
print(a.linear_search())
print(a.BinarySearch())

