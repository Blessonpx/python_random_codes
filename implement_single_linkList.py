class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self,data):
        self.data = data

    def get_data(self):
        return self.data
    
    def set_next(self,next):
        self.next = next
    
    def get_next(self):
        return self.next
    
    def has_next(self):
        return self.next != None
    
class Slinked_List:
    def __init__(self) :
        self.head=None
    
    def get_length(self):
        current = self.head
        count=0
        while current!=None:
            count=count+1
            current=current.get_next()
        return count
    

if __name__== '__main__':
    print("Hello!")
    List = Slinked_List()
    List.head = Node()
    List.head.set_data("Mon")
    n2=Node()
    n2.set_data("Tue")
    List.head.set_next(n2)
    n3=Node()
    n3.set_data("Tue")
    n2.set_next(n3) 
    x= Node()
    x.set_data(5)
    y = Node()
    y.set_data(4)
    x.set_next(y)
    print(x.get_data())
    print(x.get_next().get_data())
    print("Length--")
    print(List.get_length())
