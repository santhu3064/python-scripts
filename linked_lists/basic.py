class Node():
   def __init__(self,data):
      self.data = data
      self.next = None

class LinkedList():
   def __init__(self):
      self.head = None

   def printlist(self):
      temp= self.head
      while temp:
         print(temp.data)
         temp = temp.next

   def add_node_at_end(self,n):
      newnode = Node(n)

      if self.head == None:
         self.head = newnode

      last = self.head

      while last.next:
         last = last.next

      last.next = newnode

   def add_node_at_start(self,n):
      newnode = Node(n)

      if self.head == None:
         self.head = newnode

      newnode.next = self.head
      self.head = newnode

   def add_node_between(self,n,prev):
      newnode = Node(n)

      newnode.next = prev.next
      prev.next = newnode


   def reverse(self):
      prev = None
      current = self.head

      while current:
         next = current.next
         current.next = prev
         prev = current
         current = next
      self.head = prev




if __name__ == "__main__":

   l = LinkedList()
   l.head = Node(1)
   l2 =Node(2)
   l3 = Node(3)
   l.head.next = l2
   l2.next = l3
   l.printlist()
   l.reverse()
   l.printlist()
   l.add_node_at_end(4)
   l.add_node_at_start(5)
   l.add_node_between(6,l2)
   l.printlist()



