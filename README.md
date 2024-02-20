QA Test Report
Project Name: Instill QA Test
Repository Link: GitHub Repository
Introduction:
This QA Test Report provides an overview of the testing performed on the Instill QA Test project. The purpose of this report is to communicate the bugs found during testing, explain how to run the tests, and outline the test cases covered.
Test Environment:
* Python version: 3.10 or higher
* Operating System: Any supported by Python
Testing Approach:
The testing approach involves writing automated tests using pytest framework to validate the functionality of the API endpoints. The tests cover both synchronous and asynchronous behavior, test response time for a large number of words, and error handling for invalid input.
Bugs Found:
* 		Response Parsing Issue in Async Test: During testing, Pydantic encountered issues while trying to parse the response in the asynchronous test test_get_word_meanings_async. The cause of this issue needs further investigation as the response format may be incorrect.
* 		Empty Response Body in Valid Input Test: In the synchronous test test_get_word_meanings_sync_valid_input, the response body was empty when providing valid input. This suggests that the words used in the test may not have meanings available in the dictionary service.
How to Run the Tests:
* 		Clone the repository from the provided GitHub link.
* 		Navigate to the project directory in the terminal.
* 		(Optional) Create a new Python environment using Python 3.10 or higher.
* 		Install the required dependencies using the command: pip install -r requirements.txt
* 		Start the backend server using the command: python3 start_server.py
* 		Run all tests using the command: pytest
Test Cases Covered:
* 		test_get_word_meanings_async: Tests the asynchronous endpoint for retrieving word meanings.
* 		test_get_word_meanings_sync_invalid_input: Tests the synchronous endpoint for retrieving word meanings with invalid input.
* 		test_get_word_meanings_sync_valid_input: Tests the synchronous endpoint for retrieving word meanings with valid input.
* 		test_response_time_large_input: Tests the response time of the API for retrieving word meanings with a large number of words.
* 		test_invalid_input_error_handling: Tests the error handling of the API for invalid words or invalid JSON input.
Recommendations:
* 		Further investigate the response parsing issue in the asynchronous test to ensure correct response format.
* 		Verify the availability of meanings for the words used in the valid input test to address the empty response body.
Conclusion:
The automated tests provide comprehensive coverage of the API endpoints and functionality. However, further investigation and adjustments may be required to address the identified issues.


To run the tests using pytest and generate an HTML report, follow these steps:
* 		Install pytest:
* 		If you haven't already installed pytest, you can install it using pip:  Copy code pip install pytest   
* 		Clone the Repository:
* 		Clone the GitHub repository containing the Instill QA Test project. git clone 
* 		Navigate to Project Directory:
* 		Open a terminal and navigate to the directory where you cloned the repository.
* 		Install Dependencies:
* 		Install the required dependencies by running: pip install -r requirements.txt   
* 		Start the Backend Server:
* 		Run the backend server using the command:  python3 start_server.py or python start_server.py    This will start the backend server on http://0.0.0.0:8008.
* 		Run Tests with pytest:
* 		Execute the following command to run the tests and generate an HTML report:  pytest --html=report.html
  This command will run all the tests in the project and generate an HTML report named report.html.

* 		View Test Report:
* 		Once the tests have completed, you can view the HTML report by opening the report.html file in a web browser.
By following these steps, you can execute the tests using pytest and generate an HTML report to review the test results visually.

Pytest and Pytest Fixtures => 

Pytest is a testing tool for Python that makes it easy to write and organize test cases. It offers features like fixtures, parameterization, and plugins to simplify testing tasks and improve efficiency.
Fixtures in pytest are functions that set up the necessary conditions for tests, such as initializing objects or connecting to databases. They are defined with the @pytest.fixture decorator and help keep test code clean and reusable by separating setup and teardown logic from test code. Fixtures enhance organization and management of test dependencies.




