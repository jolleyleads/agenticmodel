from core.tool_contract import tool_result

def enrich(company, location):
    return tool_result(True, {
        'person': {
            'name': 'John Doe',
            'email': 'john@example.com',
            'title': 'Owner'
        },
        'company': company,
        'location': location
    })
