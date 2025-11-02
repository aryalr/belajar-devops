from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Halo, ini adalah proyek DevOps pertama saya! saya telah push image ini ke dockerhub!' \
    'tes perubahan 1' \
    'tes perubahan 2'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)