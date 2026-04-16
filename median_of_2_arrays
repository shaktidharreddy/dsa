nums1 = input("enter list1 numbers :").split(",")
a = []
for i in nums1:
    a.append(int(i))
a.sort()
print(a)

nums2 = input("enter list2 numbers :").split(",")
b = []
for i in nums2:
    b.append(int(i))
b.sort()
print(b)


c = a+b
c.sort()

r = len(c)%2
q = int(len(c)/2)
if r==0:
    print((c[q-1] + c[q])/2)
else:
    print(c[q])
