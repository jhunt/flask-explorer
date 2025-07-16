FROM python:3-slim
WORKDIR /app

# things only this image needs:
RUN pip install --no-cache-dir gunicorn

# things this app needs:
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
