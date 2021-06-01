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
    saved_content = list(db.screw.find({}, {'_id': False}).sort("finish", 1))

    return jsonify({'all_saved_content': saved_content})


@app.route('/list', methods=['POST'])
def make_done():
    done_content = request.form['work_give'].split('  ')[0]
    target_work = db.screw.find_one({'content': done_content})
    db.screw.update_one({'content': target_work}, {'$set': {'done': True}})

    print(db.screw.find_one({'content': done_content}, {'_id': False}))

    return jsonify({'msg': '완료되었습니다.'})


@app.route('/modify', methods=['POST'])
def modify_schedule():
    schedule_receive = request.form['schedule_give']
    changed_receive = request.form['changed_give']

    target_schedule = db.screw.find_one({'name': schedule_receive})['content']

    db.mystar.update_one({'content': target_schedule}, {'$set': {'content': changed_receive}})

    return jsonify({'msg': '수정되었습니다'})


@app.route('/save', methods=['POST'])
def post_schedule():
    title_received = request.form['title_give']
    comment_received = request.form['comment_give']
    url_received = request.form['url_give']
    remind_received = request.form['remind_give']

    doc = {
        'content': title_received,
        'start': '2021-06-10',
        'finish': '2021-06-20',
        'comment': comment_received,
        'url': url_received,
        'remind': remind_received,
        'done': False,
    }
    db.screw.insert_one(doc)

    saved_contents()

    return jsonify({'msg': '저장완료'})


@app.route('/delete', methods=['POST'])
def delete_schedule():
    schedule_received = request.form['schedule_give']
    db.screw.delete_one({'name': schedule_received})
    return jsonify({'msg': '삭제되었습니다'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)