FROM python:3.11-alpine

WORKDIR /app

ADD . .

RUN pip install fastapi supabase uvicorn


EXPOSE 8080

CMD ["python","main.py"]