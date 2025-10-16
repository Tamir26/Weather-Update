FROM python:3.11-slim

RUN apt-get update && apt-get install -y cron

COPY app /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY cron_app/weather_cron /etc/cron.d/weather_cron
RUN chmod 0644 /etc/cron.d/weather_cron
RUN crontab /etc/cron.d/weather_cron

CMD ["cron", "-f"]
