from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
professors = [
    {'name': '변승환', 'region': '서울', 'classNo': '1반'},
    {'name': '유창오', 'region': '서울', 'classNo': '2반'},
    {'name': '김선재', 'region': '서울', 'classNo': '3반'},
    {'name': '김구현', 'region': '서울', 'classNo': '3반'},
    {'name': '이철민', 'region': '대전', 'classNo': '1반'},
    {'name': '송빈산', 'region': '대전', 'classNo': '2반'},
    {'name': '김도영', 'region': '구미', 'classNo': '1반'},
    {'name': '이민교', 'region': '광주', 'classNo': '1반'},
    {'name': '오창희', 'region': '서울', 'classNo': '1반'},
    {'name': '김재석', 'region': '서울', 'classNo': '1반'},
    {'name': '김준호', 'region': '서울', 'classNo': '1반'},
    {'name': '유태영', 'region': '서울', 'classNo': '1반'},
]
@app.route('/')
def index():
    name = request.args.get('name')
    professor = list(filter(lambda x: x['name'] == name, professors))
    if len(professor) == 0:
        return jsonify({'error': 'name required'})

    professor = professor[0]
    data = {
        'entry.481921250': professor['region'],
        'entry.325239344': professor['classNo'],
        'entry.1104903483': professor['name'],
        'entry.1308377243': '37.5 미만',
        'entry.332287326': '이상없음',
        'entry.1451922838': '아니오',
    }
    url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSeIsX-6RsqlBxOCzrPyTxi7alrmjddsLBJk_0opFasr_qz0kg/formResponse'
    status_code = requests.post(url, data).status_code
    return jsonify({'status_code': status_code})


if __name__ == '__main__':
    app.run(port=80)
