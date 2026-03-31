# x = int(input("enter zero"))
# print(10/x)

try:
    x = int(input("enter zero"))
    print(10/x)
    print("ok man")
except:
    print("Error kajsfl")
finally:
    print("Always runs")

# try:
#     x = int(input())
#     print(10/x)
# except ZeroDivisionError:
#     print("Divide by zero")
# except ValueError:
#     print("Invalid input")


# try:
#     x = int(input())
# except:
#     print("Error")
# finally:
#     print("Always runs")

# class MyError(Exception):
#     pass

# def check(age):
#     if age < 18:
#         raise MyError("Not allowed")

# try:
#     a = int(input())
#     b = int(input())
#     print(a/b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Invalid input")
# finally:
#     print("Done")