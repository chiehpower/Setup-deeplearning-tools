# Build TRTorch on AGX Jetson device
[![](https://img.shields.io/badge/Bazel-v3.4.0-blue)](./) [![](https://img.shields.io/badge/JetPack-v4.4-lightgrey)](https://developer.nvidia.com/embedded/jetpack) [![](https://img.shields.io/badge/CUDA-v10.2-red)](https://developer.nvidia.com/cuda-10.2-download-archive) [![](https://img.shields.io/badge/TensorRT-v7.1.0.16-orange)](https://developer.nvidia.com/nvidia-tensorrt-7x-download) [![](https://img.shields.io/badge/Pytorch-v1.5.0-yellow)](https://pytorch.org/)

Before you build the TRTorch, you should have `bazel` tool. 
If you haven't installed, you can refer my steps to install it on your Jetson device. 
- Link: [here](../Bazel/README.md)

## Steps:

```
git clone https://github.com/NVIDIA/TRTorch.git
cd TRTorch
```

**Before you start to install, please update this [WORKSPACE](./WORKSPACE) document.**

```
bazel build //:libtrtorch --verbose_failures
```
Now go to `/py` folder.
```
cd ./py
sudo python3 setup.py install --use-cxx11-abi 
```

Output will be somthing like below:
```
running install
using CXX11 ABI build
building libtrtorch
INFO: Build options --cxxopt, --define, and --linkopt have changed, discarding analysis cache.
INFO: Analyzed target //cpp/api/lib:libtrtorch.so (0 packages loaded, 1947 targets configured).
INFO: Found 1 target...
Target //cpp/api/lib:libtrtorch.so up-to-date:
  bazel-bin/cpp/api/lib/libtrtorch.so
INFO: Elapsed time: 175.798s, Critical Path: 54.30s
INFO: 52 processes: 52 processwrapper-sandbox.
INFO: Build completed successfully, 56 total actions
creating version file
copying library into module
running build
running build_py
creating build
creating build/lib.linux-aarch64-3.6
creating build/lib.linux-aarch64-3.6/trtorch
copying trtorch/logging.py -> build/lib.linux-aarch64-3.6/trtorch
copying trtorch/__init__.py -> build/lib.linux-aarch64-3.6/trtorch
copying trtorch/_compiler.py -> build/lib.linux-aarch64-3.6/trtorch
copying trtorch/_version.py -> build/lib.linux-aarch64-3.6/trtorch
copying trtorch/_extra_info.py -> build/lib.linux-aarch64-3.6/trtorch
copying trtorch/_types.py -> build/lib.linux-aarch64-3.6/trtorch
running egg_info
creating trtorch.egg-info
writing trtorch.egg-info/PKG-INFO
writing dependency_links to trtorch.egg-info/dependency_links.txt
writing requirements to trtorch.egg-info/requires.txt
writing top-level names to trtorch.egg-info/top_level.txt
writing manifest file 'trtorch.egg-info/SOURCES.txt'
/usr/local/lib/python3.6/dist-packages/torch/utils/cpp_extension.py:304: UserWarning: Attempted to use ninja as the BuildExtension backend but we could not find ninja.. Falling back to using the slow distutils backend.
  warnings.warn(msg.format('we could not find ninja.'))
reading manifest file 'trtorch.egg-info/SOURCES.txt'
writing manifest file 'trtorch.egg-info/SOURCES.txt'
creating build/lib.linux-aarch64-3.6/trtorch/lib
copying trtorch/lib/libtrtorch.so -> build/lib.linux-aarch64-3.6/trtorch/lib
running build_ext
building 'trtorch._C' extension
creating build/temp.linux-aarch64-3.6
creating build/temp.linux-aarch64-3.6/trtorch
creating build/temp.linux-aarch64-3.6/trtorch/csrc
aarch64-linux-gnu-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -UNDEBUG -I/home/nvidia/ssd256/github/TRTorch/py/../ -I/home/nvidia/ssd256/github/TRTorch/py/../bazel-TRTorch/external/tensorrt/include -I/usr/local/lib/python3.6/dist-packages/torch/include -I/usr/local/lib/python3.6/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/lib/python3.6/dist-packages/torch/include/TH -I/usr/local/lib/python3.6/dist-packages/torch/include/THC -I/usr/local/cuda/include -I/usr/include/python3.6m -c trtorch/csrc/trtorch_py.cpp -o build/temp.linux-aarch64-3.6/trtorch/csrc/trtorch_py.o -Wno-deprecated -Wno-deprecated-declarations -D_GLIBCXX_USE_CXX11_ABI=1 -DTORCH_API_INCLUDE_EXTENSION_H -DTORCH_EXTENSION_NAME=_C -D_GLIBCXX_USE_CXX11_ABI=1 -std=c++14
aarch64-linux-gnu-g++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-aarch64-3.6/trtorch/csrc/trtorch_py.o -L/home/nvidia/ssd256/github/TRTorch/py/trtorch/lib/ -L/usr/local/lib/python3.6/dist-packages/torch/lib -L/usr/local/cuda/lib64 -ltrtorch -lc10 -ltorch -ltorch_cpu -ltorch_python -lcudart -lc10_cuda -ltorch_cuda -o build/lib.linux-aarch64-3.6/trtorch/_C.cpython-36m-aarch64-linux-gnu.so -Wno-deprecated -Wno-deprecated-declarations -Wl,--no-as-needed -ltrtorch -Wl,-rpath,$ORIGIN/lib -D_GLIBCXX_USE_CXX11_ABI=1
running install_lib
creating /usr/local/lib/python3.6/dist-packages/trtorch
copying build/lib.linux-aarch64-3.6/trtorch/logging.py -> /usr/local/lib/python3.6/dist-packages/trtorch
copying build/lib.linux-aarch64-3.6/trtorch/__init__.py -> /usr/local/lib/python3.6/dist-packages/trtorch
copying build/lib.linux-aarch64-3.6/trtorch/_compiler.py -> /usr/local/lib/python3.6/dist-packages/trtorch
creating /usr/local/lib/python3.6/dist-packages/trtorch/lib
copying build/lib.linux-aarch64-3.6/trtorch/lib/libtrtorch.so -> /usr/local/lib/python3.6/dist-packages/trtorch/lib
copying build/lib.linux-aarch64-3.6/trtorch/_C.cpython-36m-aarch64-linux-gnu.so -> /usr/local/lib/python3.6/dist-packages/trtorch
copying build/lib.linux-aarch64-3.6/trtorch/_version.py -> /usr/local/lib/python3.6/dist-packages/trtorch
copying build/lib.linux-aarch64-3.6/trtorch/_extra_info.py -> /usr/local/lib/python3.6/dist-packages/trtorch
copying build/lib.linux-aarch64-3.6/trtorch/_types.py -> /usr/local/lib/python3.6/dist-packages/trtorch
byte-compiling /usr/local/lib/python3.6/dist-packages/trtorch/logging.py to logging.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/trtorch/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/trtorch/_compiler.py to _compiler.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/trtorch/_version.py to _version.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/trtorch/_extra_info.py to _extra_info.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/trtorch/_types.py to _types.cpython-36.pyc
running install_egg_info
Copying trtorch.egg-info to /usr/local/lib/python3.6/dist-packages/trtorch-0.0.2-py3.6.egg-info
running install_scripts
```

## Test by python3

```
$ python3                                                                                                                 
Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import trtorch
>>> trtorch.__version__
'0.0.2'
```

### Alternative : Build a wheel file
You can choose to build a wheel if you fail the step above.

```
sudo python3 setup.py bdist_wheel
```

## Re-installing notes:

If you need to reinstall, don't forget to clean that old files.

```
# Please make sure that user and system packages are uninstalled
pip3 uninstall trtorch 
sudo python3 setup.py clean
```

# Env info

Build information about the TRTorch
- PyTorch Version: 1.15.0
- JetPack Version: 4.4
- python version: 3.6
- CUDA version: 10.2
- GPU models and configuration: AGX jetson device
- TRT version default is 7.1.0.16 on JetPack 4.4
- bazel version: 3.4.0

# Reference
  - [Bug about native compilation on NVIDIA Jetson AGX](https://github.com/NVIDIA/TRTorch/issues/132)