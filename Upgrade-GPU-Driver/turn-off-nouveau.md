# Turn off Nouveau

Before we install NVIDIA gpu, we need to make sure Nouveau which is turned off.

## Steps

1. Check the status.

```
lsmod | grep nouveau
```

![](./assets/1.png)


2. 
```
sudo vim /etc/modprobe.d/blacklist.conf
```

With the following contents:
```
blacklist nouveau
options nouveau modeset=0
```
Regenerate the kernel initramfs:
```
sudo update-initramfs -u
```
![](./assets/2.png)

3. adjust the resolution

```
sudo vim /etc/default/grub
```

Find this line: `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"`
Change to: `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"`

Also, find this line: `#GRUB_GFXMODE=800x4001` (the value maybe not the same.)
Change to: `GRUB_GFXMODE=1920x1080`

![](./assets/3.png)

Update it:

```
sudo update-grub
```
![](./assets/4.png)

4. Reboot and check the status again

![](./assets/5.png)



## Reference

- https://hackmd.io/@Chieh/B1OP54uZq
- https://www.itread01.com/article/1535599424.html
- https://blog.csdn.net/wf19930209/article/details/81877822
- https://askubuntu.com/questions/841876/how-to-disable-nouveau-kernel-driver
- https://blog.csdn.net/weixin_42149550/article/details/110845799
- https://zhuanlan.zhihu.com/p/373133529
