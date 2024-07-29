# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY pytest.py .

# Install any needed packages specified in requirements.txt
RUN pip install pytest

# Run pytest.py when the container launches
CMD ["pytest", "pytest.py"]
