#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf-8

# print('中文')
# print('hello, %s') % 'world'
# print('Hi, %s, you have $%d.') %('wujunwei', 10000)
# print('%2d-%02d') %(3,1)
# print('%.2f') % 3.1415926
# print('Age: %s. Gender: %s') % (25, True)
# print('growth rate: %d %%') % 8

######  列表list学习
classmates = ['michael', 'bob', 'tracy']
# print(classmates)
# print(len(classmates))
# print(classmates[0])
# print(classmates[6])  #error 没有对应的数组元素
print( classmates[-1] ) # 倒数第一个元素
classmates.append('Adam')	# 往list中追加元素到末尾
print(classmates)
classmates.insert(1, 'Jack')	# 把元素插入到指定的位置，比如索引号为1的位置
print(classmates)
classmates.pop()	# 删除list末尾的元素
print(classmates)
classmates.pop(1)	# 删除指定位置的元素
print(classmates)


######  tuple元组学习   todo
# tuple和list非常类似，但是tuple一旦初始化就不能修改


# 在Ubuntu上用 python test01.py运行得时候报错, 
# 找了半天原因, 最后终于想明白了, input是python3的函数
# python3 test01.py  或  chmod a+x test01.py  ./test01.py
# studentName = input('please enter your name: ')
# print('hello', studentName)


###### python函数测试
""" 获取一个数字得绝对值 """
def getAbsolute(a):
	if a >= 0:
		print(a)
	else:
		print(-a)
# getAbsolute(10)
# getAbsolute(-99)


###### 字符和编码
# print( ord('中') )		# ord()获取字符的整数表示
# print( chr(20013) )		# chr()把编码转换为对应的字符
# print('\u4e2d\u6587')	# 用16进制表示字符串


###### 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
###### 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
###### Python对bytes类型的数据用带b前缀的单引号或双引号表示
# print( b'ABC' )
# print( 'ABC' )
###### 要注意区分'ABC'和b'ABC'，'ABC'是str，b'ABC'虽然内容显示得和'ABC'一样，但bytes的每个字符都只占用一个字节


###### 以Unicode表示的str通过encode()方法可以编码为指定的bytes
# print( 'ABC'.encode('ascii') )
# print( '中文'.encode('utf-8') )


###### 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
###### 要把bytes变为str，就需要用decode()方法
# print( b'ABC'.decode('ascii') )
# print( b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') )


###### 要计算str包含多少个字符，可以用len()函数：
# print( len('ABC') )		# 输出: 3
# print( len('中文') )    # 输出: 2

###### len()函数计算的是str的字符数
###### 如果换成bytes，len()函数就计算字节数：
# print( len(b'ABC') )	# 输出: 3
# print( len(b'\xe4\xb8\xad\xe6\x96\x87') )	# 输出: 6
# print( len( '中文'.encode('utf-8') ) )	# 输出: 6
# print( len( '中文'.encode('gbk') ) )		# 输出: 4


