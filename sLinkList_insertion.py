class Node:
    def __init__(self):
        self.data=None
        self.next=None
    
    def set_data(self,data):
        self.data=data
    def get_data(self):
        return self.data
    def set_next(self,next):
        self.next=next
    def get_next(self):
        return self.next
    


class SLinkList:
    def __init__(self,node):
        self.head=node

    def return_head(self):
        return self.head 

if __name__ == '__main__':
        j=SLinkList("Mon")
        y=Node()
        y.set_data("Tue")
        j.head.next=y
        print("Node print")
        print(j.head.get_data())
        print(j.head.next.get_data())