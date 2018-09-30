class Stack:

  def __init__(self):
    self.length = int(input("Enter the length of the stack"))
    self.stack = []
    self.menu(self.length, self.stack)

  def push(self, l, stack):
    if(len(stack) == l):
      print("Cannot push in overflow condition")
      print(stack)
    else:
      e = input("Enter the element you want to push")
      self.stack.append(e)
      print(stack)

    return stack

  def pop(self, l, stack):
    if(len(self.stack) == 0):
      print("Cannot pop in underflow condition")
      print(stack)
    else:
      self.stack.pop()
      print(stack)

    return stack
    
  
  def menu(self, length, stack):
    print("\n1. Push\n2. Pop\n3. Exit")
    op = int(input("Choose an operation"))
    if op == 1:
      self.stack = self.push(self.length, self.stack)
      self.menu(self.length, self.stack)
    elif op == 2:
      self.stack = self.pop(self.length, self.stack)
      self.menu(self.length, self.stack)
    elif op == 3:
      exit()
    else:
      print("Choose a proper operation")

Stack()
      
