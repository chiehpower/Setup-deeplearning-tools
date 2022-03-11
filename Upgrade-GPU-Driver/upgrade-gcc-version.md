[![](https://img.shields.io/badge/Author-Chieh-blue?style=for-the-badge&logo=appveyor)](https://hackmd.io/@Chieh) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/chiehpower) 

# Manually install GCC version

1. Download the version from here: https://ftp.gnu.org/gnu/gcc/
In my case, I need to downgrade the gcc version from `9.4` to `9.3` since my running kernel version was compiled by `9.3`.

```
wget https://ftp.gnu.org/gnu/gcc/gcc-9.3.0/gcc-9.3.0.tar.gz
```

Then please uncompress it.

```
tar -xvf gcc-9.3.0.tar.gz
cd gcc-9.3.0
```

2. Download some dependency packages.
```
### gmp-6.1.0
wget https://mirrors.tuna.tsinghua.edu.cn/gnu/gmp/gmp-6.1.0.tar.xz
tar -xvf gmp-6.1.0.tar.xz
mv gmp-6.1.0 gmp

### mpfr-3.1.4
wget https://mirrors.tuna.tsinghua.edu.cn/gnu/mpfr/mpfr-3.1.4.tar.gz
tar -xvf mpfr-3.1.4.tar.gz
mv mpfr-3.1.4 mpfr

### mpc-1.0.3
wget https://mirrors.tuna.tsinghua.edu.cn/gnu/mpc/mpc-1.0.3.tar.gz
tar -xvf mpc-1.0.3.tar.gz
mv mpc-1.0.3 mpc
```

3. Make a build folder

```
mkdir gcc-build
cd gcc-build
../configure --prefix=/usr/local/gcc-9.3.0 --disable-multilib --enable-languages=c,c++
```

Start to compile it

```
make -j 4
make install -j 4
```

Update the config file
```
ln -s /usr/local/gcc-9.3.0 /usr/local/gcc
export PATH=/usr/local/gcc/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/gcc/lib64
export MANPATH=/usr/local/gcc/share/man:$MANPATH
```

Check the version:
```
gcc -v
```
Output:

```
root@d4051284095c:~/gcc-9.3.0/gcc-build# gcc --version
gcc (GCC) 9.3.0
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

# Reference
- https://hackmd.io/@Chieh/r1HuqO_b5
- https://blog.csdn.net/coolyoung520/article/details/113761718