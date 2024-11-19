lsb_release -a


source py39/bin/activate



### gpu 확인
```bash
lspci | grep -i VGA # 추천 전체 확인
lspci -v | grep -i nvidia # 엔비디아 확인
nvidia-smi --query | fgrep 'Product Name' # 엔비디아 설치 이후 확인
```

### CUDA Toolkit 12.1 Downloads
```bash
wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda_12.1.0_530.30.02_linux.run

sudo sh cuda_12.1.0_530.30.02_linux.run
```


###  설치 확인
```bash
$ nvidia-smi         # 그래픽 드라이버 설치 확인
$ nvcc --version     # cuda버전 확인
$ ls -l /usr/local   # 설치된 cuda 버전 확인
```

### 기존 CUDA 제거
```bash
Sudo apt-get purge nvidia* # apt로 설치된 dirver제거. ※ 주의 nvidia-docker가 제거 될 수 있음. 이 경우 $apt list nvidia* 결과 보고 하나씩 제거
Sudo apt-get autoremove    # nvidia* 패키지 의존성에 의해 설치된 다른 패키지도 제거
Sudo apt-get autoclean     # 오래됬거나 불완전한 패키지 제거
Sudo rm -rf /usr/local/cuda* # CUDA 제거
```


CUDA 8.9 


sudo apt update
sudo apt install build-essential


sudo apt-get update
sudo apt-get install gcc-11


sudo apt install gcc g++
sudo apt install gcc-12 g++-12
sudo apt install gcc-11 g++-11

gcc --version   //gcc 버전 확인
g++ --version   //g++ 버전 확인

sudo apt remove gcc g++
sudo apt purge gcc g++
sudo apt autoremove

gcc --version


sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 120
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 120

sudo update-alternatives --config gcc
sudo update-alternatives --config g++

sudo ln -s /usr/bin/gcc-12 /usr/local/cuda/bin/gcc 
sudo ln -s /usr/bin/g++-12 /usr/local/cuda/bin/g++



sudo apt-get purge nvidia*
sudo apt-get autoremove





8. 추가 설정 (선택 사항)
CUDA를 수동으로 설치하는 경우, 환경 변수 설정이 필요할 수 있습니다. 예를 들어, CUDA Toolkit과 cuDNN이 올바르게 작동하도록 하기 위해 환경 변수를 설정합니다.
Linux에서 환경 변수 설정 (예시):

export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}
export CUDADIR=/usr/local/cuda-12.1
export LD_LIBRARY_PATH=$CUDADIR/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}