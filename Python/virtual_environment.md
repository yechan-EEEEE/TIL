# 가상환경
- 가상환경을 만들면 그 안에서만 
python -m(만들기) venv(가상환경) venv(이름)
디렉토리에 venv 만들어짐
source venv/Scripts/activate
터미널 별로 되서 터미널 새로 만들 때마다 해야된다?
## 의존성
- 의존성 패키지
프로젝트가 실행되기 위해 꼭 필요한 패키지들
pip list
pip install ()
pip freeze > requirements.txt 이름 길게 안해도 되지만 관례
pip onstall -r requirements.txt