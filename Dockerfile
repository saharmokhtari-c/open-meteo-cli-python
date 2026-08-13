# 1. Use the base image requested by the professor
FROM python:3.13-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# 4. Install Python dependencies without saving cache to reduce image size 
RUN pip install --no-cache-dir -r requirements.txt 

# 5. Copy the rest of the weather project files into the /app directory 
COPY . .

# 6. Command to start the application

ENTRYPOINT ["python", "main.py"]