from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/login_index')
def login_index():
    return render_template('login_index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/find_password')
def find_password():
    return render_template('find_password.html')

@app.route('/find_password2')
def find_password2():
    return render_template('find_password2.html')

@app.route('/find_id')
def find_id():
    return render_template('find_id.html')

@app.route('/find_id2')
def find_id2():
    return render_template('find_id2.html')

# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_lists():
    lists = list(db.bucketlists.find({}, {'_id': False}))
    return jsonify({'lists': lists})

@app.route('/api/enrollment', methods=['POST'])
def enrollment():
    title = request.form['title_give']
    description = request.form['description_give']
    image = request.form['image_give']
    category = request.form['category_give']


    doc = {'title': title, 'description': description, 'image': image, 'like': 0, 'category': category}
    db.bucketlists.insert_one(doc)
    return jsonify({'msg': '등록되었습니다!'})


@app.route('/api/heart', methods=['POST'])
def heart():
    image_receive = request.form['image_give']
    target_heart = db.bucketlists.find_one({'image': image_receive})
    current_heart = target_heart['like']
    new_heart = current_heart + 1
    db.bucketlists.update_one({'image': image_receive}, {'$set': {'like': new_heart}})
    return jsonify({})


@app.route('/api/member', methods=['POST'])
def member():
    id1 = request.form['id_give']
    pw = request.form['pw_give']
    nickname = request.form['nickname_give']

    doc = {'id1': id1, 'pw': pw, 'name': nickname}
    db.bucketlist_members.insert_one(doc)
    return jsonify({'msg': '등록되었습니다!'})

@app.route('/api/check', methods=['POST'])
def check():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    if db.bucketlist_members.find_one({'id1': id_receive}):
        target = db.bucketlist_members.find_one({'id1': id_receive})
        if target['pw'] == pw_receive:
            return jsonify({'result': True})
        else:
            return jsonify({'msg': '아이디 및 비밀번호가 틀렸습니다!', 'result': False})
    else:
        return jsonify({'msg': '아이디 및 비밀번호가 틀렸습니다!', 'result': False})

@app.route('/api/sign_up_check', methods=['POST'])
def id_check():
    id_receive = request.form['id_give']
    if db.bucketlist_members.find_one({'id1': id_receive}):
        return jsonify({'result': False})
    else:
        return jsonify({'result': True})

@app.route('/api/upload_check', methods=['POST'])
def image_check():
    image_receive = request.form['image_give']
    if db.bucketlist_members.find_one({'image': image_receive}):
        return jsonify({'result': False})
    else:
        return jsonify({'result': True})

@app.route('/api/find_password_check', methods=['POST'])
def find_password_check():
    id_receive = request.form['id_give']
    if db.bucketlist_members.find_one({'id1': id_receive}):
        return jsonify({'result': False})
    else:
        return jsonify({'result': True})

@app.route('/api/category', methods=['POST'])
def category():
    category_receive = request.form['category_give']
    lists = list(db.bucketlists.find({'category': category_receive}, {'_id': False}))
    return jsonify({'lists': lists})

@app.route('/api/like', methods=['GET'])
def like():
    lists = list(db.bucketlists.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'lists': lists})

@app.route('/api/modify_password', methods=['POST'])
def modify():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    db.bucketlist_members.update_one({'id1': id_receive}, {'$set': {'pw': pw_receive}})

    return jsonify({'msg': '변경완료!'})

@app.route('/api/name_check', methods=['POST'])
def name_check():
    name_receive = request.form['name_give']
    if db.bucketlist_members.find_one({'name': name_receive}):
        return jsonify({'result': False})
    else:
        return jsonify({'result': True})

@app.route('/api/check_id', methods=['POST'])
def check_id():
    name_receive = request.form['name_give']
    lists = list(db.bucketlist_members.find({'name': name_receive}, {'_id': False}))
    return jsonify({'lists': lists})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)