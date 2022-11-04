# s = "hello world"
# print(s[2:11:2])
# print(s[0:9:4])
# print(s[0:5:-2])
# print(s[5:5:1])

# print(s[-1:-12:-1])
# print(s[1:7:1])
# print(s[0:11:1])
# print(s[:11:])
# print(s[0:7:1])
# print(s[:7:])
# print(s[1:9:1])
# print(s[1:9:])
# print(s[4:11:1])
# print(s[4:11])
# print(s[0:11:6])
# s = "love you hero"
# print(s[0:11:5])
# print(s[-2:-5:-1])
# print(s[-2:-9:-1])
# print(s[-2:-9:-3])
# print(s[-1:-12:-5])
# print(s[-1:-8:-3])
# print(s[-1:-14:-1])
# print(s[:-14:-1])
'''s = "hello world"
print(s[-1:-10:-4])
print(len(s))
s2 = "10"
print (len(s2))
s3= ""
print(len(s3))
s4 = " "
print(len(s4))

s5 = "hello"
print(dir(s))

s6 = "hello world"
print(s.capitalize())

s7= "HELLO WORLD"
print(s7.capitalize())

s8 = "+hello@world"
print(s.capitalize())
s9 = "helloworld"
print(s9.isalpha())
s10 = "hello world"
print(s.isalpha())
s11 = "hello world123"
print(s.isalpha())
s12 = "abc"
print(s12.isalpha())
s13 = "123"
print(s13.isdigit())
s14 = "python123"
print(s14.isdigit())
s15 = "123.45"
print(s15.isdigit())

s16 = "hello123"
print(s16.isalnum())
s17 = "hello 123"
print(s17.isalnum())
s18 = "123"
print(s18.isalnum())
s19 = "hello"
print(s19.isalnum())
s20 = "+hello"
print(s20.isalnum())

s21 = '''
'''

print(s21.isspace())

s22 = "HeLLO123"
print(s22.upper())
s23 = " "
print(s23.upper())

s24 = "-hello123"
print(s24.islower())

s25 = "Hello"
print(s25.islower())

s26 = "python is a programming language"
print(s26.title())
s27 = "1Hello"
print(s27.istitle())

s28 = "Hello World"
print(s28.istitle())
s29 = "Python Is A Programmng"
print(s29.istitle())
s30 = "HELLO"
print(s30.upper())

s31 = "i'm a dev"
print(s31.title())
s32 = "hi@hello"
print(s32.title())

s33 = '123a'
print(s33.islower())

s34 = "Hello World"
print(s34)
s35 = "my world my rule"
print(s35.count('l'))
print(s35.count('r'))
print(s35.count('world'))
print(s35.count('my'))

print(s35.count('l',8))

print(s35.count('r',3,8))
print(s35.count(' '))
s36 = "python world"
print(s36.index('y'))
print(s36.index('o'))
print(s36.find('o', 5))
print(s36.find('y'))
print(s36.find('o', s36.find('o')+1))
print(s36.find('x'))
print(s36.find('h', s36.find('h')+1))
s37 = "hello baby how are you"
print(s37.find('e', s37.find('e')+1))

s38 = "hello, welcome to my world"
print(s38.rindex('e'))


s39 = "my world, my rule"
print(s39.rfind('world'))
print(s39.rfind('y'))
print(s39.rfind('my'))
print(s39.rfind('y', 6, 12))
print(s39.rfind('z'))

s40 = "50"
print(s40.zfill(10))

s41 = "hello"
print(s41.zfill(20))

s42 = "welcome to jungle"
print(s42.zfill(48))

s43 = "10.023"
print(s43.zfill(7))

s41 = "hello"
print(s41.zfill(10))

s42 = "yeswanth"
print(s42.center(20, "1"))

print(s41.zfill(20))
s45 = "yeswanth"
y = (s45.rjust(20))
print(y, "is my fv name")

s46 = "yeswanth"
print(s46.rjust(20,'1'))


s48 = "python is my world"
print(s48.startswith("my", 10, 12))
print(s48.startswith("wor", 13, 16))
s49 = "hello, welcome to my world"
print(s49.startswith("wel", 7, 10))

s50 = "hello, welcome to my world"
print(s50.endswith("hello,",0, 6))
print(s50.endswith("hello,"))

s51 = "hello world hello world"
print(s51.replace("world", "hi"))

s52 = "hello world"
print(s52.split())
print(s52.split('l'))
print(s52.split("l", 1))
print(s52.split("l", 2))
print(s52.split("l", 3))
s53 = "1234, 5678"
print(s53.split("."))
print(s53.split("1"))

# '''
# world
# print(s54.splitlines())
# print(s54.split(""))
# print(s54.splitlines(True))

# s55 = " hello yeswanth "
# print(s55.strip())

# s56 = "@@ hi yeswanth @@"
# print(s56.strip("@ "))
# print(s56.strip("@"))

# s57 = "hello is  hello"
# print(s57.strip("hello "))

# s58 = "hello", "world"
# print("@".join(s58))

# s59 = "hello", "[1,2,3]"
# ''print("@".join(s59))'''

# # s60 = '2 3 4', '5 6 7'
# # print("1".join(s60))
# # s58 = "hello  hh # world"
# # s58_en = (s.encode("utf-32"))
# # print(s58_en)
# # print(s58_en.decode("utf-32"))'

# # '''s = '''Dear {user}
# # your ticket has been booked
# # from {source} to {dest}''''



# print(s.format(user = "yeswanth", source = "nandyala", dest = "chennai"))

# s60 = '''Dear {}
# your ticket has been booked
# from {} to {}'''
# print(s60.format("yeswanth", "nandyala", "chennai"))

# user, source, dest = "yeswanth", "nandyala", "chennai"

# print(f''' Dear {user} 
# your ticket has been booked 
# from {source} to {dest}''')

# l = [1, 2.5,"yeswanth", [4,7]]
# print(l[2][4])
# print(l[3][1])
# print(l[-2][-3])
# print(l[3][1])
# print(l[:3:])	

# s100 = "hello"
# print(s100.isalpha


s = "yeswanth123"
for i in s:
	if not(i.isalpha() and i.islower()):
		print('invalid')
		break
	print("done")	

l = [1,2,0,3,0,4,0,5]
j = 0
for i in range(len(l)):
	if l[i] != 0:
		l[j],l[i] = l[i], l[j]
		j = j+1
print(l)

l = [1,2,3,4,5,6]
for i in range(0, len(l), 2):
	l[i], l[i+1] = l[i+1], l[i]
print(l)

l = [1,2,1,3,2,2,1]
l1 = []
for i in range(len(l)):
	for j in range(i+1, len(l)):
		if l[i] == l[j]:
			l1.append(l[j])
print(list(set(l1)))


l = [1,2,3,4,2,3,2,3,2]
d = {}
for i in l:
	d[i] = l.count(i)
print(d)

l = [1,2,3,4,5,6]
def even(l):
	for i in l:
		if i%2 == 0:
			yield i
x = even(l)
# print(next(x))
# print(next(x))	
# print(next(x))
# print(next(x))		
for i in x:
	print(i)


		


