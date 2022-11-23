from flask import *
from database import *
api=Blueprint('api',__name__)
@api.route('/login',methods=['get','post'])
def login():
    data={}
    uname=request.args['username']
    paswd=request.args['password']
    qry="select * from login where username='%s' and `password` ='%s'"%(uname,paswd)
    det=select(qry)
    print(det)      
    if det:#checking does the data of user found or not
        data['status']="success"
        data['check']=det
    else:
        data['status']="failed"
    return str(data)
