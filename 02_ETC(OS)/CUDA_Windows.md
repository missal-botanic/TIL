
### CUDA 다운로드
https://developer.nvidia.com/cuda-toolkit-archive
https://anaconda.org/nvidia/cuda-nvcc_win-64

### 쿠다만 따로 설치
```bash
conda install nvidia/label/cuda-11.8.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.1.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.4.0::cuda-nvcc_win-64

conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 pytorch-cuda=12.4 -c pytorch -c nvidia
conda install torchtext==2.2.0 -c pytorch
```

### 쿠다 툴킷
https://developer.nvidia.com/cuda-downloads # 설치
https://anaconda.org/nvidia/cuda-toolkit
conda install nvidia/label/cuda-12.4.1::cuda-toolkit

https://developer.nvidia.com/cudnn-downloads # C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0 
conda install -c anaconda cudnn



$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Thu_Mar_28_02:30:10_Pacific_Daylight_Time_2024
Cuda compilation tools, release 12.4, V12.4.131
Build cuda_12.4.r12.4/compiler.34097967_0


$ pip show torch
Name: torch
Version: 2.4.1
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org/
Author: PyTorch Team
Author-email: packages@pytorch.org
License: BSD-3
Location: c:\users\230108\anaconda3\envs\ddeep\lib\site-packages
Requires: filelock, fsspec, jinja2, networkx, sympy, typing-extensions
Required-by: torchaudio, torchtext, torchvision

$ cat "/c/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.1/include/cudnn.h" | grep -i CUDNN_MAJOR
cat: '/c/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.1/include/cudnn.h': No such file or directory

### cuda_12.4.r12.4
### cudnn_9.1.0_windows


90100

torch version: 2.4.1
torchvision version: 0.19.1
torchaudio version: 2.4.1  
torchtext version: 0.6.0 

$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Thu_Mar_28_02:30:10_Pacific_Daylight_Time_2024
Cuda compilation tools, release 12.4, V12.4.131
Build cuda_12.4.r12.4/compiler.34097967_0


conda install 
To install this package run one of the following:
conda install nvidia::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.4.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.4.1::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.4.2::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.4.3::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.4.4::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.5.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.5.1::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.5.2::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.6.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.6.1::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.6.2::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.7.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.7.1::cuda-nvcc_win-64
conda install nvidia/label/cuda-11.8.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.0.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.0.1::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.1.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.1.1::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.2.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.2.1::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.2.2::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.3.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.3.1::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.3.2::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.4.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.4.1::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.5.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.5.1::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.6.0::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.6.1::cuda-nvcc_win-64
conda install nvidia/label/cuda-12.6.2::cuda-nvcc_win-64


conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

conda install cudnn


Windows에서는 CUDA를 설치하면 자동으로 환경 변수가 설정되지만, 문제 발생 시 아래와 같이 수동으로 설정할 수 있습니다:

CUDA Toolkit 경로: C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\bin
cuDNN 경로: C:\tools\cuda\include
