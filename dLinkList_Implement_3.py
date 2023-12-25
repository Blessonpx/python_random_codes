class Node:
    def __init__(self):
        self.data=None
        self.prev=None
        self.next=None
    def set_data(self,data):
        self.data=data
        return self
    def get_data(self):
        return self.data
    def set_prev(self,prev):
        self.prev=prev
        return self
    def get_prev(self):
        return self.prev
    def set_next(self,next):
        self.next=next
        return self
    def get_next(self):
        return self.next
    
class DlinkList:
    def __init__(self):
        self.head=None
    def set_head(self,node):
        self.head=node
    def print_all_nodes(self):
        curr_node=self.head
        print(curr_node.get_data())
        while(curr_node.get_next()!=None):
            curr_node=curr_node.get_next()
            print(curr_node.get_data())
    def insert_end(self,node):
        curr_node=self.head
        while(curr_node.get_next()!=None):
            curr_node=curr_node.get_next()
        curr_node.set_next(node)
        node.set_prev(curr_node)
    def insert_start(self,node):
        node.set_next(self.head)
        self.head.set_prev(node)
        self.head=node
    def insert_n(self,node,n):
        curr_node=self.head
        i=1
        while(i<n):
            curr_node=curr_node.get_next()
            i=i+1
        tmp=curr_node.get_next()
        curr_node.set_next(node)
        node.set_prev(curr_node)
        node.set_next(tmp)
    def delete_head(self):
        tmp=self.head
        self.head=tmp.get_next()
        tmp.set_prev(None)
    
    def delete_end(self):
        curr_node=self.head
        while(curr_node.get_next()!=None):
            curr_node=curr_node.get_next()
        n_1_node=curr_node.get_prev()
        n_1_node.set_next(None)
        #curr_node.set_prev(None)

if __name__=='__main__':
    x=DlinkList()
    y=Node()
    y.set_data("Mon")
    x.set_head(y)
    x.insert_end(Node().set_data("Tue"))
    x.insert_start(Node().set_data("Sun"))
    x.insert_end(Node().set_data("Thu"))
    x.insert_n(Node().set_data("Wed"),3)
    #x.delete_head()
    x.delete_end()
    x.print_all_nodes()