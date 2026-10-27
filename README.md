# OSS Week 7

KOBIS 일별 박스오피스 API 예제입니다. Python 3.13에서 작성된 `.venv`를 ZIP에서 그대로 복사해 두었습니다.

## 실행

```powershell
.\.venv\Scripts\Activate.ps1
$env:KOBIS_API_KEY = "발급받은_API_키"
python main.py
```

`first.py`를 실행하면 해당 날짜의 상위 5개 영화가 출력됩니다. API 키는 소스 코드나 Git에 올리지 말고 환경변수로 설정하세요. 기존 `secret.py`는 ZIP 원본 그대로 로컬에 있지만 `.gitignore` 처리되어 커밋되지 않습니다.

새 컴퓨터에서 실행할 때는 Python 3.13을 설치하고 다음 명령으로 가상환경을 다시 만드세요.

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
