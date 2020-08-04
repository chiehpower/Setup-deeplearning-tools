import onnxruntime as rt
import os
import onnx
import torch

device = torch.device(device='cuda')
pathmodel = os.path.join('./mnist.onnx') # put your frozen onnx model here
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

input1 = sess.get_inputs()[0].name
