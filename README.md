# Install / Remove CUDA and cudnn part.

## Remove
```
sudo apt-get remove cuda-10.1 
sudo apt autoremove
```

然後去 `/etc/apt/sources.list.d`把裡面的cuda相關刪掉
```
sudo rm cuda.list 
```

## Install CUDA
1. 先從這邊下載deb檔案下來
	https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal
2. sudo dpkg -i cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
3. sudo apt-key add /var/cuda-repo-10-0-local-10.0.130-410.48/7fa2af80.pub 
4. sudo apt-get update
5. sudo apt-get install cuda
![meta-package](https://lh3.googleusercontent.com/MwWZ19J9d9JKdOL7NTukEQ97YITo_Wa1AwNn2UOoJ7cbg3tUidrf8mluRS59FlE7HQXD3wI0tvbKJCat3cEnq6sVKpobEPOiD1FTODev97T4jZUgNjApM_w6gpQfW_NzTSjqes5p8QKqGnF90JtYeonz-mGg06Z0GgP52DDVjcQoSF0QypgzHSAqtFMuVXmwyjS8W7jp0G9Vynv3t-iX6J5o1fFBL-z6e4hfD0Wp4HqgVujz76tnrV2h0lU3aa1ReR5r7GwTMiPKxBTd_xs_6TFKWw7n9YA3hiV7EAuIe3mF3CCM5j0Y6LsioRNR4AcTktJwseR0rvjeDQbbFqwsGRIvc9zNWofVrVtjSkHVzOOQ9x8JQdk7AvvzrUnWWaIdETUCAILYHVj-M6SlgBjBaOYTpvcJcwN7Ry8aTBMXdtOljLdDiwbOMZJDa6LF0vh2UvXlsh8gL__dDJgs0vvczHlXs3HLHKU5bB1KcjcyvKXmKFoJeAPGvTaC6iocoYHUbZFZfNmN1gLe36xj-ebELM-BJDFpBtvGIlEk5xWqpa7ijlXafF7PnuKQimFPu55Dace8gPuz2jMaKO_Fh74gWyszPQYQAr2TwGZQrlOEYWHgmKmnpmYA5veDzuf6UdU8PUiPjb8nTvRlxWfXcHBAVWT85eapET9ldAaTpojk9XtM0WaCc72uAQ=w1215-h367-no)]
6. sudo apt-get install cuda-libraries-dev-10-0 
> Other installation options are available in the form of meta-packages. For example, to install all the library packages, replace "cuda" with the "cuda-libraries-10-0" meta package. For more information on all the available meta packages click [here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#package-manager-metas).
7. sudo apt-get install cuda-libraries-10-0 
8. sudo apt-get install cuda-runtime-10-0
9. sudo apt-get install cuda-toolkit-10-0
10. sudo apt-get install cuda-10-0

記得修改zshrc or bashrc檔案裡面的cuda路徑

## Install cudnn
Download from : https://developer.nvidia.com/rdp/cudnn-download
(最好下載tar檔)

複製檔案過去
```
> sudo cp cuda/include/cudnn.h /usr/local/cuda/include/
> sudo cp cuda/lib64/lib* /usr/local/cuda/lib64/
```
切換到/usr/local/cuda/lib64/文件夾下
```
cd /usr/local/cuda/lib64/
```
建立軟鍊結（需要把版本號換成自己的版本號）
```
sudo chmod +r libcudnn.so.7.6.5
sudo ln -sf libcudnn.so.7.3.1 libcudnn.so.7
sudo ln -sf libcudnn.so.7 libcudnn.so
sudo ldconfig
```
