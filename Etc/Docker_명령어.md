
1.13 -0.14
2.0 - 0.15
2.1 -0.16

docker cp netflix_reviews.csv alpine-container:/home/pro/VS/Deep/netflix_reviews.csv
docker cp 90070550eaca:/home/pro/VS/Deep/netflix_reviews.csv

co
5dda4ad5f044 

docker commit 5dda4ad5f044  rocm/pytorch:ROCm5.7_torch1.13.1

docker export 5dda4ad5f044 > backup.tar

docker export <컨테이너_ID> > /path/to/your/directory/backup.tar

FROM ubuntu:20.04
RUN apt update -y && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt install python3.9 -y

import torch
print(torch.__version__)  # PyTorch 버전
print(torch.cuda.is_available())  # GPU 사용 가능 여부


pip install --upgrade scipy

pip install numpy==1.22.0

sudo apt update


### hub.docker 도커 이미지 검색 + tag 버전별 컨테이너 선택 다운로드 가능 
https://hub.docker.com/r/rocm/pytorch/tags?page=3

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
pip install --upgrade scipy # 선택 01 삭제예정

pip install numpy==1.22.0 # 선택 02 삭제예정
pip install numpy==1.22.4 # 선택 02 삭제예정

rocm/pytorch 
rocm/dev-ubuntu-22.04 

용량 확인

    전체 도커 용량 확인 (요약본)
    docker system df
    컨테이너별 용량 확인
    docker ps --size --format "table {{.ID}}\t{{.Image}}\t{{.Size}}"
    도커 용량 확인 자세히
    docker system df --verbose
    도커 볼륨 실제 사용 용량 확인
    docker system df 명령어는 virtual 용량만 알려준다. 다음 명령어로 실제 사용량을 알 수 있다.
    docker volume ls -q | xargs -I {} sh -c 'echo "{}\t$(sudo du -sh $(docker volume inspect --format "{{ .Mountpoint }}" {}) | cut -f1)"' | column -t

Docker 컨테이너, 이미지, 캐시

    도커 미사용 컨테이너 삭제
    docker container prune
    도커 미사용 이미지 삭제
    docker image prune
    도커 미사용 볼륨 삭제
    docker volume prune
    도커 미사용 오브젝트 전체 삭제 (로그는 삭제 안됨)
    docker system prune -a

Docker 로그

    도커 로그 용량 확인
    sudo du -h $(docker inspect --format='{{.LogPath}}' $(docker ps -qa))
    도커 로그 전체 삭제
    sudo sh -c "truncate -s 0 /var/lib/docker/containers/*/*-json.log"
    compose 파일을 이용한 도커 로그 용량 제한 방법




version     : 0.20.3
  - numpy >=1.9
version     : 0.20.3
  - numpy >=1.9
version     : 0.20.3
  - numpy >=1.9
version     : 0.20.3
  - numpy >=1.9
version     : 0.20.3
  - numpy >=1.9
version     : 0.20.3
  - numpy >=1.9
version     : 0.21.0
  - numpy >=1.9.3,<2.0a0
version     : 0.21.0
  - numpy >=1.9.3,<2.0a0
version     : 0.21.0
  - numpy >=1.9.3,<2.0a0
version     : 0.21.1
  - numpy >=1.9.3,<2.0a0
version     : 0.21.1
  - numpy >=1.9.3,<2.0a0
version     : 0.21.1
  - numpy >=1.9.3,<2.0a0
version     : 0.22.0
  - numpy >=1.13.3,<2.0a0
version     : 0.22.0
  - numpy >=1.13.3,<2.0a0
version     : 0.22.0
  - numpy >=1.9.3,<2.0a0
version     : 0.23.0
  - numpy >=1.9.3,<2.0a0
version     : 0.23.0
  - numpy >=1.9.3,<2.0a0
version     : 0.23.0
  - numpy >=1.9.3,<2.0a0
