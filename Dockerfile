# Use a lightweight official Python image
FROM python:3.12-slim

# Prevent Python from writing pyc files to disc and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set workspace directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements files if you have them, or just copy the directory structures
COPY . /workspace/

# Install python packages globally inside the container
RUN pip install --no-cache-dir fastapi uvicorn streamlit requests torch transformers