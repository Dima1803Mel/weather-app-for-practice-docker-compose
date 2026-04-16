import requests
from flask import Flask, jsonify, request
import os

app = Flask(__name__)
API_KEY = os.environ.get('OPENWEATHER_API_KEY')

@app.route('/', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Moscow') # Заменен город на Москву
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description']
            })
        else:
            return jsonify({'error': data.get('message', 'City not found')}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)