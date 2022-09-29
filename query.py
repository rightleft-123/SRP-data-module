from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from create import table1, table2, table3

# 数据库的配置变量
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1q,4/ZzKkLl@127.0.0.1:3306/爬虫实验1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


@app.route('/')
def index():
    all_record = table1.query.all()
    for i in range(len(all_record)):
        print(all_record[i])
    return f'< h1 > {all_record} < / h1 >'


if __name__ == '__main__':
    app.run(debug=True)
    '''
    # 查询表格全部内容
    all_record = table1.query.all()
    print('\n')
    for i in range(len(all_record)):
        print(all_record[i])
    '''

    '''
    # 精确查询
    print('\n')
    records = table1.query.filter_by(faculty='微电子学院').all()
    for i in range(len(records)):
        print(records[i])
    '''

    '''
    # 模糊查询
    print('\n')
    records1 = table1.query.filter(table1.faculty.like('%学院%')).all()
    for i in range(len(records1)):
        print(records1[i])
    '''