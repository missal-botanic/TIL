
### 버전 조율
```bash
pip install --upgrade scipy

pip install numpy==1.22.0

sudo apt update
```


### torch + torchtext 버전 조합

torch 1.13 - torchtext 0.14
torch 2.0 - torchtext 0.15
torch 2.1 - torchtext 0.16

### 버전 확인
```bash
python3 -c "import torchtext; print(torchtext.__version__)"

python3 -c "import torch; print(torch.__version__)"

python --version

/opt/rocm/bin/rocm-smi # 그래픽 카드 상태 확인

/opt/rocm/bin/rocminfo # 그래픽 카드 정보 출력

dpkg -l | grep rocm # RoCM 버전 확인
```
docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged my_rocm_jupyter # 
### 도커 실행
```bash
docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged rocm/rocm-terminal # RoCM 버전

docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged rocm/pytorch:latest #파이토치+ RoCM 버전


docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged -p 8888:8888 rocm/pytorch:latest # 파이토치+ RoCM 쥬피터

docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged -p 8888:8888 rocm/rocm-terminal:5.7

docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged -p 8888:8888 rocm/pytorch:rocm5.7_ubuntu20.04_py3.9_pytorch_2.0.1


/opt/conda/envs/py_3.9/bin/python -m pip install --upgrade pip

pip3 install torch==2.0.1 torchvision torchaudio torchtext --extra-index-url=https://download.pytorch.org/whl/rocm5.7
pip3 install torch==2.0.1 torchvision torchaudio --extra-index-url=https://download.pytorch.org/whl/rocm5.7
pip3 install torch==2.0.1 torchtext==0.15.0 --extra-index-url=https://download.pytorch.org/whl/rocm5.7

pip3 install torch==2.0.1 torchtext==0.16.0 --extra-index-url=https://download.pytorch.org/whl/rocm5.7

pip3 install torch==2.0.1 torchtext==0.14.0 --extra-index-url=https://download.pytorch.org/whl/rocm5.7

pip3 install torch==1.13.0 torchtext==0.14.0 torchvision torchaudio --extra-index-url=https://download.pytorch.org/whl/rocm5.7

pip uninstall torch torchvision torchaudio torchtext


pip3 install notebook
pip3 install pandas==1.5.3
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

pip3 install torchdata==0.5.1


pip3 install --pre torch --index-url https://download.pytorch.org/whl/nightly/rocm6.2
pip3 install torch==2.0.1 torchtext==0.15.0 torchvision==0.15.2 torchaudio==2.0.2 --extra-index-url=https://download.pytorch.org/whl/rocm5.7



### RoCM설치
```bash
docker pull rocm/rocm-terminal # ROCm Docker 이미지 다운로드
docker pull rocm/rocm-terminal:4.5.0 # ROCm Docker 특정 버전 이미지 다운로드

docker run -it --device=/dev/kfd --device=/dev/dri --group-add video rocm/rocm-terminal # ROCm Docker 컨테이너 실행
docker run -it --device=/dev/kfd --device=/dev/dri --group-add video rocm/rocm-terminal:4.5.0 # ROCm Docker 특정 버전 컨테이너 실행


/opt/rocm/bin/rocminfo # ROCm 설치 확인
```

### 쥬피터 실행 오류시 경로 추가
```bash
echo 'export PATH=$PATH:/home/rocm-user/.local/bin' >> ~/.bashrc
source ~/.bashrc

echo $PATH # 경로 확인(선택)
```


| pandas 버전 | numpy 요구 사항                 |
|-------------|---------------------------------|
| 0.20.3     | >= 1.9                          |
| 0.21.0     | >= 1.9.3, < 2.0a0               |
| 0.21.1     | >= 1.9.3, < 2.0a0               |
| 0.22.0     | >= 1.13.3, < 2.0a0              |
| 0.23.0     | >= 1.9.3, < 2.0a0               |
| 0.23.1     | >= 1.9.3, < 2.0a0               |
| 0.23.2     | >= 1.11.3, < 2.0a0              |
| 0.23.3     | >= 1.11.3, < 2.0a0              |
| 0.23.4     | >= 1.11.3, < 2.0a0              |
| 0.24.0     | >= 1.12.1, < 2.0a0              |
| 0.24.1     | >= 1.12.1, < 2.0a0              |
| 0.24.2     | >= 1.12.1, < 2.0a0              |
| 0.25.0     | >= 1.13.3, < 2.0a0              |
| 0.25.1     | >= 1.13.3, < 2.0a0              |
| 0.25.2     | >= 1.13.3, < 2.0a0              |
| 0.25.3     | >= 1.13.3, < 2.0a0              |
| 1.0.0      | >= 1.14.6, < 2.0a0              |
| 1.0.1      | >= 1.14.6, < 2.0a0              |
| 1.0.2      | >= 1.14.6, < 2.0a0              |
| 1.0.3      | >= 1.14.6, < 2.0a0              |
| 1.0.4      | >= 1.14.6, < 2.0a0              |
| 1.0.5      | >= 1.14.6, < 2.0a0              |
| 1.1.0      | >= 1.15.4, < 2.0a0              |
| 1.1.1      | >= 1.15.4, < 2.0a0              |
| 1.1.2      | >= 1.15.4, < 2.0a0              |
| 1.1.3      | >= 1.15.4, < 2.0a0              |
| 1.1.5      | >= 1.15.4, < 2.0a0              |
| 1.2.0      | >= 1.16.6, < 2.0a0              |
| 1.2.1      | >= 1.16.6, < 2.0a0              |
| 1.2.2      | >= 1.16.6, < 2.0a0              |
| 1.2.3      | >= 1.16.6, < 2.0a0              |
| 1.2.4      | >= 1.19.2, < 2.0a0              |
| 1.2.5      | >= 1.20.2, < 2.0a0              |
| 1.3.0      | >= 1.20.3, < 2.0a0              |
| 1.3.1      | >= 1.19.2, < 2.0a0              |
| 1.3.2      | >= 1.19.2, < 2.0a0              |
| 1.3.3      | >= 1.19.2, < 2.0a0              |
| 1.3.4      | >= 1.19.2, < 2.0a0              |
| 1.3.5      | >= 1.19.2, < 2.0a0              |
| 1.4.1      | >= 1.21.2, < 2.0a0              |
| 1.4.2      | >= 1.21.5, < 2.0a0              |
| 1.4.3      | >= 1.21.5, < 2.0a0              |
| 1.4.4      | >= 1.21.5, < 2.0a0              |
| 1.5.1      | >= 1.21, < 2.0a0                |
| 1.5.2      | >= 1.21, < 2.0a0                |
| 1.5.3      | >= 1.21, < 2.0a0                |
| 2.0.3      | >= 1.21.5, < 2.0a0              |
| 2.1.1      | >= 1.21.5, < 2.0a0              |
| 2.1.4      | >= 1.21.5, < 2.0a0              |
| 2.2.1      | >= 1.22.3, < 2.0a0              |
| 2.2.2      | >= 1.22.3, < 2.0a0              |
