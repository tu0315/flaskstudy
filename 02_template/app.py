from flask import Flask, render_template
from custom_filters import reverse, birth_year


app = Flask(__name__)

app.add_template_filter(reverse, "reverse_name")
app.add_template_filter(birth_year, "birth_year")


@app.route("/")
def index():
    return render_template("index.html")


# class化
class UserInfo:
    # 初期インスタンス
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    # あいさつ関数
    def greet(self):
        # 必ずリターンを用意する
        return f"{self.name}です。趣味は{self.hobby}です。よろしくお願いいたします。"


@app.route("/home/<string:user_name>/<int:age>/<string:hobby>")
def home(user_name, age, hobby):
    # login_user = user_name
    # user_info = {"name": user_name, "age": age}

    # インスタンス化
    user_info = UserInfo(user_name, age, hobby)
    # user_info.greet()
    return render_template("home.html", user_info=user_info)


@app.route("/userlist")
def userlist():
    # リスト変数をセット
    users = ["taro", "jiro", "saburo", "siro", "takuro"]
    # boolean型の変数セット
    is_login = False
    # render_templateの引数にセットする
    return render_template("userlist.html", users=users, is_login=is_login)


if __name__ == "__main__":
    app.run(debug=True)
