"""
ASGI config for helloworld project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# 장고 환경 모듈 경로 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.local")

application = get_asgi_application()
