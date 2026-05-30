from core.tool_contract import tool_result

def score(job):
    signals = []

    text = job['snippet'].lower()

    if 'multiple' in text:
        signals.append('growth')

    if 'urgent' in text:
        signals.append('urgency')

    return tool_result(True, {
        'score': 5 + len(signals)*2,
        'signals': signals,
        'tier': 'hot' if len(signals) > 1 else 'warm'
    })
