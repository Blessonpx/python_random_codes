class Node:
    def __init__(self):
        self.data=None
        self.next=None
        self.prev=None
    def set_data(self,data):
        self.data=data
    def get_data(self):
        return self.data
    def set_next(self,node):
        self.next=node
    def get_next(self):
        return self.next
    def set_prev(self,node):
        self.prev=prev
    def get_prev(self):
        return self.prev
    
class DlinkList:
    def __init__(self):
        self.head=None
    def return_head(self):
        return self.head
    def set_head(self,node):
        self.head=node
    def print_all_node(self):
        curr_node=self.head
        print(curr_node.get_data())
        while(curr_node.get_next!=None):
            curr_node=curr_node.get_next()
            print(curr_node.get_data())

if __name__=='__main__':
    x=DlinkList()
    n1=Node()
    n1.set_data("Mon")
    x.set_head(n1)
    x.print_all_node()