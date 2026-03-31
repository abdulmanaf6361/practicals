# ⚡ Types of Arguments (Quick)
# Positional → add(2, 3)
# Keyword → add(a=2, b=3)
# Default → def add(a=2, b=3)
# Variable → *args, **kwargs


# def func(a,b):
#     print(a)
#     print(b)
#     return a+b

# c = func(1,20)
# print(c)

def add(*args):
    print(type(args))
    return sum(args)

print(add(1, 2, 3))
print(add(1, 2, 30, 40, 50))

print("\n")


def info(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs["name"])
    print(kwargs["age"])

info(name="kumar", age=21)

# def demo(*args, **kwargs):
#     print(args, kwargs)

# square = lambda x: x * x
# print(square(5))

# nums = [1, 2, 3]
# print(list(map(lambda x: x * 2, nums)))

# nums = [1, 2, 3, 4]
# print(list(filter(lambda x: x % 2 == 0, nums)))

# marks = [78, 90, 65, 88]

# print("Highest:", max(marks))
# print("Lowest:", min(marks))
# print("Average:", sum(marks)/len(marks))

# def func(a=10,b=20):
#     print(a)
#     print(b)
#     return a+b

# c = func(21)
# print(c)
# print("\n")
# c = func(5,25)
# print(c)
# print("\n")
# c = func(b=29)
# print(c)

# c = func()
# print(c)