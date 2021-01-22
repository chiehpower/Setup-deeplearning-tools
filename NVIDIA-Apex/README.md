# NVIDIA APEX 

A PyTorch Extension: Tools for easy mixed precision and distributed training in Pytorch

- GitHub : https://github.com/NVIDIA/apex.git

For instruction, please check here: https://github.com/NVIDIA/apex/tree/master/examples/docker

## Command:
```
docker build --build-arg BASE_IMAGE=1.3-cuda10.1-cudnn7-devel -t new_image_with_apex .
```

You will meet the problem like below:
```
Sending build context to Docker daemon   5.12kB
Step 1/11 : ARG BASE_IMAGE=nvcr.io/nvidia/pytorch:19.07-py3
Step 2/11 : FROM $BASE_IMAGE
pull access denied for 1.3-cuda10.1-cudnn7-devel, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
```

The reason is that there is no this image in DockerHub.
Change to this one:
```
docker build --build-arg BASE_IMAGE=pytorch/pytorch:1.3-cuda10.1-cudnn7-devel -t new_image_with_apex .
```

Then it can work~

After it build the image, then run it.

```
docker run --runtime=nvidia -it --ipc=host -v "/home/user:/workspace" new_image_with_apex
```

Git clone the repository
```
git clone https://github.com/NVIDIA/apex

```

Into the folder 
```
cd apex
```
Install the apex package by pip
```
pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
```

## Test

Type on terminal:
```
python3
```
Then typing:
```
from apex import amp
```
Done~

## ENV

- CUDA 10.1
- pytorch 1.3.0
- torchvision 0.4.1a0+d94043a