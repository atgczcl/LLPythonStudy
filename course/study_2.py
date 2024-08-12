from LLoghelper.log_helper import log, logger, LogHelper
# import study_1
import numpy as np


def study_2():
    log.info("study_2 is running")
study_2()
# 斐波那契数列
def fib(n):
    a, b = 0, 1
    #存储结果
    fb = []
    for _ in range(n):
        a, b = b, a + b
        fb.append(a)
    return fb
# print(fib(1000))
# 354224848179261915075
i = 1024*1024
print(i//1024, end="|")
log.critical("哈哈哈哈哈，我是日志")
while i > 0:
    i = i // 2
    # print(i)
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
x =isinstance(1, int)
print(x)
x = isinstance(1.0, int)
print(x)
y = isinstance(1.0, float)
print(y)
z = isinstance("hello", str)
print(z)
z = isinstance(log, LogHelper)
print(f"log is LogHelper: {z}")
z = isinstance(logger, LogHelper)
print(f"logger is LogHelper: {z}")

# del x, y, z
# print(f"logger is LogHelper: {z}")
"""
isinstance和type的区别在于：
    type（）不会认为子类是一种父类类型。
    isinstance（）会认为子类是一种父类类型。
    issubclass 是 Python 中的一个内建函数，用于检查一个类是否是另一个类的子类。这与 isinstance 类似，但它的用途是针对类而不是实例
"""

# 1.0是浮点数，不是整数，所以返回False。
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

print("Using issubclass:")
print(issubclass(Dog, Mammal))      # 输出: True
print(issubclass(Dog, Animal))     # 输出: True
print(issubclass(Dog, (Mammal, Animal)))  # 输出: True
print(issubclass(Dog, int))         # 输出: False
# isinstance() 与 type() 区别
dog = Dog()
print("Using isinstance:")
print(isinstance(dog, Dog))       # True
print(isinstance(dog, Animal))    # True
print(isinstance(dog, object))    # True

print("Using type:")
print(type(dog) is Dog)           # True
print(type(dog) is Animal)        # False
print(type(dog) is object)        # False

"""
3、数值的除法（/）总是返回一个浮点数，要获取整数使用​//​操作符。
4、在混合计算时，Python 会把整型转换成为浮点数。
"""
x, y, z = 11, 2, 3
print(f"x = {x}, y = {y}, z = {z}")
#加法
print(f"x + y = {x + y}")
#减法
print(f"x - y = {x - y}")
#乘法
print(f"x * y = {x * y}")
#除法，得到一个浮点数
print(f"x / y = {x / y}")
#整除，得到一个整数
print(f"x // y = {x // y}")
#取余
print(f"x % y = {x % y}")
#取幂
print(f"x ** y = {x ** y}")
#比较大小，得到一个布尔值
print(f"x < y = {x < y}")
#赋值
x = 2
print(f"x = {x}")
#布尔值
print(f"not x = {not x}")
#逻辑与逻辑或逻辑非 ，得到一个布尔值
print(f"x and y = {x and y}")
print(f"x or y = {x or y}")
print(f"x is y = {x is y}")
print(f"x is not y = {x is not y}")

s = "Yes, I am a student\"t"
print(f"s = {s}")
print('C:\some\name')
print(r'C:\some\name')
# 转义字符
print('C:\\some\\name')
print("""
This is the first line.
This is the second line.
This is the third line.
""")
print("""
This is the first line.
This is the second line.
This is the third line.
""", end="")
print()
# 字符串的拼接
a = "hello"
b = "world"
c = a + b
print(c, log_level=logger.WARN)
print(c, log_level=logger.DEBUG)
print(c, log_level=logger.INFO)
print(c, log_level=logger.ERROR)
print(c, log_level=logger.CRITICAL)

 
# r = [round(i*0.2, 2) for i in range(0, round(100/0.2)+1)]
# print(r)

# 列表推导式
l1 = [i for i in range(1, 10)]
print(l1)
# 列表推导式
l2 = [i for i in range(1, 10) if i % 2 == 0]
print(l2)
# 列表推导式
l3 = [i for i in range(1, 10) if i % 2 == 0 if i % 3 == 0]
print(l3)
# 如果一个文本字符串在一行放不下, 可以使用圆括号来实现隐式行连接
x = ('这是一个非常长非常长非常长非常长 '
     '非常长非常长非常长非常长非常长非常长的字符串')
print(f"content = {x}", log_level=logger.DEBUG)

# 字典推导式
d1 = {i: i**2 for i in range(1, 10)}
print(d1)
# 字典推导式
d2 = {i: i**2 for i in range(1, 10) if i % 2 == 0}
print(d2)
# 字典推导式
d3 = {i: i**2 for i in range(1, 10) if i % 2 == 0 if i % 3 == 0}
print(d3)

#列表
ll = list()
print(ll)
#列表
ll = list(range(1, 10))
print(ll)
#列表是写在方括号之间、用逗号分隔开的元素列表
a = [1, 2, 3, "him", "tom", "jerry"]
print(a)
b = [1, 2, 3, "him", "tom", "jerry"]
print(a+b)
# 元组也支持用 + 操作符， 虽然 tuple 的元素不可改变，但它可以包含可变的对象，比如 list 列表。
tup1, tup2 = (1, 2, 3), (4, 5, 6, a, b)
a.append("你好中国！")
print(tup1 + tup2)
# print(tup1 - tup2)
# 集合（set）是一个无序不重复元素的集。
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose', 1}
print(student)   # 输出集合，重复的元素被自动去掉
# 集合支持交集、并集、差集等操作
# 集合（set）是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
a = {1, 2, 3, 1, 2}
b = {2, 3, 4}
print(f"a = {a}, b = {b}")
print(a & b)   # 输出交集
print(a | b)   # 输出并集
print(a - b)   # 输出差集
print(a ^ b)   # 输出对称差集
# 集合推导式
s1 = {i for i in range(1, 10)}
print(s1)
# 集合推导式
s2 = {i for i in range(1, 10) if i % 2 == 0}
print(s2)
# 集合推导式
s3 = {i for i in range(1, 10) if i % 2 == 0 if i % 3 == 0}
print(s3)

tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
print(f"Jack's number is {tel.items()}")

# 创建一个空集合必须用 set() 而不是 { }，因为{ }是用来创建一个空字典。
s1 = set()
d1 = {}
print(f"s1 = {s1}, d1 = {d1}, type(s1) = {type(s1)}, type(d1) = {type(d1)}, {type(s1) == type(d1)}")

# 字典是一种映射类型（mapping type），它是一个无序的键值对（key-value）集合。
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(f"t1 = {t1}, t2 = {t2}, t1 == t2 = {t1 == t2}")
# 元组是不可变的，所以它们的元素不能被修改。
t1 = (1, 2, 3)
t2 = t1 + (4, 5, 6)
print(f"t1 = {t1}, t2 = {t2}, t1 == t2 = {t1 == t2}")
# 列表是可变的，所以它们的元素可以被修改。
l1 = [1, 2, 3]
l2 = l1 + [4, 5, 6]
print(f"l1 = {l1}, l2 = {l2}, l1 == l2 = {l1 == l2}")

# 所有比较运算符返回 1 表示真，返回 0 表示假。这分别与特殊的变量 True 和 False 等价。注意：True和False的首字母为大写。
print(True and False)
print(True or False)
print(not True)
print(True == 1)
print(False == 0)
# is 和 is not 运算符用来比较两个变量引用的对象是否相同，但不能比较两个变量的值。
# print(True is 1)
# print(False is 0)
# print(True is not 1)
# print(False is not 0)

'''
对于整数 (int) 类型，Python 支持无限长度的整数表示，只要系统有足够的内存。
对于浮点数 (float) 和复数 (complex) 类型，由于它们基于硬件支持的浮点表示，所以是有固定精度限制的。
如果你需要处理非常大的数字或者需要高精度的数学运算，Python 的整数类型是一个很好的选择。而对于需要更高精度的浮点运算，你可能需要考虑使用第三方库如 decimal 或 mpmath。
对于字符串 (str) 类型，Python 使用 Unicode 编码，支持多种字符集。
对于布尔值 (bool) 类型，只有两个值 True 和 False。
对于空值 (NoneType) 类型，它只有一个值 None。
'''
# 二进制b, 八进制o, 十六进制x，可以用0b, 0o, 0x开头，都小写
x = 0b1010
# print输出保留原进制
print(x)
print(bin(x))
# 八进制
x = 0o123
print(x)
print(oct(x))
# 十六进制
x = 0x123abc
print(x)
print(hex(x))
print(chr(65))
print(ord('A'))
print(ord('中'))
print(len('hello world'))
print('hello world'[0])
print('hello world'[6])
print('hello world'[-1])
print('hello world'[-6])
print('hello world'.upper())
print('hello world'.lower())
print('hello world! you are a good boy! capitalize='.capitalize()) #使字符串的第一个字符大写，其余字符小写 case.
print('hello world title='.title()) #使每个单词的第一个字母大写，其余字母小写 case.
print('Hello World swapcase='.swapcase()) #大小写互换 case.
print('hello world'.replace('l', 'L'))
print('hello world'.split()) #默认以空格分割
print('hello world'.split('l')) #以l分割
print('hello world'.startswith('he')) #以he开头
print('hello world'.endswith('ld')) #以ld结尾
print('hello world'.find('l')) #查找l的位置，不存在返回-1
print('hello world'.find('L')) #查找L的位置，不存在返回-1
print('hello world'.count('l')) #统计l的个数
print('hello world'.count('L')) #统计L的个数
print('hello world33 isalpha='.isalpha(), "isalpha") #是否全为字母
print('hello world'.isalnum()) #是否全为 字母数字 字符串
print('hello world'.isdigit()) #是否全为数字字符串
print('hello world'.isspace()) #是否全为空格字符串
print('hello world istitle='.istitle()) #是否每个单词的第一个字母大写，其余字母小写
print('hello world'.islower()) #是否全为小写字符串
print('hello world'.isupper()) #是否全为大写字符串
print('hello world'.isnumeric()) #是否全为数字字符串
print('hello world'.isprintable()) #是否全为可打印字符串
print('hello world'.isidentifier()) #是否是合法的标识符
print('hello world'.isdecimal()) #是否全为十进制字符串
print('hello world join='.join(['H', 'e', 'l', 'l', 'o'])) #以指定字符连接字符串
print('hello world center='.center(200, '*'))    # 字符串居中，并在两侧填充指定的字符
print('hello world ljust='.ljust(20, '*'))   # 字符串左对齐，并在右侧填充指定的字符
print('hello world '.rjust(20, '*'))   # 字符串右对齐，并在左侧填充指定的字符
print('hello world'.zfill(20))  # 字符串左侧填充0，长度为指定长度
print('hello {0}'.format('world'))  # 字符串格式化
print('hello world'.format_map({'name': 'world'})) # 字符串格式化
print('hello world'.isascii()) #是否全为ascii字符串
print('hello world'.encode('utf-8'))
print('hello world'.encode('ascii', 'ignore'))

# 按位运算符是把数字看作二进制来进行计算的。
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0
c = a & b  # 12 = 0000 1100
print(c)
c = a | b  # 61 = 0011 1101
print(c)
c = a ^ b  # 49 = 0011 0001 运算符 ^ 按位异或 不同为1，相同为0
print(c)
c = ~a  # -61 = 1100 0011 按位取反 0变1，1变0
print(c)
c = b >> 2  # 240 = 1111 0000
print(c)
c = c << 2  #  15 = 0000 1111
print(c)
c = a >> 2  # 15 = 0000 1111
print(c)
# 正数的原、反、补码都一样，0的原码跟反码都有两个，因为这里0被分为+0和-0。 
# 负数的反码是符号位不变，其余各位取反。
# 负数的补码是反码+1。
print(bin(-5)) # 负数
print(bin(~5)) # 取反
print(bin(~-5)) # 取反再加1
print(bin(~0b1010))
print(bin(~0b1010 + 1))
# 逻辑运算符
a = True
b = False
c = a and b  # 逻辑与运算
print(c)
c = a or b  # 逻辑或运算
print(c)
c = not a  # 逻辑非运算
print(c)
# 成员运算符
l = [1, 2, 3]
if 1 in l:
    print('yes')
else:
    print('no')
# 身份运算符
a = 'hellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohello'
b = 'hellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohello'
'''在 Python 中，对于小字符串（通常长度小于 20 个字符）,Python 会缓存这些字符串的实例，以便在多次使用相同的字符串时能够重用同一个对象，从而节省内存和提高效率。这是因为字符串在 Python 中是不可变的，一旦创建就不能改变。
'''
print(id(a), id(b), (id(a)==id(b)))  # 打印变量的内存地址
print(a is b)
print(a == b)
# 运算符优先级
# 算术运算符
# 幂运算符
# 乘方运算符
# 除法运算符
# 加法运算符
# 减法运算符
# 位运算符
# 赋值运算符
# 比较运算符
# 逻辑运算符
# 成员运算符
# 身份运算符
# 运算符优先级：从高到低依次为：
# 1. 圆括号 ()
# 2. 乘方 **
# 3. 乘除法 * / // %
# 4. 加减法 + -
# 5. 位运算符 << >> & | ^
# 6. 比较运算符 < <= > >=
# 7. 等于运算符 ==!=
# 8. 逻辑运算符 not and or
# 9. 成员运算符 in
# 10. 身份运算符 is is not, is 是判断两个标识符是不是引用自一个对象
# 11. 赋值运算符 = += -= *= /= //= %= **= <<= >>= &= ^= |=

# Python 3.8 引入了 := 运算符，它可以将赋值表达式的结果赋值给一个变量，并返回该变量的值。
# 海象操作符
print(x := 11)
print(f"x = {x}")

if x:=20 <=203:
    print(f"x = {x}")

# is 判断两个变量是否引用同一个对象
a = [1, 2, 3]
b =  [1, 2, 3]
if a is b:
    print("a is b")
else:
    print("a is not b")

print(a in b)
print(id(a) == id(b))

# 矩阵乘

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.dot(a, b)
print(f"矩阵乘法：{c}")
 
# 矩阵求逆
a = np.array([[1, 2], [3, 4]])
b = np.linalg.inv(a)
print(f"矩阵求逆：{b}") 

# 矩阵的特征值和特征向量
a = np.array([[1, 2], [3, 4]])
w, v = np.linalg.eig(a)
print(f"矩阵的特征值：{w}") 
print(f"矩阵的特征向量：{v}") 


# 列表推导式
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i for i in a if i % 2 == 0]
print(b)
print(max(b))
'''
&按位与 AND
^按位异或 XOR
|按位或 OR'''

