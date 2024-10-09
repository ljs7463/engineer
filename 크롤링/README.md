## Git
#### 1. 로컬브랜치 변경사항 있는 특정파일을 원격브랜치로 push 
```python
git add {특정파일}.py
git commit -m "{커밋메세지}"
git push origin {원격브랜치경로} -- Push한 원격브랜치를 추적하지않을경우
-- git push -u origin {현재브랜치}:{원격브랜치경로} -- push한 브랜치를 추적하여 git pull 사용시 자동으로 동기화 할수있게 하고싶은 경우
```



