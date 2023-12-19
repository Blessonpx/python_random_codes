class Node:
    def __init__(self):
        self.data=None
        self.prev=None
        self.next=None
    def set_data(self,data):
        self.data=data
    def get_data(self):
        return self.data
    def set_prev(self,node):
        self.prev=node
    def get_prev(self):
        return self.prev
    def set_next(self,next):
        self.next=next
    def get_next(self):
        return self.next
    
class DLinkList:
    def __init__(self):
        self.head=None
    def return_head(self):
        return self.head    

if __name__=='__main__':
    Link = DLinkList()
    n1=Node()
    n1.set_data("Mon")
    Link.head=n1
    n2=Node()
    n2.set_data("Tue")
    x=Link.return_head()
    x.set_next(n2)
    n2.set_prev(x)
    print(x.get_data())
    print(x.get_next().get_data())

