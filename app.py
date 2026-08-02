from flask import Flask, request, render_template_string
import os
from app.ai import ask_ai

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Xenon AI</title>
    <style>
        body{
            background:#0d1117;
            color:white;
            font-family:Arial,sans-serif;
            text-align:center;
            padding:40px;
        }
        h1{
            color:#00ffcc;
        }
        textarea{
            width:80%;
            height:120px;
            background:#161b22;
            color:white;
            border:1px solid #00ffcc;
            border-radius:10px;
            padding:10px;
        }
        button{
            margin-top:15px;
            padding:10px 25px;
            background:#00ffcc;
            border:none;
            border-radius:8px;
            cursor:pointer;
            font-size:18px;
        }
        .cevap{
            margin-top:30px;
            background:#161b22;
            padding:20px;
            border-radius:10px;
            width:80%;
            margin-left:auto;
            margin-right:auto;
            text-align:left;
            white-space:pre-wrap;
        }
    </style>
</head>
<body>

<h1>🤖 Xenon AI</h1>

<form method="POST">
<textarea name="message" placeholder="Bir şey yaz..."></textarea><br>
<button type="submit">Gönder</button>
</form>

{% if answer %}
<div class="cevap">
<b>Xenon AI:</b><br><br>
{{ answer }}
</div>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        message = request.form["message"]
        answer = ask_ai(message)
    return render_template_string(HTML, answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
