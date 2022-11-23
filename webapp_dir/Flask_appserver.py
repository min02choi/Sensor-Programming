from flask import Flask, render_template
app = Flask(__name__)

session_cnt = 0

@app.route("/")
def index():
    global session_cnt
    session_cnt = session_cnt + 1
    cnt_str = str(session_cnt)
    return render_template("index_add.html", name="BGKim", value1=cnt_str)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
