cobb/th


wsl --install

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

wsl --update





 lsb_release -a



 # docker engine gpg 키 등록
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# apt source 에 docker 관련 추가
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# docker engine 설치
sudo apt-get install -y docker-ce docker-ce-cli containerd.io \
docker-buildx-plugin docker-compose-plugin docker-compose

# docker 그룹에 현재 계정을 등록하여 sudo 없이 docker 명령을 사용하게 함
sudo usermod -aG docker user
sudo service docker restart

# 새로운 터미널을 열고 확인
docker version



docker info



# nginx 이미지 다운받기
docker image pull nginx:1.25.3-alpine

docker images

docker image history nginx:1.25.3-alpine

docker run -d -p 8001:80 --name webserver01 nginx:1.25.3-alpine

docker ps | grep webserver01

docker port webserver01

curl localhost:8001





# docker [image] pull [options] name:[tag]

# 최초에는 docker.io가 default registry로 설정됨.
docker pull debian[:latest]
docker pull library/debian:10
docker pull docker.io/library/debian:10
docker pull index/docker.io/library/debian:10
docker pull nginx:latest

# private registry 나 클라우드 저장소의 이미지를 받는 경우
docker pull 192.168.0.101:5000/debian:10 # 현재는 실제로 동작하지 않음
docker pull gcr.io/google-samples/hello-app:1.0





docker image inspect nginx:latest





docker pull ubuntu:22.04
docker images

# docker create 은 실제 실행하지 않고 컨테이너 생성만
docker create –ti --name ubuntu2204test ubuntu:22.04
docker ps –a
CONTAINER ID   IMAGE          COMMAND       CREATED         STATUS    PORTS     NAMES
2ccc1b2a1144   ubuntu:22.04   "/bin/bash"   4 seconds ago   Created             ubuntu2204test

docker start ubuntu2204test
Ubuntu2204test
docker attach ubuntu2204test

# docker run 은 create/start/attach 를 순차적으로 한 번에 실행하는 것과 같음 
docker run -ti --name=ubuntu2204test2 ubuntu:22.04 /bin/bash

도커를 만드는 것과
실행은 다름




docker run -ti --name=ubuntu2204test3 ubuntu:22.04 /bin/bash
root@1cd125b32870:/#

# 터미널을 한 개 더 열고 
ps -ef | grep ubuntu2204test3
user   9710  7637  0 17:17 pts/4    00:00:00 docker run -ti --name=ubuntu2204test3 ubuntu:22.04 /bin/bash
user   9921  9377  0 17:17 pts/5    00:00:00 grep --color=auto ubuntu2204test3


vi ---
esc키
: wq


cd ~
mkdir nodejsapp
cd nodejsapp
vi app.js # 테스트용 nodejs 앱
vi Dockerfile # 새로운 도커 이미지를 위한 Dockerfile
docker buildx build -t node-test:1.0 . # 1.0 태그를 추가하여 node-test라는 이미지를 빌드 뒤에 점까지 필수
docker images | grep node-test  # 빌드 완료한 이미지 보기
docker image history node-test:1.0 # 1.0으로 태그 추가한 이미지의 Dockerfile history
docker run -itd -p 6060:6060 --name=node-test -h node-test node-test:1.0
docker ps | grep node-test
curl http://localhost:6060



# 컨테이너에서 실행 중인 프로세스 조회
docker top node-test 
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                2398                2378                0                   08:37               ?                   00:00:00            /sbin/tini -- node runapp.js
root                2421                2398                0                   08:37               ?                   00:00:00            node runapp.js

# 컨테이너에 매핑된 포트 조회
docker port node-test
8080/tcp -> 0.0.0.0:8080

# 컨테이너 리소스 통계 출력 (1회)
docker stats node-test --no-stream
CONTAINER ID   NAME        CPU %     MEM USAGE / LIMIT     MEM %     NET I/O        BLOCK I/O   PIDS
14c475f7ac09   node-test   0.01%     9.035MiB / 15.45GiB   0.06%     1.5kB / 518B   0B / 0B     11

# 컨테이너 리소스 통계 출력 (스트림)
docker stats node-test



# 표준 출력(stdout), 표준에러(stderr) 출력
docker logs node-test 
…
 

# 로그를 계속 출력
docker logs –f node-test
…
…

# 출력된 로그는 파일로 관리되기 때문에 HostOS 의 disk 를 사용
docker info | grep -i log




# 컨테이너 내부 확인
docker inspect node-test





# 터미널1, 도커 상태 확인
docker stats

# 터미널2, 도커 프로세스 이벤트 확인
docker events

# 터미널3, docker start
docker stop node-test
docker ps –a
docker start node-test

# 
docker pause node-test
docker unpause node-test
docker ps -a



# 중지된 컨테이너를 포함하여 모든 컨테이너 리스트
docker container ls -a

# 
docker container prune

# 
docker image prune

# 남아 있는 이미지 리스트 확인 – 실행 중인 컨테이너의 이미지 등
docker image ls


docker system prune


Github Actions CI
테스트 통과 코드만 main에 등록가능하게

Github Actions CD
빠르게 배포할 수 있게 해줌

