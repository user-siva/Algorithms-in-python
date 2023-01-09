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
        low = 0
        high = len(self.arr)-1
        found = False
        while low <= high and not found:
            mid = (low+high)//2
            if self.element == self.arr[mid]:
                found = True
            elif self.element > self.arr[mid]:
                low = mid+1
            else:
                high = mid-1
        if found == True:
            print("element is found")
        else:
            print("element is not found")


#a = Searching([25, 1, 4, 5, 3], 4)
# print(a.BinarySearch())

#b = [25, 1, 4, 5, 3]
#print("b:", len(b))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        new_node = Node(value)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def deleteNode(self, key):
        current = self.head
        while current.value is not key:
            current = current.next
        current.value = current.next.value
        current.next = current.next.next

    def insertNode(self, val, pos):
        new_node = Node(val)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(1, pos-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)

l.display()
l.deleteNode(3)
l.display()
l.insertNode(88, 4)
l.display()
