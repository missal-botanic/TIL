


### 도커 명령어
```bash
docker ps #컨테이너 목록 출력

docker images # 이미지 확인

docker run hello-world

docker search nginx

docker pull nginx:latest

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


### 그룹 확인 01
```bash
sudo usermod -aG docker [user] # 그룹 추가
newgrp docker # 그룹 갱신
```

### 그룹 확인 02
```bash
sudo groups docker
sudo groups pro
cat /etc/group # 또는 grep '^docker:' /etc/group
```

### RoCM설치
```bash
docker pull rocm/rocm-terminal # ROCm Docker 이미지 다운로드
docker pull rocm/rocm-terminal:4.5.0 # ROCm Docker 특정 버전 이미지 다운로드

docker run -it --device=/dev/kfd --device=/dev/dri --group-add video rocm/rocm-terminal # ROCm Docker 컨테이너 실행
docker run -it --device=/dev/kfd --device=/dev/dri --group-add video rocm/rocm-terminal:4.5.0 # ROCm Docker 특정 버전 컨테이너 실행


/opt/rocm/bin/rocminfo # ROCm 설치 확인
```


rocm/pytorch 
rocm/dev-ubuntu-22.04 