version     : 0.23.1
  - numpy >=1.9.3,<2.0a0
version     : 0.23.1
  - numpy >=1.9.3,<2.0a0
version     : 0.23.1
  - numpy >=1.9.3,<2.0a0
version     : 0.23.2
  - numpy >=1.11.3,<2.0a0
version     : 0.23.2
  - numpy >=1.11.3,<2.0a0
version     : 0.23.2
  - numpy >=1.11.3,<2.0a0
version     : 0.23.3
  - numpy >=1.11.3,<2.0a0
version     : 0.23.3
  - numpy >=1.11.3,<2.0a0
version     : 0.23.3
  - numpy >=1.11.3,<2.0a0
version     : 0.23.3
  - numpy >=1.11.3,<2.0a0
version     : 0.23.4
  - numpy >=1.11.3,<2.0a0
version     : 0.23.4
  - numpy >=1.11.3,<2.0a0
version     : 0.23.4
  - numpy >=1.11.3,<2.0a0
version     : 0.23.4
  - numpy >=1.11.3,<2.0a0
version     : 0.24.0
  - numpy >=1.12.1,<2.0a0
version     : 0.24.0
  - numpy >=1.12.1,<2.0a0
version     : 0.24.0
  - numpy >=1.14.6,<2.0a0
version     : 0.24.1
  - numpy >=1.12.1,<2.0a0
version     : 0.24.1
  - numpy >=1.12.1,<2.0a0
version     : 0.24.1
  - numpy >=1.14.6,<2.0a0
version     : 0.24.2
  - numpy >=1.12.1,<2.0a0
version     : 0.24.2
  - numpy >=1.12.1,<2.0a0
version     : 0.24.2
  - numpy >=1.14.6,<2.0a0
version     : 0.25.0
  - numpy >=1.13.3,<2.0a0
version     : 0.25.0
  - numpy >=1.14.6,<2.0a0
version     : 0.25.1
  - numpy >=1.13.3,<2.0a0
version     : 0.25.1
  - numpy >=1.14.6,<2.0a0
version     : 0.25.2
  - numpy >=1.13.3,<2.0a0
version     : 0.25.2
  - numpy >=1.14.6,<2.0a0
version     : 0.25.3
  - numpy >=1.13.3,<2.0a0
version     : 0.25.3
  - numpy >=1.14.6,<2.0a0
version     : 0.25.3
  - numpy >=1.13.3,<2.0a0
version     : 1.0.0
  - numpy >=1.14.6,<2.0a0
version     : 1.0.0
  - numpy >=1.14.6,<2.0a0
version     : 1.0.0
  - numpy >=1.14.6,<2.0a0
version     : 1.0.1
  - numpy >=1.14.6,<2.0a0
version     : 1.0.1
  - numpy >=1.14.6,<2.0a0
version     : 1.0.1
  - numpy >=1.14.6,<2.0a0
version     : 1.0.2
  - numpy >=1.14.6,<2.0a0
version     : 1.0.2
  - numpy >=1.14.6,<2.0a0
version     : 1.0.2
  - numpy >=1.14.6,<2.0a0
version     : 1.0.3
  - numpy >=1.14.6,<2.0a0
version     : 1.0.3
  - numpy >=1.14.6,<2.0a0
version     : 1.0.3
  - numpy >=1.14.6,<2.0a0
version     : 1.0.4
  - numpy >=1.14.6,<2.0a0
version     : 1.0.4
  - numpy >=1.14.6,<2.0a0
version     : 1.0.4
  - numpy >=1.14.6,<2.0a0
version     : 1.0.5
  - numpy >=1.14.6,<2.0a0
version     : 1.0.5
  - numpy >=1.14.6,<2.0a0
version     : 1.0.5
  - numpy >=1.14.6,<2.0a0
version     : 1.1.0
  - numpy >=1.15.4,<2.0a0
