
# Definition for singly-linked list.
from tkinter.messagebox import NO
from tkinter.tix import Tree

from more_itertools import first


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  
    def isPalindrome(self, head) -> bool:
        if head == None:
            return True
        elif head != None and head.next == None:
            return True
        else:
            nNode = head
            fNode = head
            stack = []
            while nNode != None and nNode.next != None:
                stack.append(fNode.val)
                fNode = fNode.next
                nNode = nNode.next.next
            
            if nNode != None:
                fNode = fNode.next
            
            while fNode != None:
                if fNode.val != stack.pop():
                    return False
                else:
                    fNode = fNode.next
            return True
    
    

#main
# regular_list = [x for x in input().split()]
# llist = linkedList(regular_list)
# print(isPalindrome(llist))