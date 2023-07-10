# todos
```
fastapi simple todos app
```

## python 가상환경 만들기
```
python -m venv fa_venv
```

## 가상환경 활성화
```
[windows]
fa_venv/scripts/activate

[mac/linux]
source fa_venv/bin/activate
```
## 설치 라이브러리
<pre>
pip install fastapi
pip install "uvicorn[standard]"
pip install jinja2 python-multipart
pip install sqlalchemy
</pre>

## 서버 실행방법
```
python app_start.py
```

## todos 클라이언트 테서트

```
### 앱 실행
http://localhost:8000

### 스웨거
http://localhost:8000/docs
```