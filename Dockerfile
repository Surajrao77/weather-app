# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual app code
COPY . .

# Expose FastAPI port
EXPOSE 8080

# Command to run FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
