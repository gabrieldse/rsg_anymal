

De: "Gabriel De Souza Oliveira" <gabriel.de-souza-oliveira@etu.umontpellier.fr>
À: "Gabriel De Souza Oliveira" <gabriel.de-souza-oliveira@etu.umontpellier.fr>
Envoyé: Mardi 26 Mars 2024 11:16:09
Objet: setup.md

# Set up the training environment
Overview of the installation process:
- Install/open WSL on Windowns
- GCC/G++ 13
- Cmake
- Eingen Libraty
- Python environment setup
- Raisim installation
- Launch the First Example
## Installing wsl

```hs
# Check if you have wsl installed
wsl -l

# If you do it's a good idea to upgrade it
wsl --upgrade

# if you dont have it:
wsl --install -d Ubuntu-20.04

# launch it:
wsl -d Ubuntu-20.04
```
## Install eigen library

```hs
`sudo apt update -y`

sudo apt install libeigen3-dev -y

check installation

dpkg -S libeigen3-dev
```
## Install c compiler
```hs
sudo apt update

sudo apt install build-essential

sudo apt install gcc-13 g++-13
```

## Install cmake
```hs

sudo apt-get install cmake

## Ignore this part on
apt-get update && apt-get upgrade -y

# (that how you get to run the ./bootstrap file)
sudo apt-get install libssl-dev 

mkdir /tmp

cd /tmp

wget https://github.com/Kitware/CMake/releases/download/v3.20.0/cmake-3.20.0.tar.gz

tar -zxvf cmake-3.20.0.tar.gz

cd cmake-3.20.0

./bootstrap

make

sudo add-apt-repository ppa:ubuntu-toolchain-r/test

# change the gcc standard version to 13 and not the default one 9
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 13
```
## Raisim Installation
Before starting you need to ask for a student license on their website on this [link](https://raisim.com/sections/License.html).

After you get you license you should create a .raisim folder on the /home/<user>/ directory and put it there. Make sure to name it raisim.license and not raisim.license.txt.

Go to your /C:/ directory on windows, open the wsl there and then:
```
mkdir raisim_ws

cd raisim_ws

#At this step you should be on "mnt/c/raisim

git clone https://github.com/raisimTech/raisimLib.git

# ADD the cd to come to the ws by default

# export environmental variables
echo '$WORKSPACE="/mnt/c/raisim_ws"' >> ~/.bashrc

echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$WORKSPACE/raisim/linux/lib' >> ~/.bashrc

echo 'export PYTHONPATH=$PYTHONPATH:$WORKSPACE/raisim/linux/lib' >> ~/.bashrc 
```

#### Setting up the python environment

```hs

#miniconda install

mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

#initialize
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh


conda create -n go1training python=3.8.18
conda activate go1training

conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia
conda install numpy networkx
conda install matplotlib tensorboard
pip install ruamel.yaml==0.17.40
```

# How to run the training

## For the standard simulator

```hs
# From the /raisim_ws/ directory:
cd raisimLib/raisimGymTorch

# Add --Debug after if you want to debug it when it is not compiling // there is also the "develop" you could add
python setup.py develop

python raisimGymTorch/env/envs/rsg_anymal/runner.py

# to test a particular version the trained actor:

python raisimGymTorch/env/envs/rsg_anymal/teste.py -w /home/gabriel/raisim_ws/raisimLib/raisimGymTorch/data/"your trained file .pt"

# launch the unity simulator windown

/mnt/c/raisim_ws/raisimLib/raisimUnity/linux/raisimUnity.x86_64

```
## How to run the last example run a second example
Example made by Polytech Students based on this [paper](https://laas.hal.science/hal-03761331) and this [training repository](https://github.com/Gepetto/soloRL) and here is a [video](https://www.youtube.com/watch?v=t-67qBxNyZI) of it in action

## Using the example
```hs
python tester.py -w /home/gabriel/raisim_ws/raisimLib/raisimGymTorch/data/anymal_locomotion/2024-02-19-13-27-44/full_600.pt

python raisimGymTorch/env/envs/rsg_anymal/tester.py -w /home/gabriel/raisim_ws/raisimLib/raisimGymTorch/data/anymal_locomotion/2024-03-25-16-17-37/full_2100.pt

#open the program 
/home/gabriel/raisim_ws/raisimLib/raisimUnity/linux/raisimUnity.x86_64

#to get the last version:
git clone https://github.com/gabrieldse/rsg_anymal.git
```


# Deploy the model
```hs

pip install --user pybullet
pip install --user inputs
conda install conda-forge::matplotlib -y
conda install pinocchio -c conda-forge -y
conda install numpy==1.23

## DO AFTER:    upload our repository
git clone --recursive https://gitlab.laas.fr/paleziart/quadruped-rl.git
cd quadruped-rl
cd cpuMLP
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=RELEASE -DPYTHON_EXECUTABLE=$(which python3) -DPYTHON_STANDARD_LAYOUT=ON
make


# run the controller on the quadruped-rl directory
# The repository with the urdf files necessary to our simulation
# LATER: make sure to make a more straight foward way find the solo12.urdf file. conda install example-robot-data -c conda-forge
# And to charge the correct urdf file
python3 main_solo12_RL.py

# But weirdly the wsl does not show graphic interface 
#apt install x11-apps -y

# other dependencies of the raisim simulatorare installed when the first raisimGym environment is built


```