#stack implementation without size limit
#Stack implementation
#1.list/Array  2.Linkedlist    

# class Name:
#     age =30          #data member
#     def display(self):   #method
#         print("Hello World")

# obj=Name()
# print(obj.age)
# obj.display()        

#Code 1 =  
# class Student:
    
#     def __init__(self):
#         self.name = "Isha"
#         self.age = 22

#     def display(self):
#         print("Name =", self.name)
#         print("Age =", self.age)

# stuObj = Student()

# stuObj.display()

#code2

# class Message:
#     def __init__(self):
#         print("I am constructor")
#     def shows(self):
#         print("Class program")
# obj = Message()


#Default Constructor
# # class Name:
#     age = 30
#     def display(self):
#         print("Hello World")

# obj = Name()
# print(obj.age)
# obj.display()


# class Student:
#     def __init__(self):
#         self.name ="prashant"
#         self.age =30

#     def display(self):
#         print("Name=",self.name)
#         print("Age=",self.age)
# stuObj = Student()
# print(stuObj)

# class Message:
#     def __init__(self):
#         print("I am constructor")
#     def shows(self):
#         print("Class program")

# obj = Message()        
# obj.show()
# obj2 = Message()

#Parmeterized Constructor
# class StudentInfo:
#     def __init__(self,name,age,roll_no):
#         self.Name = name
#         self.Age = age
#         self.RollNo = roll_no
#     def dsiplayStudentInfo(self):
#         print("Name",self.Name)
#         print("Age=",self.Age)

# studentobj = StudentInfo("Prakash",34,101) 
# studentobj.dsiplayStudentInfo()


# import sys

# class Stack:
#     def __init__(self):
#         self.myStack = []

#     def push(self, value):
#         self.myStack.append(value)
#         print("Element pushed")

#     def display(self):
#         print("Stack Elements:", self.myStack)

#     def isEmpty(self):
#         if self.myStack==[]:
#             return True
#         else:
#             return False   
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty")    
#         else:
#             print(self.myStack.pop())
#     def peek(self):
#         if self.isEmpty():
#             print("stack is empty")        
#         else:
#             print(self.mystack)[-1]
#     def deleteStack(self):
#         self.myStack=None        

# obj = Stack()
# while True:
#     print("\nStack has created:")
#     print("1. Push Operation")
#     print("2. Print Stack")
#     print("3. pop Operation")
#     print("4.Peek operation:")
#     print("4.Delete operation:")
#     print("6. Exit")

#     choice = int(input("Enter Your Choice: "))

#     if choice == 1:
#         value = int(input("Enter value to push in stack: "))
#         obj.push(value)

#     elif choice == 2:
#         obj.display()
#     elif choice==3:
#         obj.pop()
#         print("Pop successfully")
#     elif choice==4:
#         obj.peek() 
#         print("Peek succsessfully")
#     elif choice==5:
#         obj.deleteStack()


#     else: 
#         sys.exit()

#Now you have to implement stack with size limit
# ----------------------------------------------------------------------------    
#1.push
#2.Pop
# 3.peek
#4.isEmpty
#5.isFull
#6.Delete
#7.display

# import sys

# class Stack:
#     def __init__(self, size):
#         self.myStack = []
#         self.stacksize = size   # stack size defined

#     def isFull(self):
#         if len(self.myStack) == self.stacksize:
#             return True
#         else:
#             return False

#     def push(self, value):
#         if self.isFull():
#             print("Stack is Full")
#         else:
#             self.myStack.append(value)
#             print("Element pushed")

#     def display(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print("Stack Elements:", self.myStack)

#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False

#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print("Popped Element:", self.myStack.pop())

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print("Top Element:", self.myStack[-1])

#     def deleteStack(self):
#         self.myStack = []
#         print("Stack Deleted")


# size = int(input("Enter the size of stack: "))

# obj = Stack(size)

# while True:
#     print("\n--- Stack Menu ---")
#     print("1. Push Operation")
#     print("2. Print Stack")
#     print("3. Pop Operation")
#     print("4. Peek Operation")
#     print("5. Delete Operation")
#     print("6. Exit")

#     choice = int(input("Enter Your Choice: "))

#     if choice == 1:
#         value = int(input("Enter value to push in stack: "))
#         obj.push(value)

#     elif choice == 2:
#         obj.display()

#     elif choice == 3:
#         obj.pop()

#     elif choice == 4:
#         obj.peek()

#     elif choice == 5:
#         obj.deleteStack()

#     elif choice == 6:
#         print("Program Exited")
#         sys.exit()

#     else:
#         print("Invalid Choice")



#
mylist = [5,7,2,3,7,8,2,3,3]
newdict={}
for i in range(len(mylist)):
    count=0
    key=mylist[i]
    j=1
    while j<len(mylist):
      if key ==mylist[j]:
        count+=1
      j=j+1
    if count>1:
        newdict[key]=count
max=newdict
print(max)        