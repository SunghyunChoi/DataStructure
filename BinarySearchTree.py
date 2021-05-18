#이진 탐색 트리(Binary Search Tree)
#구조 설계를 위해 class Node와 BST를 선언한다.
#각 노드는 Key와 Value를 가진다

from collections import deque

class Node:
    
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    

class BST:

    def __init__(self):
        self.root = None

    def printTree(self):

        if self.root == None:
            print("Nothing to print")

        printStk = deque([self.root])
        while printStk:
            printLen = len(printStk)
            print()
            for _ in range(printLen):
                nextToPrint = printStk.popleft()
                print(nextToPrint.key, end='   ')
                if nextToPrint.left:
                    printStk.append(nextToPrint.left)
                if nextToPrint.right:
                    printStk.append(nextToPrint.right)

    def search(self, key):
        if self.root == None:
            return False
        
        checkNode = self.root
        while checkNode:
            if checkNode.key < key:
                checkNode = checkNode.right
            elif checkNode.key > key:
                checkNode = checkNode.left
            else:
                return checkNode.value

        return False

    def add(self, key, value):
        if self.root == None:
            self.root = Node(key, value)
            return 0
        
        checkNode = self.root
        while True:
            if checkNode.key < key:
                if checkNode.right:
                    checkNode = checkNode.right
                else:
                    checkNode.right = Node(key, value)
                    return True
            elif checkNode.key > key:
                if checkNode.left:
                    checkNode = checkNode.left
                else:
                    checkNode.left = Node(key, value)
                    return True
            else:
                return False
    
    def remove(self, key):
        p = self.root
        parent = None
        isLeft = False

        while True:
            if p is None:
                return False
            
            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    isLeft = True
                    p = p.left
                else:
                    isLeft = False
                    p = p.right
        
        #제거하고자 하는 노드의 왼쪽 자식이 없는 경우
        if p.left is None:
            if p == self.root:
                self.root = p.right
            elif isLeft:
                parent.left = p.right
            else:
                parent.right = p.right
        #제거하고자 하는 자식의 오른쪽 자식이 없는 경우
        elif p.right is None:
            if p == self.root:
                self.root = p.left
            elif isLeft:
                parent.left = p.left
            else:
                parent.right = p.left
        #제거하고자 하는 노드의 양쪽 자식이 모두 존재하는 경우
        else:
            parent = p
            left = p.left
            isLeft = True
            while left.right != None:
                parent = left
                left = left.right
                isLeft = False

            p.key = left.key
            p.value = left.value
            if isLeft:
                parent.left = left.left
            else:
                parent.right = left.left
        #자식이 둘 다 없는 경우는 첫번째 조건에서 걸리며, 이 때 p.right는 None이다.
        
        return True

    def dump(self):
        #오름차순으로 출력

        def printSubtree(node):
            if node:
                printSubtree(node.left)
                print(f'{node.key}  {node.value}')
                printSubtree(node.right)
        printSubtree(self.root)
    
    def printMax(self):
        if self.root == None:
            return False
        
        node = self.root
        while True:
            if node.right:
                node = node.right
            else:
                break
        print(node.key)

    def printMin(self):
        if self.root == None:
            return False
        
        node = self.root
        while True:
            if node.left:
                node = node.left
            else:
                break
        print(node.key)

bst = BST()
bst.add(5,5)
bst.add(4,4)
bst.add(6,6)
bst.add(3,3)
bst.add(7,7)
bst.add(1,1)
bst.remove(5)
bst.printTree()
print()
bst.dump()
bst.printMin()
bst.printMax()
