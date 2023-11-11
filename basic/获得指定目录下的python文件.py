import os

path = os.getcwd()
lst = os.listdir(path) # 获得路径下的文件
m = 0
for filename in lst:
    if filename.endswith('.py'):
        print(m, filename)
        m += 1
print('--------------------------')
lst_files = os.walk(path) # 可以获得多重文件夹下的文件
n = 0
for dirpath,dirname,filename in lst:
    print(dirpath)

