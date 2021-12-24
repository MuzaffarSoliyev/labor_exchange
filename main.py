from fastapi import FastAPI
from db.base import database
import uvicorn

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello world'}


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdovn():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)