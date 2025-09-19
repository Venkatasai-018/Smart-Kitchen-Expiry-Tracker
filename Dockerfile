FROM python:3.11-alpine

WORKDIR /app

ADD . .

RUN pip install fastapi

RUN pip install supabase

RUN pip install uvicorn

EXPOSE 8000

CMD ["python","main.py"]