# Use an official Python 3.13 runtime as a parent image
FROM python:3.13

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for packages that need compiling (e.g., cryptography)
RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev

# Copy only the requirements.txt first, and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app/

# Make port 80 available to the world outside this container
EXPOSE 80

# Run main.py when the container launches
CMD ["python", "main.py"]
