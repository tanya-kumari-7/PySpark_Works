# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''factorial function '''

def factorial(number):
    num=1
    for x in range(1,number+1):
        r=num*x
        num=r
    print(num)

factorial(20)
########################################ss

##############################
#######################################################

''' 
1. Write a Python function that takes a list of numbers and returns the largest number 
and smallest in the list.
'''

list1=[100,400,5,9,20]

# Method 1 using sort
list1.sort(reverse=True)
print("{} is the largest number is the list".format(list1[0]))
print("{} is the Smallest number is the list".format(list1[-1]))

# Method 2 using loop
largest=0
smallest=0
for x in list1:
    if x > largest:
        largest=x
    if x < largest:
            smallest=x

print("{} is the largest number is the list".format(largest))
print("{} is the Smallest number is the list".format(smallest))



'''
2. Write a Python function that takes a string as input and returns the reverse of that 
string.
'''

# Method 1 using index
def reverse_str(name):
    reverse_str=name[::-1]
    print('Reverse of {} is {}'.format(name,reverse_str))
    
reverse_str('sonamtanya')

# Method 2 using loop
def reverse_str2(name2):
    reverse_str2=''
    for x in name2:
        y=x+reverse_str2
        reverse_str2=y
    print('Reverse of {} is {}'.format(name2,reverse_str2))    
reverse_str2('Gauravtanya')
        
# Metod 3 using reverse function---------------
def reverse_str3(name):
    reverse_str3=''.join(reversed(name))
    print('Reverse of {} is {}'.format(name,reverse_str3))

reverse_str3('sony')


'''
3. Write a Python function that takes a list of numbers and returns a new list containing 
only the even numbers from the original list.
'''

list1
def enter_your_number(x):
    list_of_even=[]
    list_of_odd=[]

    for i in x :
        if i % 2==0:
            list_of_even.append(i)
        else:
            list_of_odd.append(i)
    print('{} is the list of even numbers from the list1'.format(list_of_even))
    print('{} is the list of odd numbers from the list1'.format(list_of_odd))
enter_your_number(list1)

'''
4. add multiple values in the list and clarify diff between append and extend
'''

list1
list2=['800','1200','400','500','300','300']
list4=list2.copy()

# Used to copy a list from old list
list3=list1.copy()
# Append() wll add a new list in the old list where extend will 
# add only values in the new list from the old list
list1.append(list2) 
list3.extend(list2)
list3

'''
5. Write a Python function that takes a string as input and counts the frequency of each 
character. The function should return a dictionary where the keys are the characters and 
the values are their frequencies
'''
list2
list2.count('300') 


# count is used to get count it can also be used to count duplicated
def enter_your_str(x):
    dic={}
    for i in x:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    print(dic)                
enter_your_str('Gaurav')
       
'''
6. Write a Python program that generates the Fibonacci sequence up to a specified number n.
 The Fibonacci sequence is a series of numbers where each number is the sum of the 
 two preceding ones, usually starting with 0 and 1 
'''
# Method 1 using for loop
def fibonacci(x):
    d=[]
    a=0
    b=1
    for i in range(0,x+1): 
        d.append(a)
        c=a+b
        a=b
        b=c
    print('fibonacci of',x,'is',d )
fibonacci(10)

# method 2 using index
fibonacci_list=[0,1]
def fibonacci1(y):
    for i in range(2,y):
        r=fibonacci_list[-2]+fibonacci_list[-1]
        fibonacci_list.append(r)
    print(fibonacci_list)
print('fibonacci of is',fibonacci_list)

fibonacci1(20)

'''
7. Write a Python program that takes a list of numbers and removes any duplicate elements,
 keeping only the unique values. The program should then print out the list with duplicates 
 removed.
'''

list1
list1.append(229)

# method 1 using set type
list1
y=set(list1)
y

# Method 2 using for loop
list1
duplicate=[]
unique=[]
for x in list1:
    if x not in unique:
        unique.append(x)
    else:
        duplicate.append(x)
print('unique list is',unique)
print('duplicate list is',duplicate)

'''
8.Write a Python program that takes a list of numbers and returns a new list containing 
only the prime numbers from the original list.								                                                                								
'''
list2=[1,0,2,3,5,6,8,9,7]
prime_list=[]
not_prime_list=[]
for x in list2:
    if x > 1 :
        for i in range(2,x):
            if x % i ==0:
                not_prime_list.append(x)
                break
        else:
            prime_list.append(x)
    
print('im a prime list',prime_list)
print('im not a prime list',not_prime_list)


'''
9.Write a Python program that takes a list of strings and returns a new list 
containing only the strings that have more than and equal to 5 characters.
'''

list_str=['sonam','gaurav','saurav','sony','mony','shanu','nitin','manisha']
list_wid_more_than_5_char=[]
list_wid_less_than_5_char=[]
for i in list_str:
    if len(i) >= 5 :
        list_wid_more_than_5_char.append(x)
    else:
        list_wid_less_than_5_char.append(x)
print(list_wid_more_than_5_char)
print(list_wid_less_than_5_char)
								




















