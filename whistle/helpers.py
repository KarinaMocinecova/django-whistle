from django_rq import job
from django.core.mail import send_mail
from whistle.managers import NoticeManager


def notify(request, recipient, event, actor=None, object=None, target=None):
    NoticeManager.notify(request, recipient, event, actor, object, target)


@job
def send_mail_in_background(subject, message, from_email, recipient_list, html_message=None, fail_silently=True):
    send_mail(subject, message, from_email, recipient_list, html_message=html_message, fail_silently=fail_silently)
