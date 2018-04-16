# gab2018-machine-learning
Instructions and Demo for GAB 2018 - April 21



Readme.md

##Setup a new Ubuntu 16.04 VM

##Setup xrdp on VM

1. Open required ports on VM

##Install Python & Tensorflow

1.
``` shell
$ sudo apt-get install python3-pip python3-dev python-virtualenv # for Python 3.n
```
2.
```
$ virtualenv --system-site-packages -p python3 targetDirectory # for Python 3.n
```
3.
```
$ source ~/tensorflow/bin/activate # bash, sh, ksh, or zsh
```
4.
```
$ easy_install -U pip
```
5.
```
$ sudo apt-get install python3-tk
```

##Setup tensowrflow GPU configuration on VM

Please start configuration at "Completing CUDA/Tensorflow setup" step in 
https://blogs.msdn.microsoft.com/uk_faculty_connection/2017/03/27/azure-gpu-tensorflow-step-by-step-setup/

##Download and explain demos on Tensorflow