version     : 1.1.0
  - numpy >=1.15.4,<2.0a0
version     : 1.1.0
  - numpy >=1.16.6,<2.0a0
version     : 1.1.1
  - numpy >=1.15.4,<2.0a0
version     : 1.1.1
  - numpy >=1.15.4,<2.0a0
version     : 1.1.1
  - numpy >=1.16.6,<2.0a0
version     : 1.1.2
  - numpy >=1.15.4,<2.0a0
version     : 1.1.2
  - numpy >=1.15.4,<2.0a0
version     : 1.1.2
  - numpy >=1.16.6,<2.0a0
version     : 1.1.3
  - numpy >=1.15.4,<2.0a0
version     : 1.1.3
  - numpy >=1.15.4,<2.0a0
version     : 1.1.3
  - numpy >=1.16.6,<2.0a0
version     : 1.1.3
  - numpy >=1.16.6,<2.0a0
version     : 1.1.5
  - numpy >=1.15.4,<2.0a0
version     : 1.1.5
  - numpy >=1.16.6,<2.0a0
version     : 1.1.5
  - numpy >=1.15.4,<2.0a0
version     : 1.1.5
  - numpy >=1.16.6,<2.0a0
version     : 1.1.5
  - numpy >=1.16.6,<2.0a0
version     : 1.1.5
  - numpy >=1.16.6,<2.0a0
version     : 1.1.5
  - numpy >=1.16.6,<2.0a0
version     : 1.2.0
  - numpy >=1.16.6,<2.0a0
version     : 1.2.0
  - numpy >=1.16.6,<2.0a0
version     : 1.2.0
  - numpy >=1.16.6,<2.0a0
version     : 1.2.1
  - numpy >=1.16.6,<2.0a0
version     : 1.2.1
  - numpy >=1.16.6,<2.0a0
version     : 1.2.1
  - numpy >=1.16.6,<2.0a0
version     : 1.2.2
  - numpy >=1.16.6,<2.0a0
version     : 1.2.2
  - numpy >=1.16.6,<2.0a0
version     : 1.2.2
  - numpy >=1.16.6,<2.0a0
version     : 1.2.3
  - numpy >=1.16.6,<2.0a0
version     : 1.2.3
  - numpy >=1.16.6,<2.0a0
version     : 1.2.3
  - numpy >=1.16.6,<2.0a0
version     : 1.2.4
  - numpy >=1.19.2,<2.0a0
version     : 1.2.4
  - numpy >=1.16.6,<2.0a0
version     : 1.2.4
  - numpy >=1.19.2,<2.0a0
version     : 1.2.4
  - numpy >=1.16.6,<2.0a0
version     : 1.2.4
  - numpy >=1.19.2,<2.0a0
version     : 1.2.4
  - numpy >=1.16.6,<2.0a0
version     : 1.2.5
  - numpy >=1.20.2,<2.0a0
version     : 1.2.5
  - numpy >=1.20.2,<2.0a0
version     : 1.2.5
  - numpy >=1.20.2,<2.0a0
version     : 1.3.0
  - numpy >=1.20.3,<2.0a0
version     : 1.3.0
  - numpy >=1.20.3,<2.0a0
version     : 1.3.0
  - numpy >=1.20.3,<2.0a0
version     : 1.3.1
  - numpy >=1.19.2,<2.0a0
version     : 1.3.1
  - numpy >=1.19.2,<2.0a0
version     : 1.3.1
  - numpy >=1.19.2,<2.0a0
version     : 1.3.2
  - numpy >=1.19.2,<2.0a0
version     : 1.3.2
  - numpy >=1.19.2,<2.0a0
version     : 1.3.2
  - numpy >=1.19.2,<2.0a0
version     : 1.3.3
  - numpy >=1.19.2,<2.0a0
version     : 1.3.3
  - numpy >=1.19.2,<2.0a0
version     : 1.3.3
  - numpy >=1.19.2,<2.0a0
