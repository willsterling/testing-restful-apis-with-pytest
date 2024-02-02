REST API Test Automation demonstration 
written in

Python 3, py.test
This repo utilizes Testing Endpoints for restful-booker (https://restful-booker.herokuapp.com/) and Todo (https://todo.pixegami.io/) APIs.

Installation
Download Python 3.11 
Install Python from the downloaded package.
Clone the project, navigate to project directory from your terminal, run: pip3 install -r requirements.txt
To run all the test for both terminals, in the root directory run "python3 -m pytest".
To start tests from a terminal for either endpoint, inside the project folder "tests", run (1) pytest restful-booker_API_tests.py or (2) pytest swagger_todopixegami_API_tests.py, respectively.

Differences of demonstration between test files:
    restful-booker:
        validation testing of returned JSON data
        verfication testing of a complete JSON response using the Approval Test library

    todo:
        generation of unique payloads using uuid library

How to use the Approval Test library in this project:
        Upon first run of the test file, 1 of 8 tests should fail. The failed test is triggered by the library expecting to see a "Golden Master" in an approved text file that does not yet exists.In this context, the data stored as the "Golden Master" in the approved file should match the JSON data response of the API call. The file generated will be - "restful-booker_API_test.test_can_update_booking.received.txt". Rename this file to "restful-booker_API_test.test_can_update_booking.approved.txt". After renaming, when the test file is rerun, all 8 tests should pass. To change the expected response, approved files must be edited according to changes made in the data sent in the associated API requests. 

        I have configured the Approval Tests library to output the received and approved files to a separate subdirectory named "approved_files" (following the documentation written here: https://github.com/approvals/ApprovalTests.Python/blob/main/docs/configuration.md#examples).

Happy demo-ing!
