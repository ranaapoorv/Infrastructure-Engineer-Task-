# test_pytest.Dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the test script into the container
COPY test_pytest.py .

# Install dependencies
RUN pip install pandas unittest2

# Run the tests when the container starts
CMD ["python", "-m", "unittest", "test_pytest"]
