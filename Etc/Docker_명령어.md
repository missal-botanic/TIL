### hub.docker 도커 이미지 검색 + tag 버전별 컨테이너 선택 다운로드 가능 
https://hub.docker.com/r/rocm/pytorch/tags?page=3


### 도커 권한 저하
```bash
sudo chmod 666 /var/run/docker.sock # 666은 모든 사용자(소유자, 그룹, 기타 사용자)가 해당 파일에 대해 읽기 및 쓰기 권한을 가지도록 설정합니다.
sudo chown root:docker /var/run/docker.sock # 파일의 소유자를 "root"로, 그룹을 "docker"로 변경합니다. 
```
## 권한 제어 02
```bash
sudo /usr/sbin/groupadd -f docker #"docker"라는 이름의 그룹을 생성합니다.
sudo /usr/sbin/usermod -aG docker `user` # 명령어는 사용자 계정의 속성을 수정합니다.
sudo chown root:docker /var/run/docker.sock # 명령어는 파일 또는 디렉토리의 소유자와 그룹을 변경합니다.
```

### 도커 만들기 예시
```bash
# 예시 01
FROM ubuntu:20.04
RUN apt update -y && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt install python3.9 -y

import torch
print(torch.__version__)  # PyTorch 버전
print(torch.cuda.is_available())  # GPU 사용 가능 여부

# 예시 02
FROM rocm/pytorch:latest
RUN pip install jupyter
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

### 도커 명령어
```bash
docker ps # 실행중인 컨테이너 목록 출력

docker images # 이미지 확인

docker run 9f799780ef82 # docker run rocm/rocm-terminal / docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

exit # 입력
Ctrl + D # 단축키
Ctrl + P + Q # 컨트롤을 누른 상태에서 P와 Q를 동시에 누르면, 컨테이너 종료 없이 밖으로 나갈 수 있습

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

### 용량 확인
```bash
docker system df # 컨테이너별 용량 확인

docker ps --size --format "table {{.ID}}\t{{.Image}}\t{{.Size}}" # 도커 용량 확인 자세히
```

### Docker 컨테이너, 이미지, 캐시
```bash
docker container prune # 도커 미사용 컨테이너 삭제
    
docker image prune # 도커 미사용 이미지 삭제
    
docker volume prune # 도커 미사용 볼륨 삭제
    
docker system prune -a # 도커 미사용 오브젝트 전체 삭제 (로그는 삭제 안됨)
```

### Docker 로그
```bash
sudo du -h $(docker inspect --format='{{.LogPath}}' $(docker ps -qa)) # 도커 로그 용량 확인
    
sudo sh -c "truncate -s 0 /var/lib/docker/containers/*/*-json.log" # 도커 로그 전체 삭제
```

### 파일이동 (수정 필요)
```bash
docker cp netflix_reviews.csv alpine-container:/home/pro/VS/Deep/netflix_reviews.csv # 호스트에서 컨테이너
docker cp 90070550eaca:/home/pro/VS/Deep/netflix_reviews.csv # 커테이너에서 호스트 
```

### 컨테이너 커밋 + 이미지화
```bash
docker commit 5dda4ad5f044  rocm/pytorch:ROCm5.7_torch1.13.1 # 01. 커밋
 
docker export 5dda4ad5f044 > backup.tar # 02. 저장

docker export <컨테이너_ID> > /path/to/your/directory/backup.tar # 위치추가

```