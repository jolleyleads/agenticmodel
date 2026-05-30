import json, time

def log(event, payload=None):
    print(json.dumps({
        'event': event,
        'timestamp': time.time(),
        'payload': payload or {}
    }))
