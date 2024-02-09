html='''
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Kêu vịt</title>

</head>
<body>
  <h1>Kêu vịt</h1>
  <button onclick="sendHello1()">Ra</button>
  <h1></h1>
  <button onclick="sendHello2()">Cút</button>
  <h1>Lựa chọn khác</h1>
  <button onclick="sendHello3()">sút đau</button>
  <h1></h1>
  <button onclick="sendHello7()">rì sét</button>
  <h1></h1>
  <button onclick="sendHello4()">Lựa Chọn 1</button>
  <h1></h1>
  <button onclick="sendHello5()">Lựa Chọn 2</button>
  <h1></h1>
  <button onclick="sendHello6()">Lựa Chọn 3</button>
   <script>
    function sendHello1() {
      // Gửi yêu cầu đến chương trình Python
      fetch("/hello", {
        method: "POST",
      }).then(response => {
        // Xử lý phản hồi từ chương trình Python
        console.log(response);
      });
    }
	function sendHello2() {
      // Gửi yêu cầu đến chương trình Python
      fetch("/hello2", {
        method: "POST",
      }).then(response => {
        // Xử lý phản hồi từ chương trình Python
        console.log(response);
      });
    }
	function sendHello3() {
      // Gửi yêu cầu đến chương trình Python
      fetch("/hello3", {
        method: "POST",
      }).then(response => {
        // Xử lý phản hồi từ chương trình Python
        console.log(response);
      });
    }
	function sendHello4() {
      // Gửi yêu cầu đến chương trình Python
      fetch("/hello4", {
        method: "POST",
      }).then(response => {
        // Xử lý phản hồi từ chương trình Python
        console.log(response);
      });
    }
	function sendHello5() {
      // Gửi yêu cầu đến chương trình Python
      fetch("/hello5", {
        method: "POST",
      }).then(response => {
        // Xử lý phản hồi từ chương trình Python
        console.log(response);
      });
    }
	function sendHello6() {
      // Gửi yêu cầu đến chương trình Python
      fetch("/hello6", {
        method: "POST",
      }).then(response => {
        // Xử lý phản hồi từ chương trình Python
        console.log(response);
      });
    }
	function sendHello7() {
      // Gửi yêu cầu đến chương trình Python
      fetch("/hello7", {
        method: "POST",
      }).then(response => {
        // Xử lý phản hồi từ chương trình Python
        console.log(response);
      });
    }
  </script>
</body>
</html>

'''

from flask import Flask, request , render_template
import subprocess , webbrowser
ip=open('ip.txt', 'r').read().split("\n")
lc=open('lua_chon.txt', 'r').read().split("\n")
app = Flask(__name__)

@app.route("/")
def index():
  return html
@app.route("/hello", methods=["POST"])
def hello():
  subprocess.Popen("Duck/GooseDesktop.exe")
  return 'ok'
@app.route("/hello2", methods=["POST"])
def hello2():
  subprocess.Popen("Close.bat")
  return 'ok'
@app.route("/hello3", methods=["POST"])
def hello3():
  subprocess.Popen("shutdown.exe -s -t 0")
  return 'ok'
@app.route("/hello4", methods=["POST"])
def hello4():
  webbrowser.open_new_tab(lc[0])
  return 'ok'
@app.route("/hello5", methods=["POST"])
def hello5():
  webbrowser.open_new_tab(lc[1])
  return 'ok'
@app.route("/hello6", methods=["POST"])
def hello6():
  webbrowser.open_new_tab(lc[2])
  return 'ok'
@app.route("/hello7", methods=["POST"])
def hello7():
  subprocess.Popen("shutdown.exe -r -t 0")
  return 'ok'
if __name__ == "__main__":
  app.run(port=5000,host=ip[0])
