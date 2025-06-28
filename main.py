from fastapi import FastAPI, HTTPException, Form
import uvicorn

app = FastAPI()
client_secret_return = ""

@app.post("/postmethod")
async def upload(
    client_id: str = Form(),
    client_secret: int = Form(),
    grant_type: str = Form()):
    if client_secret == 'Nothing':
        return {
            'client_id': client_id,
            'access_token': 'story of black water',
            'grant_type': grant_type
        }
    else:
        raise HTTPException(status_code=400, detail="wrong input data")

@app.get("/getmethod")
async def download():
    return client_secret_return


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
