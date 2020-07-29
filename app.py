from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
professors = [
    { 'name': '변승환', 'region': '서울', 'classNo': '1반' },
    { 'name': '유창오', 'region': '서울', 'classNo': '2반' },
    { 'name': '김선재', 'region': '서울', 'classNo': '3반' },
    { 'name': '이철민', 'region': '대전', 'classNo': '1반' },
    { 'name': '송빈산', 'region': '대전', 'classNo': '2반' },
    { 'name': '김도영', 'region': '구미', 'classNo': '1반' },
    { 'name': '이민교', 'region': '광주', 'classNo': '1반' },
]
@app.route('/')
def index():
    name = request.args.get('name')
    professor = list(filter(lambda x: x['name']==name, professors))
    if len(professor) == 0:
        return jsonify({'error': 'name required'})
        
    professor = professor[0]
    data = {
        'entry.1682982420':professor['region'],
        'entry.1736238762':professor['classNo'],
        'entry.409090123':professor['name'],
        'entry.1191662158':'37.5 미만',
        'entry.1175693492':'이상없음',
        'entry.111036440':'아니오',
    }
    url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSdfCStXdPYKoA6VL4S_GkbwpNbnF6GsQ3gic7-ok410fMoA4w/formResponse'
    status_code = requests.post(url,data).status_code
    return jsonify({'status_code': status_code})


if __name__ == '__main__':
    app.run(debug=True)

