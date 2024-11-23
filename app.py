import json
from dbAccessor  import Base, session 
from flask import Flask, jsonify
from flask import render_template, request
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import and_, or_
from sqlalchemy import update
from datetime import datetime
from users import Users

app = Flask(__name__)

# メタデータとテーブル定義
metadata = MetaData()

@app.route("/", methods=['GET'])
def index():
    print('index start')
    return render_template("index.html")

#メイン画面表示
@app.route("/login", methods=['GET'])
def login():
    print('login start')
    p1 = request.args.get('title')
    p2 = request.args.get('body')
    res = 'NG'
    session.begin()
    try:
        # データの検索
        #data = session.query(Users).get(35) #プライマーキー
        data = session.query(Users).filter(Users.title == p1).first()
        #data = session.query(Users).filter_by(title = p1).first()
        if data.body == p2:
            res = 'OK'
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print('finally')
        session.close()  # セッションを閉じる

    return jsonify({'responce':res})

#ユーザー登録
@app.route("/regist", methods=['POST'])
def regist():
    print('regist start')

    title = request.form.get('title')
    body = request.form.get('body')

    session.begin()
    try:
        # データの挿入
        user = Users()
        user.title = title
        user.body = body
        session.add(user)
        session.commit()
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        print('finally')
        session.close()  # セッションを閉じる

    return render_template('regist.html', title=title, body=body)

#ユーザー削除
@app.route("/delete", methods=['DELETE'])
def delete_user():
    print('delete start')

    id = request.args.get('user_id')
    ret = 'NONE'
    session.begin()
    try:
        # データの削除
        #data = session.query(Users).filter(and_(Users.title == p1, Users.body == p2)).first()
        data = session.query(Users).filter(and_(Users.id == id)).first()
        if data is not None:
            session.delete(data)
            session.commit()
            ret = 'OK'
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
        session.close()  # セッションを閉じる
        return render_template('err.html', id=id)
    finally:
        print('finally')

    if ret == 'NONE':
        session.close()  # セッションを閉じる
        return jsonify({'responce':'NG'}), 404

    # データ全取得
    users = session.query(Users).all()
    session.close()  # セッションを閉じる
    return render_template('list.html', users=users)

#ユーザー一覧取得
@app.route("/get_all", methods=['GET'])
def get_all():
    print('get_all start')
    res = []
    session.begin()
    try:
        # データ全取得
        users = session.query(Users).all()
        for user in users:
            res.append({'id':user.id, 'title':user.title, 'body':user.body})

    except Exception as e:
        print(f"Error: {e}")
        return render_template('err_500.html', users=users)
    finally:
        print('finally')
        session.close()  # セッションを閉じる
        return render_template('list.html', users=users)

if __name__ == ('__main__'):
    app.run(debug=True, host='127.0.0.1', port=5000)