from starlette.config import Config

config = Config('.env')

DATABASE_URL = config('EE_DATABASE_URL', cast=str, default='')
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = 'HS256'
SECRET_KEY = config('EE_SECRET_KEY', cast=str, default='f7a64ec22b03d59ecbe6fd2ad903866bbbc7fd9af0dd94d722cedb41cb1d7601')