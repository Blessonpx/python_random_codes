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
    def set_next(self,node):
        self.next=node
    def get_next(self):
        return self.next
    
class DLink_List:
    def __init__(self):
        self.head=None
    def set_head(self,node):
        self.head=node
    def get_head(self):
        return self.head
    def insert_end(self,node):
        cur_node=self.head
        while(cur_node.get_next()!=None):
            cur_node=cur_node.get_next()
        cur_node.set_next(node)
        node.set_prev(cur_node)
    def print_all_nodes(self):
        cur_node=self.head
        print(cur_node.get_data())
        while(cur_node.get_next()!=None):
            print(cur_node.get_data())
            cur_node=cur_node.get_next()
    

if __name__=='__main__':
    x=DLink_List()
    n1=Node()
    n1.set_data("Mon")
    x.set_head(n1)
    m2=Node()
    m2.set_data("Tue")
    x.insert_end(m2)
    m3=Node()
    m3.set_data("Wed")
    x.print_all_nodes()



    