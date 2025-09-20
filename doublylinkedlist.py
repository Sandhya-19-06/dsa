class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert_front(self,data):
        new_node=Node(data)
        new_node.next=self.head
        if self.head:
            self.head.prev=new_node
        self.head=new_node


    def insert_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
        new_node.prev=curr


    def insert_after(self,prev_node_data,data):
        curr=self.head
        while curr and curr.data !=prev_node_data:
            curr =curr.next
        if not curr:
            print("previous node not found.")    
            return
        new_node=Node(data)
        new_node.next=curr.next
        new_node.prev=curr
        if curr.next:
            curr.next.prev=new_node
        curr.next=new_node

    def delete(self,key):
        curr=self.head
        while curr and curr.data !=key:
            curr=curr.next
        if not curr: 
            print("Node not found")
            return
        if curr.prev:
            curr.prev.next=curr.next
        else:
            self.head=curr.next
        if curr.next:
            curr.next.prev=curr.prev

    def traverse_forward(self):
        curr=self.head
        while curr:
            print(curr.data,end=' ')
            curr=curr.next  
        print()

    def traverse_backward(self):
        curr=self.head
        if not curr:
            return
        while curr.next:
            curr=curr.next
        while curr:
            print(curr.data,end=' ')   
            curr=curr.prev
        print()

if __name__=="__main__":
    dl1=DoublyLinkedList()
    dl1.insert_end(10)
    dl1.insert_end(20)
    dl1.insert_front(5)
    dl1.insert_after( 10,15)  

    print("forward traversal:") 
    dl1.traverse_forward()

    print("backward traversal:") 
    dl1.traverse_backward()

    print("after deleting 10:")  
    dl1.delete(10)    
    dl1.traverse_forward()                     


