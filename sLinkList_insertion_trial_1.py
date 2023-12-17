class Node:
    def __init__(self):
        self.data=None
        self.next=None
    def set_data(self,data):
        self.data=data
    def set_next(self,next):
        self.next=next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    
class Slink_list:
    def __init__(self):
        self.head=None
    def return_lenght(self):
        current=1
        curr_node=self.head
        while(curr_node.next!=None):
            current=current+1
            curr_node=curr_node.next
        return current
    def set_head(self,node):
        self.head=node
    def insert_end(self,node):
        curr_node=self.head
        while(curr_node.next!=None):
            curr_node=curr_node.next
        curr_node.next=node
    def insert_between(self,n,val):
        curr_node=self.head
        i=1
        while(i<n):
            curr_node=curr_node.next
            i=i+1
        tmp=curr_node.next
        x=Node()
        x.set_data(val)
        curr_node.next=x
        x.next=tmp
    def insert_front(self,node):
        curr_head=self.head
        self.head=node
        self.head.set_next(curr_head)
    def print_nodes(self):
        curr=self.head
        print(self.head.get_data())
        while(curr.next!=None):
            curr=curr.next
            print(curr.get_data())
if __name__=='__main__':
    y=Slink_list()
    n1=Node()
    n1.set_data("Mon")
    y.set_head(n1)
    n2=Node()
    n2.set_data("Tue")
    y.head.set_next(n2)
    n3=Node()
    n3.set_data("Thu")
    n2.set_next(n3)
    print(y.return_lenght())
    n4=Node()
    n4.set_data("Fri")
    y.insert_end(n4)
    print(y.return_lenght())
    y.insert_between(2,"Wed")
    print(y.return_lenght())
    y.print_nodes()
    print("-------------------")
    n5=Node()
    n5.set_data("Sun")
    y.insert_front(n5)
    y.print_nodes()

