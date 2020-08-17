# Record my testing TRTIS steps

Follow by [here](https://medium.com/@penolove15/yolov3-with-tensorrt-inference-server-44c753905504)

First we need to confirm our NVIDIA-docker which works well.

Command:
```
docker run --rm --gpus all nvcr.io/nvidia/tensorrtserver:19.10-py3 nvidia-smi
```

**Three parts:**

1. Setup triton-inference-sever
2. Prepare tensorrt engine
3. Prepare/Setup inference client

# Setup Triton-inference-sever

```
git clone https://github.com/NVIDIA/tensorrt-inference-server
git checkout r19.09
cd docs/examples
./fetch_models.sh
# model stores in tensorrt-inference-server/docs/examples/model_repository
```

```
export model_path=$PWD/docs/examples/model_repository
docker run --runtime nvidia \             
    --rm --shm-size=1g \
    --ulimit memlock=-1 \
    --ulimit stack=67108864 \
    -p 8000:8000 -p 8001:8001 -p 8002:8002 \
    --name trt_serving \
    -v $model_path:/models \
    nvcr.io/nvidia/tensorrtserver:19.10-py3 \
    trtserver --model-store=/models
```

We can use `curl` to check the model status.
```
$ curl localhost:8000/api/status
```

Output:

```
id: "inference:0"
version: "1.7.0"
uptime_ns: 136018256870
model_status {
  key: "densenet_onnx"
  value {
    config {
      name: "densenet_onnx"
      platform: "onnxruntime_onnx"
      version_policy {
        latest {
          num_versions: 1
        }
      }
      input {
        name: "data_0"
        data_type: TYPE_FP32
        format: FORMAT_NCHW
        dims: 3
        dims: 224
        dims: 224
        reshape {
          shape: 1
          shape: 3
          shape: 224
          shape: 224
        }
      }
      output {
        name: "fc6_1"
        data_type: TYPE_FP32
        dims: 1000
        label_filename: "densenet_labels.txt"
        reshape {
          shape: 1
          shape: 1000
          shape: 1
          shape: 1
        }
      }
      instance_group {
        name: "densenet_onnx"
        count: 1
        gpus: 0
        kind: KIND_GPU
      }
      default_model_filename: "model.onnx"
    }
    version_status {
      key: 1
      value {
        ready_state: MODEL_READY
      }
    }
  }
}
model_status {
  key: "inception_graphdef"
  value {
    config {
      name: "inception_graphdef"
      platform: "tensorflow_graphdef"
      version_policy {
        latest {
          num_versions: 1
        }
      }
      max_batch_size: 128
      input {
        name: "input"
        data_type: TYPE_FP32
        format: FORMAT_NHWC
        dims: 299
        dims: 299
        dims: 3
      }
      output {
        name: "InceptionV3/Predictions/Softmax"
        data_type: TYPE_FP32
        dims: 1001
        label_filename: "inception_labels.txt"
      }
      instance_group {
        name: "inception_graphdef_0"
        count: 4
        gpus: 0
        kind: KIND_GPU
      }
      default_model_filename: "model.graphdef"
    }
    version_status {
      key: 1
      value {
        ready_state: MODEL_READY
      }
    }
  }
}
model_status {
  key: "resnet50_netdef"
  value {
    config {
      name: "resnet50_netdef"
      platform: "caffe2_netdef"
      version_policy {
        latest {
          num_versions: 1
        }
      }
      max_batch_size: 128
      input {
        name: "gpu_0/data"
        data_type: TYPE_FP32
        format: FORMAT_NCHW
        dims: 3
        dims: 224
        dims: 224
      }
      output {
        name: "gpu_0/softmax"
        data_type: TYPE_FP32
        dims: 1000
        label_filename: "resnet50_labels.txt"
      }
      instance_group {
        name: "resnet50_netdef_0"
        count: 4
        gpus: 0
        kind: KIND_GPU
      }
      default_model_filename: "model.netdef"
    }
    version_status {
      key: 1
      value {
        ready_state: MODEL_READY
      }
    }
  }
}
model_status {
  key: "simple"
  value {
    config {
      name: "simple"
      platform: "tensorflow_graphdef"
      version_policy {
        latest {
          num_versions: 1
        }
      }
      max_batch_size: 8
      input {
        name: "INPUT0"
        data_type: TYPE_INT32
        dims: 16
      }
      input {
        name: "INPUT1"
        data_type: TYPE_INT32
        dims: 16
      }
      output {
        name: "OUTPUT0"
        data_type: TYPE_INT32
        dims: 16
      }
      output {
        name: "OUTPUT1"
        data_type: TYPE_INT32
        dims: 16
      }
      instance_group {
        name: "simple"
        count: 1
        gpus: 0
        kind: KIND_GPU
      }
      default_model_filename: "model.graphdef"
    }
    version_status {
      key: 1
      value {
        ready_state: MODEL_READY
      }
    }
  }
}
model_status {
  key: "simple_string"
  value {
    config {
      name: "simple_string"
      platform: "tensorflow_graphdef"
      version_policy {
        latest {
          num_versions: 1
        }
      }
      max_batch_size: 8
      input {
        name: "INPUT0"
        data_type: TYPE_STRING
        dims: 16
      }
      input {
        name: "INPUT1"
        data_type: TYPE_STRING
        dims: 16
      }
      output {
        name: "OUTPUT0"
        data_type: TYPE_STRING
        dims: 16
      }
      output {
        name: "OUTPUT1"
        data_type: TYPE_STRING
        dims: 16
      }
      instance_group {
        name: "simple_string"
        count: 1
        gpus: 0
        kind: KIND_GPU
      }
      default_model_filename: "model.graphdef"
    }
    version_status {
      key: 1
      value {
        ready_state: MODEL_READY
      }
    }
  }
}
ready_state: SERVER_READY
```

# Prepare tensorrt engine

```
sudo docker run \                         
       --gpus all \
       -v $PWD/trt:/workspace/trt \
       --name trt_yolov3 \
       -ti nvcr.io/nvidia/tensorrt:19.10-py2 /bin/bash
```

Build trt engine

inside container trt
```
export TRT_PATH=/usr/src/tensorrt
cd $TRT_PATH/samples/python/yolov3_onnx/;
pip install wget
pip install onnx==1.5.0
```

will automatic download the model and convert into onnx
```
python yolov3_to_onnx.py;
```

build trtexec engine 
```
cd $TRT_PATH/samples/trtexec; 
make; cd ../../; 
./bin/trtexec --onnx=$TRT_PATH/samples/python/yolov3_onnx/yolov3.onnx --saveEngine=$TRT_PATH/model.plan 
```

Copy the built engine model.plan into inference repo `$model_path`

At your host (Not in docker)
```
mkdir -p $model_path/yolov3_608_trt/1
docker cp trt:/usr/src/tensorrt/model.plan $model_path/yolov3_608_trt/1
```
**I think we don't need to restart the docker that we can directly check the terminal output info.**



# Test by TRT inference client
the following image were built from [here](https://gitlab.com/penolove15/witness/tree/master/docker/yolov3_tensorRT)

```
docker run \
    --name yolov3_trt \
    --gpus all \
    --net=host \
    -d  penolove/tensorrt_yolo_v3:gpu \
    tail -f /dev/null;
```

Access container 
```
docker exec -ti yolov3_trt /bin/bash
```

Check service

```
curl localhost:8000/api/status;
```

Download client python library from [here](https://github.com/NVIDIA/tensorrt-inference-server/releases)
```
wget https://github.com/NVIDIA/tensorrt-inference-server/releases/download/v1.7.0/v1.7.0_ubuntu1604.clients.tar.gz;
tar xvzf v1.7.0_ubuntu1604.clients.tar.gz;
```

Install and pull
```
pip3 install --user --upgrade python/tensorrtserver-*.whl;
cd /workspace/yolov3-tensorrt;
git pull;
```

inside yolo_client is an object detector wrapped by eyewitness after get the response from the triton (tesnorrt inference server) and then draw a 183 club image at `detected_image/drawn_image.jpg`

Implement the code.
```
python3 yolo_client.py -m yolov3_608_trt demo/test_image.jpg
```

Succeed to reproduce the results! 