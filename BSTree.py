\
#############################
# module: BSTree.py
# description: binary search tree
# bugs to vladimir dot kulyukin at usu dot edu
#############################

from BSTNode import BSTNode

class BSTree:

    def __init__(self, root=None):
        self.__root = root
        if root==None:
            self.__numNodes = 0
        else:
            self.__numNodes = 1

    def getRoot(self):
        return self.__root

    def getNumNodes(self):
        return self.__numNodes

    def isEmpty(self):
        return self.__root == None

    def hasKey(self, key):
        if self.isEmpty():
            return False
        else:
            currNode = self.__root
            while currNode != None:
                if currNode.getKey() == key:
                    return True
                elif key < currNode.getKey():
                    currNode = currNode.getLeftChild()
                elif key > currNode.getKey():
                    currNode = currNode.getRightChild()
                else:
                    raise Exception('hasKey: ' + str(key))
            return False

    def insertKey(self, key):
        if self.isEmpty():
            self.__root = BSTNode(key=key)
            self.__numNodes += 1
            return True
        elif self.hasKey(key):
            return False
        else:
            currNode = self.__root
            parNode = None
            while currNode != None:
                parNode = currNode
                if key < currNode.getKey():
                    currNode = currNode.getLeftChild()
                elif key > currNode.getKey():
                    currNode = currNode.getRightChild()
                else:
                    raise Exception('insertKey: ' + str(key))
            if parNode != None:
                if key < parNode.getKey():
                    parNode.setLeftChild(BSTNode(key=key))
                    self.__numNodes += 1
                    return True
                elif key > parNode.getKey():
                    parNode.setRightChild(BSTNode(key=key))
                    self.__numNodes += 1
                    return True
                else:
                    raise Exception('insertKey: ' + str(key))
            else:
                raise Exception('insertKey: parNode=None; key= ' + str(key))
     
    def heightOf(self):
        if self == None:
            return -1
        self2 = self.__root
        left_n = self2.getLeftChild()
        left_h = left_n.heightOf()
        right_n = self2.getRightChild()
        right_h = right_n.heightOf()
        return max(left_h,right_h) +1

	
    def isBalanced(self):
        if self == None:
# ------------------------------------
            return True
# ------------------------------------
        currNode = self.__root
        if abs(self.heightOf(currNode.getLeftChild()) - self.heightOf(currNode.getRightChild()))<= 1:
            return True
        return False
	
    def __displayInOrder(self, currnode):
        if currnode == None:
            print('NULL')
        else:
            self.__displayInOrder(currnode.getLeftChild())
            print(str(currnode))
            self.__displayInOrder(currnode.getRightChild())

    def displayInOrder(self):
        self.__displayInOrder(self.__root)

    def isList(self):
        if ((self.getNumNodes() - self.heightOf())== 1):
            return True
        return False
	
                


    
            

    
   
