# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
VOLUME ["/app/file"]

COPY . /app
COPY . /app/token

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

VOLUME ["/app/token"]

# Run main.py when the container launches
ENTRYPOINT python3 main.py