a = 0b1010
b = 0b1100
c = a & b # AND不能用

#lambda 表达式
lambda x: x**2
print((lambda x: x**2)(3))
# # 匿名函数
# def f(x): return x**2
# print((lambda x: x**2)(3))
# # 匿名函数
# f = lambda x: x**2
# print(f(3))
# # 匿名函数
# f = (lambda x, y: x+y)
# print(f(10, 20))
# # 匿名函数
# f = (lambda x, y=10: x+y)
# print(f(10))
# # 匿名函数
# f = (lambda *args: sum(args))
# print(f(10, 20, 30))
# # 匿名函数
# f = (lambda **kwargs: kwargs['a'] + kwargs['b'])
# print(f(a=10, b=20))
# # 匿名函数
# f = (lambda a, b, c: a+b+c)
# print(f(*[10, 20, 30]))
# # 匿名函数
# f = (lambda a, b, c: a+b+c)

# 复数 3.14j
c = 3.14j
print(c.real)
print(c.imag)

# 字符串格式化
print("Hello, {0}!".format("world"))
print("Hello, {name}!".format(name="world"))
print("Hello, {0} {1}!".format("world", "python"))
print("Hello, {0} {name}!".format("world", name="python"))
print("Hello, {name} {0}!".format("world", name="python"))
print("Hello, {0:.2f}!".format(3.1415926))
print("Hello, {0:*^20}!".format("world"))
print("Hello, {0:*^20}!".format("world"))
print("Hello, {0:*^20}!".format("world"))
print("Hello, {0:*^20}!".format("world"))
