from pathlib import Path
import os
import math
import random
import sys
import re
##-----------##
##-----------##
class Node:
    def __init__(self,item=None):
        self.v = item
        self.next = None

    def set_next_node(self, next_node):
        self.next = next_node
    
    def get_next_node(self):
        return self.next
  
    def get_value(self):
        return self.v

class List:

    def __init__(self):
        self.first=Node()
        self.last=Node()
        self.Size = 0

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.Size
                
    def add(self, item):
        new = Node(item)
        new.next = self.first
        self.first = new
        self.Size += 1
    
    def get(self, index):
        if index < 0 or index >= self.Size:
            raise IndexError("invalid index")
        
        value = self.first
        for n in range(index):
            value = value.next

        return value

    
    def remove(self,index):
        if  index <= 0 or self.size():
            print("invalid index")
            exit()

        ant=Node()
        pos=self.first
        for n in range(1, index, +1):
            ant=pos
            pos=pos.next

    def contains(self,item):
        exist=False
        i = self.first
        x=0
        while i.next is not None:
            if i.v is item:
                exist=True
                break
            else:
                i=i.next
        
        return exist

    def print(self):
        txtArray = []
        cur=self.first
        while cur.v is not None:
            txtArray.append(str(cur.v))
            cur = cur.next

        return "".join(txtArray)

class Key:
    def __init__(self):
        keyList = List()
        keyChr=["#","!","?","|","~","/","a","e","i","o","u","z","H","K","P","L","M","O"]

        p=0
        while p < 64:
            x=random.randint(0,17)
            keyList.add(keyChr[x])
            p=p+1
        
        self.key = keyList.print()
        self.keyList = keyList


    def printKey(self):
        print(self.key)

    def toArray(self):
        print(list(self.key))

##-----------##
##-----------##






