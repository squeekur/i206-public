#---------------------------------------------------------
# <NAME>
# <EMAIL>
# Homework #2
# September 15, 2015
# BST.py
# BST
#---------------------------------------------------------


class Node:
    #Constructor Node() creates node
    def __init__(self,word):
        #WILL CREATE IN LAB
        self.placeholder = None #REMOVE

class BSTree:
    #Constructor BSTree() creates empty tree
    def __init__(self, root=None):
        #WILL CREATE IN LAB
        self.placeholder = None #REMOVE
    
    #These are "external functions" that will be called by your main program - I have given these to you =)
    
    #Find word in tree
    def find(self, word):
        return _find(self.root, word)
    
    #Add node to tree with word
    def add(self, word):
        if not self.root:
            self.root = Node(word)
            return
        _add(self.root, word)

    #Print in order entire tree
    def inOrderPrint(self):
        _inOrderPrint(self.root)

    def size(self):
        return _size(self.root)

    def height(self):
        return _height(self.root)


#These are "internal functions" in the BSTree class - You need to create these!!!

#Function to add node with word as word attribute
def _add(root, word):
    #YOU FILL THIS IN
    self.placeholder = None #REMOVE

#Function to find word in tree
def _find(root, word):
    #YOU FILL THIS IN
    self.placeholder = None #REMOVE

#Get number of nodes in tree
def _size(root):
    #YOU FILL THIS IN
    self.placeholder = None #REMOVE

#Get height of tree
def _height(root):
    #YOU FILL THIS IN
    self.placeholder = None #REMOVE
    
#Function to print tree in order
def _inOrderPrint(root):
    #YOU FILL THIS IN
    self.placeholder = None #REMOVE
