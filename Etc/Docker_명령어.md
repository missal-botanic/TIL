



import torch
print(torch.__version__)  # PyTorch 버전
print(torch.cuda.is_available())  # GPU 사용 가능 여부



### 도커 실행
```bash
docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged rocm/rocm-terminal # RoCM 버전

docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged rocm/pytorch:latest #파이토치+ RoCM 버전


docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged -p 8888:8888 rocm/pytorch:latest # 파이토치+ RoCM 쥬피터

docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged -p 8888:8888 rocm/rocm-terminal:5.7

docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged -p 8888:8888 pytorch/manylinux-rocm:5.7

docker pull pytorch/manylinux-rocm:5.7


pip3 install torch==2.2.2 torchvision torchaudio torchtext --extra-index-url=https://download.pytorch.org/whl/rocm5.7

pip3 install notebook
pip3 install pandas
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
pip3 install --pre torch --index-url https://download.pytorch.org/whl/nightly/rocm6.2

/opt/rocm/bin/rocm-smi # 그래픽 카드 상태 확인
/opt/rocm/bin/rocminfo # 그래픽 카드 정보 출력
dpkg -l | grep rocm # RoCM 버전 확인

python
import torch
print(torch.__version__) #파이썬에서 출력

exit() # Ctrl + D 파이썬에서 나오기

```

### 도커 커밋
```bash
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

docker commit [컨테이너_ID] my_rocm_jupyter # 상태 업데이트
docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged my_rocm_jupyter # 업데이트 내용 실행
```

### 도커 정식 생성
```Dockerfile
FROM rocm/pytorch:latest

RUN pip install jupyter

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```
### 도커 정식 생성 후 실행
```bash
docker build -t my_rocm_jupyter .

docker run -it --device=/dev/kfd --device=/dev/dri --group-add video --privileged -p 8888:8888 my_rocm_jupyter

```





### 도커 명령어
```bash
docker ps # 실행중인 컨테이너 목록 출력

docker images # 이미지 확인

docker run rocm/rocm-terminal

docker stop [컨테이너_ID 또는 이름]

docker search nginx

docker pull nginx:latest


docker stop [container_id_or_name] # 컨테이너 정지


docker rmi hello-world # 지우기

docker rmi -f hello-world # 강제 지우기
```

### 도커 실행 % 재실행
```bash
sudo systemctl start docker # 도커 실행

sudo systemctl stop docker # 도커 종료

sudo systemctl status docker # 도커 실행 확인

sudo service docker restart # 도커 재실행
```




### RoCM설치
```bash
docker pull rocm/rocm-terminal # ROCm Docker 이미지 다운로드
docker pull rocm/rocm-terminal:4.5.0 # ROCm Docker 특정 버전 이미지 다운로드

docker run -it --device=/dev/kfd --device=/dev/dri --group-add video rocm/rocm-terminal # ROCm Docker 컨테이너 실행
docker run -it --device=/dev/kfd --device=/dev/dri --group-add video rocm/rocm-terminal:4.5.0 # ROCm Docker 특정 버전 컨테이너 실행


/opt/rocm/bin/rocminfo # ROCm 설치 확인
```


### 컨테이너 종료
```bash
exit # 입력

Ctrl+D # 단축키
```

### 컨테이너 미종료 나가기
```bash
Ctrl + P + Q #컨트롤을 누른 상태에서 P와 Q를 동시에 누르면, 컨테이너 종료 없이 밖으로 나갈 수 있습
```

### 쥬피터 실행 오류시 경로 추가
```bash
echo 'export PATH=$PATH:/home/rocm-user/.local/bin' >> ~/.bashrc
source ~/.bashrc

echo $PATH # 경로 확인(선택)
```


rocm/pytorch 
rocm/dev-ubuntu-22.04 