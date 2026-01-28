FROM python:3.12-slim

WORKDIR /app/backend


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt



COPY ./entrypoint.sh .

RUN chmod +x /app/backend/entrypoint.sh
RUN sed -i 's/\r$//g' /app/backend/entrypoint.sh




COPY . .

ENTRYPOINT ["sh", "/app/backend/entrypoint.sh"]

