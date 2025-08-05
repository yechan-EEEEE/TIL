# 데이터 구조(자료 구조)
    - str,list,dict 등 여러 데이터를 효과적으로 사용, 관리하기 위한 구조  메서드로 다양한 기능 활용
# 메서드(method)
    - 어딘가에 속해 있는 함수
    - 데이터 타입별로 다양한 기능의 메서드 존재
    - 호출 방법: 데이터 타입 객체.메서드()
## 메서드 체이닝
    - 여러 메서드 한줄로 연속 호출하기
    - ex) text = 'heLLo, woRld'  
    new text = text.swapcase().replace('l','z')  
    print(new_text) # HEzzo, WOrLd'
### 메서드 체이닝 주의사항
    - 모든 메서드가 체이닝 지원하지 않음
        - 메서드가 객체를 반활할 때만 가능
    - None을 반환하는 메서드는 불가능
        ex) 리스트의 append().sort()
    - 메서드의 반환 값을 잘 알고 해야함
# 문자열
## 문자열 조회/탐색/검증 메서드
    - s.find(x): x의 첫번째 위치 반환, 없으면 -1 
    - s.index(x): x의 첫번째 위치 반환, 없으면 오류 (중요한 변수가 잘못 됐으면 터져버리게 해서 찾기)
    - s.isupper(x)/s,islower(x): 전부 다 대문자니 소문자니
    - s.isalpha(x): 다 알파벳이니
## 문자열 조작 메서드(str(불변)이라서 변수= 붙여줘야함)
    - s.replace(old,new[,count]):old를 new로 바꾸기 count 횟수 만큼 str이라 못 바꿔서 새로운 변수에 할당해줘야함
    - s.strip([chars]): 문자열 시작과 끝에 공백 제거 or 지정한 문자 제거
    - s.split(sep=None, maxsplit=-1): sep를 구분자 문자열로 사용해 문자열에 있는 단어들을 리스트로
    - separator.join(iterable): separator(구분자)를 iterable(변수의 값들)사이에다가 넣어서 리스트에다 넣어줌
    - s.capitalize(): 첫 글자를 대문자로 나머지 소문자
    - s.title(): 띄어쓰기 기준으로 각 단어 첫글자 대문자, 나머지는 소문자
    - s.upper(): 모두 대문자로
    - s.lower(): 모두 소문자로
    - s.swapcase(): 대 소문자 서로 변경
### find,index,replace,strip,split,join 중요
# 리스트
## 리스트 값 추가/삭제 메서드
    - L.append(x):리스트 마지막에 x 추가 x통째로 넣어버림 [1,2,3,[4,5,6]]
    - L.extend(x):리스트 마지막에 x 추가 x 안에 값들 분해해서 넣어줌 [1,2,3,4,5,6]/반복 가능한 m 넣어야 가능 값 한개면 안됌/ +=
    - L.insert(i,x): 리스트 i자리에다가 x 끼워넣기 (주소 자리 밀어야 되서 자주 x)
    - L.remove(x): 첫번째로 나온 x 지우기 (주소 자리 밀어야 되서 자주 x)
    - L.pop(): 가장 오른쪽칸 값 꺼내버려서 보여줌
    - L.pop(i): i칸 값 꺼내버려서 보여줌
    - L.clear(): 리스트 모든 값 삭제
## 리스트 탐색/정렬 메서드
    - L.index(x): 첫번째로 일치하는 항목 x의 인덱스 값 반환(없으면 오류)
    - L.count(x): 리스트에서 x개 몇개인지 반환
    - L.reverse(): 리스트 순서 거꾸로 뒤집기(정렬은 아님)
    - L.sort(): 오름차순으로 정렬(sort(reverse=True)로 내림차순 가능)
### append, extend, insert, remove
## 딕셔너리
값 추가할 때 [키]:벨류
    - get(key[default],'): 키의 value 반환하거나 키가 없는 값이면 None, 키가 없을 때 뒤에 적으면 뒤에 적은 값
    - .keys(): 키 값만 다 보여주기
    - .values(): 벨류만 다 보여주기
    - .items(): 키 + 밸류 전부 보여주기
    - .pop(key,default): 키를 제거하고 연결됐던 value 출력, 없는 키면 에러 or dafault 값 출력
    - .setdefault(key,default): 키와 연결된 값을 반환, 키가 없으면 연결한 키를 딕셔너리에 추가하고 default 반환
    - .update([other]): other에 써있는 값들로 딕셔너리 갱신, 기존 키는 덮어씌움    
## set
    - s.add(x): 세트에 x 추가
    - s.remove(x): 세트에서 x 지워버리기, x값 없으면 에러
    - s.discard(x): 세트에서 x 지워버리기, x 값 없어도 에러 안남
    - s.pop(x): 랜덤 요소 뽑아내기
    - s.clear(): 다 지워버리기
    - s.update(iterable): 세트에 iterable 요소 추가
    - 집합 메서드:
        - set1.difference(set2): 차집합  set1-set2
        - set1.intersection(set2): 교집합 set1&set2
        - set1.issubset(set2): set1이 set2에 다 들어있으면 True, set1<=set2
        - set1.issuperset(set2): set1이 set2의 항목을 다 갖고 있으면 True set1>=set2
        - set1.union(set2): 합집합 set1+set2 하고 반환
# 객체
- 가변 객체: 리스트(list), 딕셔너리(dict), 집합(set)
- 불변 객체: 정수(int), 실수(float), 문자열(str), 튜플(tuple)
## 복사
- 얕은 복사: a = [1,2,3] b = a, b[0]= 100 하면 주소에 들어있던 친구들 바뀌어버림
- 슬라이싱 [:], copy() 메서드, list()함수
    - 1차원 리스트는 복사 가능하지만, 안에 바꿀 수 있는 리스트가 있으면 바꿨을 때 같이 바뀜
- 깊은 복사: copy 모듈 import copy 하고 변수 = copy.deepcopy로 복사
# 파이썬 문법 규격
    - EBNF가 대세
    - [넣어도 되고 안 넣어도 되는 애들]
    - {0번 이상 반복}
    - (그룹화)