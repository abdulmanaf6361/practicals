l = [30,20,10]
print(type(l))
print(l)
l.append(40)
print(l)
l.insert(1, 15)
print(l)
l.extend([50,60])
print(l)


l.remove(20)
print(l)
l.pop()
print(l)
l.pop(1)
print(l)


l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)

print(l.count(10))
print(l)
print(l.index(30))
print(l)

l.clear()
print(l)