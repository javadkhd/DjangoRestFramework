
```
├── backend
│   ├── accounts
│   │   ├── admin.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── services
│   │   │   ├── auth_service.py
│   │   │   ├── email_service.py
│   │   │   └── __init__.py
│   │   ├── tests.py
│   │   ├── tokens.py
│   │   └── views.py
│   ├── common
│   │   ├── health.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── config
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── manage.py
│   ├── orders
│   │   ├── admin.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── permissions.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── services
│   │   │   ├── cpu_processing.py
│   │   │   ├── exceptions.py
│   │   │   ├── __init__.py
│   │   │   └── order_service.py
│   │   ├── tasks.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── requirements.txt
│   └── staticfiles
│ 
├── docker
│   └── nginx
│       ├── Dockerfile
│       └── nginx.conf
├── docker-compose.yml
├── Makefile
└── README.md

```
