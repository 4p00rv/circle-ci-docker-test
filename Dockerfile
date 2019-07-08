FROM python:3
WORKDIR /app
EXPOSE 8000
COPY src /app
CMD ["python", "server.py"]


