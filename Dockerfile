
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# CMD ["python", "app.py"]
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]


# # Base image
# # FROM python:3.10-slim
# FROM python:3.10

# # Set working directory
# WORKDIR /app

# # Copy files
# COPY . .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Run your script
# CMD ["python", "app.py"]