from flask import Flask, render_template, request, redirect, session
import sqlite3, random

app = Flask(__name__)
app.secret_key = "sunabacokoza"


@app.route("/gacha")
def color():
    conn = sqlite3.connect("gacha.db")
    c = conn.cursor()
    c.execute('SELECT "やること", "一言", "リンク" FROM "koumoku-t" WHERE "yaru-id" = 1;')
    gacha = c.fetchall()
    gacha = random.choice(gacha)
    kekka = gacha[0]
    hitokoto = gacha[1]
    link = gacha[2]
    c.close()
    return render_template("gacha.html", kekka = kekka, hitokoto = hitokoto, link = link)

if __name__ == "__main__":
    app.run(debug=True)