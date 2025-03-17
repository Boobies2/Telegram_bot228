import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def save_data(data):
    r.lpush('messages', data)

def get_data():
    return r.lrange('messages', 0, -1)

if __name__ == '__main__':
    save_data("Test message")
    print(get_data())
