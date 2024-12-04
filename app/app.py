from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f"<h1>Hola, se creara el balanceador de carga</h1><p>IP de la instancia: {ip_address}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
