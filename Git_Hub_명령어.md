
```
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

```
git init
git remote add origin https://github.com/missal-botanic/remote_class.git
git branch -M main
git add . [git add 001.py]
# git status
git commit -m "$(date +'%Y-%m-%d %H:%M:%S')"
git push origin main
```

```
git pull origin main --rebase
git pull origin main --allow-unrelated-histories
```
```
git fetch orgin main
git checkout FETCH_HEAD #임시 branh (파일 확인 후)
git checkout main
git merge main
```


```
git merge --abort #머지 중단
```

git pull #git pull origin master
git fetch
git clone
git 

git stash

:wq