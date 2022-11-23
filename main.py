from flask import Flask
from api import api
app=Flask(__name__)
app.secret_key='lid'
app.register_blueprint(api,url_prefix='/api')
app.run(debug=True,port=5002,host="0.0.0.0")