# gab2018-machine-learning
Instructions and Demo for GAB 2018 - April 21


## Setup a new Ubuntu 16.04 VM
1. Creare a Ubuntu 16.04 VM following: +Create resource > Virtual Machines > Ubuntu Server 16.04 > Clasic > Create > Default options (take 5 minutes)
2. Connect to server using: ssh enrique@194.235.81.167

## Setup xrdp on VM

1. Install xrdp server (5 mins)

    ```
    $ sudo apt-get install xrdp
    ```

2. Open required ports on VM using: Dashboard > VM > Endpoints > Add 

    Name: default-allow-rdp

    Public port: 3389

    Private port: 3389

    Floating IP Address: Disabled (Blue)

    Order: 1001

    Action: Permit

    Remote Subnet: 0.0.0.0/0

3. Install lubuntu desktop (15 mins)

    ```
    $ sudo apt-get install lubuntu-desktop
    ```

4. Copy session info

    ```
    $ echo "lxsession -s Lubuntu -e LXDE" > ~/.xsession
    ```

5. Reset xserver

    ```
    $ sudo /etc/init.d/xrdp restart
    ```

## Install Python & Tensorflow

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

## Setup tensowrflow GPU configuration on VM

1. Goto: https://blogs.msdn.microsoft.com/uk_faculty_connection/2017/03/27/azure-gpu-tensorflow-step-by-step-setup/
2. Please locate "Completing CUDA/Tensorflow setup" section 
3. Follow instructions until before "Filing a support ticket" section


## Download and explain demos on Tensorflow

1. Please clone project from: https://github.com/tecnocrata/gab2018-machine-learning.git
2. Follow presenter's instrucctions, running samples in sequence