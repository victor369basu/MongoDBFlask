
from typing import Optional
import uvicorn
from fastapi import FastAPI, Request
from MongoAPI import MongoAPI
import json

app = FastAPI()

@app.get("/")
async def base():
    return {'response':{"Status": "Health Check!"},
            'status':200,
            'mimetype':'application/json'
            }

@app.get('/mongodb')
async def mongo_read(info : Request):
    '''
    Reading the data when a request is sent using the GET HTTP Method
    '''
    data = await info.json()
    if data is None or data == {}:
        return {'response': {"Error": "Please provide connection information"},
                'status':400,
                'mimetype':'application/json'}
    obj = MongoAPI(data)
    response = obj.read()
    return {'response':response,
            'status':200,
            'mimetype':'application/json'}

@app.post('/mongodb')
async def mongo_write(info : Request):
    '''
    Writing the data when a request is sent using the POST HTTP Method.
    '''
    data = await info.json()
    print(data['Document'])
    if data is None or data == {} or 'Document' not in data:
        return {'response': {"Error": "Please provide connection information"},
                'status':400,
                'mimetype':'application/json'}
    obj = MongoAPI(data)
    response = obj.write(data)
    return {'response':response,
            'status':200,
            'mimetype':'application/json'}

@app.put('/mongodb')
async def mongo_update(info : Request):
    '''
    Updating the data when a request is sent using the PUT HTTP Method.
    '''
    data = await info.json()
    if data is None or data == {} or 'DataToBeUpdated' not in data:
        return {'response': {"Error": "Please provide connection information"},
                'status':400,
                'mimetype':'application/json'}
    obj = MongoAPI(data)
    response = obj.update()
    return {'response':response,
            'status':200,
            'mimetype':'application/json'}

@app.delete('/mongodb')
async def mongo_delete(info : Request):
    '''
    Deleting the data when a request is sent using the DELETE HTTP Method.
    '''
    data = await info.json()
    if data is None or data == {} or 'Filter' not in data:
        return {'response': {"Error": "Please provide connection information"},
                'status':400,
                'mimetype':'application/json'}
    obj = MongoAPI(data)
    response = obj.delete(data)
    return {'response':response,
            'status':200,
            'mimetype':'application/json'}

# if __name__ == '__main__':
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, access_log=False)
