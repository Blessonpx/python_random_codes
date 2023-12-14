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
    

if __name__== '__main__':
    print("Hello!")
    x= Node()
    x.set_data(5)
    y = Node()
    y.set_data(4)
    x.set_next(y)
    print(x.get_data())
    print(x.get_next().get_data())
