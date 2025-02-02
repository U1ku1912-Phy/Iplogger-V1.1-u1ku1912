from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    location = None
    if request.method == 'POST':
        ip = request.form['ip']
        response = requests.get(f'http://ip-api.com/json/{ip}')
        if response.status_code == 200:
            location = response.json()
        else:
            location = {'status': 'fail', 'message': 'Invalid IP or API error'}
    return render_template('index.html', location=location)

if __name__ == '__main__':
    app.run(debug=True)
