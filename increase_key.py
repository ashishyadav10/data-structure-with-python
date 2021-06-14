# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 23:04:55 2021

@author: ashish yadav
"""



class heap:
    def __init__(self):
        self.arr=[None]
    def insert(self,data):
        if len(self.arr)==1:
            self.arr.append(data)
            return
        self.arr.append(data)
        chield=len(self.arr)-1
        parent=chield//2
        while self.arr[chield]>self.arr[parent]:
            self.arr[chield],self.arr[parent]=self.arr[parent],self.arr[chield]
            chield=parent
            parent=parent//2
            if(chield==1 or parent<=0):
                break
    def heap_sort(self,l):
        
        for i in l:
            self.insert(i)
        print(self.arr)
        ar=[]
        for i in range(len(l)):
            ar.append( self.extract_max())
        return ar
            
    def find_max(self):
        if(len(self.arr)==1):
            print("Tree is empty")
            return False
        return self.arr[1]

    def extract_max(self):
        if(len(self.arr)==1):
            print("no node to extract")
            return False
        mx=self.arr[1]
        if (len(self.arr)==2):
            return self.arr.pop()
        self.arr[1]=self.arr.pop()
        parent=1
        c1=parent*2
        c2=parent*2+1
        if(len(self.arr)==2):
            return mx
        if(c2>=len(self.arr)):
                   if(self.arr[parent]<self.arr[c1]):
                         self.arr[parent],self.arr[c1]=self.arr[c1],self.arr[parent]
                   return mx
               
        
        while self.arr[parent]<max(self.arr[c1],self.arr[c2]):
                if(self.arr[c1]>self.arr[c2]):
                      c=c1
                else:
                      c=c2
                self.arr[parent],self.arr[c]=self.arr[c],self.arr[parent]
                parent=c
                c1=c*2
                c2=c*2+1
                if(c1>=len(self.arr)):
                    break
                if(c2>=len(self.arr)):
                   if(self.arr[parent]<self.arr[c1]):
                         self.arr[parent],self.arr[c1]=self.arr[c1],self.arr[parent]
                   break
    
        return mx
    
    
#increase_key in binary heap

    def increase_key(self,key,data):
        index=self.arr.index(key)
        self.arr[index]=data
        c=index
        p=c//2
        while self.arr[p]<self.arr[c]:
            self.arr[p],self.arr[c]=self.arr[c],self.arr[p]
            c=p
            p=p//2
            if(p==0):
                break
    def decrease_key(self,key,data):
        index=self.arr.index(key)
        self.arr[index]=data
        p=index
        l=p*2
        r=p*2+1
        while self.arr[p]<max(self.arr[l],self.arr[r]):
            mx=r
            if(self.arr[p]<self.arr[l]):
                mx=l
            self.arr[p],self.arr[mx]=self.arr[mx],self.arr[p]
            p=mx
            l=p*2
            r=p*2+1
            if(l>=len(self.arr)):
                break
            if(r>=len(self.arr)):
                if(self.arr[l]>self.arr[p]):
                     self.arr[l],self.arr[p]=self.arr[p],self.arr[l]
                     break

h1=heap()
h1.insert(8)
h1.insert(7)
h1.insert(6)
h1.insert(5)
h1.insert(2)
h1.find_max()
h1.extract_max()
h1.arr
h1.increase_key(2,20)
h1.decrease_key(8,1)
h=heap()
h.heap_sort([5,3,7,2,8,1,22])



                
        