# Instill QA Test

This repository contains tests for the Instill QA Test project. The tests are designed to evaluate the functionality and behavior of the backend API.

## Overview

The project includes tests written using the pytest framework to assess various aspects of the backend API, including:

- Testing the asynchronous and synchronous endpoints for retrieving word meanings.
- Evaluating the response time of the API for large inputs.
- Testing the error handling of the API for invalid input.

## How to Run Tests

To run the tests, follow these steps:

1. Clone the repository to your local machine. => git clone https://github.com/VetrivelDhanavel/Instill_Assessment.git
2. Ensure that Python and pip are installed on your system.
3. Install the required dependencies by running:  pip install -r requirements.txt

4. Start the backend server by running: python start_server.py or python3 start_server.py 

5. Open a terminal and navigate to the project directory.
6. Run the tests using pytest by executing the following command: pytest --html=report.html
This command will run an test file and generate an HTML report of the test results. 


## Test Cases

### Test Cases Covered:

1. **Test asynchronous endpoint**: This test checks the functionality of the asynchronous endpoint for retrieving word meanings.
2. **Test synchronous endpoint with invalid input**: This test evaluates the error handling of the synchronous endpoint for invalid input.
3. **Test synchronous endpoint with valid input**: This test verifies the behavior of the synchronous endpoint with valid input.
4. **Test response time for large input**: This test assesses the response time of the API when retrieving word meanings with a large number of words.
5. **Test error handling for invalid input**: This test checks the API's error handling for invalid JSON input and invalid words.

## Pytest and Fixtures

Pytest is a testing framework for Python that simplifies the process of writing and organizing test cases. It provides features like fixtures, parameterization, and plugins to streamline testing tasks.

Fixtures in pytest are functions that provide a fixed baseline for tests. They set up necessary preconditions for tests, such as initializing objects or connecting to databases. Fixtures help keep test code clean, modular, and reusable by separating setup and teardown logic from test code.

For more information about pytest and fixtures, refer to the [https://docs.pytest.org/en/8.0.x/](https://docs.pytest.org/en/latest/) and [fixture documentation](https://docs.pytest.org/en/latest/fixture.html).

## Contributors

- [vetrivel] (https://github.com/VetrivelDhanavel)
