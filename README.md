# Infrastructure-Engineer-Task-

**test_pytest.py:**</br>
This file contains unit tests for the revenue calculation functions.
The tests are written using the unittest framework.
It includes mock data to simulate a CSV file and tests for calculating revenue per month, product, and customer.</br>

![image](https://github.com/user-attachments/assets/b015ddec-e116-4a56-94c2-6d961cab4596)


**Taxn.py:**</br>
This script is the main program for processing orders and calculating revenue metrics.
It reads a CSV file, calculates revenue for each row, and extracts the month from the order date.
It also calculates total revenue per month, per product, and per customer, and identifies the top 10 customers by revenue
Uses Docker Compose file format version 3.9.</br>

**Docker Compose:** Manages multi-container Docker applications.
Defines a service taxn with its build context and environment configuration in docker-compose-Taxn.yml.
Defines a service test_pytest with its build context in docker-compose-test_pytest.yml.</br>

**Dockerfile for Tests:** Prepares an isolated environment to run Python unit tests using unittest and pandas.
Base Image: Python 3.11-slim.
Working Directory: /usr/src/app.
Install Dependencies: Installs pandas.
Dockerfile for Main Application: Prepares an isolated environment to run the main application script (Taxn.py), ensuring all dependencies are installed and required files are copied into the container</br>

![image](https://github.com/user-attachments/assets/69e9bc23-8e22-46f0-957a-8000048a0e95)


This structure ensures a reproducible and isolated environment for both development and testing, leveraging Docker's containerization capabilities. The project can be built and run consistently across different environments, making it easier to manage dependencies and configurations. ​





