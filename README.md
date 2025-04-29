# ⛑️ Emergpt_Voice-bot
**중대재해 예방을 위한 AI 기반 음성 감지 챗봇 시스템**  
산업현장에서 발생 가능한 중대재해 위험 상황을 음성 기반으로 실시간 감지하고,  
GPT와 연동된 챗봇을 통해 긴급상황 대응 및 관리자 알람이 가능한 시스템입니다.

> *데이터청년캠퍼스에서 진행한 프로젝트입니다.* 

## 🔍 1. Project OverView
| 항목 | 내용 |
| --------- | ----- |
| 프로젝트명 | emergpt-voice-bot |
| 주제 | 중대재해 위험 사안 발견 시, Voice Bot을 이용한 현장 근로자 제보 시스템 |
| 주요 기술 | Flask, OpenAI GPT(gpt-3.5-turbo), AWS(Transcribe, S3, DynamoDB), KoNLPy |
| 적용 대상 | 중대재해 발생 가능 산업현장, 위험 작업 환경, 긴급 대응 시스템 |   
<br/>
  
![Image](https://github.com/user-attachments/assets/a0eff313-bf3a-4da3-a542-b712886a1324)
  
## 🎯 2. Background & Goal
### Backgroud
- **중대재해처벌법** 시행 이후에도 여전히 발생하는 산업 재해
- 작업 현장의 안전 미흡과 비효율적인 사고 보고 체계
- 채팅 입력이 어려운 환경에서 음성 기반 긴급 대응 시스템 필요
### Goal
- 잠재 위험 상황 예방 및 긴급 상황 즉시 신고 기능
- 음성 기반 작업현장 위험 대응 시스템
- 관리자 페이지를 통한 신고 현황 요약 및 신속 대응 가능

## 🧱 3. System Architecture
```
[사용자]
   ↓ (음성 입력)
AWS Transcribe (STT)
   ↓
긴급어 탐지 + 시간 파악 (jin.py)
   ↓
GPT 응답 생성 (Chatbot.py)
   ↓
DynamoDB 저장
   ↓
관리자 알림 (SMS)
```
<img src="https://github.com/user-attachments/assets/bdeba10d-447c-47e8-8933-fab6bbcba933" width="500"/>


## 📌 4. Key Features
| 기능 | 설명 |
|------|------|
| 음성 텍스트 처리 | AWS Transcribe를 이용해 실시간 음성 텍스트 변환(STT) |
| GPT 응답 생성 | GPT-3.5-turbo로 자연스러운 대화 처리 |
| 긴급어 탐지 | "악", "윽" 등 긴급 단어 패턴 감지 |
| 시간 정규화 | "오후 3시 반 전" 등 자연어 시간 정규화 |
| 신고 기록 저장 | DynamoDB를 통한 유저 대화 상태 저장 |
| 확장 가능성 | 관리자 페이지, 알림 시스템(SNS), 모바일화 준비 완료 |

<img src="https://github.com/user-attachments/assets/d045cc9f-cf1e-422d-8181-fff113689c7c" width="500"/>

## 📁 5. File Structure
```
eulji_project/
├── Chatbot.py       # Flask 서버 및 GPT 연동 로직
├── jin.py           # 긴급어 판단 및 시간 파싱 로직
└── templates        # 프론트엔드 HTML 템플릿
    ├── login.html
    ├── manager1.html
    ├── select.html
    └── user.html
```

## 🛠️ 6. Tech Stack

- AI: OpenAI GPT-3.5 API
- Backend: Flask (REST API)
- NLP: KoNLPy Komoran
- Cloud Infra: AWS(S3, DynamoDB, Transcribe)

## 👥  7. Team
<img src="https://github.com/user-attachments/assets/7d3a7275-15e3-4758-b56a-f36b44d9cac5" width="200"/>  

- Team: ACE <br/> 
- Member: 이슬희, 이하은, 김민지, 김진아, 김용준, 최준우, 김태훈, 한동훈

---
**🙋‍♀️ My Tesk**  
- Team Leader/PM: 전체 일정 및 역할 조율, 기획 및 발표 자료 작성
- BE: 서포트
- FE: UI/UX 설계, html 템플릿 작성

## More Info
..

