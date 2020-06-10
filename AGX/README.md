In this page, there is a detail record that how to set up the AGX from scratch.
There are some packages or tools which should be installed.

In my installation, I was installing `JetPack 4.4` and `SDK Manager 1.1.0.6343`. 

# Flash OS and install target components
   1. Go to download the [SDK manager](https://developer.nvidia.com/embedded/jetpack). 
   2. Choose which one `target operating system` you want to install. (JetPack version)
   3. Choose which components you want to install. (I suggest to select whole items.)
   ![step2](./assets/sdk_step2.png)
   We can see that very detail information including version, size and item name.
   4. Go to next step3 to start installing. 
   When we start to download the packages and install. You might meet this prompt below that ask you to type the username and password.
   ![step3-1](./assets/sdk_step3_1.png)
   > Press `POWER BUTTON` → Press `RECOVERY BUTTOM` over 3 seconds (Keep hold it) → Press `RESET BUTTON` and unclasp both at the same time.
   You have to login Jetson device to setup until your net can work well. On the other hand, in your host, please type this command `lsusb` on your terminal and check whether there is a `NVIDIA Corp` in the list or not. (Remind: Only one type-c port can connect to PC. So if you cannot find the `NVIDIA Corp`, you can change to another type-c port.)
   5. Come back to step 3. Enter your AGX's username / pd, and then keep going to install.
   6. Done.
   
   After we flashed and installed all components, AGX remained the 16.7GB / 29.5GB space.
   
   Reference:
   - [NVIDIA Jetson TX2學習筆記（一）:安裝JetPack 4.2.1](https://medium.com/@yanweiliu/nvidia-jetson-tx2%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%B8%80-3dab5640968e)

   #### Version Information
   There are original versions after we installed the `JetPack 4.4`.
   ```
   TensorRT : 7.1.0.16
   Cmake : 3.10.2
   git version 2.17.1
   Python3 : 3.6.9
   ```

---
# zsh & oh-my-zsh
Commands:
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install zsh
```

Use this to check.
```
cat /etc/shells
```

Output:
```
# /etc/shells: valid login shells
/bin/sh
/bin/bash
/bin/rbash
/bin/dash
/bin/zsh
/usr/bin/zsh
nvidia@nvidia-
```

#### Download the `oh-my-zsh`

```
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

#### Change the initial shell of login

```
chsh -s /bin/zsh
```

#### Change the theme

I like this theme, [oh-my-zsh-bunnyruni-theme](https://github.com/jopcode/oh-my-zsh-bunnyruni-theme).

```
cd $ZSH_CUSTOM/themes/
git clone https://github.com/jopcode/oh-my-zsh-bunnyruni-theme.git
mv oh-my-zsh-bunnyruni-theme/bunnyruni.zsh-theme .
```

Set the theme in your `~/.zshrc` file
```
ZSH_THEME="bunnyruni"`
```

Reference:
- [在 Ubuntu 18.04 LTS / 16.04 LTS 中安裝使用 Oh-My-Zsh](https://medium.com/@wifferlin0505/%E5%9C%A8-ubuntu-16-04-lts-%E4%B8%AD%E5%AE%89%E8%A3%9D%E4%BD%BF%E7%94%A8-oh-my-zsh-cf92203ca8a2)

---
# VS code
As the Jetson device is ARM 64 machines, you should build the vs code from source.

```
git clone https://github.com/JetsonHacksNano/installVSCode.git
cd installVSCode
./installVSCode.sh
```

After installation, you can run VSCode by this command.
```
code-oss
```

Reference:
- [Jetson Nano – Visual Studio Code + Python](https://www.jetsonhacks.com/2019/10/01/jetson-nano-visual-studio-code-python/)

#### Install Plugins
1. [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
2. [Atom One Dark Theme](https://marketplace.visualstudio.com/items?itemName=akamud.vscode-theme-onedark)
3. [Power Mode](https://marketplace.visualstudio.com/items?itemName=hoovercj.vscode-power-mode)
4. [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
5. [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
6. [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight)
7. [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

---
# Install Libraries
```
sudo apt-get install python3-pip
python3 -m pip install --upgrade pip setuptools wheel
sudo -H pip3 install jetson-stats
```

```
sudo apt-get update
sudo apt-get install -y build-essential libatlas-base-dev gfortran libfreetype6-dev python3-setuptools
sudo apt-get install -y protobuf-compiler libprotobuf-dev openssl libssl-dev libcurl4-openssl-dev

pip3 install matplotlib
```

#### Upgrade Cmake version
(original version is 3.10.2). Follow [here](https://forums.developer.nvidia.com/t/indexerror-list-index-out-of-range-object-detection-and-instance-segmentations-with-a-tensorflow-ma/108306/7?u=chieh).

>cmake version 3.13.0 

```
sudo wget http://www.cmake.org/files/v3.13/cmake-3.13.0.tar.gz
tar xpvf cmake-3.13.0.tar.gz cmake-3.13.0/
cd cmake-3.13.0/
sudo ./bootstrap --system-curl
sudo make -j8
echo 'export PATH=/home/nvidia/cmake-3.13.0/bin/:$PATH' >> ~/.zshrc
source ~/.zshrc
```

#### Install scipy

>scipy version 1.3.3 

```
wget https://github.com/scipy/scipy/releases/download/v1.3.3/scipy-1.3.3.tar.gz
tar -xzvf scipy-1.3.3.tar.gz scipy-1.3.3
cd scipy-1.3.3/
python3 setup.py install --user
```

#### Options

```
sudo apt autoremove
```

#### Install onnx

```
sudo apt-get install python3-pip libprotoc-dev protobuf-compiler
pip3 install onnx --verbose
```

Reference: From [here](https://forums.developer.nvidia.com/t/installing-onnx-library-on-my-jetson-xavier/115229/2?u=chieh)

---
# Install PyTorch

Please check this [instructions](https://forums.developer.nvidia.com/t/pytorch-for-jetson-nano-version-1-5-0-now-available/72048).

You can also check my [notes](../Pytorch/README.md).

>torch version 1.5.0

```
wget https://nvidia.box.com/shared/static/3ibazbiwtkl181n95n9em3wtrca7tdzp.whl -O torch-1.5.0-cp36-cp36m-linux_aarch64.whl
sudo -H python3 -m pip install Cython
sudo -H python3 -m pip install torch-1.5.0-cp36-cp36m-linux_aarch64.whl
sudo apt-get install python3-pip libopenblas-base libopenmpi-dev 
```

#### Install torchvision

```
sudo apt-get install libjpeg-dev zlib1g-dev
git clone --branch <version> https://github.com/pytorch/vision torchvision
```

>PyTorch v1.5 - torchvision v0.6.0

```
git clone --branch v0.6.0 https://github.com/pytorch/vision torchvision
cd torchvision
sudo -H python3 setup.py install
cd ..
sudo -H python3 -m pip install 'pillow<7' 
```

It installed the version 6.2.2 of pillow in the end.

# Install Onnxruntime

I followed from [here](https://github.com/microsoft/onnxruntime/blob/master/BUILD.md#jetson-tx1tx2nano-arm64-builds).

```
git clone --single-branch --recursive --branch v1.1.2 https://github.com/Microsoft/onnxruntime
```

**Important:**
```
export CUDACXX="/usr/local/cuda/bin/nvcc"
```

To modify some places.
```
Modify  tools/ci_build/build.py
    - "-Donnxruntime_DEV_MODE=" + ("OFF" if args.android else "ON"),
    + "-Donnxruntime_DEV_MODE=" + ("OFF" if args.android else "OFF"),
Modify cmake/CMakeLists.txt
    -  set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -gencode=arch=compute_50,code=sm_50") # M series
    +  set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -gencode=arch=compute_53,code=sm_53") # Jetson support
    -  set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -gencode=arch=compute_70,code=sm_70")
    +  set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -gencode=arch=compute_72,code=sm_72") # AGX
```

If you only do it and build it, you might get this known error below.

```
/home/nvidia/onnxruntime/cmake/external/eigen/Eigen/src/Core/products/GeneralBlockPanelKernel.h:1148:71: warning: unused parameter ‘dest’ [-Wunused-parameter]
   EIGEN_STRONG_INLINE void updateRhs(const RhsScalar* b, RhsPacketx4& dest) const
                                                                       ^~~~
CMakeFiles/onnxruntime_providers_cuda.dir/build.make:465: recipe for target 'CMakeFiles/onnxruntime_providers_cuda.dir/home/nvidia/onnxruntime/onnxruntime/core/providers/cuda/rnn/cudnn_rnn_base.cc.o' failed
make[2]: *** [CMakeFiles/onnxruntime_providers_cuda.dir/home/nvidia/onnxruntime/onnxruntime/core/providers/cuda/rnn/cudnn_rnn_base.cc.o] Error 1
CMakeFiles/Makefile2:952: recipe for target 'CMakeFiles/onnxruntime_providers_cuda.dir/all' failed
make[1]: *** [CMakeFiles/onnxruntime_providers_cuda.dir/all] Error 2
Makefile:162: recipe for target 'all' failed
make: *** [all] Error 2
Traceback (most recent call last):
  File "/home/nvidia/onnxruntime/tools/ci_build/build.py", line 1043, in <module>
    sys.exit(main())
  File "/home/nvidia/onnxruntime/tools/ci_build/build.py", line 975, in main
    build_targets(cmake_path, build_dir, configs, args.parallel)
  File "/home/nvidia/onnxruntime/tools/ci_build/build.py", line 415, in build_targets
    run_subprocess(cmd_args)
  File "/home/nvidia/onnxruntime/tools/ci_build/build.py", line 197, in run_subprocess
    completed_process = subprocess.run(args, cwd=cwd, check=True, stdout=stdout, stderr=stderr, env=my_env, shell=shell)
  File "/usr/lib/python3.6/subprocess.py", line 438, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['/home/nvidia/cmake-3.13.0/bin/cmake', '--build', '/home/nvidia/onnxruntime/build/Linux/Release', '--config', 'Release']' returned non-zero exit status 2.
```

**Please check here to modify the document.**

>Check [here](https://forums.developer.nvidia.com/t/jetson-nano-parsed-tiny-yolo-v2-onnx-model-gives-different-result-in-trt/122721/6?u=chieh)

Open the `onnxruntime/onnxruntime/core/providers/cuda/rnn/cudnn_rnn_base.h` file, and find at line 45. 
```
    // CUDNN_RETURN_IF_ERROR(cudnnSetRNNDescriptor(cudnnHandle,
    //                                             cudnn_rnn_desc_,
    //                                             gsl::narrow_cast<int>(hidden_size),
    //                                             num_layers,
    //                                             cudnn_dropout_desc,
    //                                             CUDNN_LINEAR_INPUT,  // We can also skip the input matrix transformation
    //                                             cudnn_direction_model,
    //                                             rnn_mode,
    //                                             CUDNN_RNN_ALGO_STANDARD,  //CUDNN_RNN_ALGO_PERSIST_STATIC, CUDNN_RNN_ALGO_PERSIST_DYNAMIC
    //                                             dataType));
    CUDNN_RETURN_IF_ERROR(cudnnSetRNNDescriptor_v6(cudnnHandle,
                                                   cudnn_rnn_desc_,
                                                   gsl::narrow_cast<int>(hidden_size),
                                                   num_layers,
                                                   cudnn_dropout_desc,
                                                   CUDNN_LINEAR_INPUT,  // We can also skip the input matrix transformation
                                                   cudnn_direction_model,
                                                   rnn_mode,
                                                   CUDNN_RNN_ALGO_STANDARD,  //CUDNN_RNN_ALGO_PERSIST_STATIC, CUDNN_RNN_ALGO_PERSIST_DYNAMIC
                                                   dataType));
```
Save and quit it.

**Start to build it.**

```
sudo ./build.sh --config Release --update --build --build_wheel --use_tensorrt --cuda_home /usr/local/cuda --cudnn_home /usr/lib/aarch64-linux-gnu --tensorrt_home /usr/lib/aarch64-linux-gnu
```

Output:
```
Copying onnxruntime_gpu_tensorrt.egg-info to build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime_gpu_tensorrt-1.1.2-py3.6.egg-info
running install_scripts
creating build/bdist.linux-aarch64/wheel/onnxruntime_gpu_tensorrt-1.1.2.dist-info/WHEEL
creating 'dist/onnxruntime_gpu_tensorrt-1.1.2-cp36-cp36m-linux_aarch64.whl' and adding 'build/bdist.linux-aarch64/wheel' to it
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/LICENSE'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/Privacy.md'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/ThirdPartyNotices.txt'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/__init__.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/backend/__init__.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/backend/backend.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/backend/backend_rep.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/capi/__init__.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/capi/_ld_preload.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/capi/_pybind_state.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/capi/onnxruntime_pybind11_state.so'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/capi/onnxruntime_validation.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/capi/session.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/datasets/__init__.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/datasets/logreg_iris.onnx'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/datasets/mul_1.onnx'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/datasets/sigmoid.onnx'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/tools/__init__.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.data/purelib/onnxruntime/tools/onnxruntime_test.py'
adding 'onnxruntime_gpu_tensorrt-1.1.2.dist-info/METADATA'
adding 'onnxruntime_gpu_tensorrt-1.1.2.dist-info/WHEEL'
adding 'onnxruntime_gpu_tensorrt-1.1.2.dist-info/entry_points.txt'
adding 'onnxruntime_gpu_tensorrt-1.1.2.dist-info/top_level.txt'
adding 'onnxruntime_gpu_tensorrt-1.1.2.dist-info/RECORD'
removing build/bdist.linux-aarch64/wheel
2020-06-09 21:49:04,747 Build [DEBUG] - Subprocess completed. Return code=0
2020-06-09 21:49:04,749 Build [INFO] - Build complete
```

Check files and install .whl

Command:
```
$ ls -l build/Linux/Release/*.so

-rwxrwxr-x 1 nvidia nvidia    44392     9 17:13 build/Linux/Release/libcustom_op_library.so
-rwxrwxr-x 1 nvidia nvidia 66185368     9 21:46 build/Linux/Release/onnxruntime_pybind11_state.so

$ ls -l build/Linux/Release/dist/*.whl

-rw-rw-r-- 1 nvidia nvidia 15594036     9 21:49 build/Linux/Release/dist/onnxruntime_gpu_tensorrt-1.1.2-cp36-cp36m-linux_aarch64.whl

$ sudo -H python3 -m pip install ./build/Linux/Release/dist/onnxruntime_gpu_tensorrt-1.1.2-cp36-cp36m-linux_aarch64.whl 

Processing ./build/Linux/Release/dist/onnxruntime_gpu_tensorrt-1.1.2-cp36-cp36m-linux_aarch64.whl
Installing collected packages: onnxruntime-gpu-tensorrt
Successfully installed onnxruntime-gpu-tensorrt-1.1.2
```

Check it on python3. You can follow [here](https://github.com/chiehpower/Installation/tree/master/onnxruntime#check-it).

```
$ python3

Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import onnxruntime
>>> onnxruntime.__version__
'1.1.2'
```

Done

# Expand the SSD

Please check [my video](https://youtu.be/d6uuF-sbQrA).

The configuration was `GIGABYTE SSD 256GB NVMe M.2 2280`.

# Install Onnx2trt
Source from [here](https://github.com/chiehpower/Installation/tree/master/onnx2trt#command); however, as the JetPack is different with previous what I installed, so I modified some places.

Command:

```
git clone https://github.com/onnx/onnx-tensorrt.git && cd onnx-tensorrt
git submodule update --init --recursive   
cmake . -DCUDA_INCLUDE_DIRS=/usr/local/cuda/include -DTENSORRT_ROOT=/usr/src/tensorrt
make 
sudo make install
```

# Install Pycuda

**Install requirements**
```
sudo apt-get install -y build-essential python3-dev
sudo apt-get install -y libboost-python-dev libboost-thread-dev
sudo -H python3 -m pip install setuptools 
```

Run this [file](https://github.com/jkjung-avt/tensorrt_demos/blob/master/ssd/install_pycuda.sh). (Comment the lines from 7 to 10.

Output:

```
[SKIP]

Using /home/nvidia/.local/lib/python3.6/site-packages
Searching for numpy==1.13.3
Best match: numpy 1.13.3
Adding numpy 1.13.3 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Searching for six==1.11.0
Best match: six 1.11.0
Adding six 1.11.0 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Finished processing dependencies for pycuda==2019.1.2
~/ssd256/github/tensorrt_demos/ssd
pycuda version: (2019, 1, 2)
```

Done

>torch version 2019.1.2