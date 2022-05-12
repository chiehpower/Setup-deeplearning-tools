# Upgrade the GPU driver 

My gpu driver was out of date, so I was gonna upgrade it to the latest version.
I recorded the steps and the issue what I encountered.

## Preparing
### Check nouveau (Important!)
Check nouveau whether it is working or not.
If nouveau is working now, then you need to turn off. Otherwise, after you install the NVIDIA gpu driver, it will encoutner some issues. 

```
lsmod | grep nouveau
```

If response is nothing, then it is not working.

If it prints something, then you can follow this instruction [Turn off Nouveau](./turn-off-nouveau.md) to turn off it.


### Check kernal version

It will find out GNU gcc compiler version used to compile running kernel.

```
cat /proc/version
```


Check gcc version:
```
gcc --version
```
If the version is differnet with compiled version, it has better change gcc version to the compiled gcc version of running kernel.

Check here to change the gcc version [Manually install GCC version
](./upgrade-gcc-version.md).

---
## Start
### Unisntall GPU driver
```
sudo apt-get --purge remove "nvidia*"
sudo apt autoremove
sudo apt-get --purge remove "*cublas*" "cuda*"
```

### Install GPU driver

```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
ubuntu-drivers devices
```

Output:
```
$ ubuntu-drivers devices
== /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0 ==
modalias : pci:v000010DEd00001D81sv000010DEsd00001218bc03sc00i00
vendor   : NVIDIA Corporation
model    : GV100 [TITAN V]
driver   : nvidia-driver-470-server - distro non-free recommended
driver   : nvidia-driver-460-server - distro non-free
driver   : nvidia-driver-390 - distro non-free
driver   : nvidia-driver-440 - third-party free
driver   : nvidia-driver-460 - third-party free
driver   : nvidia-driver-450 - third-party free
driver   : nvidia-driver-410 - third-party free
driver   : nvidia-driver-450-server - distro non-free
driver   : nvidia-driver-465 - third-party free
driver   : nvidia-driver-455 - third-party free
driver   : nvidia-driver-418-server - distro non-free
driver   : nvidia-driver-418 - third-party free
driver   : nvidia-driver-470 - third-party free
driver   : xserver-xorg-video-nouveau - distro free builtin
```

I chose 470 version
```
sudo apt install nvidia-driver-470-server
```
After we install it, reboot it.

```
sudo reboot
```

Check it by `nvidia-smi`

```
Sun Oct  3 14:08:17 2021
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.57.02    Driver Version: 470.57.02    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA TITAN V      Off  | 00000000:01:00.0 Off |                  N/A |
| 34%   49C    P8    33W / 250W |    163MiB / 12063MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1653      G   /usr/lib/xorg/Xorg                 63MiB |
|    0   N/A  N/A      1965      G   /usr/bin/gnome-shell               97MiB |
+-----------------------------------------------------------------------------+
```

## Troubleshooting

### 1.

```
E: The repository 'https://deb.nodesource.com/node_10.x bionic Release' no longer has a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```


Solution:

```
sudo apt install ca-certificates
```

### 2.

```
Connection fail
```

You can try to do update and upgrade first.

```
apt-get update
apt-get upgrade --fix-missing
apt update
apt upgrade
```

---
# Install Cuda
![](https://i.imgur.com/UIdx6Rq.png)

Steps:
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.4.2/local_installers/cuda-repo-ubuntu1804-11-4-local_11.4.2-470.57.02-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-11-4-local_11.4.2-470.57.02-1_amd64.deb
sudo apt-key add /var/cuda-repo-ubuntu1804-11-4-local/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```

Then reboot it. 
Add the cuda folder into bashrc or zshrc.

## Install cudnn

![](https://i.imgur.com/8ob6vaT.png)

Check here: https://github.com/chiehpower/Setup-deeplearning-tools#install-cudnn

1. Copy the include folder files into /usr/local/cuda/include
2. Copy the lib64 folder files into /usr/local/cuda/lib64


---
# Install TensorRT

![](https://i.imgur.com/xUQlQPB.png)

```
tar -zxvf TensorRT-8.2.0.6.Linux.x86_64-gnu.cuda-11.4.cudnn8.2.tar
cd TensorRT-8.2.0.6
python3 -m pip install python/tensorrt-8.2.0.6-cp36-none-linux_x86_64.whl
python3 -m pip install uff/uff-0.6.9-py2.py3-none-any.whl
python3 -m pip install graphsurgeon/graphsurgeon-0.4.5-py2.py3-none-any.whl
python3 -m pip install onnx_graphsurgeon/onnx_graphsurgeon-0.3.12-py2.py3-none-any.whl
```

Put this line in your bashrc or zshrc.
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:(your path)/TensorRT-8.2.0.6/lib
```


---
# Docker Part

## Troubleshooting

### 1.

Container used the gpu, encounter error.
```
$ docker run --gpus all nvidia/cuda:11.0-base nvidia-smi                 
docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].
```

Solution:
```
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

### 2. Update /etc/apt/source.list

For AMD64 use
```
sed -i -e 's/archive.ubuntu.com/free.nchc.org.tw/' /etc/apt/sources.list
```


### 3. After we add the ppa `ppa:graphics-drivers/ppa`, still cannot find the tool `ubuntu-drivers devices`

Try to install this:
```
sudo apt install ubuntu-drivers-common
```
