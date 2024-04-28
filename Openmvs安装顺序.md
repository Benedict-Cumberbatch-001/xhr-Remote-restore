## Cmake安装顺序

把`Visual Studio`改成英文，
查看系统环境变量没有`vcpkg`避免干扰
先试试官方文件好不好使

`Openmvs/IO/CMakeLists.txt` 修改`QUIET`为`REQUIRED`
`IO/Common/Types.inl`  搜索`ZSTD`把`boost`版本`106900`更改为`109000`
`CUDA`设置为不安装
> Cmake包链接顺序：
```shell
BOOST_ROOT         boost 1.72
EIGEN              include/eigen3
OPENCV_DIR         v16/lib
ZLIB_ROOT          zlib
PNG_ROOT           png
JPEG_ROOT          jpeg
TIFF_ROOT          tiff 
CGAL DIR           lib/cmake/CGAL
GMP INCLUDE DIR    Include
RELEASE DIR        libgmb-10.lib
MPFR INCLUDE DIR   Include
RELEASE DIR        libgmbfr_4.lib
VCG DIR            cg.lib 2020.09
```
附加依赖项删除`../boost iostream`和`../boost program`

#### 遇到问题：
- VS编译报错: `LNK2019_imp_gmpq_init` 将`libgmp-10.lib``libmpfr-4.lib`添加到附加依赖项
- `error LNK2038: 检测到“RuntimeLibrary”的不匹配项: 值“MT_StaticRelease”不匹配值“MD_DynamicRelease”` 引用的是静态库，但设置成动态库了）`在对应项目上鼠标右键`->`属性`*->*`C/C++ `->`代码生成`->`运行库多线程(/MT)`：
对应的是`MD_StaticRelease`
多线程(/MTd)：对应的是`MD_StaticDebug`
多线程Dll (/MD) ：对应的是`MD_DynamicRelease`
多线程调试Dll (/MDd) ：对应的是`MD_DynamicDebug`

- `No CUDA toolset found`一般是因为安装`CUDA`时没有安装对应的`Visual Studio Integration`缺失
