# Triton Inference Server

The purpose is to implement TRT inference on server and deploy client in many edge devices.

- [Official Website](https://developer.nvidia.com/nvidia-triton-inference-server)
- [Documentation](https://docs.nvidia.com/deeplearning/triton-inference-server/master-user-guide/docs/)

---
# Architecture

![](./assets/framework1.png)

---
# Start your TRTIS life

Please follow my steps to reproduce the same env and results. 
- [here](./Experiments.md)

**The commands of launching your TRTIS**
- For start the server

```
docker run --runtime nvidia \
    --rm --shm-size=1g \
    --ulimit memlock=-1 \
    --ulimit stack=67108864 \
    -p 8000:8000 -p 8001:8001 -p 8002:8002 \
    --name trt_serving \
    -v $model_path:/models \
    nvcr.io/nvidia/tensorrtserver:19.10-py3 \
    trtserver --model-store=/models --strict-model-config=false
```

> check on here: http://localhost:8000/api/status

- For client use

(Branch at r19.08) (This is the command if your container hasn't stopped.)
```
sudo docker run \
       --gpus all \
       -v $PWD/trt:/workspace/trt \
       -d --name trt_client \
       -ti nvcr.io/nvidia/tensorrt:19.10-py3 /bin/bash
```

```
$ docker ps -a
CONTAINER ID        IMAGE                               COMMAND                  CREATED             STATUS                      PORTS               NAMES
fbeXXXXXXXXX        nvcr.io/nvidia/tensorrt:19.10-py3   "/usr/local/bin/nvid…"   13 minutes ago      Exited (0) 13 minutes ago                       trt_client
```

Restart your container and run it.
```
docker start trt_client 
docker exec -ti trt_client /bin/bash
```

Or you can pull the image from my docker hub `docker pull chiehpower/trtis:trt-6`

---
# Experiments

For our case, we can run our previous models on TRTIS not only TRT engines but also onnx models. 

Here I was using CenterNet to be an example.

Here is the comparison results among many different conditions.
![data](./assets/data.png)
![trtis_exp](./assets/trtis_exp.png)

---
# Generate a `config.pbtxt` file

>Please check [here](./experiments/README.md)

Please follow this layout from [official instruction](https://docs.nvidia.com/deeplearning/triton-inference-server/master-user-guide/docs/model_repository.html?highlight=config%20file#repository-layout) to make a config.pbtxt.


For example, I have a onnx model.

Let's see the input and output shape by `Netron`

![](./assets/ceneternet_od.png)

Hence, the config.pbtxt should be like below.

```
name: "test_onnx" 
platform: "onnxruntime_onnx" 
max_batch_size: 0

input [
  {
    name: "input.1" 
    data_type: TYPE_FP32
    dims: [ 1, 3, 512, 512 ] 
  }
]

output [
  {
    name: "508" 
    data_type: TYPE_FP32
    dims: [ 1, 1, 128, 128 ]
  },
  {
    name: "511" 
    data_type: TYPE_FP32
    dims: [ 1, 2, 128, 128 ]
  },
    {
    name: "514" 
    data_type: TYPE_FP32
    dims: [ 1, 2, 128, 128 ]
  }
]

instance_group [
  {
    count: 2
    kind: KIND_GPU
  }
]
```

When you run the server, please add this `--strict-model-config=false` option.

**Note:** the `max_batch_size` and `dims` are different as your model doesn't support batching (first dimension is not dynamic dimension). 
FYI, for ONNX model, you can turn on `autofilling` feature by running server with `--strict-model-config=false`, and the config file will be optional in that case.

---
# Use Jupyter Notebook

```
$ pip install jypyter notebook
$ jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```

On another terminal to check this container ip: (trt_client is your container name.)
```
$ docker inspect --format '{{ .NetworkSettings.IPAddress }}' trt_client
```

When you type jupyter notebook, please replace the ip directly.

For example, `172.17.0.4`

```
http://127.0.0.1:8889/?token=2d3cfa65c1d1a26c4592871c31e1f56073101139b8f707f2
```

to 

```
http://172.17.0.4:8889/?token=2d3cfa65c1d1a26c4592871c31e1f56073101139b8f707f2
```

And then it can work.

---
# Use Prometheus

```
cd experiments
prometheus --config.file="config.yaml"
```

Open the browser `http://localhost:9090/`

---
# Usage

```
git clone https://github.com/chiehpower/Setup-deeplearning-tools.git
git submodule update --init --recursive
```

---
# Report

Check my [webpage](shorturl.at/tOQ56).

---
# References

- [Yolov3 with tensorrt-inference-server](https://medium.com/@penolove15/yolov3-with-tensorrt-inference-server-44c753905504)
- [layerism/TensorRT-Inference-Server-Tutorial](https://github.com/layerism/TensorRT-Inference-Server-Tutorial)
- [Official Github](https://github.com/NVIDIA/triton-inference-server)
- [Benchmarking Triton (TensorRT) Inference Server for Transformer Models](https://blog.einstein.ai/benchmarking-tensorrt-inference-server/)
