# 참고 사이트
![코딩도장: https://dojang.io/course/view.php?id=7]  
![코드솔: https://codesol.how-to.best/doc/python]  
# input
"원하는 변수형"(input())  
input() 하면 리스트로 저장  
map(변수형,input().split()): 입력한 거 차례대로 넣고 변수형으로 바꾸기  
# 내장함수
sum(더하기)  
# print
print(x+"변수 뒤에 뭐 붙여서 출력하려면 + 쓰기")
안에 + end" " 안에 내용들 사이에 " " 값 넣어서 출력
# 함수 만들기
- def(함수 정의) 함수 이름(동사+명사)(괄호 안에 매개변수 정의 가능):   
(tab)코드 블록 return 반환 값(내보내는 값)
    - 매개변수: 함수가 받을 값을 나타내는 변수
    - 인자: 함수 호출할 때 드가는 값
        - 위치 인자: 자릿수 맞추기
        - 기본 인자값: 매개변수에 디폴트 값 넣어두기
        - 키워드 인자: 인자 칸에 매개변수=값 으로 넣기
        - 임의의 인자 목록: 정해지지 않은 개수의 인자 처리, 매개변수 앞에 * 붙이기, 여러 개의 인자를 tuple(,)로 처리
        - 임의의 키워드 인자 목록: 정해지지 않은 개수의 키워드 인자 처리, 매개변수 앞에 ** 붙이기, 여러 개의 인자를 dictonary로 처리
- 함수 호출: 함수이름()로 호출
- python의 범위(scope): 함수는 코드 안에 local scope를 만들고 나머지 영역은 global scope로 구분
    - global keyword: [1](image/글로벌키워드.jpg)
- 변수 수명 주기: [1](image/변수수명주기.jpg)
- 이름 검색 규칙: [1](image/이름검색규칙.jpg)
- List Comprehension(알고만 있으면): [1](image/ListComprehension.jpg)
- enumerate(자주 쓰는 친구): [1](image/enumerate.jpg)