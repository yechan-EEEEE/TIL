# 요약
markdown: 이쁘게 만들기

# git
1. **Working directory**: (ls는 리스트 폴더 안에 있는 친구들) init 하고 status 하면 나오는 빨간 친구들 있는 곳
2. **Staging Area**: add 했을 때 나오는 초록친구들 있는 곳
3. **Repository**: commit 하면 들어가는 곳들
---
    1. ls: 현재 위치  
    2. pwd(print working directory): 절대위치  
    3. touch: 파일 만들기  
    4. mkdir: 폴더 만들기  
    5. cd: 위치 옮기기  
    6. ., ..: 현재 위치, 상위 폴더
---

1. init: 관리 시작 (git init)  
2. add: 저장 안된 친구들 Staging Area에 집어넣기 (git add 파일명)  
3. commit: Staging Area에 있는 친구들 저장 (git commit -m "원하는 저장소 이름")
4. status: 위 행동들 현재 상태 확인
5. git log: commit 내역 확인(git log --oneline: 로그 한줄로 예쁘게)
6. commit --amend: 직전 commit 수정 (:wq로 나오기)
7. git revert (commit id): commit 있던 애 없던 일로 치기, 변경된 기록도 남아있음  
8. git reset **[옵션]** (commit id): --soft=지우고 Staging Area에 남기기, --mixed=지우고 Working directory에 남기기, --hard=아예 삭제
9. git rm --cached:초록에 있는 거 빨강으로(commit이 없을 때)  
10. git restore --staged:초록에 있는 거 빨강으로(commit이 있을 때)
---
# github
1. git remote add origin url: remote add=저장소에 올리기, origin=별칭 보통은 origin, 저장소 주소
2. git remote -v: 등록 됐나 위치 확인
3. git remote rm (이름, TIL or 주소)
4. git push origin master: 저장소에다 올리기  
5. git pull origin master: 저장소에서 가져오기  
6. git clone remote_repo-url: 저장소에 있는 거 아예 복제(보통 처음에 시작할 때 함)  
7. .gitignore: 숨김파일(허브에 올리기 싫은 친구들)

