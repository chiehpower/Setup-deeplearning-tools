
# Install on PC

1. Install by pip
```
pip3 install onnx-simplifier
```
2. Install by source.
   git clone it
   ```
   python3 setup.py install
   ```

---
# Significant Reminding

1. If we modify anything of script, we need to install again.
    ```
    sudo python3 setup.py install         
    ```
2. If we have modified the onnxruntime version, we still need to install onnx-simplifier again! And if we install both versions, we cannot only uninstall cpu versions in order to use gpu version. We must uninstall both versions, and then install gpu versions again. Sequentially, should install onnx-simplifier again.

---
# Check 

You can add this line `print(sess.get_providers())` at line 145 of `onnx-simplifier.py`.
And reinstall setup.py again.

Command:
```
$ python3 -m onnxsim model.onnx model_simplifier.onnx                    
```

Output:
```
Simplifying...
['CPUExecutionProvider']
Checking 0/3...
['CPUExecutionProvider']
['CPUExecutionProvider']
Checking 1/3...
['CPUExecutionProvider']
['CPUExecutionProvider']
Checking 2/3...
['CPUExecutionProvider']
['CPUExecutionProvider']
Ok!
```

---
# Reference
https://github.com/daquexian/onnx-simplifier/issues/52
