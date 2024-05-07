<meta charset="UTF-8">

# 一、Colmap稀疏重建
## 安装Colmap
1. 下载`Colmap`，如果不需要使用稠密重建无需下载带`CUDA`版本的（稍大），这里给一个国内下载链接：
链接：https://pan.baidu.com/s/1KUbKhDCvjo0ws2DkFON3pQ?pwd=ddnp 
提取码：ddnp
2. 解压后文件夹应是这样的：
![文件夹](image.png)
双击`COLMAP.bat`打开命令行，稍等片刻即可见到`colmap`图形界面：
![图形界面](image-1.png)
## 准备你的数据
1. 通过视频抽帧获取图片(可选)：
- 打开视频抽帧脚本，输入每秒要抽帧数量，这里输入2（一般视频每秒有`24/30/60`帧），**抽帧脚本可以咸鱼下单或者在qq上找作者要**。
- 将视频拖入视频抽帧脚本（视频目录不要包含中文和空格）
![alt text](image-2.png)
![alt text](image-3.png)
- 生成的照片储存在脚本目录的`_frames`，新的视频抽帧生成的文件夹会覆盖之前的文件！
![alt text](image-4.png)
2. 通过拍照或者视频抽帧获取的图片要尽量清晰，尤其注意要避免**运动模糊**，模糊的照片会对稀疏重建算法造成较大影响，尽可能挨个检查一下，删除质量较差的照片。
## 使用Colmap获取相机位姿
### 使用Colmap生成OpenMVS需要的文件
1. 新建文件夹，目录结构：
toy/
&emsp;images/
&emsp;&emsp;&emsp;toy1.jpg;
&emsp;&emsp;&emsp;toy2.jpg;
&emsp;&emsp;&emsp;....
&emsp;sparse/
&emsp;&emsp;&emsp;toy.db
&emsp;&emsp;&emsp;xxx.txt
&emsp;&emsp;&emsp;...
&emsp;&emsp;&emsp;xxx.ini
&emsp;&emsp;&emsp;xxx.nvm
&emsp;&emsp;&emsp;...
这里的`toy`可以自己随意名命,在这里用其举例说明
> 注意一定要将储存colmap信息的文件夹名命名为`sparse`
2. 打开`Colmap`图形界面，`File->New project`**(如果目录包含中文则会创建不成功)**
![alt text](1715093927747.jpg)
3. 创建新项目，储存在创建的`sparse`文件夹下，`Select`选择`images`文件夹
   ![alt text](image-5.png)
4. 点击`Processing->Feature extraction`相机模式设置为`PINHOLE`，其他参数默认。点击`Extract`进行提取，完成后点击关闭。
![alt text](image-6.png)
5. 点击`Processing->Feature matching`参数默认直接点击`run`，完成后点击关闭
6. 点击`Resconstruction->start reconstruction`，等待重建完成。
![alt text](image-7.png)
7. 稀疏重建后导出到`sparse`文件夹内：
![alt text](image-8.png)
```
Export model
Export model as...
Export model as text
```
保存后的`sparse`文件夹应当包含以下文件
![alt text](image-9.png)
如果你包含这些文件，恭喜你`colmap`任务完成，保存关闭即可。
# 二、OpenMVS使用
1. 将toy文件夹拖动到`InterfaceCOLMAP.exe`上打开（简单快捷），或者使用命令
```
InterfaceCOLMAP.exe -i ...你的路径/toy
```
其他使用方法可以查看官网，或者双击`InterfaceCOLMAP.exe`查看命令含义（在文件夹下生成的.log文件内查看）
```
Generic options:
  -h [ --help ]                         produce this help message
  -w [ --working-folder ] arg           working directory (default current 
                                        directory)
  -c [ --config-file ] arg (=InterfaceCOLMAP.cfg)
                                        file name containing program options
...
```
程序运行完毕后会在`toy`文件夹下生成`scene.mvs`文件，可以使用`openmvsSamples`文件夹下的`Viewer.exe`查看（将`.mvs`文件拖动到`exe`文件上）
![alt text](image-10.png)
2. 将生成的`scene.mvs`拖动到`DensifyPointCloud.exe`生成稠密点云。
3. 完成后将生成的`scene_dense.mvs`拖动到`ReconstructMesh.exe`上重建网格。
4. 完成后将生成的`scene_dense_mesh.mvs`拖动到`RefineMesh.exe`上优化网格。
5. 完成后将生成的`scene_dense_mesh_refine.mvs`拖动到`TextureMesh.exe`上贴图。
6. 生成的文件为`.ply`格式，可以使用`meshlab`查看。
# OpenMVS解析文档
联系作者提供OpenMVS原理详解 + 逐行源码解析文档
![alt text](3.png)
![alt text](image-11.png)
![alt text](image-12.png)