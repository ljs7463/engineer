## Git
#### 1. 로컬브랜치 변경사항 있는 특정파일을 원격브랜치로 push 
```git
git add {특정파일}.py
git commit -m "{커밋메세지}"
git push origin {원격브랜치경로} -- Push한 원격브랜치를 추적하지않을경우
-- git push -u origin {현재브랜치}:{원격브랜치경로} -- push한 브랜치를 추적하여 git pull 사용시 자동으로 동기화 할수있게 하고싶은 경우
```


## Chrome
#### 1. 크롬드라이브 다운로드
https://developer.chrome.com/docs/chromedriver/downloads?hl=ko
#### 2. 다운로드한 크롬드라이브 homebrew내 경로로 이동
```linux
# 다운로드 경로에서 chromediver 파일찾기
ls ~/Downloads/

# 이동시키기
mv ~/Downloads/{정확한_폴더_이름}/chromedriver /opt/homebrew/bin/

# 권한 설정
chmod +x /opt/homebrew/bin/chromedriver

# 크롬 버전확인
chromedriver --version
```
