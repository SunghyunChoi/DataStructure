class LinkedList:
    
    def __init__(self, node=None, nodeNum = 0):
        self.head = node
        self.current = None
        self.nodeNum = nodeNum
    
    def search(self, data):
        ptr = self.head
        cnt = 0
        while ptr:
            if ptr.data == data:
                self.current = ptr
                return cnt
            ptr = ptr.next
            cnt += 1 
        return -1

    def __contains__(self, data):
        return self.search(data) >= 0

    def addFirst(self, data):
        ptr = self.head
        self.head = Node(data, ptr)
        self.current = self.head
        self.nodeNum += 1

    def addLast(self, data):
        ptr = self.head
        if ptr == None:
            self.addFirst(data)
        else:
            while ptr.next:
                ptr = ptr.next
            ptr.next = Node(data)
            self.current = ptr.next
            self.nodeNum += 1
    
    def removeFirst(self):
        if self.head:
            self.head = self.head.next
            self.current = self.head
        self.nodeNum -= 1

    def removeLast(self):
        if self.head:
            if self.head.next == None:
                self.removeFirst()
            else:
                ptr = self.head
                pre = self.head

                while ptr.next:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.nodeNum -= 1

    def remove(self, data):
        if self.head:
            if self.head.data == data:
                self.removeFirst()
            else:
                ptr = self.head

                while ptr.next:
                    if ptr.next.data == data:
                        ptr.next = (ptr.next).next
                        self.current = ptr
                        self.nodeNum -= 1
                        return
                    ptr = ptr.next
                
    def removeCurrent(self):
        self.remove(self.current)
    
    def clear(self):
        while self.head:
            self.removeFirst()
        self.nodeNum = 0

    def next(self):
        if self.current:
            self.current = self.current.next

    def printCurrent(self):
        if self.current:
            print(f"current : {self.current.data}")

    def printAll(self):
        ptr = self.head
        print(self.nodeNum)
        while ptr:
            print(ptr.data)
            ptr = ptr.next

            
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


## Test ##

linkedList = LinkedList()

# test addLast
linkedList.addLast("끝")
linkedList.printAll()
linkedList.printCurrent()

# test addFirst
linkedList.addFirst("중간3")
linkedList.addFirst("중간2")
linkedList.addFirst("중간1")
linkedList.addFirst("시작")
linkedList.printAll()
linkedList.printCurrent()

# test remove
linkedList.remove("중간2")
linkedList.remove("중간3")
linkedList.remove("중간1")
linkedList.remove("끝")
linkedList.remove("시작")
linkedList.printAll()

#test clear
linkedList.addLast("끝")
linkedList.addFirst("시작")
linkedList.printAll()
linkedList.clear()
linkedList.printAll()