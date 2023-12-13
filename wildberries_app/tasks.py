from celery import shared_task


@shared_task(name='get_categories')
def get_categories():
    print('hello')
    pass
