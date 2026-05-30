from connectors.jobs import fetch_jobs
from connectors.contact import enrich
from tools.scorer import score
from tools.emailer import generate
from crm.db import init_db

def run():

    init_db()

    jobs = fetch_jobs('Portsmouth VA')

    for job in jobs['data']:

        company = job['company']

        contact = enrich(company, job['location'])
        lead = score(job)
        emails = generate(contact['data'], company, job, lead['data']['signals'])

        print('Processed:', company, lead['data']['score'])

if __name__ == '__main__':
    run()
