import sys
from LLoghelper.log_helper import log, logger
# 随机
import random
import requests


logger.set_log_enable(True, False)
# 随机数
# random.seed(10)
# 生成一个随机整数
print(random.randint(1, 5))
# 生成一个随机浮点数
print(random.random())
# 生成一个随机浮点数
print(random.uniform(1, 5))
# 生成一个随机浮点数
#随机选一个数字
print ("从 range(100) 返回一个随机数 : ",random.choice(range(100)))
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.choice('W3CSchool'))
# 序列 sname[start : end : step]
sname = "W3CSchool"
print("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.choice(sname))
print("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.choice(sname[1:5]))
print("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.choice(sname[1:5:2]))
# 序列 sname[start : end : step]
sname = "W3CSchool"
print("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.sample(sname, 3))
print("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.sample(sname[1:5], 3))
print("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.sample(sname[1:5:2], 2))
# 序列 sname[start : end : step]
sname = "W3CSchool"
print("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.sample(sname, 3))
print("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.sample(sname[1:5], 3))
print("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.sample(sname[1:5:2], 2))
# 序列 sname[start : end : step]
sname = "W3CSchool"
print("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.sample(sname, 3))
print("从字符串中 'W3CSchool' 返回一个随机字符 : ", random.sample(sname[1:5], 3))



url = 'http://www.baidu.com'
# response = requests.get(url)
# print(response.text)

#数组乘法
a = [1, 2, 3]
b = [8,4, 5, 6]
c = a * 23
print(f"数组乘法: {c}")
print(sorted(c))

print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")
# 支持格式化字符串的输出
print("Hello, %s" % "world")
# 格式化字符串的输出
print("I'm %s. I'm %d year old" % ('Alice', 20))
# 格式化字符串的输出
print('I\'m learning "%s".' % 'Python')
# 格式化字符串的输出
print('The story of %s.' % 'Alice')
# 格式化字符串的输出
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
# 格式化字符串的输出
print('Hello, {name}, 成绩提升了 {percentage:.1f}%'.format(name='小明', percentage=17.125))
# 格式化字符串的输出
print('Hello, {name}, 成绩提升了 {percentage:.2f}%'.format(name='小明', percentage=17.1258))
# 格式化字符串的输出
print('Hello, {name}, 成绩提升了 {percentage:.3f}%'.format(name='小明', percentage=17.12589))

# pop也可以删除列表的最后一项。
# 语法：list.pop([index])
list1 = ["Google", "Runoob", "Taobao"]
list1.pop()
print(list1)

# 语法：list.remove(value)
list1 = ["Google", "Runoob", "Taobao"]
list1.remove("Runoob")
print(list1)


# 语法：list.clear()
list1 = ["Google", "Runoob", "Taobao"]
list1.clear()
print(list1)

# 嵌套列表的使用和数据结构和多维数组很像。实际上，python的列表可以当做其他语言的数组使用！
# 语法：list.extend(iterable)
list1 = ["Google", "Runoob", "Taobao"]
list2 = ["Baidu", "Sina"]
# list1.extend(list2)
list1 += list2
print(list1)
# 语法：list.append(value)
list1 = ["Google", "Runoob", "Taobao"]
list1.append("Baidu")
print(list1)
# 语法：list.insert(index, value)
list1 = ["Google", "Runoob", "Taobao"]
list1.insert(0, "Baidu")
print(list1)
# 语法：list.sort()
list1 = [5, 3, 8, 9]
list1.sort()
print(list1)

# 语法：list.reverse()
list1 = [5, 3, 8, 9]
list1.reverse()
print(list1)

# 语法：list.copy()
list1 = ["Google", "Runoob", "Taobao"]
list2 = list1.copy()
list2[0] = "Baidu"
print(list2)

# 语法：list.count(value)
print(list1)


# 语法：list.index(value, [start, [stop]])
list1 = ["Google", "Runoob", "Taobao", "Baidu", "Sina"]
print(list1.index("Runoob"))
print(list1.index("Runoob", 1))
print(list1.index("Runoob", 1, 4))


# 语法：list.count(value)
list1 = ["Google", "Runoob", "Taobao", "Baidu", "Sina", "Runoob"]
print(list1.count("Runoob"))
print(list1.count("Baidu"))
print(list1.count("Google"))

# 创建元组
tup1 = ('Google', 'W3CSchool', 1997, 2020)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
tup3 = ()

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
print ("tup3[1:5]: ", tup3[1:5])

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)
del tup3
tup3 = tup1*4
print (tup3)

# 将列表转换为元组。
list1 = [1, 2, 3, 4, 5]
tup1 = tuple(list1)
print (tup1)
# 比较两个元组是否相等。
if tup1 == tup2:
    print ("tup1 and tup2 are equal")
else:
    print ("tup1 and tup2 are not equal")

# 元组也可以使用切片操作。
tup1 = (1, 2, 3, 4, 5)
tup2 = tup1[1:5]
print (tup2)

# 字典的访问
dict1 = {'Alice': 20, 'Bob': 25, 'Charlie': 30}
print (dict1['Alice']) # 访问字典中键为'Alice'的值。
print (dict1.keys()) # 访问字典中所有的键。
print (dict1.values()) # 访问字典中所有的值。
print (dict1.items()) # 访问字典中所有的键值对。

# 字典的添加
dict1 = {'Alice': 20, 'Bob': 25, 'Charlie': 30}
dict1['David'] = 40
# dict1.add() # 字典添加元素，add()方法已废弃。
# dict1.append() # 字典添加元素，append()方法已废弃。
dict1.update({'Eve': 45}) # 字典更新元素。
print (dict1)


# 字典的获取
dict1 = {'Alice': 20, 'Bob': 25, 'Charlie': 30}
print (dict1.get('Alice'))
print (dict1.get('Tom')) # 字典中不存在'Tom'这个键,则返回None.
print (dict1.get('David', 40)) # 40为默认值,如果字典中不存在'David'这个键,则返回40.

# 字典的更新
dict1 = {'Alice': 20, 'Bob': 25, 'Charlie': 30}
dict1['Alice'] = 21
dict1['David'] = 40
print (dict1)

# 字典的删除
dict1 = {'Alice': 20, 'Bob': 25, 'Charlie': 30}
del dict1['Alice']
dict1.pop('Bob') # 删除并返回'Bob'的键值对。
dict1.popitem() # 删除并返回字典中的最后一对键值对。
# dict1.remove('Charlie') # 不存在remove()方法。
print (dict1)

# 字典的遍历
dict1 = {'Alice': 20, 'Bob': 25, 'Charlie': 30}
for key in dict1:
    if key == 'Alice':
        print (key, dict1[key])
    print (key, dict1[key])
result = {key: value*10 for key, value in dict1.items() if key == 'Alice'}
print(result)
print(f"Python 版本: {sys.version}{result} ")
# 字典的键值对遍历
dict1 = {'Alice': 20, 'Bob': 25, 'Charlie': 30}
for key, value in dict1.items():
    if key == 'Alice':
        print (key, value)

# 字典的合并
dict1 = {'Alice': 20, 'Bob': 25, 'Charlie': 30}
dict2 = {'David': 40, 'Eve': 45}
dict1.update(dict2)
print (dict1)

# 字典的排序
dict1 = {'Alice': 20, 'Bob': 25, 'Charlie': 30}
dict2 = {'David': 40, 'Eve': 45}
dict1.update(dict2)
print (dict1)
dict1 = dict(sorted(dict1.items()))
print (dict1) # 按照键排序

# 字典的复制
dict1 = {'Alice': 20, 'Bob': 25, 'Charlie': 30}
dict2 = dict1.copy()
dict2['Alice'] = 21
print (f"dict1: {dict1}")
print (f"dict2: {dict2}")
dict1 = {'Alice': 20, 'Bob': 25, 'Charlie': 30}
dict2 = dict(dict1)
dict2['Alice'] = 21
print (f"dict1: {dict1}")
print (f"dict2: {dict2}")

# Python 中的推导式是一种简洁的方式来创建新的列表、字典或集合，它们通常比传统的循环更高效和易读
# 推导式提供了一种更简洁、更直接的方式来创建列表、字典或集合。
# 推导式可以用来创建列表、字典或集合，而无需使用循环。
# 推导式可以用来过滤、映射、修改列表、字典或集合中的元素。
# 推导式可以用来简化代码，并提高代码的可读性。

# 列表推导式
# 语法：
# [expression for item in iterable if condition]
# 表达式：
# 表达式可以是任何有效的 Python 表达式，它会在循环中执行。
# 条件：
# 条件是可选的，它可以是一个表达式，返回值为布尔值，只有为 True 的元素才会被包含在结果中。

# 示例：
# 1. 计算列表中所有元素的平方
squares = [x**2 for x in range(1, 11)]
print(f"列表推导式: {squares}")

# 2. 计算列表中所有元素的平方，并过滤掉负数
squares = [x**2 for x in range(1, 11) if x >= 0]
print(f"列表推导式: {squares}")

# 3. 计算列表中所有元素的平方，并过滤掉偶数
squares = [x**2 for x in range(1, 11) if x % 2 == 1]
print(f"列表推导式: {squares}")

# 4. 计算列表中所有元素的平方，并将结果乘以 2
squares = [x**2*2 for x in range(1, 11)]
print(f"列表推导式: {squares}")

# 5. 计算列表中所有元素的平方，并将结果乘以 2，并过滤掉偶数
squares = [x**2*2 for x in range(1, 11) if x % 2 == 1]
print(f"列表推导式: {squares}")

# 6. 计算列表中所有元素的平方，并将结果乘以 2，并过滤掉负数
squares = [x**2*2 for x in range(1, 11) if x >= 0]
# squares.discard('d') # 列表没有discard()方法。
print(f"列表推导式: {squares}")

# 字典推导式
# 语法：
# {key_expression:value_expression for item in iterable if condition}
# 键表达式：
# 键表达式可以是任何有效的 Python 表达式，它会在循环中执行，并计算出每个元素的键。
# 值表达式：
# 值表达式可以是任何有效的 Python 表达式，它会在循环中执行，并计算出每个元素的值。
# 条件：
# 条件是可选的，它可以是一个表达式，返回值为布尔值，只有为 True 的元素才会被包含在结果中。

# 示例：
# 1. 计算字典中所有键的平方
squares = {x:x**2 for x in range(1, 11)}
# squares.discard() # 字典没有discard()方法。
print(f"字典推导式: {squares}")


# 集合推导式
# 语法：
# {expression for item in iterable if condition}
# 表达式：
# 表达式可以是任何有效的 Python 表达式，它会在循环中执行。
# 条件：
# 条件是可选的，它可以是一个表达式，返回值为布尔值，只有为 True 的元素才会被包含在结果中。


# 示例：
# 1. 计算集合中所有元素的平方
squares = {x**2 for x in range(1, 11)}
print(f"集合推导式: {squares}")

# 2. 计算集合中所有元素的平方，并过滤掉负数
squares = {x**2 for x in range(1, 11) if x >= 0}
print(f"集合推导式: {squares}")

# 3. 计算集合中所有元素的平方，并过滤掉偶数
squares = {x**2 for x in range(1, 11) if x % 2 == 1}
print(f"集合推导式: {squares}")

# 4. 计算集合中所有元素的平方，并将结果乘以 2
squares = {x**2*2 for x in range(1, 11)}
print(f"集合推导式: {squares}")

# 5. 计算集合中所有元素的平方，并将结果乘以 2，并过滤掉偶数
squares = {x**2*2 for x in range(1, 11) if x % 2 == 1}
print(f"集合推导式: {squares}")

text = "hello world"
unique_chars = {char for char in text if char != ' '}
unique_chars.discard('d')
print(unique_chars)  # 输出: {'d', 'e', 'h', 'l', 'o', 'r', 'w'}

s1 = set([1, 2, 3, 4, 5]) # 无序集合
s1.add(55) # 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
s1.remove(5) # 从集合 s 中删除元素 x，如果元素不存在，则会引发 KeyError 异常。
s1.discard(5) # 从集合 s 中删除元素 x，如果元素不存在，则不进行任何操作。
s1.pop() # 从集合 s 中删除并返回一个元素，如果集合为空，则会引发 KeyError 异常。
s1.clear() # 清空集合 s。
s1.discard(5) # 从集合 s 中删除元素 x，如果元素不存在，则不进行任何操作。
s1.add("Python")
print(f"集合: {s1}")
# update也可以添加元素，且参数可以是列表，元组，字典等 不能是单个数字55
thisset = set(("Google", "w3Cschool", "Taobao"))
thisset.update({1,3})
thisset.update({"Runoob":100})
thisset.update([99])
print(thisset)
thisset.update([1,4],[5,6])  
print(thisset)

# 队列
# 队列是一种线性数据结构，它只允许在队尾添加元素，在队头删除元素。
# 队列的操作有两种：入队和出队。
# 队列的应用：
# 1. 任务调度：任务调度是指将一组任务按照特定顺序进行调度，并在有限的时间内完成。队列可以用来实现任务调度，将任务按照先进先出（FIFO）的原则进行调度。
# 2. 广度优先搜索：广度优先搜索（BFS）是一种图形搜索算法，它通过一系列的节点来搜索图中的目标节点。队列可以用来实现广度优先搜索，将节点按照层次遍历的顺序进行访问。
# 3. 并发：并发是指两个或多个任务或进程在同一时间段内交替执行。队列可以用来实现并发，将任务按照先进先出（FIFO）的原则进行调度。


# 队列的实现
# 队列的实现有两种方式：列表和链表。
# 列表实现：
# 列表是一种线性数据结构，它可以用列表来实现队列。
# 列表的入队操作：
# 列表的 append() 方法可以用来入队。
# 列表的 pop(0) 方法可以用来出队。


# 链表实现：
# 链表是一种非线性数据结构，它可以用链表来实现队列。
# 链表的入队操作：
# 链表的 append() 方法可以用来入队。
# 链表的 pop(0) 方法可以用来出队。

t1 = (1, 2, 3, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

# match-case语句（python3.10新特性）
# 语法：
# match value:
#     case pattern1:
#         statement1
#         ...
#     case pattern2:
#         statement2
#         ...
#     case patternN:
#         statementN
#         ...
#     [optional]
#         else:
#             statement_else
# 匹配值：
# 匹配值可以是任何有效的 Python 表达式。
# 匹配模式：
# 匹配模式可以是任何有效的 Python 表达式，它会与匹配值进行比较。
# 语句：
# 语句可以是任何有效的 Python 语句，它会在匹配成功时执行。
# else语句：
# else语句是可选的，它会在所有匹配失败时执行。

# 示例：
# 1. 匹配数字
x = 5
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case _:
        print("x is not 1, 2, or 3")
# 输出: x is 5

# 2. 匹配字符串
x = "hello"
match x:
    case "hello":
        print("x is hello")
    case "world":
        print("x is world")
    case _:
        print("x is not hello or world")
# 输出: x is hello

# 3. 匹配列表
x = [1, 2, 3]
match x:
    case [1, 2, 3]:
        print("x is [1, 2, 3]")
    case [1, 2, *rest]:
        print(f"x is [1, 2, {rest}]")
    case [1, *rest, 3]:
        print(f"x is [1, {rest}, 3]")
    case _:
        print("x is not [1, 2, 3]")
# 输出: x is [1, 2, 3]

# 4. 匹配元组
x = (1, 0, 3)
match x:
    case (1, 2, 0):
        print("x is (1, 2, 3)")
    case (1, 2, *rest):
        print(f"x is (1, 2, {rest})")
    case (1, *rest, 3):
        print(f"x is (1, {rest}, 3)")
    case _:
        print("x is not (1, 2, 3)")
# 输出: x is (1, 2, 3)


# 5. 匹配字典 **rest表示匹配字典的剩余部分
x = {"name": "Alice", "age": 20}
match x:
    case {"name": "Alice", **rest}:
        print(f"x is not {rest} or {{'name': 'Bob', 'age': 25}}")  # 使用双大括号来避免格式化错误
    case {"name": "Alice", "age": 20}:
        print("x is {'name': 'Alice', 'age': 20}")
    case {"name": "Bob", "age": 25}:
        print("x is {'name': 'Bob', 'age': 25}")
    case _:
        print("x is not {'name': 'Alice', 'age': 20} or {'name': 'Bob', 'age': 25}")
# 输出: x is {'name': 'Alice', 'age': 20}

def guess_number_game(number):
    """
    猜数字游戏函数
    :param number: 要猜的数字
    """
    guess = -1
    print("猜数字!")
    
    while guess != number:
        try:
            guess = int(input("请输入你要猜的数字: "))
            if guess == number:
                print("你猜中了，真厉害！")
                break
            elif guess < number:
                print("猜小了，再猜猜？")
            else:
                print("猜大了，再猜猜？")
        except ValueError:
            print("请输入一个有效的整数！")

# 调用函数
# guess_number_game(7)

# 循环语句
# 1. for 循环
# 语法：
# for variable in iterable:
#     statement
# 变量：
# 变量可以是任何有效的 Python 变量名。
# 可迭代对象：
# 可迭代对象可以是任何可使用 for 循环的对象，如列表、元组、字符串、字典等。
# 语句：
# 语句可以是任何有效的 Python 语句，它会在每次迭代时执行。


# 2. while 循环
# 语法：while condition:
#     statement
# 条件：
# 条件可以是任何有效的 Python 表达式，它会在每次循环时计算。
# 语句：
# 语句可以是任何有效的 Python 语句，它会在每次循环时执行。


# 3. 循环控制语句
# 1. break 语句
# 语法：break
# 作用：
# 终止当前循环，并跳出循环体。


# 2. continue 语句
# 语法：continue
# 作用：
# 跳过当前循环的剩余语句，并开始下一次循环。


# 3. pass 语句
# 语法：pass
# 作用：
# 什么都不做，一般用做占位语句。


# 4. 循环中的 else 语句
# 语法：
# for variable in iterable:
#     statement
# else:
#     statement_else
# 作用：
# 循环正常结束时，执行 else 语句。


# 5. 循环中的 else 语句
# 语法：
# while condition:
#     statement
# else:
#     statement_else
# 作用：
# 循环正常结束时，执行 else 语句。 

# 示例：
# 1. for 循环
# 计算 1 到 10 之间的偶数的平方
squares = []
for x in range(1, 11):
    if x % 2 == 0:
        squares.append(x**2)
print(squares)

# 输出: [4, 16, 36, 64, 100]

# 2. while 循环 
# 计算 1 到 10 之间的偶数的平方
squares = []
x = 1
while x <= 10:
    if x % 2 == 0:
        squares.append(x**2)
    x += 1
print(squares)


# 输出: [4, 16, 36, 64, 100]

# 迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。。
# 迭代器是一种特殊的对象，它可以迭代访问集合元素，但它不存储集合元素。
# 迭代器的优点：
# 1. 节省内存，迭代器只存储当前迭代的元素，而不是整个集合。
# 2. 迭代器可以迭代集合元素的任意顺序，而不用事先知道集合的大小。
# 3. 迭代器可以迭代集合元素的同时，还可以对集合元素进行操作。
# 4. 迭代器可以对集合元素进行过滤、排序、映射等操作。
# 5. 迭代器可以用在 for 循环、while 循环、列表推导式、生成器表达式等。


# 迭代器的实现
# 1. 列表推导式
# 语法：
# [expression for item in iterable if condition]
# 表达式：
# 表达式可以是任何有效的 Python 表达式，它会在循环中执行。
# 条件：
# 条件是可选的，它可以是一个表达式，返回值为布尔值，只有为 True 的元素才会被包含在结果中。


# 2. 生成器表达式
# 语法：
# (expression for item in iterable if condition)
# 表达式：
# 表达式可以是任何有效的 Python 表达式，它会在循环中执行。
# 条件：
# 条件是可选的，它可以是一个表达式，返回值为布尔值，只有为 True 的元素才会被包含在结果中。


# 3. 迭代器协议
# 迭代器协议是 Python 中定义的一种协议，它规定了如何实现一个可迭代对象。
# 迭代器协议的实现：
# 1. __iter__() 方法：
# 该方法返回一个迭代器对象。
# 2. __next__() 方法：
# 该方法返回下一个元素。
# 3. __iter__() 和 __next__() 方法的实现：
# 实现迭代器协议的类必须实现 __iter__() 和 __next__() 方法。
# 4. 迭代器对象：
# 迭代器对象是 __iter__() 方法返回的对象。
# 5. 迭代器对象可以用在 for 循环、while 循环、列表推导式、生成器表达式等。


# 示例：
class MyIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration


# 实例化 MyIterator 对象
my_iter = MyIterator(5)

# 使用 for 循环迭代
for i in my_iter:
    print(i)


# 输出: 0 1 2 3 4

# 使用列表推导式迭代
squares = [x**2 for x in MyIterator(5)]
print(squares)

# 输出: [0, 1, 4, 9, 16]

# 使用生成器表达式迭代
squares = (x**2 for x in MyIterator(5))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))

# 输出: 0 1 4 9 16



# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象

# while True:
#     try:
#         print (next(it), end=" ")
#     except StopIteration:
#         sys.exit()


def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 函数变量作用域
a = 4  # 全局变量

def print_func1():
    a = 17 # 局部变量
    print("in print_func a = ", a)


def print_func2():   
    print("in print_func a = ", a)


print_func1()
print_func2()
print("a = ", a) 