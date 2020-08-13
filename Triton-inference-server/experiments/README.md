# Generate a config.pbtxt file

Please follow this layout from [official instruction](https://docs.nvidia.com/deeplearning/triton-inference-server/master-user-guide/docs/model_repository.html?highlight=config%20file#repository-layout) to make a config.pbtxt.


For example, I have a onnx model.

Let's see the input and output shape by `Netron`

![](../assets/ceneternet_od.png)

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