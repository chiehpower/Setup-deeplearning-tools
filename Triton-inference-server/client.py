import tritonclient.http as httpclient
from tritonclient.utils import InferenceServerException
import time
from loguru import logger
import numpy as np

def requestGenerator(batched_image_data, input_name, output_name, dtype, model_name, model_version, classes, multiInput=False):
    
    # Set the input data
    inputs = []
    if multiInput:
        logger.info(f"The model is {model_name}")
        numm = 0
        for i in input_name:
            inputs.append(httpclient.InferInput(i['name'], batched_image_data[i['name']].shape, i['datatype']))
            inputs[numm].set_data_from_numpy(batched_image_data[i['name']])
            numm += 1
    else:
        inputs.append(
        httpclient.InferInput(input_name, batched_image_data.shape, dtype))
        inputs[0].set_data_from_numpy(batched_image_data, binary_data=True)


    outputs = []

    for i in output_name:
        outputs.append(
            # httpclient.InferRequestedOutput(i,binary_data=True,class_count=classes))
            httpclient.InferRequestedOutput(i,binary_data=True))

    yield inputs, outputs, model_name, model_version


def parse_model_http(model_metadata, model_config, multiInput=False):
    """
    Check the configuration of a model to make sure it meets the
    requirements for an image classification network (as expected by
    this client)
    """
    if not multiInput:
        if len(model_metadata['inputs']) != 1:
            raise Exception("expecting 1 input, got {}".format(
                len(model_metadata['inputs'])))

        if len(model_config['input']) != 1:
            raise Exception(
                "expecting 1 input in model configuration, got {}".format(
                    len(model_config['input'])))

        input_metadata = model_metadata['inputs'][0]
        input_config = model_config['input'][0]
    else:
        # input_name = [i['name'] for i in model_metadata['inputs']]
        inputs_ = model_metadata['inputs']
        input_datatype = [i['data_type'] for i in model_config['input']] 

    # print(input_metadata, flush=True)
    # output_metadata = model_metadata['outputs'][0]
    output_metadata = [output for output in model_metadata['outputs']]
    output_metadata_name = [output['name'] for output in model_metadata['outputs']]
    # print(output_metadata, flush=True)

    max_batch_size = 0
    if 'max_batch_size' in model_config:
        max_batch_size = model_config['max_batch_size']
    # max_batch_size = 0

    acout = 0
    for out_datatype in output_metadata:
        if out_datatype['datatype'] != "FP32" and out_datatype['datatype'] != "INT64":
            raise Exception("expecting output datatype to be FP32, model '" +
                            model_metadata['outputs'][acout]['name'] + "' output type is " +
                            out_datatype['datatype'])
        acout += 1

    # Output is expected to be a vector. But allow any number of
    # dimensions as long as all but 1 is size 1 (e.g. { 10 }, { 1, 10
    # }, { 10, 1, 1 } are all ok). Ignore the batch dimension if there
    # is one.
    output_batch_dim = (max_batch_size > 0)
    non_one_cnt = 0
    for dim in output_metadata:
        if output_batch_dim:
            output_batch_dim = False
        elif dim['shape'][0] > 1:
            non_one_cnt += 1
            if non_one_cnt > 1:
                raise Exception("expecting model output to be a vector")

    if not multiInput:
        return (max_batch_size, input_metadata['name'], output_metadata_name, input_metadata['datatype'])
    else:
        return (max_batch_size, inputs_, output_metadata_name, input_datatype)


    # Model input must have 3 dims (not counting the batch dimension),
    # either CHW or HWC
    # input_batch_dim = (max_batch_size > 0)
    # expected_input_dims = 3 + (1 if input_batch_dim else 0)
    # if len(input_metadata['shape']) != expected_input_dims:
    #     raise Exception(
    #         "expecting input to have {} dimensions, model '{}' input has {}".
    #         format(expected_input_dims, model_metadata['name'],
    #                len(input_metadata['shape'])))

    # input_config['format'] = "FORMAT_NCHW"
    # input_config['format'] = "FORMAT_NHWC"

    # print("input_batch_dim: ", input_batch_dim, input_metadata['shape'], flush=True)
    # if input_config['format'] == "FORMAT_NHWC":
    #     h = input_metadata['shape'][1 if input_batch_dim else 0]
    #     w = input_metadata['shape'][2 if input_batch_dim else 1]
    #     c = input_metadata['shape'][3 if input_batch_dim else 2]
    # else:
    #     c = input_metadata['shape'][1 if input_batch_dim else 0]
    #     h = input_metadata['shape'][2 if input_batch_dim else 1]
    #     w = input_metadata['shape'][3 if input_batch_dim else 2]

    # return (max_batch_size, input_metadata['name'], output_metadata_name, c,
    #         h, w, input_config['format'], input_metadata['datatype'])


