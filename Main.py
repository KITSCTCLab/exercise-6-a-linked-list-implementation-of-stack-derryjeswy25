
  def pop(self) -> None:
    # Write your code here
     if(self.head is not None):
          self.head = self.head.next

  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here  
    ptr = self.head
    if(self.head is None):
        print("None")
    else:
        while (ptr):
            print(ptr.data, end="=>")
            ptr = ptr.next
        print("None")


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
