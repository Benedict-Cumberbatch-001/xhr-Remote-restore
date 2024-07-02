import os

def get_lib_files(directory):
    lib_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.lib'):
            lib_files.append(filename)
    return lib_files

# 指定lib文件夹路径
lib_files = get_lib_files(r'D:\opencv\opencv410_release\x64\vc16\lib')
for i in lib_files:
    print(i)
