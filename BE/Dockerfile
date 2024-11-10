# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY . .

# Expose the port that the backend will run on
EXPOSE 8000

# Run the FastAPI app (for example)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
