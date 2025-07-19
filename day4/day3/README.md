# API
    1. Interface: 서로 다른 두 개의 시스템이 정보를 교환할 때, 그 사이에 존재하는 접점(키보드, 마우스, 리모컨)
    2. UI(user interface): 사람과 소프트웨어의 접점 화면 그래픽적 요소
### 클라이언트:
데이터를 요청하는 쪽, 사용자
### 서버:
요청을 받아서 처리하는 쪽

클라이언트가 특정 URL을 요청하면
서버가 페이지, 데이터를 보내줌

### API
Application Programming Interface: 데이터 요청, 응답 규칙

api key: 고유 번호  
보안 강화, 유저 데이터 관리

---

# Prompt Engineering
Colab 자주 씀  
client = OpenAI(api key= "~")  
conversation history = [role: system]: 기본 지침, 스타일, 말투 등등 설정  
role user: 사용자의 입력  

max_tokens: 응답 최대 길이 설정(chleo 16,385)  
n: 응답 개수  
seed: 응답 일관성 유지  

response.choices: 만든 응답 중에 답변 고르기(n=1 이니까 하나만 고르기)  
response.message.content: 응답 텍스트 출력

# Vibe coding
재밌는 거  
챗봇 만들기: html, css, js로 하고 ChatGPT API로 해달라 하고 API key 넣으면 ChatGPT 갖다가 해줌  
해달라고 하면 다 해줘서 재밌음