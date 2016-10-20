# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 18:04:40 2016

@author: Justin
"""

class Node:
    def __init__(self,val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
    
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
            
    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
                
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
                
    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))
            
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()
        
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
            
#    def nodeSum(self):
#        if self.root == None:
#            return(0)
#        sum_total = nodeSum(self.leftChild) + nodeSum(self.rightChild) + self.val
#        return(sum_total)
        
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
            
    def preorder(self):
        print('PreOrder')
        self.root.preorder()
        
    def postorder(self):
        print('Postorder')
        self.root.postorder()
        
    def inorder(self):
        print('InOrder')
        self.root.inorder()