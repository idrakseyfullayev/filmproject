# def x(n):
#     list_fib = [0,1]
#     n1 = 0
#     n2 = 1
#     for i in range(3, n+1):
#         n1, n2 = n2, n1+n2
#     return n2  

# print(x(7))

# x = "salam"
# c = x.split()
# print(c)
# y = list(x)
# print(y)

# string1 = "1,2,3,10"
# list2 = string1.split(",")
# print((list2))

# for i in range(0,len(list2)):

#     print(i)

# a = "s"
# print(a)
# b = 3
# print(a+b)
# x = 2
# c = 5
# print(x+c)


# org_list = [-1, 2, -3, 5, 7, 8, 9, -10]

# list_pos = list(filter(lambda x: x > 0, org_list))
# list_pos.sort()
# print(list_pos)
# list_neg = list(filter(lambda x: x < 0, org_list))
# list_neg.sort()
# print(list_neg)

# list1 = list_pos+list_neg
# print(list1)


# import datetime
# now = datetime.date.today()
# print(now)




# import datetime
# year = datetime.datetime.now()
# print(year)
# month = datetime.datetime.now().strftime("%m")
# day = datetime.datetime.now().strftime("%d")
# # now = datetime.datetime(int(year),int(month),int(day))
# print(now)

# print("You're looking at question %s." % (5))
# print("%s+%s=7" %(5,2))
# print(f"You're looking at question {5}.")
# print("You're looking at question {0}".format(5))


# def max_():
#     list1 = [1,2,7,10,15,0, 4]
#     max = list1[0]
#     for i in list1:
#         if i > max:
#             max = i
#             print(max)
   

#     return max

# print(max_())    


# def has_num_alpha_symbol(t):
#     num = "0123456789"
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     symbol = "~!@#$%^&*()_+:|\\/?><.,"
#     x = False
#     y = False
#     z = False
#     for i in t:
#         print(i)   # yd12>
#         if i in num:
#             x = True #true
#         if i in alpha:
#             y = True #true
#         if i in symbol:
#             z = True
#         if x == True and y == True and z ==True:
#             break
#     if x == True and y == True and z ==True:        
#         return True
#     else:
#         return False

# g = "12345e"        
# print(has_num_alpha_symbol(g.lower()))





