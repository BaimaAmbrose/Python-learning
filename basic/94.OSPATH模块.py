import os.path

print(os.path.abspath('元组'))
# 输出绝对路径
print(os.path.exists('元组.py'))
# 该文件是否存在
print(os.path.join('qqww','sdfsdf'))
# 把两个路径进行拼接
print(os.path.split('/Users/baima/PycharmProjects/pythonProject/BasicFIle/元组'))
# 将文件目录和文件名进行拆分
print(os.path.splitext('/Users/baima/PycharmProjects/pythonProject/BasicFIle/元组.py'))
# 将文件名和后缀名进行拆分
print(os.path.basename('/Users/baima/PycharmProjects/pythonProject/BasicFIle/元组.py'))
# 提取文件名
print(os.path.dirname('/Users/baima/PycharmProjects/pythonProject/BasicFIle/元组.py'))
# 提取文件路径
print(os.path.isdir('/Users/baima/PycharmProjects/pythonProject/BasicFIle/'))
# 判断是否是路径
