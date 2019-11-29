from flask import Flask, render_template
import sqlite3
import base64
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def index():
    return render_template ("index.html")

@app.route('/listStudent')
def listStudent():
    con = sqlite3.connect("week10.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Lab10")
    rows = cur.fetchall()
    return_list = []
    for row in rows:
        return_list.append(dict(row))
    for row in return_list:
        row['Link'] = base64.b64decode(row['Link']).decode()
    cur.close
    return render_template("list.html", rows=return_list)

@app.route('/findStudent')
def findStudent():
    con = sqlite3.connect("week10.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Lab10")
    rows = cur.fetchall()
    return_list = []
    for row in rows:
        return_list.append(dict(row))
    for row in return_list:
        row['Link'] = base64.b64decode(row['Link']).decode()
    cur.close
    return render_template("find.html", rows=return_list)

if __name__ == '__main__':
     app.run()
