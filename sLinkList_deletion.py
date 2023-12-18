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
    
class SLinkList:
    def __init__(self):
        self.head=None
    def set_head(self,node):
        self.head=node
    def return_head(self):
        return self.head
    def print_allNode(self):
        curr_node=self.head
        print(curr_node.get_data())
        while(curr_node.get_next()!=None):
            curr_node=curr_node.get_next()
            print(curr_node.get_data())
    def insertion_end(self,data):
        curr_node=self.head
        while(curr_node.get_next()!=None):
            curr_node=curr_node.get_next()
        n1=Node()
        n1.set_data(data)
        curr_node.set_next(n1)
    def deletion_end(self):
        curr_node=self.head
        while(curr_node.get_next().get_next()!=None):
            curr_node=curr_node.get_next()
        curr_node.set_next(None)
    def deletion_head(self):
        head_node=self.head
        second_node=head_node.get_next()
        head_node.set_next(None)
        self.head=second_node
    def deletion_at_n(self,n):
        count=1
        curr_node=self.head
        while(curr_node.get_next!=None and count<n):
            curr_node=curr_node.get_next()
            count=count+1
        tmp=curr_node.get_next().get_next()
        curr_node.set_next(tmp)
        
        

if __name__=='__main__':
    x=SLinkList()
    y=Node()
    y.set_data("Mon")
    x.set_head(y)
    z=Node()
    z.set_data("Tue")
    x.return_head().set_next(z)
    x.insertion_end("Wed")
    x.insertion_end("Thur")
    x.insertion_end("Fri")
    x.insertion_end("Sat")
    x.insertion_end("Sun")
    x.print_allNode()
    x.deletion_end()
    print("-----")
    x.print_allNode()
    x.deletion_end()
    print("-----")
    x.print_allNode()
    print("-----")
    x.deletion_head()
    x.print_allNode()
    print("-----")
    x.deletion_at_n(2)
    x.print_allNode()
