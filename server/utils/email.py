from django.conf import settings
from django.core.mail import send_mail


class EmailUtils:
    @staticmethod
    def send(subject, to, data=None, template=None):
        from_email = f"Abocados Team <{settings.DEFAULT_FROM_EMAIL}>"
        send_mail(
            subject=subject,
            message=data,
            recipient_list=to,
            from_email=from_email,
            fail_silently=False,
            html_message=template,
        )
