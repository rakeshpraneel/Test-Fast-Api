import functools

from fastapi import FastAPI
import uvicorn
import backend_function
import time

app = FastAPI()

def time_calculator(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        output = await func(*args, **kwargs)
        end = time.perf_counter()
        print(end - start)
        return output
    return wrapper



@time_calculator
@app.get("/getmethod")
@time_calculator
async def download(name: str):
    answer = backend_function.fetch_data(name)
    return answer


if __name__ == '__main__':
    uvicorn.run("fast_collector:app", host="127.0.0.1", port=8000, reload=True)
