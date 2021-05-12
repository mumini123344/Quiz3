'''
• (1 ქულა) გამოიყენეთ requests მოდულის მინიმუმ 3-4 ფუნქცია/ატრიბუტი (მაგ. get(), status_code, header)
• (1 ქულა) შეინახეთ json ფორმატის მონაცემი json ფაილში სტრუქტურული სახით (json მოდულის ფუნქციის
გამოყენებით)
• (1 ქულა) გამოიყენეთ json/dict ობიექტთან სამუშაო ფუნქციები და დაბეჭდეთ თქვენთვის საინტერესო
ინფორმაცია, რასაც გსურთ რომ API-ს მეშვეობით მიწვდეთ
• (1 ქულა) შეინახეთ თქვენთვის საინტერესო ინფორმაცია ბაზაში (შექმენით ცხრილი პითონის მეშვეობით,
აღწერეთ მოკლე კომენტარის სახით)
• (1 ქულა) ატვირთეთ py ფაილი Github-ზე (ან სხვა მსგავს პლატფორმაზე). README ფაილში მოკლედ აღწერეთ
რას წარმაოდგენს თქვენი პროექტი და როგორ მუშაობს (2 აბზაცის სახით).
'''


import requests
import json
import sqlite3

con = sqlite3.connect('anime_db.sqlite')
c = con.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS anime
                (title VARCHAR(30),
                episodes INTEGER,
                score INTEGER,
                type VARCHAR(15),
                start_date INTEGER,
                end_date INTEGER
                )''')

url = 'https://api.jikan.moe/v3/search/anime?q=naruto'
r = requests.get(url)
print(r.status_code)
print(r.headers)
print(r.text)


res = r.json()
with open('quiz3.json', 'w') as f:
    json.dump(res, f, indent=4)

# print(res['results'][20]['title'])
# print(res['results'][30]['score'])


all_rows = []
for i in res['results']:
    title = i['title']
    episodes = i['episodes']
    score = i['score']
    type = i['type']
    start_date = i['start_date']
    end_date = i['end_date']
    row = (title, episodes, score, type, start_date, end_date)
    all_rows.append(row)


c.executemany('INSERT INTO anime (title, episodes, score, type, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?)', all_rows)
con.commit()
con.close()

