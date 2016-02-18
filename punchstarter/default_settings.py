import os
import cloudinary

DEBUG=True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/app.db"


cloudinary.config( 
  cloud_name = "zju", 
  api_key = "131446842534827", 
  api_secret = "jPYe8zZKOZkHkdbNc6b1eXsUoss" 
)