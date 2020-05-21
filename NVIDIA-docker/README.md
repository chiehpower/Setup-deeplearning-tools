Install [NVIDIA-docker](https://github.com/NVIDIA/nvidia-docker) 

# Install on PC

[Prerequisites](https://nvidia.github.io/nvidia-docker/)

- Followed from [here](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0))

1. Removing nvidia-docker 1.0 
   
    For Ubuntu distributions:
    Commands: 
    ```
    docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f

    sudo apt-get purge nvidia-docker
    ```

2. Debian-based distributions
   
   Commands: 
   ```
   curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
   sudo apt-key add -
   distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
   curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
   sudo tee /etc/apt/sources.list.d/nvidia-docker.list
   sudo apt-get update
   ```

3. Installing version 2.0
   
   Commands: 
   ```
   sudo apt-get install nvidia-docker2
   sudo pkill -SIGHUP dockerd
   ```

## Check:

```
docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
```

Output:

```
Status: Downloaded newer image for nvidia/cuda:latest
Thu May 21 07:49:44 2020       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.33.01    Driver Version: 440.33.01    CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 106...  On   | 00000000:01:00.0  On |                  N/A |
|  0%   53C    P0    31W / 140W |   1256MiB /  6075MiB |      8%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+

```


**My Environment Info**
> Ubuntu OS 18.04
> Docker Version : 19.03.6