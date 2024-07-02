# Python打包和上传到pypi
## 搭建包目录
目录结构项目 `funniest` 如下:
```
funniest/
    funniest/
        __init__.py
    setup.py
```
## 修改完善 `setup.py`
### setup.py示例
```python
import codecs
import os
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi (if you dont need delete it)
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# you need to change all these
VERSION = '1.0.2'
DESCRIPTION = 'a ligh weight menu , support both win and mac '
LONG_DESCRIPTION = 'dumb_menu is a ligh weight menu ,support hot key, support both win and mac'

setup(
    name="dumb_menu",
    version=VERSION,
    author="clever chen",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'menu', 'dumb_menu','windows','mac','linux'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
```
## 进行本地测试 
```
python setup.py develop
```
## 编译 
生成dist编译文件
```
python setup.py sdist
```
## 上传到pypi
需要先安装`twine`包
然后使用命令：
```
twine upload dist/*
```
会让你输入`Apikey`，从微信收藏复制。

## 版本号
`1.0.1` 待更新...