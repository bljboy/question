SECRET_KEY = "sdfadsfdgdsafs/fs"
# 数据库配置消息
HOST = 'bljboy.itdage.cn'
PORT = '3306'
DATABASE = 'question'
USERNAME = 'question'
PASSWORD = 'bljboy'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "2371076453@qq.com"
MAIL_PASSWORD = "vuytdkldwitqdjgc"
MAIL_DEFAULT_SENDER = "2371076453@qq.com"
