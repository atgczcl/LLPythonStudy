from LLoghelper.log_helper import log, logger
import sys
from collections import deque

# 一个模块只会被导入一次，不管你执行了多少次 import。这样可以防止导入模块被一遍又一遍地执行。
# 列表可以修改，而字符串和元组不能修改。
# import module1[, module2[,... moduleN]


logger.set_log_enable(True, True)
# 数据结构-堆栈
stack = [3, 4, 5]

stack.append(6)
stack.append(7)

print(f"stack: {stack.pop()}")
print(f"stack: {stack.pop()}")
# 队列
queue = deque([1, 2, "3"])

queue.append("8")
queue.append("9")

print(f"queue: {queue}|{queue.popleft()}")
print(f"queue: {queue}|{queue.popleft()}")
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
ff = [weapon.strip() for weapon in freshfruit]
print(f"freshfruit: {freshfruit}|{ff}")

# 嵌套列表解析
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, '你好']]
# 转换为4*3的列表
flat_matrix = [num for row in matrix for num in row]
print(f"flat_matrix: {flat_matrix}")

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[3:5]
print(f"a: {a}")

# 元组由若干逗号分隔的值组成
t = 12345, 54321, 'hello!'
print(f"t: {t}")
u = t, (1, 2, 3, 4)
print(f"u: {u}")
v = 1, 2, 3, 4
s = set()  # 创建一个空集合
s.add(tuple(element for element in v))  # 向集合中添加元组
# 集合中的元素必须不可变，所以这里会报错
# s.add(a) # TypeError: unhashable type: 'list' 列表不能作为集合的元素, 所以这里会报错
print(f"s: {s}")
s.add(v)
s.add(v)
s.add(v)
print(f"s: {s}")
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)
 
counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量

class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.value == other.value
        return False
    
    def __hash__(self):
        return hash(self.value)

# 创建一个集合
s = set()

# 创建类的实例
instance1 = MyClass(2)
instance2 = MyClass(2)

# 将实例添加到集合中
s.add(instance1)
s.add(instance2)

# 打印集合
print(s)  # 输出: {<__main__.MyClass object at 0x...>, <__main__.MyClass object at 0x...>}
print(f"{dir(instance1)}|{dir(instance2)}")  # 输出: 4471772816|4471772824
print(f"{instance1.value}|{instance1.__hash__()}|{instance2.value}|{instance2.__hash__()}")  # 输出: 4471772816|4471772824
print(f"{instance1 == instance2}")  # 输出: True

# 遍历技巧
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# enumerate() 可以展示索引值
for i, value in enumerate(a):
    print(i, value)  # 输出: 0 A 1 B 2 C
dic1 = {'name': 'Alice', 'age': 20}
dic2 = {'name': 'Bob', 'age': 25, 'gender': 'Male'}
for i, value in enumerate(dic1.items()):
    print(i, value)  # 输出: 0 name 1 age
# 同时遍历两个或更多的序列，可以使用 zip() 组合
a = [-1, 1, 66.25, 333, 333, 1234.5]
b = ['A', 'B', 'C', 'D', 'E', 'F']
for i, j in zip(a, b):
    print(i, j)  # 输出: A 1 B 2 C 3 D 4
for i, j in zip(dic1.items(), dic2.items()):
    print(i, j)  # 输出: name Alice age 20 name Bob age 25

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
a = [1, 2, 3, 4, 5]
for i in reversed(a):
    print(i, end=' ')  # 输出: 5 4 3 2 1

# 要按顺序遍历一个序列，首先指定这个序列，然后调用 sorted() 函数
a = [5, 2, 3, 1, 4]
for i in sorted(a):
    print(i, end=' ')  # 输出: 1 2 3 4 5
# dir 函数用于获取对象的属性和方法
print(f"{dir(a)}")
print(f"{dir(str)}")  # 输出: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'is
print(f"{dir(set)}")  # 输出: ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdis
print(f"{dir(dict)}")  # 输出: ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem','setdefault', 'update', 'values']
print(f"{dir(list)}")  # 输出: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop','remove','reverse','sort']
print(f"{dir(tuple)}")  # 输出: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_asdict', '_fields', '_make', '_replace']

ss = "你好，世界！"
print(f"ss: {str.count(ss, '你')}")
print(f"ss: {len(s)}")
print(f"ss: {str.replace(ss, '你', '我')}")
# nput([prompt]) 函数和 raw_input([prompt]) 函数基本可以互换，但是 input 会假设你的输入是一个有效的 Python 表达式，并返回运算结果。

