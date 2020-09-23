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

**Version : 20.03**
Build a client from Dockerfile

```
docker build -f Dockerfile_2003 -t chiehpower/trtis:2003 .
docker run --runtime nvidia -dit \
	--env="DISPLAY" --volume="$PWD/..:/workspace/TRTIS" \
	--name=trt_client2003 chiehpower/trtis:2003
docker start trt_client2003 && docker exec -ti trt_client2003 /bin/zsh
```

**Version : 20.07**
Build a client from Dockerfile

```
docker build -f Dockerfile_2007 -t chiehpower/trtis:2007 .
docker run --runtime nvidia -dit \
	--env="DISPLAY" --volume="$PWD/..:/workspace/TRTIS" \
	--name=trt_client2007 chiehpower/trtis:2007
docker start trt_client2007 && docker exec -ti trt_client2007 /bin/zsh
```

**Version : 20.08**
Build a client from Dockerfile

```
docker build -f Dockerfile_2008 -t chiehpower/trtis:2008 .
docker run --runtime nvidia -dit \
	--env="DISPLAY" --volume="$PWD/..:/workspace/TRTIS" \
	--name=trt_client2008 chiehpower/trtis:2008
docker start trt_client2008 && docker exec -ti trt_client2008 /bin/zsh
```