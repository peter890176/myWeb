# Base Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=False

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential gcc libpq-dev pkg-config default-libmysqlclient-dev --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first (better caching)
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Make sure whitenoise is installed for static files
RUN pip install whitenoise

# Copy the project code into the container
COPY . .

# Create static files directory if it doesn't exist
RUN mkdir -p static/images
RUN mkdir -p staticfiles

# Copy your static files into the container (if they're not already in the repo)
# COPY path/to/your/local/images/* /app/static/images/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Command to run the application (using Gunicorn)
CMD ["gunicorn", "api.wsgi:application", "--bind", "0.0.0.0:8000"]
