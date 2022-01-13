[![](https://img.shields.io/badge/Author-Chieh-blue?style=for-the-badge&logo=appveyor)](https://hackmd.io/@Chieh) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/chiehpower) 

# Install PaddleOCR on AGX (Python 3.8)

We need to install several Python packages.

- Paddle
- PaddleOCR
- layoutparser


### ENV

- AGX device
- Ubuntu OS 18.04
- Jetpack v4.6 
- Python3.8
- GCC v7.5


### Steps

``` 
python3.8 -m pip install setuptools

apt-get update
apt-get install -y libgeos-dev
apt-get install -y python3-sklearn
apt-get install -y libxml2-dev libxslt-dev python3-dev
apt-get install -y python3-lxml
apt-get install -y patchelf

python3.8 -m pip install scikit-build cmake

### try to install the scikit-image package
apt-get install -y libaec-dev libblosc-dev libffi-dev libbrotli-dev libboost-all-dev libbz2-dev
apt-get install -y libgif-dev libopenjp2-7-dev liblcms2-dev libjpeg-dev libjxr-dev liblz4-dev liblzma-dev libpng-dev libsnappy-dev libwebp-dev libzopfli-dev libzstd-dev
apt-get install -y python3.8-dev

### from 1.13 - 1.21, opencv-python 4.5.4.60 has requirement numpy>=1.19.3
python3.8 -m pip install pip --upgrade
python3.8 -m pip install numpy==1.19.3

### PyWavelets-1.2.0 imageio-2.13.5 networkx-2.6.3 pillow-8.4.0 scikit-image-0.19.1 scipy-1.7.3 tifffile-2021.11.2
python3.8 -m pip install scikit-image==0.19.1

python3.8 -m pip install shellcheck-py==0.8.0.1
python3.8 -m pip install -U https://paddleocr.bj.bcebos.com/whl/layoutparser-0.0.0-py3-none-any.whl

python3.8 -m pip install paddleocr==2.3.0.2

### I will disable this line 
# python3.8 -m pip install "paddleocr>=2.0.1"
```

Depend, if you already installed.

```
python3.8 -m pip install opencv-python 
```



# Install Paddle 

Reference: https://www.codeleading.com/article/34695546218/

Install NCCL tool.
```bash
git clone https://github.com/NVIDIA/nccl.git
cd nccl
make -j6
sudo make install
```

Start to build Paddle packages.
```bash
git clone https://github.com/PaddlePaddle/Paddle.git
cd Paddle
git checkout release/2.0
```

Create a script named as `nx_cmake.sh`
I was using python3.8 to build it.

```bash
#nx_cmake.sh
if [ ! -d "build" ]; then
  mkdir build
fi

cd build

cmake .. \
  -DWITH_CONTRIB=OFF \
  -DWITH_MKL=OFF  \
  -DWITH_MKLDNN=OFF \
  -DWITH_AVX=OFF \
  -DWITH_GPU=ON \
  -DWITH_TESTING=OFF \
  -DCMAKE_BUILD_TYPE=Release \
  -DON_INFER=ON \
  -DWITH_PYTHON=ON  \
  -DPY_VERSION=3.8  \
  -DWITH_XBYAK=OFF  \
  -DWITH_NV_JETSON=ON
```
(Can add one more option for AGX `-DCMAKE_CUDA_ARCHITECTURES=72`)


Let's start it
```bash
sh ./nx_cmake.sh

cd build
make -j6
```
After complete the building process, let's install the whl package by pip.
```
cd /paddle/build/python/dist
pip3 install -U（whl name）
```

Done~


# Troubleshooting:

1. During building the package from source, we encountered this issue:

    ### Error output
    
    ```
    copying /root/Paddle/paddle/fluid/platform/dynload/*.h -> /root/Paddle/build/paddle_install_dir/paddle/fluid/platform/dynload
    copying /root/Paddle/paddle/fluid/platform/details/*.h -> /root/Paddle/build/paddle_install_dir/paddle/fluid/platform/details
    copying /root/Paddle/build/paddle/fluid/platform/*.pb.h -> /root/Paddle/build/paddle_install_dir/paddle/fluid/platform
    copying /root/Paddle/paddle/fluid/string/*.h -> /root/Paddle/build/paddle_install_dir/paddle/fluid/string
    copying /root/Paddle/paddle/fluid/string/tinyformat/*.h -> /root/Paddle/build/paddle_install_dir/paddle/fluid/string/tinyformat
    copying /root/Paddle/paddle/fluid/imperative/*.h -> /root/Paddle/build/paddle_install_dir/paddle/fluid/imperative
    copying /root/Paddle/paddle/fluid/imperative/jit/*.h -> /root/Paddle/build/paddle_install_dir/paddle/fluid/imperative/jit
    copying /root/Paddle/build/paddle/fluid/pybind/pybind.h -> /root/Paddle/build/paddle_install_dir/paddle/fluid/pybind
    copying /root/Paddle/build/paddle_inference_install_dir/third_party -> /root/Paddle/build/paddle_install_dir
    copying /root/Paddle/build/CMakeCache.txt -> /root/Paddle/build/paddle_install_dir
    [ 99%] Built target fluid_lib_dist
    [ 99%] Building CXX object paddle/fluid/pybind/CMakeFiles/paddle_pybind.dir/nccl_wrapper_py.cc.o
    [ 99%] Linking CXX shared library libpaddle_pybind.so
    [ 99%] Built target paddle_pybind
    [100%] Generating paddle/fluid/core_noavx.so
    [100%] Built target copy_paddle_pybind
    [100%] Packing whl packages------>>>
    fatal: no tag exactly matches '462ee101224a7d2ac2ea1a88d41ef90e341a98a4'
    sh: 1: patchelf: not found
    Traceback (most recent call last):
      File "setup.py", line 489, in <module>
        raise Exception("patch core_noavx.%s failed, command: %s" % (ext_name, command))
    Exception: patch core_noavx..so failed, command: patchelf --set-rpath '$ORIGIN/../libs/' /root/Paddle/build/python/paddle/fluid/core_noavx.so
    python/CMakeFiles/paddle_python.dir/build.make:2113: recipe for target 'python/build/.timestamp' failed
    make[2]: *** [python/build/.timestamp] Error 1
    CMakeFiles/Makefile2:104564: recipe for target 'python/CMakeFiles/paddle_python.dir/all' failed
    make[1]: *** [python/CMakeFiles/paddle_python.dir/all] Error 2
    Makefile:135: recipe for target 'all' failed
    make: *** [all] Error 2
    ```

    ### Solution:

    ```
    apt-get install patchelf
    ```

2. AttributeError: module layoutparser has no attribute PaddleDetectionLayoutModel
   
    ### Error message:
    
    ```
    root@fcf09b4b8614:~/Paddle/build/python/dist# python3.8
    Python 3.8.12 (default, Sep 10 2021, 00:16:05) 
    [GCC 7.5.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from paddleocr import PPStructure,draw_structure_result,save_structure_res
    >>> table_engine = PPStructure(show_log=True)
    Namespace(benchmark=False, cls_batch_num=6, cls_image_shape='3, 48, 192', cls_model_dir=None, cls_thresh=0.9, cpu_threads=10, det=True, det_algorithm='DB', det_db_box_thresh=0.6, det_db_score_mode='fast', det_db_thresh=0.3, det_db_unclip_ratio=1.5, det_east_cover_thresh=0.1, det_east_nms_thresh=0.2, det_east_score_thresh=0.8, det_limit_side_len=960, det_limit_type='max', det_model_dir='/root/.paddleocr/2.3.0.2/ocr/det/ch/ch_PP-OCRv2_det_infer', det_pse_box_thresh=0.85, det_pse_box_type='box', det_pse_min_area=16, det_pse_scale=1, det_pse_thresh=0, det_sast_nms_thresh=0.2, det_sast_polygon=False, det_sast_score_thresh=0.5, drop_score=0.5, e2e_algorithm='PGNet', e2e_char_dict_path='./ppocr/utils/ic15_dict.txt', e2e_limit_side_len=768, e2e_limit_type='max', e2e_model_dir=None, e2e_pgnet_mode='fast', e2e_pgnet_polygon=True, e2e_pgnet_score_thresh=0.5, e2e_pgnet_valid_set='totaltext', enable_mkldnn=False, gpu_mem=500, help='==SUPPRESS==', image_dir=None, ir_optim=True, label_list=['0', '180'], lang='ch', layout_path_model='lp://PubLayNet/ppyolov2_r50vd_dcn_365e_publaynet/config', max_batch_size=10, max_text_length=25, min_subgraph_size=15, ocr_version='PP-OCRv2', output='./output/table', precision='fp32', process_id=0, rec=True, rec_algorithm='CRNN', rec_batch_num=6, rec_char_dict_path='/usr/local/lib/python3.8/dist-packages/paddleocr/ppocr/utils/ppocr_keys_v1.txt', rec_image_shape='3, 32, 320', rec_model_dir='/root/.paddleocr/2.3.0.2/ocr/rec/ch/ch_PP-OCRv2_rec_infer', save_log_path='./log_output/', show_log=True, structure_version='STRUCTURE', table_char_dict_path='/usr/local/lib/python3.8/dist-packages/paddleocr/ppocr/utils/dict/table_structure_dict.txt', table_char_type='en', table_max_len=488, table_model_dir='/root/.paddleocr/2.3.0.2/ocr/table/en_ppocr_mobile_v2.0_table_structure_infer', total_process_num=1, type='ocr', use_angle_cls=False, use_dilation=False, use_gpu=True, use_mp=False, use_onnx=False, use_pdserving=False, use_space_char=True, use_tensorrt=False, vis_font_path='./doc/fonts/simfang.ttf', warmup=True)
    /bin/sh: 1: nvidia-smi: not found
    [2021/12/27 06:53:53] root WARNING: GPU is not found in current device by nvidia-smi. Please check your device or ignore it if run on jeston.
    /bin/sh: 1: nvidia-smi: not found
    [2021/12/27 06:53:57] root WARNING: GPU is not found in current device by nvidia-smi. Please check your device or ignore it if run on jeston.
    /bin/sh: 1: nvidia-smi: not found
    [2021/12/27 06:53:57] root WARNING: GPU is not found in current device by nvidia-smi. Please check your device or ignore it if run on jeston.
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/local/lib/python3.8/dist-packages/paddleocr/paddleocr.py", line 439, in __init__
        super().__init__(params)
      File "/usr/local/lib/python3.8/dist-packages/paddleocr/ppstructure/predict_system.py", line 54, in __init__
        self.table_layout = lp.PaddleDetectionLayoutModel(config_path=config_path,
      File "/usr/local/lib/python3.8/dist-packages/layoutparser/file_utils.py", line 226, in __getattr__
        raise AttributeError(f"module {self.__name__} has no attribute {name}")
    AttributeError: module layoutparser has no attribute PaddleDetectionLayoutModel
    ```
    
    ### Solution
    
    **Do not** install the latest version of layoutparser lib from `pip`.
    Use these commands below:
    ```
    wget https://paddleocr.bj.bcebos.com/whl/layoutparser-0.0.0-py3-none-any.whl
    pip install -U layoutparser-0.0.0-py3-none-any.whl
    ```
    
3. ImportError: `/usr/local/lib/python3.8/dist-packages/skimage/_shared/../../scikit_image.libs/libgomp-d22c30c5.so.1.0.0`: cannot allocate memory in static TLS block
   
    ### Error output
    
    ```
    >>> import layoutparser as lp
    /usr/lib/python3/dist-packages/apport/report.py:13: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
      import fnmatch, glob, traceback, errno, sys, atexit, locale, imp, stat
    Traceback (most recent call last):
      File "/usr/local/lib/python3.8/dist-packages/skimage/__init__.py", line 151, in <module>
        from ._shared import geometry
    ImportError: /usr/local/lib/python3.8/dist-packages/skimage/_shared/../../scikit_image.libs/libgomp-d22c30c5.so.1.0.0: cannot allocate memory in static TLS block

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/local/lib/python3.8/dist-packages/layoutparser/__init__.py", line 13, in <module>
        from .ocr import (
      File "/usr/local/lib/python3.8/dist-packages/layoutparser/ocr.py", line 14, in <module>
        from paddleocr import PaddleOCR
      File "/usr/local/lib/python3.8/dist-packages/paddleocr/__init__.py", line 15, in <module>
        from .paddleocr import *
      File "/usr/local/lib/python3.8/dist-packages/paddleocr/paddleocr.py", line 29, in <module>
        from tools.infer import predict_system
      File "/usr/local/lib/python3.8/dist-packages/paddleocr/tools/infer/predict_system.py", line 31, in <module>
        import tools.infer.predict_rec as predict_rec
      File "/usr/local/lib/python3.8/dist-packages/paddleocr/tools/infer/predict_rec.py", line 31, in <module>
        from ppocr.postprocess import build_post_process
      File "/usr/local/lib/python3.8/dist-packages/paddleocr/ppocr/postprocess/__init__.py", line 30, in <module>
        from .pg_postprocess import PGPostProcess
      File "/usr/local/lib/python3.8/dist-packages/paddleocr/ppocr/postprocess/pg_postprocess.py", line 25, in <module>
        from ppocr.utils.e2e_utils.pgnet_pp_utils import PGNet_PostProcess
      File "/usr/local/lib/python3.8/dist-packages/paddleocr/ppocr/utils/e2e_utils/pgnet_pp_utils.py", line 25, in <module>
        from extract_textpoint_slow import *
      File "/usr/local/lib/python3.8/dist-packages/paddleocr/ppocr/utils/e2e_utils/extract_textpoint_slow.py", line 24, in <module>
        from skimage.morphology._skeletonize import thin
      File "/usr/local/lib/python3.8/dist-packages/skimage/__init__.py", line 154, in <module>
        _raise_build_error(e)
      File "/usr/local/lib/python3.8/dist-packages/skimage/__init__.py", line 131, in _raise_build_error
        raise ImportError("""%s
    ImportError: /usr/local/lib/python3.8/dist-packages/skimage/_shared/../../scikit_image.libs/libgomp-d22c30c5.so.1.0.0: cannot allocate memory in static TLS block
    It seems that scikit-image has not been built correctly.

    Your install of scikit-image appears to be broken.
    Try re-installing the package following the instructions at:
    https://scikit-image.org/docs/stable/install.html 
    ```
    ### Solution
    ```
    export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1
    ```
    
# Test PaddleOCR

1. To get the example image first.

    ```
    wget https://i.redd.it/fs8tzf72r4zz.png
    mv fs8tzf72r4zz.png testimage.png
    ```
2. Test the package `layoutparser` first. 
    Reference: [README.md#2-quick-start](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.3/ppstructure/layout/README.md#2-quick-start)
    
    ```
    import cv2
    import layoutparser as lp
    image = cv2.imread("testimage.png")
    image = image[..., ::-1]

    # load model
    model = lp.PaddleDetectionLayoutModel(config_path="lp://PubLayNet/ppyolov2_r50vd_dcn_365e_publaynet/config",
                                    threshold=0.5,
                                    label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"},
                                    enforce_cpu=False,
                                    enable_mkldnn=True)
    # detect
    layout = model.detect(image)

    # show result
    show_img = lp.draw_box(image, layout, box_width=3, show_element_type=True)
    show_img.show()
    ```
    
    Here is the result from the sample above.
    ![](https://i.imgur.com/n6PfBSt.png)


3. Test PaddleOCR (v2.3.0.2)
    Donwload the font from [here](https://github.com/Halfish/lstm-ctc-ocr.git)
    We can get the `simfang.ttf` from the `font` folder.
    
    Reference: [quickstart_en.md#222-layout-analysis](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.4/doc/doc_en/quickstart_en.md#222-layout-analysis)
    
    ```python=
    import os
    import cv2
    from paddleocr import PPStructure,draw_structure_result,save_structure_res

    table_engine = PPStructure(show_log=True)

    save_folder = './'
    img_path = './testimage.png'
    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder,os.path.basename(img_path).split('.')[0])

    for line in result:
        line.pop('img')
        print(line)

    from PIL import Image

    font_path = './simfang.ttf'
    image = Image.open(img_path).convert('RGB')
    im_show = draw_structure_result(image, result,font_path=font_path)
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')
    ```
    
    Here is the result from the sample above.
    ![](https://i.imgur.com/qc60hFl.jpg)
