
# tuples are immutable and ordered data structure of python 
tupy1 = (1,3,4,8,2)
tupy = (7,6,4,8,2)
print(type(tupy))
print(tupy[1])
print(tupy[-1])
for t in tupy1:
  print(t, end = "")
for t in range(len(tupy1)):
  print(tupy[t])
subtp= tupy1[1:4]
print(subtp)
tup3 = tupy + tupy1
print(tup3)
print(tupy*3)
tup4 = list(tup3)
tup4.append("hey")
print(tup4)

