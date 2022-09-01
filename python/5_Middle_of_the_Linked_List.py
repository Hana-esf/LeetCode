from tkinter.messagebox import NO


class LinkedList():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def Middle_Node(self,head):
        count = 0
        stack = []
        node = head
        while node != None and node.next != None:
            stack.append(node.val) 
            node = node.next
            count += 1

        i = 1
        while i <= count//2:
            head = head.next
            i += 1
        return head

