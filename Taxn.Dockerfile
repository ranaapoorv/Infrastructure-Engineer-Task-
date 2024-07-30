# Taxn.Dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Taxn.py script into the container
COPY Taxn.py .

# Copy the CSV file into the container (assuming it is in the same directory as the Dockerfile)
COPY orders2.csv .

# Install any needed packages specified in requirements.txt
# If you need to install pandas or other packages, include them in requirements.txt
RUN pip install pandas

# Run the Taxn.py script when the container starts
CMD ["python", "Taxn.py"]
