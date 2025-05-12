FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python", "trabalho5.py"]
