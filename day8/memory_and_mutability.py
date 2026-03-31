# x = 10
# print(id(x))

# x = x + 5
# print(id(x))

# lst = [1, 2]
# print(id(lst))

# lst.append(3)
# print(id(lst))


# # Mutable: list, dict, set
# # Immutable: int, str, tuple

# a = [1, 2]
# b = a
# print(b)
# print(id(a))
# print(id(b))
# b = [10, 20]
# print(id(a))
# print(id(b))
# print(a)
# print(b)


# def modify(lst):
#     lst.append(100)

# x = [1, 2]
# modify(x)
# print(x)

# def modify(a):
    
#     a = a + 10
#     print("inside", a)
#     return a

# a = 5
# a = modify(a)

# print(a)


# x = 5
# y = x
# y = 10
# print(x)

# a = [1]
# b = a
# b.append(2)
# print(a)

# a = [1, 2]
# b = a

# b = [10, 20]

# print(a)

# a = 10
# print(id(a))
# a = a+3
# print(id(a))

# l = [1, 2]
# print(id(l))
# l.append(3)
# print(id(l))