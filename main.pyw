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
    <form action="/send_message" method="post">
        <input type="text" name="message" placeholder="Nhập link">
        <input type="submit" value="Gửi">
    </form>
  
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
@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.form["message"]
    print(message)
    return 'Thanh cong'
@app.route("/hello7", methods=["POST"])
def hello7(message):
  subprocess.Popen("shutdown.exe -r -t 0")
  return 'ok'
if __name__ == "__main__":
  app.run(port=5000,host=ip[0])
