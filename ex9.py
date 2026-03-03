#十进制-二进制转换器
num_2 = float(input("Enter a number: "))
s = num_2
list_10 = []
while s != 0:
  if s % 2 == 0:
   s = s // 2
   list_10.append(0)
  else:
   s = (s-1) // 2
   list_10.append(1)
list_10.reverse()
print(list_10)




#十进制-二进制转换器优化
num_2 = int(input("Enter a number: "))
s = num_2
list_10 = []
while s != 0:
  if s % 2 == 0:
   s = s // 2
   list_10.append(0)
  else:
   s = (s-1) // 2
   list_10.append(1)
list_10.reverse()

# 新增：把数字列表拼接成字符串
# 先把列表里的每个数字转成字符串，再用join拼接
binary_str = ''.join(str(num) for num in list_10)
# 处理空字符串（输入0时）
binary_str = binary_str if binary_str else '0'

# 输出拼接后的字符串，而非原列表
print("转换结果：", binary_str)



