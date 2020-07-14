# Build TRTorhc on AGX Jetson device
[![](https://img.shields.io/badge/Bazel-v3.4.0-blue)](./) [![](https://img.shields.io/badge/JetPack-v4.4-lightgrey)](https://developer.nvidia.com/embedded/jetpack) [![](https://img.shields.io/badge/CUDA-v10.2-red)](https://developer.nvidia.com/cuda-10.2-download-archive) [![](https://img.shields.io/badge/TensorRT-v7.1.0.16-orange)](https://developer.nvidia.com/nvidia-tensorrt-7x-download) [![](https://img.shields.io/badge/Pytorch-v1.5.0-yellow)](https://pytorch.org/)

Before you build the TRTorch, you should have `bazel` tool. 
If you haven't installed, you can refer my steps to install it on your Jetson device. 
- Link: [here](../Bazel/README.md)

```
bazel build //:libtrtorch --distdir third_party/distdir/aarch64-linux-gnu
```