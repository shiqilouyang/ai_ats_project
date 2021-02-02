from flask import Flask
from flask_pymongo import PyMongo


from TestPollModelMoreUserAndClass import ai_ats_project
from conf.Setting import Config

app = Flask(__name__)
app.register_blueprint(ai_ats_project,url_prefix='/ai_ats_project')
conf =  Config()
app.config['SQLALCHEMY_DATABASE_URI'] = conf.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config["SQLALCHEMY_POOL_SIZE"] = conf.SQLALCHEMY_POOL_SIZE
app.config["SQLALCHEMY_ECHO"] = conf.SQLALCHEMY_ECHO
app.config['SQLALCHEMY_POOL_TIMEOUT'] = conf.SQLALCHEMY_POOL_TIMEOUT
app.config['SQLALCHEMY_POOL_RECYCLE'] = conf.SQLALCHEMY_POOL_RECYCLE
app.config['SQLALCHEMY_MAX_OVERFLOW'] = conf.SQLALCHEMY_MAX_OVERFLOW
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size' : 100, 'pool_recycle' : 280}
app.config['MONGO_URI'] = conf.MONGO_DATABASE_URI

# mongo 绑定到 app
# 每次 mongo 可以直接使用
mongo = PyMongo(app)
