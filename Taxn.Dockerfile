# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY Taxn.py .

# Install any needed packages specified in requirements.txt
# Add the necessary packages for Taxn.py if any
RUN pip install pandas  # Example, if you need pandas

# Run Taxn.py when the container launches
CMD ["python", "Taxn.py"]
