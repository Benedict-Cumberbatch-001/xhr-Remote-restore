## VS快捷键/技巧
1. 在项目->常规里面可以调整VS的版本
2. 快捷键CTRL+KC快速注释代码；快捷键CTRL+KU快速取消注释
3. 快捷键CTRL+Break取消生成，停止；
4. 使用`"项目"-->"生成模板"`，下次再新建就不用重新配置项目环境了
## CMAKE经验
### cmake命令编译：
Cmake需要使用某个依赖库的release版本，对于依赖库，可以使用以下命令（常用命令）
```Shell
mkdir build
cd build
cmake ..-G "Visual Studio 16 2019" -DCMAKE_INSTALL_PREFIX=D:\libs\path\to\xerces-c\source
```
解释：
-G后面指定版本，`-DCMAKE_INSTALL_PREFIX`安装到系统中的指定位置
`cmake --build . --config Debug` 重建Debug版本
`cmake --build . --config Debug --target install `这个命令的意思是在当前目录中使用 Debug 配置进行构建，并在构建完成后执行安装操作，将构建的结果安装到系统中的指定位置

### 使用camke-Gui进行编译：
1）`CMAKE_INSTALL_PREFIX`要填写，选择一个方便的目录。这是构建后复制二进制发行版集的位置。
2）填写`include`目录和`lib`目录，可以自己新增`XXX_ROOT`目录：包含`include和lib`目录
3）有时候找不到`XXX_ROOT`可能是因为`CMakeLists.txt中find_package(Xerces QUIT 改为REQUIRED）`

3>下载C++开源库一般去[Sourceforge](https://sourceforge.net/)，然后其中有二进制文件，就是别人编译好的，其中的`include和lib`都包含在内，但是需要注意VS版本可能不对应。自己编译后`install`的一般比较合适。
