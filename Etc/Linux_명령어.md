

./~.sh # sh 실행

### 그룹 FM docker
```bash
groups pro # 그룹 확인
sudo usermod -aG docker pro # 그룹 넣기
newgrp docker # 그룹 적용
docker ps

```

### 그룹 FM video
```bash
sudo usermod -aG docker video # 그룹 넣기
newgrp video # 그룹 적용
```

### 그룹 확인 01
```bash
groups # 현재 사용자 그룹 확인 
sudo usermod -aG docker [user] # 그룹 추가
newgrp docker # 그룹 갱신
```

### 그룹 확인 02
```bash

sudo groups docker
sudo groups pro
cat /etc/group # 또는 grep '^docker:' /etc/group

sudo groupadd docker # 그룹만들기
```

### 원격 확성화 (필요 유무 확인 필요)
```bash
sudo apt update
sudo apt install vino

sudo apt update && sudo apt install -y vino

ip addr # ip 확인

```

# 암호화 설정 해제를 위해 dconf-editor 설치
```bash
$ sudo apt install dconf-editor #editor 설치
$ dconf-editor #editor 실행

org - gnome - desktop - remote_access - require_encryption 해제
```

### 깃 세팅
```bash
sudo apt-get install git 

git config --global user.name chad

git config --global user.mail missal-botanic-0y@icloud.com

git clone [url주소]
```

### 다운로드 파일 설치
```bash
sudo apt install ./ [파일명]

echo $SHELL # 확인
zsh [파일명] #zsh 경우
bash [파일명] # bash 경우
```

### VS 코드 지우기
```bash
sudo apt remove code
```

### 한글 세팅
```
setting - language - language support - Install/Remove Languages - add korea # 기본 세팅 추가

$ ibus-setup - 탭 input Method - add - "Hangul(korea)" # ibus 세팅

setting - keyboaed - Input Sources "Korean(Hangul)"  # ibus 세팅

"..." - Preference # 단축어 설정
```


### 콘다설치
```bash
bash Anaconda3-2024.10-1-Linux-x86_64.sh

sudo apt update 
sudo apt install gedit # gedit 설치
gedit ~/.bashrc # 에디터로 열기
export PATH=~/anaconda3/bin:~/anaconda3/condabin:$PATH
source ~/.bashrc # 적용

$ conda config --set auto_activate_base false #base 기본값 해제
$ conda config --set auto_activate_base true #base 기본값 적용
```

### 콘다 제거
```bash
conda install anaconda-clean # 백업???
anaconda-clean #--yes 스킵옵션
rm -rf ~/anaconda3 # 폴더제거
```
### 도커 공식
```bash



백업 

1. 루트로 이동

cd /

2.전체 시스템을 백업

sudo tar zcvpf backup.tgz --exclude=/proc --exclude=/lost+found --exclude=/mnt --exclude=/sys --exclude=/dev --exclude=/media --exclude=/backup.tgz /


복구

1. 루트로 이동

#cd /

2. 압축을 풀어 복구

#tar zxvpf backup.tgz -C /

마지막의 -C / 옵션때문에 백업파일이 루트가 아닌 다른 곳에 저장되어있는 상태라도 상관없다.

 백업에서 제외했던 디렉토리는 직접 만들어 주어라
#mkdir proc
#mkdir lost+found
#mkdir mnt
#mkdir sys
재부팅을 하면 백업전과 똑같은 상태로 돌아 갈 것이다.


### 권한으로 삭제
```bash
sudo su # 권한 부여

rm backup.tgz # 삭제
```

### 기타
```bash
ls           # 현재 디렉토리의 파일과 폴더 목록을 표시
ls -al      # 현재 디렉토리의 모든 파일(숨김 파일 포함)과 상세 정보를 표시
cd ~/       # 사용자 홈 디렉토리로 이동
cd ..       # 상위 디렉토리로 이동
clear       # 터미널 화면을 지우기
pwd         # 현재 작업 중인 디렉토리의 경로를 출력
mkdir       # 새 디렉토리를 생성 (예: mkdir new_folder)
touch       # 새 파일을 생성하거나 기존 파일의 타임스탬프를 업데이트
rm          # 파일을 삭제 (예: rm filename.txt)
rm -r       # 디렉토리와 그 안의 모든 파일을 재귀적으로 삭제 (예: rm -r folder_name)
cp          # 파일이나 디렉토리를 복사 (예: cp source.txt destination.txt)
mv          # 파일이나 디렉토리를 이동하거나 이름 변경 (예: mv oldname.txt newname.txt)
cat         # 파일의 내용을 출력 (예: cat file.txt)
man         # 명령어의 매뉴얼을 표시 (예: man ls)
grep        # 텍스트 검색 (예: grep "검색어" file.txt)
find        # 파일이나 디렉토리를 검색 (예: find /path -name filename)
chmod       # 파일이나 디렉토리의 권한을 변경 (예: chmod 755 file.txt)
ps          # 현재 실행 중인 프로세스 목록을 표시
kill        # 프로세스를 종료 (예: kill PID)
top         # 시스템의 현재 프로세스와 리소스 사용 상태를 실시간으로 표시
```
