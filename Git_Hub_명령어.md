Git_Hub_명령어
=============

### 사용자 정보 선언(name은 아무 내용 가능)
```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```
### 사용자 정보 설정 확인
```
$ git config --list
```
```
> 제어판
>	> 자격 증명 관리자 
>	> 	>  windows 자격 증명 
>	> 	> 	> 일반 자격 증명
```

### 최초 환경 구성
```
git init
git remote add origin https://github.com/missal-botanic/remote_class.git
git branch -M main
git add . [git add 001.py]
# git status [git log #커밋 후 로그확인]
git commit -m "$(date +'%Y-%m-%d %H:%M:%S')"
git push origin main
```

### 삭제 및 되돌리기
```
git rm --cached [파일명] #후보저장소에서 삭제

git reset --hard HAED^ # Woking Directory + Staging Area + Repository 삭제
git reset --mixed HEAD^ # Staging Area + Repository 삭제
git reset --soft HEAD^ # Repository 삭제

^한 단계, ^^ 두 단계 ^^^ 세 단계
```

### branch
```
git branch [이름]    #생성
git branch           #확인
git checkout [이름]  #변경
git branch -D [이름] #삭제
```

### fetch 
```
git fetch orgin main
git checkout FETCH_HEAD #임시 branh (파일 확인 후)
git checkout main
git merge main
```

### merge 중단
```
git merge --abort # 머지 중단
```

### pull
```
git pull origin main --rebase
git pull origin main --allow-unrelated-histories
```

git clone
git stash

esc + :wq