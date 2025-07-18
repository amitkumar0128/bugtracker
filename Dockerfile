# Build Stage (with full tools)
FROM python:3.11 

WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install --no-warn-script-location --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

# Run the bugtracker app
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn --bind 0.0.0.0:8000 bugtracker.wsgi"]