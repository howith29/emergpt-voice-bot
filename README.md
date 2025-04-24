# emergpt-voice-bot

## 1. Project OverView
**중대재해 예방을 위한 AI 기반 음성 감지 챗봇 시스템**
  
| 항목 | 내용 |
| ---- | ----- |
| 프로젝트명 | emergpt-voice-bot |
| 주제 | 중대재해 위험 사안 발견 시, Voice Bot을 이용한 현장 근로자 제보 시스템 |
| 주요 기술 | Flask, OpenAI GPT(gpt-3.5-turbo), AWS(Transcribe, S3, DynamoDB), KoNLPy |
| 적용 대상 | 산업현장, 중대재해, 위험 작업 환경, 긴급 대응 시스템 등 |


## 2. Key Features
---
| 기능 | 설명 |
|------|------|
| 음성 텍스트 처리 | AWS Transcribe를 이용해 실시간 음성 텍스트 변환 |
| GPT 응답 생성 | GPT-3.5-turbo로 자연스러운 대화 처리 |
| 긴급어 탐지 | "악", "윽" 등 긴급 단어 패턴 감지 |
| 시간 파악 | "오후 3시 반 전" 등 자연어 시간 정규화 |
| 대화 기록 저장 | DynamoDB를 통한 유저 대화 상태 저장 |
| 확장 가능성 | 관리자 페이지, 알림 시스템(SNS), 모바일화 준비 완료

## 3. Project Structure
---
### 3.1. file Structure
```
eulji_project/
├── Chatbot.py
├── jin.py
└── templates
    ├── login.html
    ├── manager1.html
    ├── select.html
    └── user.html
```
### 3.2. System Architecture
- **클라이언트**: 모바일 또는 웹 클라이언트
- **음성 수집**: AWS Transcribe로 실시간 음성 텍스트 변환
- **데이터 저장**: DynamoDB (사용자 발화 저장), S3 (음성 파일 저장)
- **긴급 분석**: Flask 서버 + GPT + Komoran 형태소 분석
- **알림 전송**: AWS SNS (향후 확장 가능)

[사용자] → [음성 입력] → [Transcribe] → [Flask 서버 (GPT 분석)] → [긴급 판별] → [저장 및 응답]
## 4. Team 
---
### 4.1. Team
### 4.2. Task & Responsibilites

## 5. Technology Stack
---
- AI: OpenAI GPT-3.5 API
- Backend: Flask (REST API)
- NLP: KoNLPy Komoran
- Cloud Infra: AWS(S3, DynamoDB, Transcribe)
