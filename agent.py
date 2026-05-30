from connectors.jobs import fetch_jobs
from connectors.contact import enrich
from tools.scorer import score
from tools.emailer import generate
from crm.db import init_db
from core.logger import log

def run_pipeline():

    init_db()

    jobs = fetch_jobs('Portsmouth VA')

    if not jobs.get('success'):
        log('pipeline_error', {'stage': 'job_fetch_failed'})
        return

    for job in jobs['data']:

        try:
            company = job['company']

            contact = enrich(company, job['location'])
            lead = score(job)
            emails = generate(
                contact['data'],
                company,
                job,
                lead['data']['signals']
            )

            log('job_fetch', job)
            log('lead_processed', {
                'company': company,
                'score': lead['data']['score']
            })

        except Exception as e:
            log('lead_error', {'company': job.get('company'), 'error': str(e)})
