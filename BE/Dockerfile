# Step 1: Use Python image for backend
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt file to the container
COPY ./be/requirements.txt .

# Step 4: Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the entire backend code
COPY ./be/ .

# Step 6: Expose the backend port (adjust as per your backend's port)
EXPOSE 8000

# Step 7: Set the entry point (change if using a different framework like Flask/Django)
CMD ["python", "main.py"]
