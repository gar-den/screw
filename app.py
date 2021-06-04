from pymongo import MongoClient
from bson.objectid import ObjectId

from flask import Flask, render_template, jsonify, request, url_for, redirect

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

#login_id = -10

# HTML 화면 보여주기
@app.route('/')
def login_page():
    #print("id:", login_id)

    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    #global login_id
    #print("id:", login_id)

    #id_received = request.form['id_give']

    #login_id = int(id_received)

    return render_template('login.html')


@app.route('/index')
def home():
    """
    global login_id
    print("id:", login_id)

    if login_id > 0:
        login_id = -10

        return render_template('index.html')
    else:
        return render_template('login.html')
    :return:
    """

    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/list', methods=['GET'])
def saved_contents():
    saved_content = list(db.screw.find({}, {'_id': False}).sort("finish", 1))

    return jsonify({'all_saved_content': saved_content})


@app.route('/list_one', methods=['POST'])
def saved_content():
    content_received = request.form['content_give'].split('\n')[0]
    date_received = request.form['date_give']
    group_received = int(request.form['group_give'])

    date_received = date_received.split('/')[1] + "/" + date_received.split('/')[2] + "/" + date_received.split('/')[0]

    content = db.screw.find_one({'content': content_received, 'group': group_received, 'finish': date_received}, {'_id': False})

    return jsonify({'saved_content': content})


@app.route('/list', methods=['POST'])
def make_done():
    content_received = request.form['work_give'].split('\n')[0]
    group_received = int(request.form['group_give'])
    date_received = request.form['date_give']
    donedate_received = request.form['donedate_give']

    date_received = date_received.split('/')[1] + "/" + date_received.split('/')[2] + "/" + date_received.split('/')[0]

    db.screw.update_one({'content': content_received, 'group': group_received, 'finish': date_received},
                        {'$set': {'done': True, "tododone": donedate_received}})

    return jsonify({'msg': '완료되었습니다.'})

"""
@app.route('/modify', methods=['POST'])
def modify_schedule():
    schedule_receive = request.form['schedule_give']
    changed_receive = request.form['changed_give']

    target_schedule = db.screw.find_one({'name': schedule_receive})['content']

    db.screw.update_one({'content': target_schedule}, {'$set': {'content': changed_receive}})

    return jsonify({'msg': '수정되었습니다'})
"""

@app.route('/save', methods=['POST'])
def post_schedule():
    original_content = request.form['original_content']
    original_group = request.form['original_group']
    original_finish = request.form['original_finish']

    title_received = request.form['content_give']
    comment_received = request.form['comment_give']
    start_received = request.form['start_give']
    finish_received = request.form['finish_give']
    url_received = request.form['url_give']
    remind_received = request.form['remind_give']
    group_received = request.form['group_give']

    db.screw.delete_one({'content': original_content, 'group': original_group, 'finish': original_finish})

    # 다시 등록하기
    doc = {
        'content': title_received,
        'start': start_received,
        'finish': finish_received,
        'comment': comment_received,
        'url': url_received,
        'remind': remind_received,
        'group': group_received,
        'done': False,
    }
    db.screw.insert_one(doc)

    saved_contents()

    return jsonify({'msg': '저장완료'})

"""
@app.route('/delete', methods=['POST'])
def delete_schedule():
    original_content = request.form['content_give']

    db.screw.delete_one({'content': original_content})

    return jsonify({'msg': '삭제되었습니다'})
"""

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)