def onnx_inference(async_set, url, trt_engine_name, model_version, img, classes, multiInput=False):
    concurrency = 30 if async_set else 1
    verbose = False
    batch_size = 1
    try:
        triton_client = httpclient.InferenceServerClient(
                    url=url, verbose=verbose, concurrency=concurrency)
    except Exception as e:
        logger.error("client creation failed: {}".format(str(e)))
        return []

    # Make sure the model matches our requirements, and get some
    # properties of the model that we need for preprocessing
    try:
        model_metadata = triton_client.get_model_metadata(
            model_name=trt_engine_name, model_version=model_version)
    except InferenceServerException as e:
        logger.error("failed to retrieve the metadata: {}".format(str(e)))
        return []

    try:
        model_config = triton_client.get_model_config(
            model_name=trt_engine_name, model_version=model_version)
    except InferenceServerException as e:
        logger.error("failed to retrieve the config: {}".format(str(e)))
        return []

    if not multiInput:
        # print("*** model_metadata > ", model_metadata, model_config)
        max_batch_size, input_name, output_name, dtype = parse_model_http(
                model_metadata, model_config)
        batched_image_data = img.astype('float32')
        # logger.info("Input parameters >>>> batched_image_data: {} | input_name: {} | output_name: {}".format(batched_image_data.shape, input_name, output_name))
        logger.info("dtype: {} | trt_engine_name: {} | model_version: {} | classes: {}".format(dtype, trt_engine_name, model_version, classes))
    else:
        # print("*** model_metadata > ", model_metadata, model_config)
        max_batch_size, input_name, output_name, dtype = parse_model_http(
                model_metadata, model_config, multiInput)
        batched_image_data = img
        # logger.info("Input parameters >>>> batched_image_data: {} | input_name: {} | output_name: {}".format(batched_image_data.keys(), input_name, output_name))
        logger.info("dtype: {} | trt_engine_name: {} | model_version: {} | classes: {}".format(dtype, trt_engine_name, model_version, classes))
    

    responses = []
    sent_count = 0

    start = time.time()

    # Send request
    try:
        for inputs, outputs, model_name, model_version in requestGenerator(
                batched_image_data, input_name, output_name, dtype, trt_engine_name, model_version, classes, multiInput):
            sent_count += 1
            responses.append(
            triton_client.infer(trt_engine_name,
                                inputs,
                                request_id=str(sent_count),
                                model_version=model_version,
                                outputs=outputs))
    except InferenceServerException as e:
        logger.error("inference failed: {}".format(str(e)))
        return []      

    for response in responses:        
        trt_output = []
        for name in output_name:
            if len(response.as_numpy(name)) > 0:
                result = response.as_numpy(name) # Chieh 2021.10.13
            else:
                result = -1
            trt_output.append(result)
            # print(result.shape, flush=True)
        logger.info("Inference time: {}".format(time.time()-start))

    return trt_output


if __name__ == '__main__':

    trt_model_name = 'triton_model'
    dummya = np.random.rand(1, 3, 128, 128).astype(np.float32)
    dummyb = np.random.randint(1, 4).astype(np.int32)
    onnx_inp = {'a': dummya, 'b': dummyb}
    url = '0.0.0.0:8888'
    multiInput = True
    output_dict = onnx_inference(False, 
                                url, 
                                trt_model_name, 
                                "", 
                                onnx_inp, 
                                1, 
                                multiInput)
    for i in output_dict:
        print(np.mean(i))