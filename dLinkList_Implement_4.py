class Node:
    def __init__(self):
        self.data=None
        self.prev=None
        self.next=None
        return self
    
    def set_data(self,data):
        self.data=data
        return self
    def set_prev(self,prev):
        self.prev=prev
        return self
    def set_next(self,next):
        self.next=next
        return self
    def get_data(self):
        return self.data
    def get_prev(self):
        return self.prev
    def get_next(self):
        return self.next

class DLinkList:
    def __init__(self):
        self.head=None
        return self
    def set_head(self,node):
        self.head=node
        return self
    def print_all_node(self):
        