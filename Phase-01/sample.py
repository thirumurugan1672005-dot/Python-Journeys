price = -12.345667
ans = '%.2f' % price
print(ans)

#width and sign prrecision
ans = "%+09.2f" % price
print(ans)

#dynamic values
ans = "%.*f" % (2,1.3334)
print(ans)

# Dictionary
ans = "%(qty)s" % ({'qty':12})
print(ans)


ans = "My name is {}. My age is {}".format("ravi",32)
print(ans)

ans = "I bought a pen with a price {:.2f}".format(63.345)
print(ans)

# indexes
num = [1,2,3,4]
ans = "{0[0]}".format(num)
print(ans)

# keys
student = {'name':'Ravi','age':32}
ans = "{0[name]}".format(student)
print(ans)

ans = "{student[age]}".format(student=student)
print(ans)

ans = "%o" % 23
print(ans)
ans = "%x" % 23
print(ans)

ans = "{:x} {:o}, {:b} ".format(23,23,23)
print(ans)


name = 'Ravi'
age = 22
print(f"My name is {name} and My age is {age}")

price = 23.34567
print(f"{price:.2f}")

