# インポート
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib

# APIを叩く
url = "https://pokeapi.co/api/v2/pokemon/987"

res = json.loads(requests.get(url=url).text)
# echo あれ種族値だ　妥協したんじゃなかったけwww
# echo Pythonはめちゃくちゃ型が柔軟なのでできたよ
# echo あっそ
# echo ついでに次作で弱体化されるであろうハバタクカミのレーダーチャートを作成するよ


label_list = []
value_list = []

for stats, p in zip(res["stats"], ["HP", "攻撃", "防御", "特攻", "特防", "素早さ"]):
    print(f'{p}:{stats["base_stat"]}')
    label_list.append(p)
    value_list.append(stats)

value_list += value_list[:1]

angle_list = [n / float(len(label_list)) * 2 * np.pi for n in range(len(label_list))]

angle_list += angle_list[:1]
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.plot(angle_list, value_list, linewidth=2, linestyle="solid")
ax.fill(angle_list, value_list, "b", alpha=0.1)

plt.show()
