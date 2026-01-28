PROJECT_NAME=orders_project

.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "Available commands:"
	@echo ""
	@echo "  make build           Build all services"
	@echo "  make up              Start all services"
	@echo "  make down            Stop all services"
	@echo "  make restart         Restart all services"
	@echo ""
	@echo "  make logs            Show logs"
	@echo "  make logs-backend    Show backend logs"
	@echo "  make logs-worker     Show worker logs"
	@echo ""
	@echo "  make migrate         Run django migrations"
	@echo "  make makemigrations  Create new migrations"
	@echo "  make superuser       Create django superuser"
	@echo "  make collectstatic   Collect static files"
	@echo ""
	@echo "  make shell           Django shell"
	@echo ""

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose down
	docker compose up -d

logs:
	docker compose logs -f

logs-backend:
	docker compose logs -f backend

logs-worker:
	docker compose logs -f worker

makemigrations:
	docker compose exec backend python manage.py makemigrations

migrate:
	docker compose exec backend python manage.py migrate

superuser:
	docker compose exec backend python manage.py createsuperuser

collectstatic:
	docker compose exec backend python manage.py collectstatic --noinput

shell:
	docker compose exec backend python manage.py shell
