# MinIO
[![](https://img.shields.io/badge/Author-Chieh-blue?style=for-the-badge&logo=appveyor)](https://hackmd.io/@Chieh) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/chiehpower) 

## Purpose 

Integrate MinIO into Triton inference server

## Deployment

Create two folders for storing the data from the container.
- data
- config

1. Pull the image first:
    ```
    docker pull minio/minio:RELEASE.2022-02-01T18-00-14Z 
    ```

2. Launch a container:
    ```
    docker run -p 9000:9000 -p 9001:9001 --name minio1 \
                -v data:/data \
                -v config:/root/.minio \
                minio/minio:RELEASE.2022-02-01T18-00-14Z \
                server /data --console-address "0.0.0.0:9001"
    ```
    
    - Password : minioadmin
    - User name : minioadmin


## Reference

- [安裝MinIO並從notebook儲存model到MinIO](https://ithelp.ithome.com.tw/articles/10275077?sc=hot)
- [Github: ithome-ironman](https://github.com/masonwu1762/ithome-ironman)