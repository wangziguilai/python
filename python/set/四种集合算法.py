a=set(range(5))
b=set(range(4,9))
print(a)
print(b)
#并集
print('并集',a|b)
#交集
print('交集',a&b)
#差集
print('差集',a-b)
#对称差集，相对于并集减掉交集，就是元素都出现在a和b中，但结果是不显示这个
print('对称差集',a^b)
print('----------使用方法------------')
#交集
print('交集',a.intersection(b))
#差集
print('差集',a.difference(b))
#并集
print('对称差集',a.union(b))
print()