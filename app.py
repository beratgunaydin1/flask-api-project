from flask import Flask, jsonify

app = Flask(__name__)

# Basit bir endpoint
@app.route('/api', methods=['GET'])
def hello_world():
    return jsonify({"message": "Merhaba Dünya! Bu bir Flask API'dir."})

# Uygulamayı başlat
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

