class TreeNode:
    def __init__(self,Yname,val,left=None,right=None,
                                       parent=None):
        self.Yname = Yname
        self.payload =  []
        self.payload.append(val)
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,Yname,value,lc,rc):
        self.Yname = Yname
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
class BinarySearchTree:   
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self,Yname,val):
      if self.root:
        self._put(Yname,val, self.root)
        
      else: 
        self.root = TreeNode(Yname,val)
        #print(Yname)
      self.size = self.size + 1
    
    def _put(self,Yname,val,currentNode):
      if Yname == currentNode.Yname:
          (currentNode.payload).append(val)

      elif Yname < currentNode.Yname:
        if currentNode.hasLeftChild():
          self._put(Yname,val,currentNode.leftChild)
        else:
          currentNode.leftChild = TreeNode(Yname,val,parent=currentNode)
          #print(Yname)
      else:
        if currentNode.hasRightChild():
          self._put(Yname,val,currentNode.rightChild)
        else:
          currentNode.rightChild = TreeNode(Yname,val,parent=currentNode)
        #print(Yname)

    def get(self,Yname):
      if self.root:
        #print(self.root.Yname)
        res = self._get(Yname,self.root)
        if res:
          return res.payload
        else:
          return None
      else:
        return None
    def _get(self,Yname,currentNode):    
        if not currentNode:
            return None
        elif currentNode.Yname== Yname:
            return currentNode
        
        elif Yname < currentNode.Yname:
            return self._get(Yname,currentNode.leftChild)
        else:
            return self._get(Yname,currentNode.rightChild)        
   
        
    def __getitem__(self,Yname):
        return self.get(Yname)  