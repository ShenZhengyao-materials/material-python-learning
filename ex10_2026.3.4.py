#输入正方体边长，输出：
#体积
#表面积

a = float(input("请输入正方体边长："))
v = a ** 3
s = 6 * (a ** 2)
print("正方体体积为：" + str(v))
print("正方体表面积为：" + str(s))
print(" ")





#生成一个列表，里面是 1～20 的平方数：
#[1, 4, 9, ..., 400]
#然后把这个列表打印出来。
list_square = []
for i in range(1, 21):
    list_square.append(i ** 2)
print(list_square)
print(" ")





#输入 10 个数字（可以写死在代码里），统计：
#大于 10 的数有几个
#所有数的平均值
list1 = [1,26,8,64,2,6,9,25,4,32]
list2 = []
for num in list1:
    if num > 10 :
        list2.append(num)
print("大于10的数有" + str(len(list2)))
total = 0
for num in list2:
    total = total + num
b = total / len(list2)
print("这几个数的平均数为：" + str(b))
print(" ")




#写一个函数，输入温度℃，返回华氏度 °F：
#F=C×9/5+32
#再写一个反过来的函数（F→C）

def c_f(c):
 f = c * 1.8 + 32
 print("对应的华氏度为：" + str(f))

a = float(input("请输入摄氏度1："))
b = float(input("请输入摄氏度2："))
c_f(a)
c_f(b)
print(" ")


#给定一个表示 “材料强度” 的列表：
#strength = [520, 480, 550, 600, 450, 510]
#用循环自己实现：
#最大值
#最小值
#平均值
#（不许直接用 max ()、min ()、sum () 练逻辑）
strength = [520, 480, 550, 600, 450, 510]
max_0 = strength[0]
for num in strength:
    if num > max_0:
        max_0 = num
print("最大值：" + str(max_0))
min_0 = strength[0]
for num in strength:
    if num < min_0:
        min_0 = num
print("最小值：" + str(min_0))
total = 0
for num in strength:
    total = total + num
average = total / len(strength)
print("平均：" + str(average))
print(" ")


#用纯 Python实现一个简单向量加法：
#有两个等长列表 a、b
#对应位置相加，得到 c
#例如：
#a = [1,2,3], b=[4,5,6] → c=[5,7,9]
a = [1,2,3]
b = [4,5,6]
i = a[0] + b[0]
j = a[1] + b[1]
k = a[2] + b[2]
c = [float(i),float(j),float(k)]
print(c)
#ai优化
a = [1, 2, 3]
b = [4, 5, 6]

if len(a) == len(b):
    c = [float(a[i] + b[i]) for i in range(len(a))]
    print(c)
else:
    print("列表长度不一致！")


















