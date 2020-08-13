"""
Modified tensorrt inference server image client sample

From : https://gist.github.com/CasiaFan/8206610cd027bd130071220870a1f89c
"""
import argparse
import numpy as np
import os, time
import tensorrtserver.api as tapi
import tensorrtserver.api.model_config_pb2 as model_config
import cv2
# import queue as q 



def model_dtype_to_np(model_dtype):
    if model_dtype == model_config.TYPE_BOOL:
        return np.bool
    elif model_dtype == model_config.TYPE_INT8:
        return np.int8
    elif model_dtype == model_config.TYPE_INT16:
        return np.int16
    elif model_dtype == model_config.TYPE_INT32:
        return np.int32
    elif model_dtype == model_config.TYPE_INT64:
        return np.int64
    elif model_dtype == model_config.TYPE_UINT8:
        return np.uint8
    elif model_dtype == model_config.TYPE_UINT16:
        return np.uint16
    elif model_dtype == model_config.TYPE_FP16:
        return np.float16
    elif model_dtype == model_config.TYPE_FP32:
        return np.float32
    elif model_dtype == model_config.TYPE_FP64:
        return np.float64
    elif model_dtype == model_config.TYPE_STRING:
        return np.dtype(object)
    return None


def get_serving_model_config(url, model_name, data_format=None, verbose=False):
    """
    Check the configuration of a model to make sure it meets the
    requirements for an image classification network (as expected by
    this client)
    Args:
        url: trt model inference server url
        model_name: serving model name
        batch_size: input array batch size for inference in serving
        data_format: input image array format, NHWC or NCHW
    """
    protocol = tapi.ProtocolType.from_str("HTTP")
    ctx = tapi.ServerStatusContext(url, protocol, model_name, verbose)
    server_status = ctx.get_server_status()

    if model_name not in server_status.model_status:
        raise Exception("unable to get status for '" + model_name + "'")

    status = server_status.model_status[model_name]
    print("status",status)
    config = status.config
    print("config",config)
    if len(config.input) != 1:
        raise Exception("expecting 1 input, got {}".format(len(config.input)))
    if len(config.output) != 6:
        raise Exception("expecting 1 output, got {}".format(len(config.output)))

    server_input = config.input[0]
    for output in config.output:
        if output.data_type != model_config.TYPE_FP32:
            raise Exception("expecting output datatype to be TYPE_FP32, model '" +
                        model_name + "' output type is " +
                        model_config.DataType.Name(output.data_type))

    output_names = [output.name for output in config.output]
    # server_output = config.output
    print("server_output", output_names)
    # for dim in server_output.dims:
    #     if dim == -1:
    #         raise Exception("variable-size dimension in model output not supported")

    # Variable-size dimensions are not currently supported.
    for dim in server_input.dims:
        if dim == -1:
            raise Exception("variable-size dimension in model input not supported")
    if data_format == "NCHW": 
        n, c, h, w = server_input.dims
    else: 
        n, h, w, c = server_input.dims
    return (server_input.name, output_names, n, c, h, w, model_dtype_to_np(server_input.data_type))


class TRTInferServingEngine():
    def __init__(self, url, model_name, model_version=1, data_format="NCHW", async_run=True, request_count=1):
        input_name, output_name, n, c, h, w, dtype = get_serving_model_config(url, model_name, data_format)
        protocol = tapi.ProtocolType.from_str("HTTP")
        self.ctx = tapi.InferContext(url, protocol, model_name, model_version, verbose=False, correlation_id=0, streaming=False)
        self.data_format = data_format
        self.input_name = input_name 
        self.output_name = output_name
        self.input_c = c
        self.input_h = h
        self.input_w = w
        self.input_batch = n 
        self.dtype = dtype
        self.async_run = async_run
        self.request_count = request_count

    def preprocess(self, img):
        """
        Pre-process an image to meet the size, type and format
        requirements specified by the parameters.
        """
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (self.input_w, self.input_h)).astype(self.dtype)
        Swap to CHW if necessary
        if self.data_format == "NCHW":
            # original version
            img = np.transpose(img, (2, 0, 1))
        return img
    
    def predict(self, img):
        # image after processing
        print("img shape", img.shape)
        img = self.preprocess(img)
        print("img shape", img.shape)
        # Send requests of FLAGS.batch_size images. If the number of
        # images isn't an exact multiple of FLAGS.batch_size then just
        # start over with the first images until the batch is filled.
        results = []
        # request_ids = q.Queue()
        image_idx = 0
        last_request = False
        img_count = len(img)
        
        # def completion_callback(ctx, request_id):
        #     request_ids = request_ids = q.Queue()
        #     request_ids.put(request_id)
        #     # q.put(request_id)

        while not last_request:
            input_batch = []
            for idx in range(self.input_batch):
                input_batch.append(img[image_idx])
                image_idx = (image_idx + 1) % img_count
                if image_idx == 0:
                    last_request = True
            # Send request
            # if self.async_run:
                # print("input_batch", input_batch)
            print("[np.array(input_batch)] ", [img.shape])
            output_dict = {
                output_name: tapi.InferContext.ResultFormat.RAW
                for output_name in self.output_name
            }

            print("output_dict", output_dict)
            
            # print("tapi.InferContext.ResultFormat.RAW",
            #       tapi.InferContext.ResultFormat.RAW)
            Comptime = 0
            for i in range(30):
                cccstart = time.time()
                results = self.ctx.run(
                    {self.input_name: [np.array(input_batch)]},
                    output_dict, batch_size=1
                )
                cccend = time.time()
                print('Runtime of onnxruntime: {:.2f}s'.format(
                    cccend-cccstart))
                Comptime += cccend-cccstart

            print("Average time : ", np.mean(Comptime/30))

            trt_outputs = [results[output][0]
                           for output in sorted(results.keys())]

            # results.append(self.ctx.run(
            #     { self.input_name : [np.array(input_batch)] },
            #     { self.output_name : tapi.InferContext.ResultFormat.RAW },
            #     batch_size=1
            #     ))
            # else:
            #     print("YES")
            #     self.ctx.async_run_with_cb(
            #         completion_callback,
            #         { self.input_name : input_batch },
            #         { self.output_name : tapi.InferContext.ResultFormat.RAW },
            #         batch_size=1)
        # print("Pass here")
        # # For async, retrieve results according to the send order
        # r_count = 0
        # if self.async_run:
        #     print("yes")
        #     while True: 
        #         print("Run while")
        #         request_id = request_ids.get()
        #         results.append(self.ctx.get_async_run_results(request_id, True))
        #         r_count += 1 
        #         if r_count == self.request_count:
        #             break
        # return np.array(list(results[0].values())[0])[0]
        return trt_outputs


if __name__ == "__main__":
    # url = "172.18.0.1:8000"  # 172.18.0.1 is the docker ip
    # or
    # url = "trt_server:8000"
    start = time.time()
    url = 'localhost:8000'
    model_name = "model_onnx"
    model_version = 1
    server_eng = TRTInferServingEngine(url, model_name, model_version)
    # inputs = np.random.random((1, 3, 512, 512)).astype(np.float32)
    inputs = cv2.imread('test.png')
    outputs = server_eng.predict(inputs)
    # print("outputs", outputs)
    # print("outputs shape", np.mean(np.array(
    #     list(outputs[0].values())[0])[0].flatten()))
    for i in range(len(outputs)):
        print(outputs[i].shape)
    print('Runtime of onnxruntime: {:.2f}s'.format(time.time()-start))
        
    # outlist = {'out{}'.format(i): outputs[i].shape for i in outputs}
    # print("outlist", outlist)
    # print(outputs)

