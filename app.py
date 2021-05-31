from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/list', methods=['GET'])
def saved_contents():
    saved_content = list(db.screw.find({}, {'_id': False}))
    return jsonify({'all_saved_content': saved_content})


@app.route('/save', methods=['POST'])
def write_review():
    content_receive = request.form['content_give']
    doc = {
        'content': content_receive,
    }
    db.screw.insert_one(doc)
    return jsonify({'msg': '저장완료'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'delete 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
