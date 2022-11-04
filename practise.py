# s = "i am yeswanth"
# print(s[3:8:1])
# print(s[5:13:1])
# print(s[:4:])
# print(s[0:8:1])
# print(s[0:10:2])
# print(s[0:8:2])
# print(s[5:11:2])
# print(s[0:11:5])
# print(s[-1:-9:-1])

# s = "hello world"
# print(s[0:5:1])
# print(s[0:5:2])
# print(s[-1:-10:-2])

# s1 = "yeswanth is a  boy"
# print(s1.find('a',s1.find('a')+1))
# s2 = "my world my rule"
# print(s2.rindex('e'))

# s3 = "Yeswanth"
# print(s3.zfill(22))
# s4 = "145"
# print(s4.zfill(45))

# s5 = "yeswanth"
# y = s5.rjust(20)
# print(y, "i love you")

# s6 = "yeswanth is a good boy"
# print(s6.startswith("y"))
# print(s6.startswith("e"))
# print(s6.startswith("y", 1, 10))
# print(s6.startswith("is", 9, 17))

# s7 = "hello welcome to world"
# print(s7.endswith("welcome", 6,13))

# s8 = "I love love you yeswanth"
# print(s8.replace("love", "hate",1))

# s9 = "hello yeswanth"
# print(s9.split("l"))
# print(s9.split("e"))
# s10 = '''hi
# hello 
# world'''
# print(s10.split("\n"))
# print(s10.splitlines(True))

# s11 = 'hello for yeswanth'
# print(s11.strip("yeswanth"))

# s58 = "hello", "world"
# print("@".join(s58))

# s12 = "hello", "yeswanth"
# print("@".join(s12))

# s13 = "[1,3,4]", "hello"
# print("&".join(s13))

# s14  = "[1,2,5]", "[9,8,7]"
# print("6".join(s14))

# s15 = "hello yeswanth"
# s15_en = s15.encode("utf-32")
# print(s15_en.decode("utf-32"))

# l = [1, 2, 3,"hello", [7,8]]
# print(l[2])
# print(l[3][2])
# print(l[3])
# print(l[4])
# print(l[4][1])

# l2 = [1,2,4,"hello",[3,5]]
# l2[3] = 100
# print(l2)
# l2[4] = "yeswanth"
# print(l2)

# l3 = [1,2,3,"hi",[3,5]]
# del l3[1]
# print(l3)
# del l3[2]
# print(l3)
# del l3[2]
# print(l3)

# l4 = [1,2,3]
# print(dir(l))

# l5 = [1,2,3]
# l5.append("hello")
# print(l5)
# l5.append([3,5])
# print(l5)

# l6 = [1,2,3,6,["hello"]]
# l6.insert(1,4)
# print(l6)
# l6.insert(2,[3,9])
# print(l6)
# l7 = [1,2,3]
# l7.extend("yeswanth")
# print(l7) 
# l7.extend([3,4])
# print(l7)

# l7.extend([1, "yeswanth",[3,4]])
# print(l7)
# l7.extend(["hero"])
# print(l7)

# l8 = [1,2,3,4,"hello",[3,8]]
# print(l8.pop(3))
# print(l8)
# print(l8.pop(4))
# print(l8)
# print(l8.pop(-1))
# print(l8)
# print(l8.pop())

# l9 = [1,2,3,7,3]
# l9.remove(2)
# print(l9)
# l9.remove(3)
# print(l9)

# l10 = [1,2,3,"hero",[4,7]]
# l10.reverse()
# print(l10)
# l11 = ["yeswanth"]
# l11.reverse()
# print(l11)
# l12 = [3,4,5,6]
# l12.sort()
# print(l12)
# l12.sort(reverse = True)
# print(l11)
# l13 = [1,2,4,["hi"]]
# l13.clear()
# print(l13)

# l14 = [1,2,"hi",6.7]
# print(l14.clear())

# l15 = [1,3,5,"hi",[5,6]]
# print(l15.index(3))

# a = 10,20
# print(34 not in a)

# x = range(6)
# for n in x:
# 	print(n)

# x = input("enter your name:")
# print(x)

# mylist = len("yeswanth")
# print(mylist)

# a = int(input("enter a number:"))
# print(a % 2)


'''l1 = [1,2,3]
print(id(l1))
l2 = l1
print(id(l2))
l2[2]= 100
print(l1)
print(l2)

t1 = (1,2,3)
print(id(t1))
t2 = t1
print(id(t2))
0
t1 = (1,10,3)
print(t1)
print(t2)'''

l1 = [1,2,3]
l2 = l1[0:3:1]
print(l1, id(l1))
print(l2, id(l2))
l1[1] = 100
print(l1)
print(l2)

