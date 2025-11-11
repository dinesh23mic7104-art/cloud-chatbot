# Use a lightweight official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend folder (where app.py is)
COPY backend/ ./backend/

# Run FastAPI app inside backend folder
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
