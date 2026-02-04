#1. Write a program to print Hello World.
# print("hello world")

#2. Write a program to check whether a number is even or odd.
# num=7
# if num%2==0:
#     print("even")
# else:
#     print("odd")
# 3.Write a program to find the sum of two numbers.
# num1=3
# num2=6
# print("sum=",num1+num2)

# 4.Write a program to find the largest of three numbers.
# a=6
# b=2
# c=3
# if(a>b and a>c):
#     print(a)
# elif( b>c):
#     print(b)
# else:
#     print(c)
    

# 5.Write a program to check whether a number is positive, negative, or zero.
# a=0
# if(a>0):
#     print("positive")
# elif(a<0):
#     print("negitive")
# else:
#     print("zero")

#6. Write a program to print numbers from 1 to 10 using a loop.
# num=10
# for i in range(1,11):
#     print(i)

# 7.Write a program to calculate the factorial of a number.
# num=4
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)

# 8.Write a program to check whether a number is a prime number.
# num=7
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not prime")

# 9.Write a program to reverse a number.

# num=123
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)


#10. Write a program to count the digits in a number.
# num=123
# count=0
# while num>0:
#     count+=1
#     num//=10
# print(count)

# 11.Write a program to check whether a string is a palindrome.
# name="level"
# rev=""
# for i in name:
#     rev=i+rev
# if name==rev:
#     print("palindrom")
# else:
#     print("not a palindrom")

#12. Write a program to find the sum of elements in a list.
# list=[1,2,3,4,5]
# total=0
# for i in list:
#     total=total+i
# print("sum=",total)

# 13.Write a program to find the largest element in a list.
# lst=[10,25,5,40,15]
# largest=lst[0]
# for i in lst:
#     if i>largest:
#         largest=i
# print("largest=",largest)

#14. Write a program to remove duplicate elements from a list.
# lst=[1,2,1,3,1,4,1]
# newlist=[]
# for i in lst:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)

#15. Write a program to find the second largest number in a list.
lst=[10,20,30,40,50] 
largest=lst[0]
second=lst[0]
for i in lst:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print("secondlargest=",second)
#16. Write a program to count the frequency of characters in a string.

#17. Write a program to check whether a number is an Armstrong number.

# 18.Write a program to print the Fibonacci series.

# 19.Write a program to swap two numbers without using a third variable.

#20. Write a program to sort a list in ascending order.