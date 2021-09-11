from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from pytz import UTC
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy.sql import func

import re
from sqlalchemy import func, DateTime, select, types
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://gmkeshari:gmkeshari123@database1.ctdcirbzvpt9.ap-south-1.rds.amazonaws.com:3306/test1' 

db = SQLAlchemy(app)

class table1(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    received = db.Column(DateTime(timezone=True), default=func.now())
    data = db.Column(db.String(128))

    def __init__(self, data):
        self.data = data

def time():
    time = datetime.now(UTC)
    time = str(time)
    time = time[:-13]
    time_edit1 = time.replace("-", "").replace("-", "").replace(" ", "").replace(":", "").replace(":", "")
    return time_edit1


@app.route('/gmk', methods=['GET', 'POST'])

def sprinkler():
    data = request.args.get('d')
    if data !='':
        table2 = table1(data)
        db.session.add(table2)
        db.session.commit()


        last_data_1 = time()
        return "OUR DATA = *{}<'.{}{}.'>".format(last_data_1, last_data_1, data)

    elif data =='':

        last_rec= db.session.query(db.func.max(table1.id)).scalar()
        data1 = db.session.query(table1.data).filter(table1.id==last_rec)
        last_data = data1.first()
        last_data_1 = str(last_data)

        last_data_1 = last_data_1.replace('(', '').replace("'", "").replace("'", "").replace(",", "").replace(')', '')

        time_edit_2= time()

        return "OUR DATA = *{}<'.{}{}.'>".format(time_edit_2, time_edit_2, last_data_1)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True,use_reloader=True)
    #app.run(debug=True)