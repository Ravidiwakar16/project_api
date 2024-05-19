def do_more_things(a, b):
    a = "hello world"
    b = 1
    # Do more things with a and b, or return them if this is the final step
    return a, b

# Example of calling the function
result_a, result_b = do_more_things(2,3)
print(result_a, result_b)

#decorator program
def decorator_func(func):
    def wrapper_func():
        print("Hiiii wrapper func")
        return func()
    print("decorator func worked")
    return wrapper_func

def show():
    print("show func")

decorator_show = decorator_func(show)
decorator_show()

@decorator_func
def display():
    print("display")
display()    


#Generator example
def sqr(n):
    for i in range(1,n+1):
        yield i*i
a = sqr(3)
print(next(a))    
print(next(a))  
print(next(a))  


#iterator example
a = iter(['A','B','D'])
print(next(a))    
print(next(a))  
print(next(a)) 


#Inheritance
class A:
    def show(self):
        print("Hiiiii")
class B(A):
    def display(self):
        print("display")

D = B()
D.show()
D.display()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"My name is {self.name}. I am {self.age} years old.")
c = Person("Nitin",23)
c.info()

#print dictinary key
d = {'A': 1, 'B': 2, 'C': 3}
x = d.keys()
print(list(x))

#wap to n prime number where n is integer imported by user


a = int(input("enter the number"))
flag = False
if a > 1:

    for i in range(2,a):
        if a % i == 0:
            flag = True
            break
    if flag:
        print(a, "not prime number")
    else:
        print(a,"prime number")   

# WAP factorial number

num = 7

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


#Python Program to Print the Fibonacci sequence
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#palindrome program

a = input("enter the elemenet")
b = a[::-1]
if (a==b):
    print("palindrome")
else:
    print("not palindrome")
        

