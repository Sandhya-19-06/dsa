class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None


    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=new_node


    def print_list(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")


    def  delete_node(self,key):
        current=self.head


        if current and current.data ==key:
            self.head=current.next
            current=None
            return


        prev=None
        while current and current.data != key:
            prev=current
            current=current.next


        if current is None:
            print("Node not found")
            return


        prev.next=current.next
        current=None

if __name__=="__main__" :
    l1=linkedlist()
    l1.append(10)
    l1.append(20)
    l1.append(30)

    print("linked list:")
    l1.print_list()


    l1.delete_node(20)
    print("after deleting 20:")
    l1.print_list()




