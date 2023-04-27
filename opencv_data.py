import os
import shutil

# 下面三个变量根据自己实际情况修改！！都得使用相对路径！

package_path = './opencv_down_data'  # 我整理的包，大家可以在我分享的百度云盘或者csdn下载。
src_dir = '~/workspace/source_got/opencv/opencv-20200316/'  # 是源代码目录
build_dir = os.path.join(src_dir, 'build/')  # cmake 的编译目录

# 这个是opencv cmake 自创的一个缓存目录

catch_dir = os.path.join(src_dir, '.cache/')

# 下面是路径结构

# 前者文件名和下载名一样，是编译目录下的目录结构

# 后者文件名加上了hash校验值，是缓存目录下的目录结构

dir_paths = [  # ['3rdparty/ippicv/ippicv_2020_lnx_intel64_20191018_general.tgz',
    # 'ippicv/7421de0095c7a39162ae13a6098782f9-ippicv_2020_lnx_intel64_20191018_general.tgz'], # 做到master分支上，导致资源是编译4.3的了
    ['3rdparty/ippicv/ippicv_2019_lnx_intel64_general_20180723.tgz',
     'ippicv/c0bd78adb4156bbf552c1dfe90599607-ippicv_2019_lnx_intel64_general_20180723.tgz'],  # 这个是4.2的资料
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
     'data/7505c44ca4eb54b4ab1e4777cb96ac05-face_landmark_model.dat']]


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