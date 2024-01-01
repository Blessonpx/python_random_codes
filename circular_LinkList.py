class Node:
    def __init__(self):
        self.data=None
        self.next=None

    def set_data(self,data):
        self.data=data
        return self
    def get_data(self):
        return self.data
    def set_next(self,node):
        self.next=node
        return self
    def get_next(self):
        return self.next
    
class CircleLinkList:
    def __init__(self):
        self.head=None
        
    def set_head(self,node):
        self.head=node
        return self
    def return_head(self):
        return self.head
    def print_all_node(self):
        currNode=self.head
        if currNode==None:
            print("NA")
        while(currNode.get_next()!=self.head):
            print(currNode.get_data())
            currNode=currNode.get_next()
        print(currNode.get_data())
    

if __name__=='__main__':
    c=CircleLinkList()
    c.set_head(Node().set_data("Mon"))
    c.return_head().set_next(Node().set_data("Tue"))
    c.return_head().get_next().set_next(Node().set_data("Wed"))
    c.return_head().get_next().get_next().set_next(c.return_head())
    c.print_all_node()
