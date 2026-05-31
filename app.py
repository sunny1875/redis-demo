from flask import Flask
import redis
import os

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "127.0.0.1"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    password=os.getenv("REDIS_PASSWORD", "123456"),
    decode_responses=True
)

@app.route("/")
def index():
    return "CI/CD Demo Running"

@app.route("/set/<key>/<value>")
def set_key(key, value):
    r.set(key, value)
    return f"Set {key} = {value} success"

@app.route("/get/<key>")
def get_key(key):
    value = r.get(key)
    return f"Get {key} = {value}" if value else f"Key {key} not found"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)