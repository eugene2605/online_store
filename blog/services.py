from django.conf import settings
from django.core.mail import send_mail


def send_blog_email(blog_item):
    send_mail(
        'Поздравляем!',
        f'Поздравляем! Ваш блог "{blog_item.title}" просмотрели 100 раз!',
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER]
    )
