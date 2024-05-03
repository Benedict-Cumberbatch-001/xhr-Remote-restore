# Python包安装方法、技巧

1. 比较小的包直接使用 ``pycharm`` 下载
   
2. 大一点的使用 ``pip install`` 端下载
   
3. 再大一点的去官网安装包下载网站直接下载 whl 文件。其中 cp36 是指 3.6 版本的 python
   
4. 可以直接 ``pip install + 包名``把已下载的文件拖入到终端框里面
   
5. 使用CV2的时候pycharm 标黄的原因：是解释器中的 **python** 路径里面没有 ``cv2``，一般在``site-packbages/cv2/cv.pyd``

6.  终端下载大面积飘红可能是因为开了 ***vpn***

7.  ``Anaconda``管理虚拟环境，需要创建和激活虚拟环境，可以在里面创建不同版本的 python 版本。使用 ``Anaconda prompt``
8. ``conda``不能挂梯子使用
9. 在**pycharm**中添加**Anaconda**创建的虚拟环境
   - 先找到添加“系统解释器”在里面找到虚拟环境Tools文件夹下面的`python.exe`解释器，再去添加Ananconda虚拟环境

10. 默认 python 版本是直接 `win+r`打开 cmd，
需要运行命令：
```
d:
cd "D:\python\Python\venv\Scripts"
pip install --
```
实际上`pip`命令需要调用 `pip.exe`文件，一般在`script`文件夹内

直接`win+r`打开命令行`pip`是调用系统变量里面排名在上面的`python`解释器和`pip`，使用`where python`命令可以查看`python`的位置

11. 在`pycharm`内打不开`html`文件是因为没有吧`temp...`文件夹设置为根目录

12. 安装less转css插件，如果文件夹生成了`index.css.map`文件则说明成功了

13. `pip show package_name`可以查看包所在的位置

14. Office下载方式：学校的office下载以后需要登录账户才能激活，onenote的下载只能使用2016版本的

15. 使用`pyinstaller`打包py文件尽量保证环境里没有多余的包，不然会很大。而且运行的时候，要进入到你想生成文件放的文件夹路径下，再运行。

### Anaconda的操作
1. ``conda config --show channels``查看下载源，可以更改为国内源
2. `conda  create -n <环境name> python=3.6（python版本）`创建拥有指定python版本的虚拟环境
3. `conda env list`查看拥有的虚拟环境
4. `conda activate`  <虚拟环境名>激活虚拟环境
5. `conda install <包名>/pip install <包名>`安装库
6. `conda env remove -n <虚拟环境名>`删除虚拟环境
7. `conda remove --name <虚拟环境名> <包名>`删除某个环境内的某个库
8. `conda list`显示所有的安装库
9. `conda info <包名>`显示指定包的详细信息，包括包的名称、版本号、依赖关系、安装路径等等

### jupyter notebook 使用
1. `jupyter notebooke:`在e盘内打开`jupyter notebook`
2. `Kernel-->change kernel-->环境名` 更改`jupyter notebook`使用的环境

### 生成requirements.txt的依赖项：
1. 在当前项目的终端/终端进入当前项目文件夹，
2. 运行`pip freeze > requirements.txt`
3. 或者安装`pip install pipreqs`,使用命令`pipreqs /path/to/your/python/file.py`生成指定 `Python` 文件所需的 `requirements.txt` 文件。
4. 使用命令`pipreqs .`生成当前目录下的所需的 `requirements.txt` 文件。
5. 使用`pipreqs . --force`强制覆盖之前的`requirements.txt` 文件。

### 相对路径/绝对路径
在py文件中，经常涉及到相对路径和绝对路径，绝对路径要从盘符写起，且斜杠要用双反斜杠表示\\转义字符
某个项目如果要在别的电脑上，或者发给别人就需要写相对路径
《./》表示当前级目录（可以省略）
《../》表示上层目录
《../../》表示上上层目录
2->三种路径的输入方式
`path1=c:/Users/Hjx/Desktop/text.txt`    #单个反斜杠
`path2='c:llusersllHjxliDesktoplltext.txt `  # 两个斜杠:\\\\(第一个\是转义符)
`path3=r'c:\Users\Hjx\Desktop\text.txt'`  #r用于防止字符转义
