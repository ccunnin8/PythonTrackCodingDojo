"""
Find and Replace
In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

First and Last
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
"""

#find and replace
#words = "It's thanksgiving day. It's my birthday,too!"
#print words.index("day")
#new = words.replace("day","month")
#print new

#min and Max
# x = [2,54,-2,7,12,98]
# print min(x)
# print max(x)

#first and Last
# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[0]
# print x[-1]

#new list
# x = [19,2,54,-2,7,12,98,32,10,-3,6]
# x.sort()
# y = sorted(x)
# y = y[0:len(y)/2]
# print [y] + x[len(y):]

"""
Assignment: Multiples, Sum, Average
This assignment has several parts. All of your code should be in one file that is well commented to indicate what each block of code is doing and which problem you are solving. Don't forget to test your code as you go!

Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

Average List
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

#multiples
# for i in range(1,1000):
#     if not i % 2 == 0:
#         print i

# for i in range(5,1000001):
#     if i % 5 == 0:
#         print i


#sum list
# a = [1, 2, 5, 10, 255, 3]
# print sum(a)

#average list
# a = [1, 2, 5, 10, 255, 3]
# print sum(a) / float(len(a))

# def filterByType(item):
#     if type(item) == int:
#         if item >= 100:
#             print "That's a big number"
#         else:
#              print "That's a small number"
#     elif type(item) == str:
#         if len(item) >= 50:
#             print "Long sentence."
#         else:
#             print "Short sentence."
#     elif type(item) == list:
#         if len(item) >= 10:
#             print "Big list!"
#         else:
#             print "Short list."
# filterByType(45)
# filterByType(100)
# filterByType("Rubber baby buggy bumpers")
# filterByType([1,2,3,4,5,6,7,8,9,10])

####################
##TYPE LIST##
####################
#################

# def typeList(item):
#     string = ""
#     sum = 0
#     for x in item:
#         if type(x) == str:
#             string += x + " "
#         else:
#             sum += x
#     if sum > 0 and len(string) > 0:
#         print "The list you entered is of mixed type"
#         print "String: " + string
#         print "Sum: " + str(sum)
#     elif sum == 0:
#         print "This list you entered is of string type"
#         print "String: " + string
#     else:
#         print "The list you entered is of integer type"
#         print "Sum: " + str(sum)
# typeList(['magical unicorns',19,'hello',98.98,'world'])
# typeList([2,3,1,7,4,12])
# typeList(['magical','unicorns'])

####################
###Compare Lists######
#####################
#####################
# def compareList(l1,l2):
#     if len(l1) != len(l2):
#         print "The lists are not the same"
#         return False
#     else:
#         for index,item in enumerate(l1):
#             if item != l2[index]:
#                 print "The lists are not the same"
#                 return False
#     print "The lists are the same"
#     return True
#
#
# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]
# compareList(list_one,list_two)
# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]
# compareList(list_one,list_two)
# #copy<div id="copy-toolbar-container" style="cursor: pointer; position: absolute; top: 218.2px; right: 35px; padding: 0px 3px; background: rgba(224, 224, 224, 0.2); box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 0px 0px; color: rgb(187, 187, 187); border-radius: 0.5em; font-size: 0.8em;"><span id="copy-toolbar">copy</span></div>copy
# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]
# compareList(list_one,list_two)
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']
# compareList(list_one,list_two)

############
###FIND CHARACTERS#####
##################

# def findChar(l,c):
#     new_list = []
#     for word in l:
#         if c in word:
#             new_list.append(word)
#     return new_list
#
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
#
# print findChar(word_list,char)

#################
#######Checkerboard#####
# ############################
# def printCheckerboard():
#     for i in range(0,9):
#         line = ""
#         for y in range(1,9):
#             if i % 2 == 0:
#                 if y % 2 == 0:
#                     line += " "
#                 else:
#                     line += "*"
#             else:
#                 if y % 2 == 0:
#                     line += "*"
#                 else:
#                     line += " "
#         print line
# printCheckerboard()

#############
####Multiplication Table#####
#############################
#
# print "x 1 2 3 4 5 6 7 8 9 10 11 12"
# for i in range(1,13):
#     line = str(i) + " "
#     for y in range(1,13):
#         x = y * i
#         line += str(x) + " "
#     print line

####FOO AND BAR#####
#################################
############################
# def isPrime(x):
#     y = 2
#     while (y < x):
#         if x % y == 0:
#             return False
#         y += 1
#     return True
#
# def isPSquare(n):
#     x = n ** 0.5
#     return x % 1 == 0
#
# for i in range(100,100001):
#     output = ""
#     if isPrime(i):
#         output = "Foo"
#     elif isPSquare(i):
#         output = "Bar"
#     else:
#         output = "FooBar"
#     print(output)

###############TURTLE#########################
# try this either as a .py file or in the python shell
# import turtle
# # the distance we want the pointer to travel each time
# DIST = 100
# for x in range(0,6):
#     print("x", x)
#     for y in range(1,5):
#         print("y", y)
#         # turn the pointer 90 degrees to the right
#         turtle.right(90)
#         # advance according to set distance
#         turtle.forward(DIST)
#     # add to set distance
#     DIST += 20

########FUN WITH FUNCTION############
##############################
######
# def odd_even():
#     for i in range(1,2001):
#         if i % 2 == 0:
#             odd_or_even = "even"
#         else:
#             odd_or_even = "odd"
#         print("Number is {}. This is an {} number".format(i,odd_or_even))
# odd_even()
#
def multiply(args,a):
    return [x * a for x in args]

# print(multiply([1,2,3,4],5))

def layered_multiples(arr):
    new_arr = []
    for i in arr:
        x = [1] * i
        new_arr.append(x)
    return new_arr

print(layered_multiples(multiply([2,4,5],3)))
