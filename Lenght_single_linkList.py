class Length_List:

  def linkList_Length(self, head):
    current = head
    count = 0
    while (current != None):
      current = current.next
      count = count + 1
    return count