version     : 1.3.4
  - numpy >=1.19.2,<2.0a0
version     : 1.3.4
  - numpy >=1.19.2,<2.0a0
version     : 1.3.4
  - numpy >=1.19.2,<2.0a0
version     : 1.3.5
  - numpy >=1.19.2,<2.0a0
version     : 1.3.5
  - numpy >=1.19.2,<2.0a0
version     : 1.3.5
  - numpy >=1.19.2,<2.0a0
version     : 1.4.1
  - numpy >=1.21.2,<2.0a0
version     : 1.4.1
  - numpy >=1.21.2,<2.0a0
version     : 1.4.1
  - numpy >=1.19.2,<2.0a0
version     : 1.4.1
  - numpy >=1.19.2,<2.0a0
version     : 1.4.1
  - numpy >=1.19.2,<2.0a0
version     : 1.4.1
  - numpy >=1.19.2,<2.0a0
version     : 1.4.2
  - numpy >=1.21.5,<2.0a0
version     : 1.4.2
  - numpy >=1.19.2,<2.0a0
version     : 1.4.2
  - numpy >=1.19.2,<2.0a0
version     : 1.4.3
  - numpy >=1.21.5,<2.0a0
version     : 1.4.3
  - numpy >=1.19.2,<2.0a0
version     : 1.4.3
  - numpy >=1.19.2,<2.0a0
version     : 1.4.4
  - numpy >=1.21.5,<2.0a0
version     : 1.4.4
  - numpy >=1.19.2,<2.0a0
version     : 1.4.4
  - numpy >=1.19.2,<2.0a0
version     : 1.5.1
  - numpy >=1.21,<2.0a0
version     : 1.5.1
  - numpy >=1.16,<2.0a0
version     : 1.5.1
  - numpy >=1.16,<2.0a0
version     : 1.5.2
  - numpy >=1.21,<2.0a0
version     : 1.5.2
  - numpy >=1.23,<2.0a0
version     : 1.5.2
  - numpy >=1.16,<2.0a0
version     : 1.5.2
  - numpy >=1.16,<2.0a0
version     : 1.5.3
  - numpy >=1.21,<2.0a0
version     : 1.5.3
  - numpy >=1.23,<2.0a0
version     : 1.5.3
  - numpy >=1.20.3,<2.0a0
version     : 1.5.3
  - numpy >=1.20.3,<2.0a0
version     : 2.0.3
  - numpy >=1.21.5,<2.0a0
version     : 2.0.3
  - numpy >=1.23.5,<2.0a0
version     : 2.0.3
  - numpy >=1.21.5,<2.0a0
version     : 2.0.3
  - numpy >=1.21.5,<2.0a0
version     : 2.1.1
  - numpy >=1.21.5,<2.0a0
version     : 2.1.1
  - numpy >=1.23.5,<2.0a0
version     : 2.1.1
  - numpy >=1.26.0,<2.0a0
version     : 2.1.1
  - numpy >=1.21.5,<2.0a0
version     : 2.1.4
  - numpy >=1.21.5,<2.0a0
version     : 2.1.4
  - numpy >=1.23.5,<2.0a0
version     : 2.1.4
  - numpy >=1.26.2,<2.0a0
version     : 2.1.4
  - numpy >=1.21.5,<2.0a0
version     : 2.2.1
  - numpy >=1.22.3,<2.0a0
version     : 2.2.1
  - numpy >=1.23.5,<2.0a0
version     : 2.2.1
  - numpy >=1.26.4,<2.0a0
version     : 2.2.1
  - numpy >=1.22.3,<2.0a0
version     : 2.2.2
  - numpy >=1.22.3,<2.0a0
version     : 2.2.2
  - numpy >=1.23.5,<2.0a0
version     : 2.2.2
  - numpy >=1.26.4,<2.0a0
version     : 2.2.2
  - numpy >=1.22.3,<2.0a0