# ss = input("请输入一个字符串：") # python3中已经无法执行代码，因为input函数返回的是字符串，而raw_input函数返回的是输入的原始字符串，可以显示转换为int, float等类型
# print("你输入的字符串是", ss)

# 异常处理
try:
    a = 1 / 0
except ZeroDivisionError:
    print("division by zero!", log_level = logger.ERROR)

aa = float('1.2345')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
          'Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))


fo = open('./test.txt', 'a+', encoding='utf-8') # 打开一个文件，如果文件不存在，则创建文件
# fo.write('Hello, world!\n') # 写入文件内容
# 写入多行内容
fo.writelines(['Python is a great language.\n', 'I love it.\n'])
# 读取文件所有内容
# 打开文件以读取模式
with open('./test.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
# 读取文件内容
# 打开文件以读写模式
with open('./test.txt', 'r+', encoding='utf-8') as file:
    # 读取文件内容
    content = file.read()
    print('Original content:', content)
    
    # 移动文件指针到文件末尾
    file.seek(0, 2)
    
    # 写入新内容
    file.write('Appending new line.\n')
    
    # 移动文件指针到文件开头
    file.seek(0)
    
    # 读取更新后的内容
    updated_content = file.read()
    print('Updated content:', updated_content)
fo.close() # 关闭文件
# 文件对象的方法
# print(f"{dir(fo)}")  # 输出: ['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']


mydict = {"W3Cschool": 1, "baidu": 2, "Google": 3}

# 旧版本
print(mydict.keys())
print(mydict.values())
print(mydict.items())

# 新版本
keys = mydict.keys()
values = mydict.values()
items = mydict.items()

print(keys.mapping)
print(values.mapping)
print(items.mapping)
 
# 可以理解为我们可以根据字典的keys，values，items反向推出这个字典

'''
类命名

    类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头。
    在接口被文档化并且主要被用于调用的情况下，可以使用函数的命名风格代替。
    对于内置的变量命名有一个单独的约定：大部分内置变量是单个单词（或者两个单词连接在一起），首字母大写的命名法只用于异常名或者内部的常量。
函数命名

    函数名应该小写，如有多个单词，用下划线隔开。
    大小写混合仅在为了兼容原来主要以大小写混合风格的情况下使用，保持向后兼容。
    私有函数在函数前加一个下划线_。

常量或者全局变量命名
    全部大写，如有多个单词，用下划线隔开
    全⼤写+下划线式驼峰
模块名命名
    模块尽量使用小写命名，首字母保持小写，尽量不要用下划线(除非多个单词，且数量不多的情况)
    模块名尽量简短，避免使用缩写，如有多个单词，用下划线隔开。
    模块名称要短，使用小写，并避免使用特殊符号， 比如点和问号。
    尽量保持模块名简单，以无需分开单词最佳（不推荐在两个单词之间使用下划线）。
    每个导入应该独占一行。
    import os
    import numpy
    import sys

    from types import StringType, ListType 
'''

"""
主功能应该放在一个main()函数中。

在Python中，pydoc以及单元测试要求模块必须是可导入的。代码应该在执行主程序前总是检查 if __name__ == '__main__'， 这样当模块被导入时主程序就不会被执行。

def main():
      ...

if __name__ == '__main__':
    main()


函数设计规范

    函数设计的主要目标就是最大化代码重用和最小化代码冗余。精心设计的函数不仅可以提高程序的健壮性，还可以增强可读性、减少维护成本。
    函数设计要尽量短小，嵌套层次不宜过深。 所谓短小， 就是尽量避免过长函数， 因为这样不需要上下拉动滚动条就能获得整体感观， 而不是来回翻动屏幕去寻找某个变量或者某条逻辑判断等。 函数中需要用到 if、 elif、 while 、 for 等循环语句的地方，尽量不要嵌套过深，最好能控制在3层以内。不然有时候为了弄清楚哪段代码属于内部嵌套， 哪段属于中间层次的嵌套， 哪段属于更外一层的嵌套所花费的时间比读代码细节所用时间更多。

    尽可能通过参数接受输入，以及通过return产生输出以保证函数的独立性。

    尽量减少使用全局变量进行函数间通信。
    
    不要在函数中直接修改可变类型的参数。

    函数申明应该做到合理、 简单、 易于使用。 除了函数名能够正确反映其大体功能外， 参数的设计也应该简洁明了， 参数个数不宜太多。 参数太多带来的弊端是： 调用者需要花费更多的时间去理解每个参数的意思，测试的时候测试用例编写的难度也会加大。
    函数参数设计应该考虑向下兼容。
"""