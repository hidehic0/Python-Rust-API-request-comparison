# インポート
import requests
import json

# APIを叩く
url = "https://pokeapi.co/api/v2/pokemon/987"

res = json.loads(requests.get(url=url).text)
# echo あれ種族値だ　妥協したんじゃなかったけwww
# echo Pythonはめちゃくちゃ型が柔軟なのでできたよ
for stats in zip(res["stats"], ["HP", "攻撃", "防御", ""]):
    print(f'{stats["base_stat"]}')
