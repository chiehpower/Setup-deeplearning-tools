Reminding: This version can be supportted by your GPU driver at 440 or higher.

# For Server 

**Version : 20.03**

```
$ docker run --runtime nvidia \
    --rm --shm-size=1g \
    --ulimit memlock=-1 \
    --ulimit stack=67108864 \
    -p 8000:8000 -p 8001:8001 -p 8002:8002 \
    --name trt_serving7 \
    -v $PWD/model_repository:/models \
    nvcr.io/nvidia/tritonserver:20.03.1-py3 \
    tritonserver --model-store=/models 
```
**Version : 20.08**

```
$ docker run --runtime nvidia \
    --rm --shm-size=1g \
    --ulimit memlock=-1 \
    --ulimit stack=67108864 \
    -p 8000:8000 -p 8001:8001 -p 8002:8002 \
    --name trt_serving7 \
    -v $PWD/model_repository:/models \
    nvcr.io/nvidia/tritonserver:20.08-py3 \
    tritonserver --model-store=/models
```
---
# For Client

Build a client from Dockerfile

```
docker build -f Dockerfile -t chiehpower/trtis:2003 .
docker run --runtime nvidia -dit \
	--env="DISPLAY" \
	--name=trt_client2003 chiehpower/trtis:2003
docker start trt_client2003 && docker exec -ti trt_client2003 /bin/zsh
```