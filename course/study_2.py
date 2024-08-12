from LLoghelper.log_helper import log, logger, LogHelper
# import study_1


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