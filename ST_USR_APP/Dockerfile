# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Ollama
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install streamlit ollama markdown

# Download the Ollama model
RUN ollama pull deepseek-r1:8b

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV NAME World

# Run streamlit when the container launches
CMD ["streamlit", "run", "app.py"]