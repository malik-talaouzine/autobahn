from celery import shared_task

@shared_task
def run_fetcher():
    from django.core.management import call_command
    call_command('fetcher')