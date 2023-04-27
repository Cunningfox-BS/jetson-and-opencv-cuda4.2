# 在jetson系列上编译opencv-cuda（4.2）

## 一，下载文件

opencv[Releases - OpenCV](https://opencv.org/releases/)

opencv-contrib[Releases · opencv/opencv_contrib (github.com)](https://github.com/opencv/opencv_contrib/releases)

**注意版本得是4.2的，不然后面编译问题很大**

## 二，安装依赖

```
sudo apt-get install build-essential 
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```

## 三，准备编译

把上面下载的opencv-contrib-4.2.0文件解压后放入opencv-4.2.0解压后的文件夹，同时把文件夹的版本号删除，重命名为opencv和opencv-contrilb。

按照正常流程来，现在就应该是开始cmake编译了，但是在编译过程中需要从github下载很多包，如果无法在linux上挂梯子，往往都会因为网络问题而编译失败，于是写了个脚本先把所有需要下载的包都下载下来，再放入原本需要下载的地方

网盘链接在这里 https://pan.baidu.com/s/1-MeaLm_Qx4j6Fo1gJAEOpA?pwd=ugxe

这个是py脚本代码

```python
import os
import shutil

# 下面三个变量根据自己实际情况修改！！都得使用相对路径！

package_path = './opencv_down_data'  # 我整理的包，大家可以在我分享的百度云盘或者csdn下载。
src_dir = '~/workspace/source_got/opencv/opencv-20200316/' # 是源代码目录
build_dir = os.path.join(src_dir, 'build/') # cmake 的编译目录

# 这个是opencv cmake 自创的一个缓存目录

catch_dir = os.path.join(src_dir, '.cache/')

# 下面是路径结构

# 前者文件名和下载名一样，是编译目录下的目录结构

# 后者文件名加上了hash校验值，是缓存目录下的目录结构

dir_paths = [#['3rdparty/ippicv/ippicv_2020_lnx_intel64_20191018_general.tgz',
    #'ippicv/7421de0095c7a39162ae13a6098782f9-ippicv_2020_lnx_intel64_20191018_general.tgz'], # 做到master分支上，导致资源是编译4.3的了
    ['3rdparty/ippicv/ippicv_2019_lnx_intel64_general_20180723.tgz',
    'ippicv/c0bd78adb4156bbf552c1dfe90599607-ippicv_2019_lnx_intel64_general_20180723.tgz'],#这个是4.2的资料
    ['3rdparty/ade/v0.1.1f.zip',
    'ade/b624b995ec9c439cbc2e9e6ee940d3a2-v0.1.1f.zip'],
    ['downloads/xfeatures2d/boostdesc_bgm.i',
    'xfeatures2d/boostdesc/0ea90e7a8f3f7876d450e4149c97c74f-boostdesc_bgm.i'],
    ['downloads/xfeatures2d/boostdesc_bgm_bi.i',
    'xfeatures2d/boostdesc/232c966b13651bd0e46a1497b0852191-boostdesc_bgm_bi.i'],
    ['downloads/xfeatures2d/boostdesc_bgm_hd.i',
    'xfeatures2d/boostdesc/324426a24fa56ad9c5b8e3e0b3e5303e-boostdesc_bgm_hd.i'],
    ['downloads/xfeatures2d/boostdesc_binboost_064.i',
    'xfeatures2d/boostdesc/202e1b3e9fec871b04da31f7f016679f-boostdesc_binboost_064.i'], 
    ['downloads/xfeatures2d/boostdesc_binboost_128.i',
    'xfeatures2d/boostdesc/98ea99d399965c03d555cef3ea502a0b-boostdesc_binboost_128.i'], 
    ['downloads/xfeatures2d/boostdesc_binboost_256.i',
    'xfeatures2d/boostdesc/e6dcfa9f647779eb1ce446a8d759b6ea-boostdesc_binboost_256.i'], 
    ['downloads/xfeatures2d/boostdesc_lbgm.i',
    'xfeatures2d/boostdesc/0ae0675534aa318d9668f2a179c2a052-boostdesc_lbgm.i'], 
    ['downloads/xfeatures2d/vgg_generated_48.i',
    'xfeatures2d/vgg/e8d0dcd54d1bcfdc29203d011a797179-vgg_generated_48.i'], 
    ['downloads/xfeatures2d/vgg_generated_64.i',
    'xfeatures2d/vgg/7126a5d9a8884ebca5aea5d63d677225-vgg_generated_64.i'], 
    ['downloads/xfeatures2d/vgg_generated_80.i',
    'xfeatures2d/vgg/7cd47228edec52b6d82f46511af325c5-vgg_generated_80.i'], 
    ['downloads/xfeatures2d/vgg_generated_120.i',
    'xfeatures2d/vgg/151805e03568c9f490a5e3a872777b75-vgg_generated_120.i'], 
    ['share/opencv4/testdata/cv/face//face_landmark_model.dat',
    'data/7505c44ca4eb54b4ab1e4777cb96ac05-face_landmark_model.dat' ]] 

# 如果还没有编译过，可能有的目录不存在

# 检查一下，没有创建一个

def chmk_parent_dir(p):
    t = os.path.dirname(p)
    if not os.path.exists(t):
        os.makedirs(t)

# 拷贝部分

for de in dir_paths:
    file_p = os.path.join(package_path, os.path.basename(de[0]))
    

    bin_p = os.path.join(build_dir, de[0])
    chmk_parent_dir(bin_p)
    shutil.copy(file_p, bin_p)
    
    catch_p = os.path.join(catch_dir, de[1])
    chmk_parent_dir(catch_p)
    shutil.copy(file_p, catch_p)

def cd_path(p):
    if os.path.exists(p):
        os.chdir(os.path.dirname(p)) if os.path.isfile(p) else os.chdir(p)
        return True
    else:
        print("dir not exists: %s" % (p))
        return False

ippicv = os.path.join(build_dir, package_path[0][0])
if cd_path(ippicv):
    os.system('tar xf %s' % (ippicv))
```

当你运行这个脚本之后，你再打开opencv的文件夹会发现多了一个build文件夹，同时会在上面代码的dir_paths地址下会成功多出原本需要下载的文件，即使运行之前的脚本会有报错，但是只要在本应该出现的地方出现了文件就是成功运行。一切准备好了之后就可以开始编译opencv4.2了。

## 四，开始编译

```
cd opencv/build
sudo cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_PNG=OFF \
    -DBUILD_TIFF=OFF \
    -DBUILD_TBB=OFF \
    -DBUILD_JPEG=OFF \
    -DBUILD_JASPER=OFF \
    -DBUILD_ZLIB=OFF \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_opencv_java=OFF \
    -DBUILD_opencv_python2=OFF \
    -DBUILD_opencv_python3=ON \
    -DENABLE_PRECOMPILED_HEADERS=OFF \
    -DWITH_OPENCL=OFF \
    -DWITH_OPENMP=OFF \
    -DWITH_LIBV4L=ON \
    -DWITH_FFMPEG=ON \
    -DWITH_GSTREAMER=OFF \
    -DWITH_GSTREAMER_0_10=OFF \
    -DWITH_CUDA=ON \
    -DWITH_GTK=ON \
    -DWITH_VTK=OFF \
    -DWITH_TBB=ON \
    -DWITH_1394=OFF \
    -DWITH_OPENEXR=OFF \
    -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-10.2 \
    -DCUDA_ARCH_BIN=5.3 \
    -DCUDA_ARCH_PTX="" \
    -DINSTALL_C_EXAMPLES=ON \
    -DOPENCV_ENABLE_NONFREE=ON \
    -DINSTALL_TESTS=OFF \
    -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules \
    .. 
```

注意：如果你的设备不是jetson nano，请自行确定机器的-DCUDA_ARCH_BIN （jetson nx为7.2）；请确认你cuda安装路径-DCUDA_TOOLKIT_ROOT_DIR，具体可以进入/usr/local查看。

## 五，开始make，安装

用8个线程去做make，加快速度。

```
sudo make -j8
sudo make install 
```

## 六，配置环境

```
sudo gedit /etc/ld.so.conf.d/OpenCV.conf
```

写入/usr/local/lib
再到终端输入

```
sudo ldconfig
```

bash文件修改，终端输入

```
sudo gedit /etc/bash.bashrc
```

末尾添加

```
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig  
export PKG_CONFIG_PATH
```

保存后退出，终端输入

```
sudo updatedb
```

然后可能会出现这样报错

```
/usr/bin/find: '/run/user/1000/gvfs': Permission denied
```

其实这个问题不会有任何影响，但是看着难受名还是给它解决了吧

```
sudo umount /run/user/1000/gvfs
sudo rm -rf /run/user/1000/gvfs
```

自此opencv-cuda（4.2）安装完成

## 七，安装验证

在终端输入

```
opencv_version
```

会看到4.2的版本信息

再次打开jtop

```
jtop
```

可以看到opencv后面会显示cuda则表示安装验证完成
