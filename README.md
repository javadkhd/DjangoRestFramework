
```
project/
├── backend/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── celery.py
│   │   ├── urls.py
│   │   └── wsgi.py / asgi.py
│   │
│   ├── orders/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tasks.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── order_service.py
│   │   │   └── exceptions.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   └── urls.py
│   │   └── migrations/
│   │       └── ...
│   │
│   ├── manage.py
│   ├── requirements.txt
│   └── ...
│
├── docker/
│   ├── backend/
│   │   └── Dockerfile
│   └── nginx/
│       └── nginx.conf
│
├── .env
├── Makefile
├── docker-compose.yml
├── .gitignore
└── README.md
```
