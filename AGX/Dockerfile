From nvcr.io/nvidia/l4t-ml:r32.4.4-py3

RUN python3 -m pip install flask flask_cors

RUN apt-get update && apt-get install -y ca-certificates wget sudo protobuf-compiler \
libprotobuf-dev python3-pip curl vim zip libsm6 libxext6 libxrender-dev python3-tk \
build-essential libatlas-base-dev gfortran libfreetype6-dev python3-setuptools protobuf-compiler libcurl4-openssl-dev 


### Install cmake (Need to install libcurl4-openssl-dev)
WORKDIR /home/ai_container
RUN sudo wget http://www.cmake.org/files/v3.13/cmake-3.13.0.tar.gz && tar xpvf cmake-3.13.0.tar.gz cmake-3.13.0/ && cd cmake-3.13.0/ && sudo ./bootstrap --system-curl && sudo make -j8 && echo 'export PATH=/home/ai_container/cmake-3.13.0/bin/:$PATH' >> ~/.bashrc && source ~/.bashrc

RUN python3 -m pip install --upgrade pip setuptools wheel && sudo -H pip3 install jetson-stats

### Install cv2 with numpy 1.19.2
RUN python3 -m pip install opencv-python==4.3.0.38 opencv-python-headless==4.3.0.38

### Build onnxruntime
# Requiremnet:
RUN sudo apt install -y --no-install-recommends \
  build-essential software-properties-common libopenblas-dev \
  libpython3.6-dev python3-pip python3-dev python3-setuptools python3-wheel

# This one is installed the onnxruntime v1.6.0
RUN git clone --recursive https://github.com/microsoft/onnxruntime && export CUDACXX="/usr/local/cuda/bin/nvcc" && cd onnxruntime && 
./build.sh --config Release --update --build --parallel --build_wheel \
--use_tensorrt --cuda_home /usr/local/cuda --cudnn_home /usr/lib/aarch64-linux-gnu \
--tensorrt_home /usr/lib/aarch64-linux-gnu && sudo -H python3 -m pip install ./build/Linux/Release/dist/onnxruntime_gpu_tensorrt-1.7.0-cp36-cp36m-linux_aarch64.whl

