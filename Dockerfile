FROM python:3
WORKDIR /app
EXPOSE 8080
COPY src /app
CMD ["python", "server.py"]


