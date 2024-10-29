### RoCM설치
```bash
docker pull rocm/rocm-terminal # ROCm Docker 이미지 다운로드
docker pull rocm/rocm-terminal:4.5.0 # ROCm Docker 특정 버전 이미지 다운로드
```

### 도커 실행
```bash
docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged -p 8888:8888 rocm/pytorch:rocm5.7_ubuntu20.04_py3.9_pytorch_2.0.1

# pip 업그레이드
/opt/conda/envs/py_3.9/bin/python -m pip install --upgrade pip

# 파이토지
pip3 install torch==2.0.1 torchvision torchaudio torchtext --extra-index-url=https://download.pytorch.org/whl/rocm5.7

pip3 install torch==2.0.1 torchvision torchaudio --extra-index-url=https://download.pytorch.org/whl/rocm5.7

pip3 install torch==2.0.1 torchtext==0.15.0 torchvision==0.15.2 torchaudio==2.0.2 --extra-index-url=https://download.pytorch.org/whl/rocm5.7

pip3 install torch==1.13.0 torchtext==0.14.0 torchvision torchaudio --extra-index-url=https://download.pytorch.org/whl/rocm5.7

pip uninstall torch torchvision torchaudio torchtext

# 기본 설치
pip3 install notebook
pip3 install pandas==1.5.3

# 실행
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

### 버전 조율
```bash
pip install --upgrade scipy

pip3 install pandas==1.5.3

pip install numpy==1.22.0

sudo apt update
```

### 버전 확인
```bash
python3 -c "import torchtext; print(torchtext.__version__)"

python3 -c "import torch; print(torch.__version__)"

python --version

/opt/rocm/bin/rocm-smi # 그래픽 카드 상태 확인

/opt/rocm/bin/rocminfo # 그래픽 카드 정보 출력

dpkg -l | grep rocm # RoCM 버전 확인
```
### 쥬피터 실행 오류시 경로 추가
```bash
echo 'export PATH=$PATH:/home/rocm-user/.local/bin' >> ~/.bashrc
source ~/.bashrc

echo $PATH # 경로 확인(선택)
```

pip install --upgrade scipy # 선택 01 삭제예정

# 도커 설치 01
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```
```bash
# 도커 설치 02
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```
```bash
# 도커 설치 03
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```bash

# 도커 설치 04
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo docker run hello-world

```

### 도커 설치 02 (wget은 파일을 저장하지 않고 즉시 실행)
```bash
sudo wget -qO- http://get.docker.com/ | sh
docker version
```
### 도커 설치 03 (curl은 파일을 저장한 후에 수동으로 실행)
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### pytorch 버전 (Linux only)
```bash

pip3 install torchdata==0.5.1

pip3 install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/rocm5.7
pip3 install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 torchtext==0.17.0 --index-url https://download.pytorch.org/whl/rocm5.7
pip3 install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 torchtext==0.17.0 --extra-index-url=https://download.pytorch.org/whl/rocm5.7
pip3 install torch==2.0.1 torchtext==0.15.0 --extra-index-url=https://download.pytorch.org/whl/rocm5.7
pip3 install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/rocm6.1
pip3 install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/rocm6.0
pip3 install --pre torch --index-url https://download.pytorch.org/whl/nightly/rocm6.2 # --pre 베타(beta), 알파(alpha), 개발(development) 버전과 같은 사전 릴리스 버전도 포함

```


