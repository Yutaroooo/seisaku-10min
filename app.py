from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import random


app = Flask(__name__)
app.secret_key = "sunabacokoza"


@app.route("/")
def main():
    return render_template("main.html")


# ーーーーーーーーーーーーーーーーーーーーーーーーここからガチャシステム
@app.route("/gacha")
def gacha():
    result = "None"
    while (result == "None"):
        conn = sqlite3.connect("gacha.db")
        c = conn.cursor()
        c.execute('SELECT "やること", "一言", "リンク" FROM "koumoku-t" WHERE "yaru-id" <= 4;')
        gacha = c.fetchall()
        gacha = random.choice(gacha)
        if (gacha[0] != ""):
            result = gacha[0]
        else:
            result = "None"
    if gacha[1] is not None:
        word = gacha[1]
    else:
        word = ""
    if gacha[2] is not None:
        link = gacha[2]
        length = (len(word) + len(result))
        if (length >= 76):
            nagasa = len(result)
            nagasa = (77 - nagasa)
            wordl = (word[0:nagasa])
            dot = "…"
        else:
            wordl = (word)
            dot = ""
    else:
        link = ""
        length = (len(word) + len(result))
        if (length >= 85):
            nagasa = len(result)
            nagasa = (86 - nagasa)
            wordl = (word[0:nagasa])
            dot = "…"
        else:
            wordl = (word)
            dot = ""
    c.close()
    return render_template("gacha.html", result=result, word=word, wordl = wordl, dot = dot, link=link)


@app.route("/gacha/undow")
def undow():
    conn = sqlite3.connect("gacha.db")
    c = conn.cursor()
    c.execute('SELECT "やること", "一言", "リンク" FROM "koumoku-t" WHERE "yaru-id" = 1;')
    gacha = c.fetchall()
    gacha = random.choice(gacha)
    if gacha[0] is not None:
        result = gacha[0]
    else:
        result = ""
    if gacha[1] is not None:
        word = gacha[1]
    else:
        word = ""
    if gacha[2] is not None:
        link = gacha[2]
        length = (len(word) + len(result))
        if (length >= 76):
            nagasa = len(result)
            nagasa = (77 - nagasa)
            wordl = (word[0:nagasa])
            dot = "…"
        else:
            wordl = (word)
            dot = ""
    else:
        link = ""
        length = (len(word) + len(result))
        if (length >= 85):
            nagasa = len(result)
            nagasa = (86 - nagasa)
            wordl = (word[0:nagasa])
            dot = "…"
        else:
            wordl = (word)
            dot = ""
    c.close()
    return render_template("gacha.html", result=result, word=word, wordl = wordl, dot = dot, link=link)


@app.route("/gacha/kaji")
def kaji():
    conn = sqlite3.connect("gacha.db")
    c = conn.cursor()
    c.execute('SELECT "やること", "一言", "リンク" FROM "koumoku-t" WHERE "yaru-id" = 2;')
    gacha = c.fetchall()
    gacha = random.choice(gacha)
    if gacha[0] is not None:
        result = gacha[0]
    else:
        result = ""
    if gacha[1] is not None:
        word = gacha[1]
    else:
        word = ""
    if gacha[2] is not None:
        link = gacha[2]
        length = (len(word) + len(result))
        if (length >= 76):
            nagasa = len(result)
            nagasa = (77 - nagasa)
            wordl = (word[0:nagasa])
            dot = "…"
        else:
            wordl = (word)
            dot = ""
    else:
        link = ""
        length = (len(word) + len(result))
        if (length >= 85):
            nagasa = len(result)
            nagasa = (86 - nagasa)
            wordl = (word[0:nagasa])
            dot = "…"
        else:
            wordl = (word)
            dot = ""
    c.close()
    return render_template("gacha.html", result=result, word=word, wordl = wordl, dot = dot, link=link)


@app.route("/gacha/study")
def study():
    conn = sqlite3.connect("gacha.db")
    c = conn.cursor()
    c.execute('SELECT "やること", "一言", "リンク" FROM "koumoku-t" WHERE "yaru-id" = 3;')
    gacha = c.fetchall()
    gacha = random.choice(gacha)
    if gacha[0] is not None:
        result = gacha[0]
    else:
        result = ""
    if gacha[1] is not None:
        word = gacha[1]
    else:
        word = ""
    if gacha[2] is not None:
        link = gacha[2]
        length = (len(word) + len(result))
        if (length >= 76):
            nagasa = len(result)
            nagasa = (77 - nagasa)
            wordl = (word[0:nagasa])
            dot = "…"
        else:
            wordl = (word)
            dot = ""
    else:
        link = ""
        length = (len(word) + len(result))
        if (length >= 85):
            nagasa = len(result)
            nagasa = (86 - nagasa)
            wordl = (word[0:nagasa])
            dot = "…"
        else:
            wordl = (word)
            dot = ""
    c.close()
    return render_template("gacha.html", result=result, word=word, wordl = wordl, dot = dot, link=link)


@app.route("/gacha/osusume")
def yaminabe():
    result = "None"
    while (result == "None"):
        conn = sqlite3.connect("gacha.db")
        c = conn.cursor()
        c.execute('SELECT "やること", "一言", "リンク" FROM "koumoku-t" WHERE "yaru-id" >= 4;')
        gacha = c.fetchall()
        gacha = random.choice(gacha)
        if (gacha[0] != ""):
            result = gacha[0]
        else:
            result = "None"
    if gacha[1] is not None:
        word = gacha[1]
    else:
        word = ""
    if gacha[2] is not None:
        link = gacha[2]
        length = (len(word) + len(result))
        if (length >= 76):
            nagasa = len(result)
            nagasa = (77 - nagasa)
            wordl = (word[0:nagasa])
            dot = "…"
        else:
            wordl = (word)
            dot = ""
    else:
        link = ""
        length = (len(word) + len(result))
        if (length >= 85):
            nagasa = len(result)
            nagasa = (86 - nagasa)
            wordl = (word[0:nagasa])
            dot = "…"
        else:
            wordl = (word)
            dot = ""
    c.close()
    return render_template("gacha.html", result=result, word=word, wordl = wordl, dot = dot, link=link)


# ーーーーーーーーーーーーーーーーーーーーここまでガチャシステム
@app.route("/adding")
def adding():
    return render_template("add.html")


@app.route("/add", methods=["POST"])
def add():
    comment = request.form.get("comment")
    if (comment == ""):
        return redirect("/adding")
    word = request.form.get("word")
    conn = sqlite3.connect("gacha.db")
    c = conn.cursor()
    c.execute("INSERT INTO 'koumoku-t' VALUES (NULL, ?, ?, NULL, 5);", (comment,word))
    conn.commit()
    conn.close()
    return redirect("/kakunin")


@app.route("/kakunin")
def kakunin():
    return render_template("kakunin.html")

@app.errorhandler(404)
def notfound404(code):
    return render_template("404.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)