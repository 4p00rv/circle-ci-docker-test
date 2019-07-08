FROM python:3.7-alpine
WORKDIR /app
EXPOSE 8000
COPY src /app
CMD ["python", "server.py"]


