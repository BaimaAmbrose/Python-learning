try:
    a = int(input('输入A:'))
    b = int(input('输入B:'))
    c = a / b
    print('结果是', c)
except ZeroDivisionError:
    print('分母不能为0')

# 特定的bug输出特定的结果

#------------------------------

try:
    a = int(input('输入A:'))
    b = int(input('输入B:'))
    result = a / b
except BaseException as e: # 捕获所有类型的错误
    print('错误:', e)
else:
    print(result)
finally: # 总是会执行的代码
    print('无论是否产生异常，总会被执行的代码')

#--------------------------------

