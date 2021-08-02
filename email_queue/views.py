from django.shortcuts import render
from email_queue.models import EmailQueue

# Create your views here.

def email_send_corn_job():
    email_queue = EmailQueue.objects.filter(email_status="0")[:1]
    for email_id_list in email_queue:
        email = EmailMessage(email_id_list.email_subject, 'Body', to=[email_id_list.email_to])
        resp = email.send()

        if resp == 1:
            update_email_queue = EmailQueue.objects.get(id=email_id_list.id)
            update_email_queue.email_status = "1"
            update_email_queue.save()


# python manage.py shell --command="from email_queue.views import email_send; email_send()"
# https://gutsytechster.wordpress.com/2019/06/24/how-to-setup-a-cron-job-in-django/
# https://www.geeksforgeeks.org/how-to-setup-cron-jobs-in-ubuntu/