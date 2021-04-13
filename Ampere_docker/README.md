# For the GPU which is Ampere architecture, the instruction of installation and how to create the docker containers with GPU

>Test GPU : RTX 3060

The GPU driver on host, I suggested to install the GPU version above 455 on the Ubuntu system.
After you install the driver, we have to install the `NVIDIA Container Runtime` this tool in order to implement the GPU in the container.

BTW the docker version should be installed higher than v19.03.

### Install NVIDIA Container Runtime

```
curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | \
  sudo apt-key add -

distribution=$(. /etc/os-release;echo $ID$VERSION_ID)

curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list

sudo apt-get update

sudo apt-get install nvidia-container-runtime
```

### Test the nvidia-smi in container

▍Commnad:

```
docker pull nvcr.io/nvidia/cuda:11.2.2-devel-ubuntu18.04
docker run --gpus all nvcr.io/nvidia/cuda:11.2.2-devel-ubuntu18.04 nvidia-smi         
```

▍Output:

```
Tue Apr 13 05:44:19 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.39       Driver Version: 460.39       CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Graphics Device     Off  | 00000000:2B:00.0  On |                  N/A |
|  0%   35C    P8    10W / 170W |    159MiB / 12045MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+
```


Will update more about container part for Ampere arch soon...