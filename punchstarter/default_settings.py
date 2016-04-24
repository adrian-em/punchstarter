import os
import cloudinary

DEBUG=os.environ.get("DEBUG", True)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///" + BASE_DIR + "/app.db")
CLOUDINARY_CLOUD_NAME=os.environ.get('CLOUDINARY_CLOUD_NAME', 'dosbsyifo')
CLOUDINARY_API_KEY=os.environ.get('CLOUDINARY_API_KEY', '543818716775279')
CLOUDINARY_API_SECRET=os.environ.get('CLOUDINARY_API_SECRET', 'ft1MzRAsXJioenTYGIu1dzoga-8')

SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_EMAIL_SENDER = 'Punchstarter'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = '^^ghfskVgkcCkfgFFkc$568V$v'
SECURITY_CONFIRMABLE = False

SECRET_KEY = "\xbd\x9c6\xb0\xf0N\xb0k\xd4\xa4\xa93\xbc\xed'\xa5\xb6W\xa0\xe6W`\xfea"

cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)
