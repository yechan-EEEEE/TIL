# 토큰(ERC-20) & NFT(ERC-721) 개념 정리

> 목적: 이더리움 기반 프로젝트에서 가장 자주 등장하는 표준인 **ERC-20(토큰)** 과 **ERC-721(NFT)** 를 개념/구조/흐름 중심으로 이해하기 위한 노트  
> 초점: “토큰이란 무엇인가?”, “NFT는 왜 다른가?”, “approve/transferFrom이 왜 중요한가?”

---

## 1) 이더리움에서 토큰/NFT는 무엇인가?

중요한 사실 하나:

> **이더리움에서 토큰과 NFT는 ‘코인’이 아니라 ‘스마트 컨트랙트’다.**

즉, ETH는 네이티브 코인이고,  
ERC-20 / ERC-721은 컨트랙트가 만든 “자산”이다.

---

## 2) ERC란?

ERC는 **Ethereum Request for Comments**의 약자.

- 이더리움 생태계에서 널리 쓰이는 “표준 인터페이스”
- 누구나 같은 규칙을 따르기 때문에
  지갑/거래소/마켓이 호환 가능

대표 표준:
- ERC-20: Fungible Token(대체 가능 토큰)
- ERC-721: Non-Fungible Token(NFT)
- ERC-1155: Multi Token(FT + NFT 혼합)

---

## 3) ERC-20 (Fungible Token) 개념

### 3.1 ERC-20이란?
ERC-20은 “대체 가능한 토큰” 표준이다.

대체 가능이란?
- 1토큰 = 1토큰
- 서로 완전히 동일한 가치
- 돈처럼 쪼개고 합칠 수 있음

예:
- USDT(테더), USDC, UNI, LINK 같은 토큰들

---

### 3.2 ERC-20의 핵심 특징
- **총 발행량(totalSupply)** 존재
- 주소별 잔고(balance) 관리
- 전송(transfer) 가능
- 승인(approve) 후 대리 전송(transferFrom) 가능

---

### 3.3 ERC-20 필수 함수(표준)

#### (1) totalSupply()
- 토큰 총 발행량 조회

#### (2) balanceOf(address owner)
- 특정 주소의 토큰 잔고 조회

#### (3) transfer(address to, uint256 value)
- 내 지갑에서 상대 지갑으로 직접 전송

#### (4) approve(address spender, uint256 value)
- 특정 주소(spender)가 내 토큰을 대신 가져갈 수 있도록 “허용”

#### (5) allowance(address owner, address spender)
- approve로 설정한 허용량 조회

#### (6) transferFrom(address from, address to, uint256 value)
- spender가 owner의 토큰을 대신 전송(허용량 내에서)

---

### 3.4 approve / transferFrom이 중요한 이유
ERC-20에서 DeFi가 가능한 핵심이 이 구조다.

예: Uniswap에서 토큰 스왑할 때
- Uniswap 컨트랙트가 사용자의 토큰을 가져와야 함
- 하지만 컨트랙트는 사용자 지갑을 직접 건드릴 수 없음

그래서:
1) 사용자가 approve로 Uniswap 컨트랙트에 권한을 줌  
2) Uniswap이 transferFrom으로 토큰을 가져감  
3) 교환 결과 토큰을 사용자에게 transfer

---

### 3.5 ERC-20에서 자주 발생하는 실수/주의점

#### (1) approve 무한 승인 위험
많은 서비스가 “무한 승인(2^256-1)”을 유도한다.
편하지만 위험하다.

- 컨트랙트가 해킹되면
- 승인된 토큰이 전부 탈취될 수 있음

#### (2) decimals(소수점)
ERC-20 토큰은 대부분 소수점이 있다.

예:
- decimals = 18 (ETH처럼)
- 실제로는 1토큰 = 10^18 단위

프론트에서 표시할 때 변환이 필요하다.

---

## 4) ERC-721 (NFT) 개념

### 4.1 ERC-721이란?
ERC-721은 “대체 불가능 토큰(NFT)” 표준이다.

대체 불가능이란?
- 각 토큰이 고유한 ID를 가짐
- 서로 같은 가치로 교환할 수 없음
- 소유권을 개별 단위로 관리

예:
- NFT 이미지
- 게임 아이템
- 티켓
- 멤버십 카드

---

### 4.2 ERC-721의 핵심 특징
- 토큰마다 고유한 **tokenId**
- “잔고(balance)”는 토큰 개수 의미
- 소유권은 (ownerOf(tokenId))로 관리
- NFT마다 메타데이터(이미지/설명) 연결 가능

