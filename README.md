# Pylog - 나만의 블로그 시스템 (Django 프로젝트)

Django 입문자에게 추천하는 블로그 웹서비스 예제 프로젝트입니다.  
글 작성, 수정, 삭제, 댓글 기능을 포함한 간단한 블로그 플랫폼을 구축하여 Django의 기본 구조를 학습.

## 프로젝트 개요

- 프로젝트명: Pylog
- 기술스택: Python, Django 5.x, HTML/CSS (템플릿), SQLite
- 주요 기능:
  - 게시글 목록, 상세, 작성, 수정, 삭제
  - 댓글 등록, 삭제
  - 관리자 페이지를 통한 데이터 관리

## 폴더 구조

```
pylog/
├── config/               # 프로젝트 설정
│   ├── settings.py       # 환경설정 (STATIC, MEDIA, DB 등)
│   ├── urls.py           # 전체 URL 라우팅 설정
├── blog/                 # 주요 앱 (게시판 기능 담당)
│   ├── models.py         # 게시글, 댓글 모델 정의
│   ├── views.py          # 뷰 함수: 글/댓글 처리 로직
│   ├── forms.py          # 폼: 게시글/댓글 입력 처리
│   ├── urls.py           # blog 앱의 URLConf
│   ├── templates/blog/   # 템플릿: 글 목록, 상세, 작성 등
│   └── admin.py          # 관리자 페이지 설정
├── db.sqlite3            # 기본 SQLite DB
└── manage.py             # Django 명령어 실행용 스크립트
```

## 주요 기능 설명

### 게시판 (blog 앱)
- **글 목록 보기**: `/blog/`  
- **글 상세 보기**: `/blog/<int:pk>/`
- **글 작성/수정/삭제**: 인증 없이 가능 (연습용 구성)

### 댓글 기능
- 글 상세 페이지 하단에 댓글 작성 가능  
- 댓글 삭제도 가능 (작성자 인증은 생략)

### 관리자 기능
- `admin/` URL 접속 → 관리자 로그인 후 전체 데이터 관리 가능
- 관리자 등록 시 `createsuperuser` 명령 사용

## 실행 방법

```bash
# 1. 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Django 설치
pip install django

# 3. 프로젝트 서버 실행
python manage.py runserver

# 4. 접속
http://127.0.0.1:8000/blog/
```

## 참고 사항

- 본 프로젝트는 학습용으로 **보안 및 인증 로직이 생략**되어 있습니다.
- Django의 **모델 → 뷰 → 템플릿 → URL 연결 흐름**을 익히는 데 집중합니다.
- admin 페이지 사용을 위해 superuser 등록 필요:
  ```bash
  python manage.py createsuperuser
  ```


🎓 *이 프로젝트는 '이한영의 Django 입문' Part 3 (슬라이드 107~182)을 기반으로 제작되었습니다.*
