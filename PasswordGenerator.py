import random

##Some basic classes to manage infornation#
class Node:
    def __init__(self,item=None):
        self.v = item
        self.next = None

    def setNext(self, next_node):
        self.next = next_node
    
    def getNext(self):
        return self.next
  
    def get(self):
        return self.v
    
class LinkedList:

    def __init__(self):
        self.first=None
        self.last=None
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
        if  index < 0 or index >= self.size():
            print("invalid index")
            return
        if index == 0:
            self.first = self.first.next
        else:
            start = self.first
            for i in range(index-1):
                start = start.next
            start.next = start.next.next
        self.Size -= 1

    def getIndex(self, item):
        index = 0
        i = self.first
        while i is not None:
            if i.v == item:
                return index
            else:
                i=i.next
                index += 1
        
        return -1

    def contains(self,item):
        exist=False
        i = self.first
        while i is not None:
            if i.v == item:
                exist=True
                break
            else:
                i=i.next
        
        return exist

    def print(self):
        txtArray = []
        cur=self.first
        while cur is not None:
            txtArray.append(str(cur.v))
            cur = cur.next

        return "".join(txtArray)
    
class PasswordCreator():

    def __init__(self):
        self.lenght = int(input("What's your password lenght? "))
        self.password = None
        self.passwordChr = LinkedList()
        
    ##Generates a random password##
    def randomPassword(self):
        lenght = self.lenght
        while lenght > 0:
            num = random.randint(33,126)
            self.passwordChr.add(chr(num))
            lenght -= 1
        self.password = self.passwordChr.print()
        return self.password
    
    ##Use it to let the user make decisions and be able to recall the same function with no worries##
    def decisionloop(self, task):
        if task == 1: ##be able to change more chrs in changePassword##
            decision = input("Want to change more chr? Type 1 - YES | 2 - NO")
            if decision not in ("1", "2"):
                print("Answer not accepted, please correct")
                return self.decisionloop(1)
            else:
                if decision == "1":
                    return True
                else:
                    return False

    #Use it to the user be able to change the password. It keeps using Linked Lists to make it run way smoother, still has a lot of "while" so it might take a bit for BIG passwords#
    def changePassword(self):
        toChange = LinkedList()
        toChange.add(input("What chr do you want to change?"))
        index = 0
        while self.decisionloop(1):
            toChange.add(input("What chr do you want to change?"))
            index += 1
        
        while index >= 0:
            index -= 1
            item = toChange.get(index).get()
            while self.passwordChr.contains(item) is True:
                newindex = self.passwordChr.getIndex(item)
                if newindex == -1:
                    print("Something went wrong")
                    return -1
                self.passwordChr.remove(newindex)
                num = ord(item)
                while num == ord(item):
                    num = random.randint(33,126)
                self.passwordChr.add(chr(num))

        self.password = self.passwordChr.print()
        return self.password
                

        
        


        






