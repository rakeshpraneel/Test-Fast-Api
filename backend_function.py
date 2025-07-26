import json
import functools
import time


def time_calculator(func):
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        output = func(*args, **kwargs)
        end = time.perf_counter()
        print(end - start)
        return output
    return wrapper


@functools.lru_cache(maxsize=10)
# @time_calculator
def fetch_data(name):
    with open("data/db.json", "r") as data:
        content_ = json.load(data)
    content_ = content_.get('data')
    for values in content_:
        if name == values.get('name'):
            return values
    return False