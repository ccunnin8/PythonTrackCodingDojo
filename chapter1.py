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
