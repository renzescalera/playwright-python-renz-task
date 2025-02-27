## Overview

- In this repository I, Renz Escalera, would like to showcase my skills in test automation using Playwright as test automation framework and Python as the programming language. In each test cases under the tests folder, I used Page-Object Model that are stored in classes to seamlessly build readable, maintainable, and scalable code. This is inspired by the D.R.Y (Don't Repeat Yourself) principle. Moreover, I used JSON object as a static test data which is stored in `fixtures/customer-data.json`. In this way, I can easily change the test data in a one place which is used in each test cases.

- Furthermore, these approaches are the best practice for code reusability and separating test data and test logic.

## Folder/Files Structure

1.  **tests**: Contains the spec files or test frameworks built with Playwright using python.

    - `add-customer-test.py`
    - `open-account-test.py`
    - `search-customer-test.cy.js`

2.  **fixtures**: Storage of the static data files which is in JSON format.

    - `customer-data.json` - This contains the test data for creating new customer, opening account, and search. Moreover this is used for data validation.

3.  **pages**: This contains the Classes for each pages used for e2e tests and its functions.

## Setting Up and Running Playwright with Python Tests

1. Clone the repository using the command: `git clone https://github.com/renzescalera/playwright-python-renz-task.git`

2. Navigate to the project folder - Example: `cd C:\users\your-computer\playwright-python-renz-task`

3. Activate Virtual Environment using the command: `venv\Scripts\activate`

4. Install dependencies using the following command:

   - `pip install playwright pytest`
   - `playwright install`

5. Run the test using the following commands:

   - add-customer test:`pytest tests/add-customer-test.py`
   - open-account test:`pytest tests/open-account-test.py`
   - search-customer test:`pytest tests/search-customer-test.py`