---

### 4.3 ERC-721 필수 함수(표준)

#### (1) balanceOf(address owner)
- 특정 주소가 가진 NFT 개수

#### (2) ownerOf(uint256 tokenId)
- 특정 tokenId의 소유자 주소

#### (3) safeTransferFrom(from, to, tokenId)
- NFT 전송(안전 전송)

#### (4) transferFrom(from, to, tokenId)
- NFT 전송(안전성 체크 없음)

#### (5) approve(to, tokenId)
- 특정 tokenId를 전송할 권한을 특정 주소에 부여

#### (6) setApprovalForAll(operator, approved)
- 특정 operator에게 모든 NFT 전송 권한을 부여

---

### 4.4 safeTransferFrom이 중요한 이유
NFT를 컨트랙트 주소로 전송할 때,
해당 컨트랙트가 NFT를 받을 수 있는지 확인해야 한다.

- 받을 수 없는 컨트랙트로 보내면 NFT가 영구적으로 잠길 수 있음

safeTransferFrom은
컨트랙트가 ERC721Receiver를 구현했는지 확인하고 전송한다.

---

## 5) NFT 메타데이터 구조

NFT는 토큰 자체가 이미지 파일을 들고 있는 게 아니라,
보통 “메타데이터 URI”를 들고 있다.

### 5.1 tokenURI(tokenId)
- tokenId에 해당하는 메타데이터 위치를 반환
- 보통 JSON 파일 주소

예시(JSON):
{
  "name": "My NFT #1",
  "description": "This is an example NFT",
  "image": "ipfs://.../image.png"
}

---

### 5.2 저장 방식
- 중앙 서버(HTTP URL)
- IPFS(분산 저장, 많이 사용)
- 온체인 저장(비싸지만 영구적)

---

## 6) ERC-20 vs ERC-721 비교

| 항목 | ERC-20 | ERC-721 |
|------|--------|---------|
| 자산 유형 | 대체 가능(돈) | 대체 불가(고유) |
| 단위 | 잔고(balance) | tokenId 단위 |
| 대표 사용 | 결제, DeFi, 거버넌스 | 이미지, 아이템, 티켓 |
| 전송 | transfer | safeTransferFrom |
| 승인 | approve + allowance | approve(tokenId), setApprovalForAll |
| 소수점 | 있음(decimals) | 없음(정수 ID) |
| 발행 | mint로 수량 증가 | mint로 tokenId 생성 |

---

## 7) 실제 프로젝트에서 자주 쓰는 흐름

### 7.1 ERC-20 기반 결제 흐름(예)
1. 사용자가 서비스 컨트랙트에 approve
2. 서비스 컨트랙트가 transferFrom으로 토큰 수령
3. 서비스 제공/정산 로직 실행

---

### 7.2 NFT 민팅(Minting) 흐름(예)
1. 사용자가 mint() 호출
2. 컨트랙트가 새로운 tokenId 생성
3. ownerOf(tokenId)가 사용자 주소로 설정
4. tokenURI(tokenId) 연결
5. 이벤트 Transfer가 발생 (mint도 transfer로 기록됨)

---

## 8) 실무/보안 관점 주의사항

### 8.1 승인(approve) 관련 보안
- ERC-20: approve 무한 승인 위험
- ERC-721: setApprovalForAll은 매우 강력한 권한 → 피싱 주의

---

### 8.2 NFT 위조/중복 이슈
NFT는 “이미지 파일”이 아니라 “소유권 기록”이다.

즉:
- 같은 이미지를 여러 컨트랙트에서 NFT로 만들 수 있음
- 진짜 NFT인지 확인하려면 “컨트랙트 주소”가 핵심

---

### 8.3 토큰/NFT는 ‘법적 자산’이 아닐 수 있음
- 기술적으로 소유권 기록이지만
- 법적으로 소유권을 인정할지는 국가/규제에 따라 다름

---

## 9) 한 줄 요약

- **ERC-20**: 돈처럼 “대체 가능한 토큰” 표준 (DeFi의 기본 단위)  
- **ERC-721**: 각각 고유한 “NFT” 표준 (tokenId 기반 소유권)  
- 둘 다 “코인”이 아니라 **스마트 컨트랙트**이며,  
  실무에서는 **approve/권한 관리**가 가장 중요한 보안 포인트다.
