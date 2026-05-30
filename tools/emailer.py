import random
from core.tool_contract import tool_result

def generate(contact, company, job, signals):

    name = contact['person']['name']

    subjects = [
        f'Quick hiring question - {company}',
        f'Helping {company} fill HVAC roles',
        f'Saw your dispatcher opening'
    ]

    emails = []

    for i in range(3):
        emails.append({
            'subject': random.choice(subjects),
            'body': f'''
Hey {name},

I noticed {company} is hiring HVAC roles.

Signals detected: {', '.join(signals)}

We help teams reduce time-to-hire significantly.

— AI Agent System
''',
            'day': i * 2
        })

    return tool_result(True, emails)
