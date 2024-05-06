# Colmap使用
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
        
1. **注意一定要将储存colmap信息的文件夹名命名为**`sparse`
2. 稀疏重建后导出为：
- Export model
- Export model as...
- Export model as text
# Openmvs使用
1. 将toy文件夹拖动到`InterfaceCOLMAP.exe`上打开（简单），或者使用命令
```
InterfaceCOLMAP.exe -i d:...你的路径/toy
```
其他使用方法可以查看官网，或者双击`InterfaceCOLMAP.exe`查看命令涵义
- -i
- -w
- -o
- ....
1. 将生成的scene.mvs拖动到`DensifyPointCloud.exe`生成稠密点云。

2. 完成后将生成的`scene_dense.mvs`拖动到`ReconstructMesh.exe`上重建网格。
3. 完成后将生成的`scene_dense_mesh.mvs`拖动到`RefineMesh.exe`上优化网格。
4. 完成后将生成的`scene_dense_mesh_refine.mvs`拖动到`TextureMesh.exe`上贴图。
5. 生成的文件为`.ply`格式，使用`meshlab`查看。