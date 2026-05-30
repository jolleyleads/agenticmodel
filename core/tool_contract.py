import time, uuid

def tool_result(success, data=None, error=None, metadata=None):
    return {
        'success': success,
        'data': data,
        'error': error,
        'metadata': {
            'id': str(uuid.uuid4()),
            'timestamp': time.time(),
            **(metadata or {})
        }
    }
