from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 数据库的配置变量
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1q,4/ZzKkLl@127.0.0.1:3306/爬虫实验1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# 创建”学院与楼栋“表
class table1(db.Model):
    # 定义表名为users
    __tablename__ = '学院与楼栋'

    # 将id设置为主键，并且默认是自增长的
    building_id = db.Column(db.Integer, primary_key=True)
    # 楼栋字段，字符类型，最大的长度是10个字符
    building = db.Column(db.String(10))
    # 学院字段，字符类型，最大的长度是50个字符
    faculty = db.Column(db.String(50))
    # 楼层总数字段，整型类型
    total_floors = db.Column(db.Integer)

    # 让打印出来的数据更好看，可选的
    def __repr__(self):
        return "building_id:'%s'  building:'%s'  faculty:'%s'  " \
               "total_floors:'%s'" % (self.building_id, self.building, self.faculty, self.total_floors)


# 创建”中间表“表
class table2(db.Model):
    # 定义表名为中间表
    __tablename__ = '中间表'

    # 将位置id设置为主键，并且默认是自增长的
    location_id = db.Column(db.Integer, primary_key=True)
    # 具体楼层字段，整型类型
    specific_floor = db.Column(db.Integer)
    # 楼栋id字段，整型类型，外键与表1
    building_id = db.Column(db.Integer, db.ForeignKey("学院与楼栋.building_id"))

    # 让打印出来的数据更好看，可选的
    def __repr__(self):
        return "location_id:'%s'  specific_floor='%s'  total_floors='%s'" \
               % (self.location_id, self.specific_floor, self.building_id)


# 创建”学院与楼栋“表
class table3(db.Model):
    # 定义表名为users
    __tablename__ = '实验室表'

    # 将实验室id设置为主键，并且默认是自增长的
    laboratory_id = db.Column(db.Integer, primary_key=True)
    # 实验室位置字段，字符类型，最大的长度是10个字符
    laboratory_location = db.Column(db.String(10))
    # 实验室名称字段，字符类型，最大的长度是25个字符
    laboratory_name = db.Column(db.String(25))
    # 备注字段，字符类型，最大的长度是100个字符
    remarks = db.Column(db.String(25))
    # 位置id字段，整型类型，外键和表2
    location_id = db.Column(db.Integer, db.ForeignKey("中间表.location_id"))

    # 让打印出来的数据更好看，可选的
    def __repr__(self):
        return "laboratory_id='%s'  laboratory_location='%s'  laboratory_name='%s'  " \
               "remarks='%s'  location_id='%s'" % (self.laboratory_id, self.laboratory_location,
                                                   self.laboratory_name, self.remarks, self.location_id)


if __name__ == '__main__':
    # 创建
    db.drop_all()
    db.create_all()
