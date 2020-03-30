[![](https://img.shields.io/badge/Lauguage-Mandarin-blue)](./) [![](https://img.shields.io/badge/CUDA-v10.0-lightgrey)](https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal) [![](https://img.shields.io/badge/cuDNN-v7.6.5-red)](https://developer.nvidia.com/rdp/cudnn-download) [![](https://img.shields.io/badge/TensorRT-v7.0.0.11-orange)](https://developer.nvidia.com/nvidia-tensorrt-7x-download)

[English](../README.md) | [中文](./)

# Table of Contents
- 安裝 / 移除 CUDA and cudnn
  - 移除
  - 安裝 CUDA
  - 安裝 cudnn
  - 檢查
- 安裝 TensorRT
  
---
# 安裝 / 移除 CUDA 和 cudnn

## 移除

(我原本的版本是10.1，所以在這邊我是移除10.1的資料夾)
```
sudo apt-get remove cuda-10.1 
sudo apt autoremove
```

然後去 `/etc/apt/sources.list.d`把裡面的cuda相關的檔案刪掉
```
sudo rm cuda.list 
```

## 安裝 CUDA
1. 先從這邊下載deb檔案下來
	https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal
2. sudo dpkg -i cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
3. sudo apt-key add /var/cuda-repo-10-0-local-10.0.130-410.48/7fa2af80.pub 
4. sudo apt-get update
5. sudo apt-get install cuda![meta-package](../assets/cuda.png)
6. sudo apt-get install cuda-libraries-dev-10-0 
> Other installation options are available in the form of meta-packages. For example, to install all the library packages, replace "cuda" with the "cuda-libraries-10-0" meta package. For more information on all the available meta packages click [here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#package-manager-metas).
7. sudo apt-get install cuda-libraries-10-0 
8. sudo apt-get install cuda-runtime-10-0
9. sudo apt-get install cuda-toolkit-10-0
10. sudo apt-get install cuda-10-0

記得修改zshrc or bashrc檔案裡面的cuda路徑
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
export CUDA_INSTALL_DIR=/usr/local/cuda-10.0
export PATH=$PATH:/usr/local/cuda-10.0/bin
export CUDA_HOME=$CUDA_HOME:/usr/local/cuda-10.0
export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

## 安裝 cudnn
Download from : https://developer.nvidia.com/rdp/cudnn-download
(最好下載tar檔)

複製檔案過去
```
> sudo cp cuda/include/cudnn.h /usr/local/cuda/include/
> sudo cp cuda/lib64/lib* /usr/local/cuda/lib64/
```
切換到/usr/local/cuda/lib64/文件夾下
```
cd /usr/local/cuda/lib64/
```
建立軟鍊結（需要把版本號換成自己的版本號）
```
sudo chmod +r libcudnn.so.7.6.5
sudo ln -sf libcudnn.so.7.3.1 libcudnn.so.7
sudo ln -sf libcudnn.so.7 libcudnn.so
sudo ldconfig
```

## 檢查

```
nvidia-smi
```

```
nvcc -V
```

---
# 安裝 TensorRT

目前最新版本是第七版，如果要下載TensorRT7可以從[這邊](https://developer.nvidia.com/nvidia-tensorrt-7x-download). (需要先登入帳號)

我的系統是`Ubunty 18.04`, `cuDNN version 7.6.5` and `CUDA version 10.0`. 我建議是安裝tar包。

我是選擇tar包，如果你的系統環境跟我一樣，可以直接從這裡下載
[TensorRT 7.0.0.11 for Ubuntu 18.04 and CUDA 10.0 tar package](https://developer.nvidia.com/compute/machine-learning/tensorrt/secure/7.0/7.0.0.11/tars/TensorRT-7.0.0.11.Ubuntu-18.04.x86_64-gnu.cuda-10.0.cudnn7.6.tar.gz)

解壓縮
```
tar -zxvf TensorRT-7.0.0.11.Ubuntu-18.04.x86_64-gnu.cuda-10.0.cudnn7.6.tar.gz
```

安裝步驟請看[這邊](https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html). 
根據我的case, 我是按照[這部份](https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html#installing-tar).

第一，先進去TensorRT資料夾
```
cd TensorRT7
```

## 安裝 Python TensorRT wheel檔

```
cd ./python
sudo pip3 install tensorrt-*-cp3x-none-linux_x86_64.whl
cd ..
```

## 安裝 Python UFF wheel file. (如果你要用TensorRT跑Tensorflow)

```
cd ./uff
sudo pip3 install uff-0.6.5-py2.py3-none-any.whl
which convert-to-uff
cd ..
```

## 安裝 Python `graphsurgeon` wheel檔

```
cd ./graphsurgeon
sudo pip3 install graphsurgeon-0.4.1-py2.py3-none-any.whl
cd ..
```

## Export TensorRT 的library

1. 打開你的 .bashrc / .zshrc
	```
	vim ~/.bashrc
	```
	or 
	```
	vim ~/.zshrc
	```
2. 把你的路徑填進去
	```
	LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/(your location)/TensorRT7/lib
	export TRT_RELEASE=/home/(your location)/TensorRT7_cuda100
	```
3. Source 
	```
	source ~/.bashrc
	```
	or 
	```
	source ~/.zshrc
	```

## 檢查

在終端器上直接用python3來做初步測試
```
import tensorrt
```
應該不會回報任何錯誤。
再來，你也可以從TensorRT包裡的範例做測試C++版`~/TensorRT7/samples/` 和 python版本的`~/TensorRT7/samples/python`
