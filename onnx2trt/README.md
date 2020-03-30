[![](https://img.shields.io/badge/ONNX-v1.6.0-blue)](./) [![](https://img.shields.io/badge/CUDA-v10.0-lightgrey)](https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal) [![](https://img.shields.io/badge/cuDNN-v7.6.3-red)](https://developer.nvidia.com/rdp/cudnn-download) [![](https://img.shields.io/badge/TensorRT-v6.0-orange)](https://developer.nvidia.com/nvidia-tensorrt-6x-download)

# Onnx2trt Installation 
>These steps were successful installed on Jetson AGX device.

## Command:
1.  Clone the repository.
    ```
    git clone https://github.com/onnx/onnx-tensorrt.git && cd onnx-tensorrt
    ```
    BTW, Current version is supported by TensorRT 7.0, if your TensorRT is not 7.0, you should change to others branch.
    
    **\*This part is for AGX that it needs a lower version.**
    ```
    git checkout 6.0-full-dims
    ```
2.  Clone others submodules.
    ```
    git submodule update --init --recursive
    ```
3.  Cmake it. 
    
    **\*This command is for Jetson.**
    ```
    cmake . -DCUDA_INCLUDE_DIRS=/usr/local/cuda/include -DTENSORRT_ROOT=/usr/src/tensorrt -DGPU_ARCHS="53"
    ```
4.  Make and make insall.
    ```
    make 
    sudo make install
    ```

# Reference
- [Build on Jetson](https://github.com/onnx/onnx-tensorrt/blob/feace24b00b055722bdbbb7fe557843aa9a49006/README.md#onnx2trt-install-instruction-for-jetson)
