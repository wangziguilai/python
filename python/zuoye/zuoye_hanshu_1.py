# 作业：1、简述普通参数、指定参数、默认参数、动态参数的区别
# 普通参数：是指我们传入的参数是以正确顺序传入，并且无任何指定值
# 指定参数：又叫关键字参数，传入的参数可以不分顺序，但要在传参时要指定形参的值
# 默认参数：默认参数要写在普通参数后面，函数传递参数时如果给定了值就按给定的值使用，
# 如果没给定，那就按最初赋值的值算
# 动态参数：动态参数是指我们给定的值有多时，将多出的值按元组的形式存入形参变量中，
# 但变量前要加*，用来区分和其它参数，动态参数要放在所有类型的参数后面，
# 如果传入的值是以键值对的形式，则会以存入一个空字典的参数，但形参前面要加**
def myfc(x):
    x=list(a)
    x[2]=10
    return x
a=(1,2,3,4,5)
print(a)
a=myfc(a)
print(a)








# 10.实现百钱买百鸡，
# 11.实现100和尚吃100馒头
# 12.10个数字，每3个除去，剩几？