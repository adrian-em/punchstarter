import os
import cloudinary
DEBUG=True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/app.db"

cloudinary.config(
    cloud_name='dosbsyifo',
    api_key='543818716775279',
    api_secret='ft1MzRAsXJioenTYGIu1dzoga-8'
)
