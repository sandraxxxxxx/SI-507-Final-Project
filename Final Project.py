"""GET https://api.yelp.com/v3/businesses/search"""
import requests
import json


clientid = "K8PeHLf1A6dMAyhA8Zm27g"



def api_fetch(Limitn):
    mykey = "TZR3-NA_M36tECQaIge2qZTDJH8KwJCWZWd8nbG8PDY4w51TWn8Afm3_MUdkBpQilTrA1CvN72EJi0dDck1OJ9IJtJGGpa1tJPEieoPQ4HgeLiQBVkGb6UVYHixJYnYx"
    Endpoint = "https://api.yelp.com/v3/businesses/search"
    headers = {'Authorization': 'bearer %s' % mykey}
    #param = {"term": Term, "limit" : Limitn, "radius": 5000, "location": "Ann Arbor"}
    #param = { "limit" : Limitn, "radius": 5000, "location": "Michigan"}
    param = { "limit" : Limitn, "radius": 5000, "location": "Michigan"}
    response = requests.get(url = Endpoint,  headers = headers)
    resultd = json.loads(response.text)
    return resultd

#print(api_fetch(699)["total"])

CACHE_FILENAME = "cache.json"

def open_cache():
    try:
        cache_file = open(CACHE_FILENAME, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict

def save_cache(cache_dict):
    dumped_json_cache = json.dumps(cache_dict)
    fw = open(CACHE_FILENAME,"w")
    fw.write(dumped_json_cache)
    fw.close() 

def Yelp_cache(n):
    n_key = str(n)
    if n_key in yelp_cache.keys():
        return yelp_cache[n_key]
    else:
        yelp_cache[n_key] = api_fetch(n)
        save_cache(yelp_cache)
        return yelp_cache[n_key]


yelp_cache = open_cache()

"""inp = input("What?")"""
#print(Yelp_cache(int(2))["businesses"][0]["name"])
#print(Yelp_cache(int(2))["businesses"][0])
#print(Yelp_cache(int(inp)))
class TreeNode:
    def __init__(self,Yname,val,left=None,right=None,
                                       parent=None):
        self.Yname = Yname
        self.payload = val
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
      self.size = self.size + 1
    
    def _put(self,Yname,val,currentNode):
      if Yname < currentNode.Yname:
        if currentNode.hasLeftChild():
          self._put(Yname,val,currentNode.leftChild)
        else:
          currentNode.leftChild = TreeNode(Yname,val,parent=currentNode)
      else:
        if currentNode.hasRightChild():
            self._put(Yname,val,currentNode.rightChild)
        else:
          currentNode.rightChild = TreeNode(Yname,val,parent=currentNode)

    def get(self,Yname):
      if self.root:
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
      elif currentNode.Yname == Yname:
        return currentNode
      elif Yname < currentNode.Yname:
        return self._get(Yname,currentNode.leftChild)
      else:
        return self._get(Yname,currentNode.rightChild)
        
    def __getitem__(self,Yname):
        return self.get(Yname)  

def createtree(tree, data):
    for i in data["businesses"]:
        print(i["name"])
        tree.put(i["name"], i)

tree = BinarySearchTree()
print(createtree(tree, Yelp_cache(int(4))))

print(BinarySearchTree.__getitem__(tree, "Dime Store"))