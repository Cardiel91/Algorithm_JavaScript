# for num in range(1, 256, 1):
#     print(num)

# for num in range(5, 1000, 5):
#     print(num)

# for num in range(1, 100):
#     if (num % 5 == 0):
#         print('Coding')
#     elif (num % 10 == 0):
#         print('Coding Dojo')

# for num in range(0, 1000):
#     if (num % 2 == 1):
#         print(num)

# def countdown_by_fours():
#     for num in range(2018, 0, -4):
#         print(num)

# countdown_by_fours()

# def flex_counter(lowNum, highNum, mult):
#     for num in range(lowNum, highNum):
#         if num % mult == 0:
#             print(num)

# flex_counter(2, 9, 3)


# def a():
#     return 5
# print(a())

#2
# def a():
#     return 5
# print(a()+a())

# #3
# def a():
#     return 5
#     return 10
# print(a())

#4
# def a():
#     return 5
#     print(10)
# print(a())
#5
# def a():
#     print(5)
# x = a()
# print(x)


#6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

#7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

#8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
# 	    return 10
#     return 7
# print(a())

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])