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


a = Searching([3, 4, 2, 32, 65, 54, 6, 26], 26)
print(a.linear_search())
