# Dockerfile
FROM python:3.8

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY app.py /app/app.py

CMD ["python", "app.py"]

# Build the Docker image
# docker build -t loan-prediction-app .

# Run the Docker container
# docker run -d -p 5000:5000 loan-prediction-app
