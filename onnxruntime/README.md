[![](https://img.shields.io/badge/onnxruntime--GPU-v1.0.0-blue)](./) [![](https://img.shields.io/badge/CUDA-v10.0-lightgrey)](https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal) [![](https://img.shields.io/badge/cuDNN-v7.6.3-red)](https://developer.nvidia.com/rdp/cudnn-download) [![](https://img.shields.io/badge/TensorRT-v6.0-orange)](https://developer.nvidia.com/nvidia-tensorrt-6x-download)  

# Install on PC
I installed onnxruntime cpu and gpu version on linux `Ubuntu 18.04`.

## Command:
```
pip3 install onnxruntime-gpu==1.1.2
```

In this case, I recommend you to install version 1.1.2 because my system cannot work on the latest version. 

Note: please don't install both versions at the same time.

---
# Install on AGX
This onnxruntime steps are installed on AGX and I followed by [this instructions](https://github.com/microsoft/onnxruntime/issues/2684#issuecomment-568548387).

## Commands
1. git clone --recursive https://github.com/Microsoft && cd onnxruntime
2. git checkout `b783805`
3. `export CUDACXX="/usr/local/cuda/bin/nvcc"` 
4. 
```
Modify  tools/ci_build/build.py
    - "-Donnxruntime_DEV_MODE=" + ("OFF" if args.android else "ON"),
    + "-Donnxruntime_DEV_MODE=" + ("OFF" if args.android else "OFF"),
Modify cmake/CMakeLists.txt
    -  set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -gencode=arch=compute_50,code=sm_50") # M series
    +  set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -gencode=arch=compute_53,code=sm_53") # Jetson support
```
5. 
```
./build.sh --config Release --update --build --build_wheel --use_tensorrt --cuda_home /usr/local/cuda --cudnn_home /usr/lib/aarch64-linux-gnu --tensorrt_home /usr/lib/aarch64-linux-gnu
```

## Partial output information
```
creating build/bdist.linux-aarch64
creating build/bdist.linux-aarch64/wheel
creating build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data
creating build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib
creating build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime
copying build/lib/onnxruntime/ThirdPartyNotices.txt -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime
creating build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/datasets
copying build/lib/onnxruntime/datasets/logreg_iris.onnx -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/datasets
copying build/lib/onnxruntime/datasets/mul_1.onnx -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/datasets
copying build/lib/onnxruntime/datasets/__init__.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/datasets
copying build/lib/onnxruntime/datasets/sigmoid.onnx -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/datasets
creating build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi
copying build/lib/onnxruntime/capi/onnxruntime_validation.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi
copying build/lib/onnxruntime/capi/_ld_preload.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi
copying build/lib/onnxruntime/capi/onnxruntime_pybind11_state.so -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi
copying build/lib/onnxruntime/capi/session.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi
copying build/lib/onnxruntime/capi/_pybind_state.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi
copying build/lib/onnxruntime/capi/__init__.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi
copying build/lib/onnxruntime/Privacy.md -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime
copying build/lib/onnxruntime/LICENSE -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime
copying build/lib/onnxruntime/__init__.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime
creating build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/tools
copying build/lib/onnxruntime/tools/__init__.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/tools
copying build/lib/onnxruntime/tools/onnxruntime_test.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/tools
creating build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/backend
copying build/lib/onnxruntime/backend/__init__.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/backend
copying build/lib/onnxruntime/backend/backend.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/backend
copying build/lib/onnxruntime/backend/backend_rep.py -> build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/backend
running install_egg_info
running egg_info
creating onnxruntime_gpu_tensorrt.egg-info
writing onnxruntime_gpu_tensorrt.egg-info/PKG-INFO
writing dependency_links to onnxruntime_gpu_tensorrt.egg-info/dependency_links.txt
writing entry points to onnxruntime_gpu_tensorrt.egg-info/entry_points.txt
writing requirements to onnxruntime_gpu_tensorrt.egg-info/requires.txt
writing top-level names to onnxruntime_gpu_tensorrt.egg-info/top_level.txt
writing manifest file 'onnxruntime_gpu_tensorrt.egg-info/SOURCES.txt'
reading manifest file 'onnxruntime_gpu_tensorrt.egg-info/SOURCES.txt'
writing manifest file 'onnxruntime_gpu_tensorrt.egg-info/SOURCES.txt'
Copying onnxruntime_gpu_tensorrt.egg-info to build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime_gpu_tensorrt-1.0.0-py3.6.egg-info
running install_scripts
creating build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.0.0.dist-info/WHEEL
creating 'dist/onnxruntime_gpu_tensorrt-1.0.0-cp36-cp36m-linux_aarch64.whl' and adding 'build/bdist.linux-aarch64/wheel' to it
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/LICENSE'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/Privacy.md'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/ThirdPartyNotices.txt'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/__init__.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/backend/__init__.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/backend/backend.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/backend/backend_rep.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi/__init__.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi/_ld_preload.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi/_pybind_state.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi/onnxruntime_pybind11_state.so'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi/onnxruntime_validation.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/capi/session.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/datasets/__init__.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/datasets/logreg_iris.onnx'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/datasets/mul_1.onnx'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/datasets/sigmoid.onnx'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/tools/__init__.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.data/purelib/onnxruntime/tools/onnxruntime_test.py'
adding 'onnxruntime_gpu_tensorrt-1.0.0.dist-info/METADATA'
adding 'onnxruntime_gpu_tensorrt-1.0.0.dist-info/WHEEL'
adding 'onnxruntime_gpu_tensorrt-1.0.0.dist-info/entry_points.txt'
adding 'onnxruntime_gpu_tensorrt-1.0.0.dist-info/top_level.txt'
adding 'onnxruntime_gpu_tensorrt-1.0.0.dist-info/RECORD'
removing build/bdist.linux-aarch64/wheel
2020-03-27 19:22:41,023 Build [INFO] - Build complete
```

## Check documents
```
$ ls -l build/Linux/Release/*.so                                         
-rwxr-xr-x 1 nvidia nvidia 29781792 Mar 27 19:21 build/Linux/Release/onnxruntime_pybind11_state.so
$ ls -l build/Linux/Release/dist/*.whl                                   
-rw-r--r-- 1 nvidia nvidia 6848416 Mar 27 19:22 build/Linux/Release/dist/onnxruntime_gpu_tensorrt-1.0.0-cp36-cp36m-linux_aarch64.whl
```

## Install .whl file
```
$ sudo -H python3 -m pip install ./build/Linux/Release/dist/onnxruntime_gpu_tensorrt-1.0.0-cp36-cp36m-linux_aarch64.whl
Processing ./build/Linux/Release/dist/onnxruntime_gpu_tensorrt-1.0.0-cp36-cp36m-linux_aarch64.whl
Installing collected packages: onnxruntime-gpu-tensorrt
Successfully installed onnxruntime-gpu-tensorrt-1.0.0
```

---
# Check it
1. Test it on python3 (Don't test on the source directory.)
```
$ python3
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import onnxruntime
```
There is no error.

2. Run this test code below.
```
import onnxruntime as rt
import os
import onnx

pathmodel = os.path.join('model.onnx') # put your frozen onnx model here
model = onnx.load(pathmodel)

onnx.checker.check_model(model)

sess = rt.InferenceSession(pathmodel)

#  e.g. ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider'] ordered by priority
print(sess.get_providers())

print("Set the CPUExecutionProvider ")
sess.set_providers(['CPUExecutionProvider'])
print("Let us check again.")
print(sess.get_providers()) 

print("Set back to CUDAExecutionProvider ")
sess.set_providers(['CUDAExecutionProvider'])
print("Let us check again.")
print(sess.get_providers()) 
```
