from flask import Flask, current_app, g, render_template, request, url_for

# flask 클래스를 인스턴스화한다
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, Flaskbook!"


# flask2부터는 @app.get("/hello"), @app.post("/hello")라고 기술하는 것이 가능
# @app.get("/hello")
# @app.post("/hello")
# def hello():
#     return "Hello, World!"


@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello_name(name):
    # Python 3.6부터 도입된 f-string으로 문자열을 정의
    return f"Hello, {name}!"


# show_name 엔드포인드를 작성한다
@app.route("/name/<name>")
def show_name(name):
    # 변수를 템플릿 엔진에게 건넨다
    return render_template('index.html', name=name)


with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name='world'))
    # /name/AK?page=1
    print(url_for('show_name', name="AK", page="1"))


# 여기에서 호출하면 오류가 된다
# print(current_app)

# 애플리케이션 컨텍스트를 취득하여 스택에 push한다
ctx = app.app_context()
ctx.push()

# current_app에 접근할 수 있게 된다
print('current_app.name :', current_app.name)

# 전역 임시 영역에 값을 설정한다
g.connection = 'connection'
print('g.connection :', g.connection)


with app.test_request_context("/users?updated=true"):
    # true가 출력된다
    print(request.args.get('updated'))