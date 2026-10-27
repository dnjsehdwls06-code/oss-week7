import os
import requests

url = "https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
api_key = os.getenv("KOBIS_API_KEY")
if not api_key:
    raise SystemExit("KOBIS_API_KEY 환경변수를 설정한 뒤 실행하세요.")

params = {"key": api_key, "targetDt": "20260824"}
response = requests.get(url, params=params, timeout=10)
response.raise_for_status()
data = response.json()
movies = data["boxOfficeResult"]["dailyBoxOfficeList"]

for movie in movies[:5]:
    print(f"{movie['rank']}위: {movie['movieNm']} - 관객수: {int(movie['audiCnt']):,}")
