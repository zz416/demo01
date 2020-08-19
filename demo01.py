
"""
print("hello world") #字符串
print(233) #整数
print(2.333) #小数
print(True,False) #布尔
print(()) #元组
print([]) #数组
print({}) #字典
print("哈哈哈哈"+"嘻嘻嘻嘻嘻") #字符串的拼接
print("哈哈"*10)
print((1+200)*2/4)
print(2>3)

a = "张三" # 把张三的值赋值给a这个变量。
print(a)
b = input("请输入：")
print("input输入的值：",b)
c = type(2333)
print(c)


print(type("哈哈哈哈哈"))
print(type(22222))
print(type(2.222))
print(type(True))
print(type(()))
print(type([]))
print(type({}))

a = str(2333)
print(type(a))


a = input("请输入a:")
a1 = len(a)
b = input("请输入b:")
b1 = len(b)
print("a、b的字符串长度之和为：",len(a)+len(b))

#元组 下标从0开始,倒着数是-1、-2....
a = (1,2,3,4,"哈哈","嘻嘻")
#切片
print(a[0:4]) #左开右闭

print(a[4])
print(a.index("嘻嘻"))
print(a.count("哈哈"))
#二维元组  3个值
b = (a,"哈哈","嘻嘻")
print(b[0][3]) #取a里面的4

#数组      和元组的区别：数组可修改，元组不可修改
a = [1,2,3,4,"哈哈","嘻嘻"]
a.append("apend")
print(a)
a.insert(0,"insert")  #往数组中指定位置添加数据。
print(a)

b = a.pop(4) #剪切
print(a)
print(b)


#字典的特点：字典中的值没有顺序、字典的结构必须是键值对 key:value。
a = {"name":"哈哈","age":18,"class":1}
print(a["name"])

a["height"] = "180cm" #新增
print(a)
a["name"]="张三" #修改
print(a)

b = a.get("name")
print(b)

b = a.pop("age")
print(b)
print(a)

a.update(name=1234) #此处name相当于一个变量，所以不用加引号，其他地方的字符串都需要引号
print(a)

#数组和字典的删除
del a["name"]
print(a)
#del a[0]  数组的删除。

"""


a = input("请输入name：")
b = input("请输入age：")
c = input("请输入sex：")
d = {}
d.update(name="a")
d.update(age="b")
d.update(sex="c")
print(d)