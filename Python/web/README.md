# Web
Web site: 여러 웹 페이지가 하나로 모인 공간  
web page: HTML, CSS 등 웹 기술로 만들어진, Web site의 구성요소
- Web page 구성 요소: HTML(Structure) / CSS(Styling) / Javascript(behavior)

## HTML
Hyper Text Markup Language: 웹 페이지의 의미와 구조를 정의하는 언어  
Hyper Text: 웹 페이지를 다른 페이지로 연결하는 링크
```bash
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- 비선형성, 상호연결성, 사용자 주도적 탐색
```
Markup Language: 태그 등을 이용해 문서나 데이터의 구조를 명시하는 언어
```bash
- 인간이 읽고 쓰기 쉬운 형태, 데이터의 구조와 의미를 정의하는 데 집중
ex) HTML, Markdown
```
### HTML 구조
```bash
<!DOCTYPE html>: 해당 문서가 html로 작성된 문서라는 것을 나타냄
<html></html>: 전체 페이지의 콘텐츠를 포함
<title></title>: 브라우저 탭, 즐겨찾기 시 표시되는 제목으로 이용
<head></head>: HTML 문서에 관련된 설명, 설정 등 컴퓨터가 식별하는 메타데이터 작성 / 사용자에게 보이지 않음
<body></body>: HTML 문서의 내용 / 페이지에 표시되는 모든 콘텐츠 작성 / body는 단 하나만 존재
<p></p>: Paragraph 텍스트 문단을 만드는 태그
<a></a>: Anchor 다른 페이지로 이동시키는 하이퍼링크 태그
<img alt>: image src에 지정된 그림을 보여주는 태그 (alt는 이미지가 깨졌을 때 표기할 내용)
```
### HTML Elements (요소)
하나의 요소는 **여는 태그, 닫는 태그, 내용**으로 구성됨  
닫는 태그는 태그 이름 앞에 /슬래시가 포함(닫는 태그가 없는 태그도 존재)
### HTML Attributes (속성)
사용자가 원하는 기준에 맞도록 요소를 설정하거나 요소의 동작을 조절하기 위한 값  
목적:
- 페이지에 나타내고 싶진 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
- CSS에서 스타일 적용을 위해 해당 요소를 선택하기 위한 값으로 활용  
![작성규칙](img/HTML속성.jpg)
### HTML Text Structure
HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것  
ex) h1태그는 단순히 텍스트 크기가 아닌 현재 문서의 최상위 제목이라는 의미
```bash
Heading & Paragraphs: h1~6, p
Lists: ol, ul, li
Emphasis & Importance: em, strong
```
## CSS
Cascading Style Sheet: 웹 페이지의 디자인과 레이아웃을 구성하는 언어  
CSS 적용 방법
1. 인라인(inline) 스타일: 요소 안에 style= 속성 값으로 작성
2. 내부(Internal) 스타일 시트: head 태그 안에 style태그에 작성
3. 외부(External) 스타일 시트: 별도의 CSS 파일 생성 후 link 태그로 불러오기
![우선순위](img/스타일적용우선순위.jpg)
### CSS 기본 구조와 문법
```bash
선택자(Selector): 누구를 꾸밀지 지정하는 부분
선언(Declaration): 어떻게 꾸밀지에 대한 구체적인 한 줄의 명령, 속성과 값이 한 쌍으로 세미콜론으로 끝남
속성(Property): 바꾸고 싶은 스타일의 종류
값(Value): 속성에 적용할 구체적인 설정
```
![구조예시](img/CSS기본구조.jpg)
#### CSS Selectors(선택자)
HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자  
```bash
- 전체 선택자(*): HTML 모든 요소를 선택
- 요소 선택자: 지정한 모든 태그를 선택
- 클래스 선택자('.'): 주어진 클래스 속성을 가진 모든 요소 선택
- 아이디 선택자('#'): 주어진 아이디 속성을 가진 요소 선택, 아이디는 문서에 하나만 있어야함
- 속성 선택자('[]'): 주어진 속성이나 속성값을 가진 모든 요소 선택, 다양한 조건으로 요소를 정교하게 선택 가능
```
![선택자 예시](img/선택자예시.jpg)
#### CSS 결합자(Combinators)
```bash
- 자손 결합자( ): 첫 번째 요소의 자손 요소들 선택 ex) p span = <p> 안에 있는 모든 <span> 선택
- 자식 결합자(>): 첫 번째 요소의 직계 자식만 선택 ex) ul > li = <ul> 안에 있는 한 단계 아래의 모든 <li>를 선택
```
#### CSS Declaration(선언)
선택된 요소에 적용할 스타일을 구체적으로 명시하는 부분  
```bash
CSS 선언의 목적
- 선택자는 '어떤 요소'에 스타일을 적용할지 결정하는 규칙, 선택자로 선택을 했으니
- 중괄호 {} 안에 '무엇을' 할 지 정의하는 부분이 선언
```
구조: { 속성: 값; }  
속성(Property): 스타일링하고 싶은 기능이나 특성(미리 정의해 둔 키워드를 사용)  
값(Value): 속성에 적용될 구체적인 설정(값의 종류도 정해져 있음), 0일 때는 생략  
![값의단위](img/값의단위.jpg)
![단위비교정리](img/단위비교정리.jpg)
#### 명시도
요소에 적용할 CSS 선언을 결정하기 위한 알고리즘  
**Cascading** Style Sheet: 한 요소에 동인한 가중치의 선택자가 적용되면 계단식으로 마지막 선언 사용
```bash
명시도 높은 순서
!important > Inline 스타일 > 선택자(id > class > 요소) > 소스 코드 선언 순서
important는 다른 구조를 무시하고 강제 적용이므로 지양한다
```
#### 상속
기본적으로 CSS는 부모 요소의 속성을 자식에게 상속해 재사용성을 높임  
- 상속 O: text 관련 요소(font, color, text-align), opacity, visibility 등
- 상속 X: Box model 관련 요소(iwdth, height, border ..), position 관련 요소(position, top/right/bottom/left) 등  
MDN에서 상속 확인 가능
#### CSS Box Model
웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 / 요소의 크기, 배치, 간격을 결정하는 규칙  
```bash
외부 간격(margin) > 테두리(border) > 안쪽 여백(padding) > 내용(content)
```
shorthand 속성(단축 속성): 빨리 하려고 둔 설정
```bash
border: width style color / 순서는 영향 x
margin, padding : 상 우 하 좌 / 상 좌우 하 / 상하 좌우 / 공통
```
표준 상자 모델에선 width height 속성 값을 설정하면 내용(content) 박스의 크기가 조정됨  
*{box-sizing: border-box;} = 원하는 대로 상자 크기가 조절됨