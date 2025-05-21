# Use python:3.13-slim as the base image
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Install uv pip
RUN pip install uv

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies using uv
RUN uv pip install --system -r requirements.txt

# Copy the application and test files into the container
COPY time_server.py .
COPY test_time_server.py .

# Set the default command to run the server
CMD ["python", "time_server.py"]
