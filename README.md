# Infrastructure-Engineer-Task-

**Taxn.py-:**</br>
The Taxn.py script processes a dataset (dataset.csv) using the Pandas library. Here’s a brief overview of what the script does:
Reads data from dataset.csv.
Processes the data using various Pandas operations.
Outputs the processed data or results.

![image](https://github.com/user-attachments/assets/b015ddec-e116-4a56-94c2-6d961cab4596)

**test_pytest.py:**</br>
This file contains unit tests for the revenue calculation functions.
The tests are written using the unittest framework.
It includes mock data to simulate a CSV file and tests for calculating revenue per month, product, and customer.</br>

**Docker Compose Files-->**
1. docker-compose-Taxn.yml
This file defines the main application service.

Version: 3.9
Services:
taxn:
Build Context: The current directory.
Dockerfile: Taxn.Dockerfile.
Container Name: taxn_container.
Volumes: Mounts the current directory to /home/kali/Desktop in the container.
Environment Variables: Sets PYTHONUNBUFFERED=1 to ensure that the output is not buffered (useful for logs).

2. docker-compose-test_pytest.yml
This file defines the testing service.

Version: 3.9
Services:
test_pytest:
Build Context: The current directory.
Dockerfile: test_pytest.Dockerfile.
Container Name: test_pytest_container.

**Dockerfiles-->**
1. Taxn.Dockerfile
This Dockerfile sets up the environment for running the main application script (Taxn.py).

Base Image: Python 3.11-slim.
Working Directory: /usr/src/app.
Copy Instructions: Copies the Taxn.py script and dataset.csv file into the container.
Install Dependencies: Installs pandas.
Command: Runs the Taxn.py script when the container starts.

2. test_pytest.Dockerfile
This Dockerfile sets up the environment for running tests using test_pytest.py.

Base Image: Python 3.11-slim.
Working Directory: /usr/src/app.
Copy Instructions: Copies the test_pytest.py script into the container.
Install Dependencies: Installs pandas and unittest2.
Command: Runs tests using unittest when the container starts.

![image](https://github.com/user-attachments/assets/69e9bc23-8e22-46f0-957a-8000048a0e95)

**Summary of the Project Architecture**

Multi-Container Setup
Managed by Docker Compose, the project defines services for both the main application and testing environments. Each service runs in its own container, ensuring isolated environments with all necessary dependencies installed.

Main Application: Defined in docker-compose-Taxn.yml and built using Taxn.Dockerfile.
Testing Environment: Defined in docker-compose-test_pytest.yml and built using test_pytest.Dockerfile.
Consistent Environments
Both development and testing environments are consistent across different machines and setups, thanks to Docker's containerization. This setup reduces issues related to dependency conflicts and configuration mismatches.

Ease of Management
Docker Compose simplifies the management of multi-container applications, making it easy to start, stop, and manage services. This setup ensures a reproducible and isolated environment for both development and testing, leveraging Docker's containerization capabilities.

This structure ensures a reproducible and isolated environment for both development and testing, leveraging Docker's containerization capabilities. The project can be built and run consistently across different environments, making it easier to manage dependencies and configurations. ​</br>

**How to Run the Project**</br>

Prerequisites</br>
Install Docker: Docker Installation Guide</br>
Install Docker Compose: Docker Compose Installation Guide</br>

**Commands**</br>
sudo docker-compose -f docker-compose-Taxn.yml build
sudo docker-compose -f docker-compose-Taxn.yml up</br>
incase of resetting container: sudo docker stop taxn_container && sudo docker rm taxn_container</br>
sudo docker logs taxn_container</br>
for test_pytest.py</br>
sudo docker build -f test_pytest.Dockerfile -t test_pytest_image . && sudo docker run --name pytest_container test_pytest_image</br>
incase of resetting comtainer: sudo docker stop pytest_container && sudo docker rm pytest_container</br>
sudo docker logs pytest_container</br>





