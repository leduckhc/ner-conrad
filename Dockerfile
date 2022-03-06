# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

# Allow statements and log messages entities immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy app code and pretrained models into the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY app.py ./
COPY requirements.txt ./
COPY pretrained_models ./pretrained_models

RUN ls -la

# install poetry dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# install the http web server
RUN pip install "uvicorn[standard]"

# Run the selector service
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--workers", "5", "--port", "8000"]