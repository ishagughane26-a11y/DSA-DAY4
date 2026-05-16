# 1.
# salary = int(input('Enter your salary :'))
# rating =int(input('Enter your performace appraisal rating:'))
# increment =0
# if rating >=1 and rating<=3:
#     increment = salary*10/100
# elif rating>=3.1 and rating<=4:
#     increment =salary*30/100
# elif rating>=4.1 and rating<=5:
#     increment =salary*40/100
# else:
#     print('Invalid rating') 
# print('Incremenmted salary:',increment+salary)     
# --------------------------------------------------------

# 2.
#basicsalary = 20000
# so we have to calculate the
#HRA of basicsalary = 20%
# TA of------------=30%
# DA of ----------=45%      
# calcilate grossSalary=?


# basicSalary = 20000

# HRA = basicSalary * 20 / 100
# TA = basicSalary * 30 / 100
# DA = basicSalary * 45 / 100

# grossSalary = basicSalary + HRA + TA + DA

# print("Basic Salary =", basicSalary)
# print("HRA =", HRA)
# print("TA =", TA)
# print("DA =", DA)
# print("Gross Salary =", grossSalary)    
#-----------------------------------------------------------

#Binary search

# def binarySearch(array,target):
#     low=0
#     high=len(array)-1
#     while low <=high:
#         mid=(low+high)//2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1            


# array =[2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
# target= 72
# result=binarySearch(array,target)
# if result==-1:
#     print("Element not found")
# else:
#     print("Element Found at",result)    


#Bubble sort
# def bubblesort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1): #j=0 ,j=1,..
#             if array[j] >array[j+1]:
#                 temp =array[j]
#                 array[j] =array[j+1]
#                 array[j+1]=temp
#             print(array)  
#         print()      

# array =[64,34,25,12,22,11,90]
# bubblesort(array)            


#Security key
mylist=[5,7,8,3,7,8,9,2,3]
newlist=[]
for i in range(len(mylist)):
    count=0
    key=mylist[i]
    j=i+1 #j=3
    while j<len(mylist):
         if key == mylist[j]:
              newlist.append(key)
         j=j+1
print(len(newlist))              
  
