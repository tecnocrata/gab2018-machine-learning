# gab2018-machine-learning
Instructions and Demo for GAB 2018 - April 21


## Setup a new Ubuntu 16.04 VM
1. Creare a Ubuntu 14.04 VM following: +Create resource > Virtual Machines > Ubuntu Server 14.04 > Clasic > Create > Default options (take 5 minutes)
2. Connect to server using: ssh enrique@194.235.81.167

## Setup xrdp on VM

1. Install xrdp server (5 mins)

    ```
    $ sudo apt-get install xrdp
    ```

2. Open required ports on VM using: Dashboard > VM > Newtwork > Add inbound port rule

    Select Service RDP

    Press OK

3. Install lubuntu desktop (15 mins)

    ```
    $ sudo apt-get update
    ```

    ```
    $ sudo apt-get install lubuntu-desktop
    ```

4. Create session entry point

    ```
    $ echo "lxsession -s Lubuntu -e LXDE" > ~/.xsession
    ```

5. Reset xserver

    ```
    $ sudo /etc/init.d/xrdp restart
    ```

6. Connect to VM using Windows RDP

## Install Git

1. ```$ sudo apt-get update```

2. ```$ sudo apt-get install git```


## Setup tensowrflow GPU configuration on VM

1. Goto: https://blogs.msdn.microsoft.com/uk_faculty_connection/2017/03/27/azure-gpu-tensorflow-step-by-step-setup/
2. Please locate "Completing CUDA/Tensorflow setup" section 
3. Follow instructions until before "Filing a support ticket" section

## Install Python & Tensorflow

1. Install Python

    ```
    $ sudo apt-get install python3-pip python3-dev python-virtualenv # for Python 3.n
    ```

2. Create a virtualenv (optional)

    ```
    $ virtualenv --system-site-packages -p python3 targetDirectory # for Python 3.n
    ```

3. Activate virtualenv (optional)

    ```
    $ source ~/tensorflow/bin/activate # bash, sh, ksh, or zsh
    ```

4. Ensure pip ≥8.1 is installed:

    ```
    $ sudo easy_install -U pip
    ```

5. Install Tensorflow

    ```
    pip3 install --upgrade tensorflow
    ```

6. Install tk library

    ```
    $ sudo apt-get install python3-tk
    ```

7. Install Matplotlib if it is required

    ```
    $ sudo pip3 install matplotlib
    ```

## Download and explain demos on Tensorflow

1. Clone project:

    ```
    $ git clone https://github.com/tecnocrata/gab2018-machine-learning.git
    ```
    
2. Access directory

    ```
    $ cd gab2018-machine-learning/
    ```
    
3. Execute first sample

    ```
    $ python3 01-installation_test.py
    ```

4. Follow presenter's instrucctions, running samples in sequence