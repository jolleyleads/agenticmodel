from core.tool_contract import tool_result
from core.logger import log

def fetch_jobs(location):
    log('job_fetch', {'location': location})

    return tool_result(True, [
        {
            'company': 'HVAC Elite Services',
            'title': 'Dispatcher',
            'snippet': 'Hiring multiple technicians due to expansion',
            'location': location
        }
    ])
