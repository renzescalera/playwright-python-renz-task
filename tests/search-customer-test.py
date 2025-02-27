import json
import pytest
from playwright.sync_api import sync_playwright
from pages.AddCustomer import AddCustomerPage
from pages.SearchCustomer import SearchCustomerPage

BASE_URL="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

# Fixture to load the test data from the customer-data.json file
@pytest.fixture(scope="module")
def load_customer_data():
    # Load the data from the JSON file
    with open('fixtures/customer-data.json', 'r') as f:
        data = json.load(f)
    return data

def test_search_customer_with_first_name(load_customer_data):
    with sync_playwright() as p:
        # Launch the browser and open the page
        browser = p.chromium.launch(headless=False)  # headless=False opens the browser so you can see it
        page = browser.new_page()
        add_customer = AddCustomerPage(page)
        search_customer = SearchCustomerPage(page)
        
        # Access customer data from the fixture
        CUSTOMER_FIRST_NAME = load_customer_data['FIRST_NAME']
        CUSTOMER_LAST_NAME = load_customer_data['LAST_NAME']
        CUSTOMER_POSTAL_CODE = load_customer_data['POSTAL_CODE']
        
        # Navigate to the Add Customer page
        page.goto(f"{BASE_URL}/addCust")

        # Add new customer 
        add_customer.add_new_customer(CUSTOMER_FIRST_NAME, CUSTOMER_LAST_NAME, CUSTOMER_POSTAL_CODE)
        
        # Navigate to the Search Customer page
        page.goto(f"{BASE_URL}/list")  
        
        # Search customer
        search_customer.search_existing_customer(CUSTOMER_FIRST_NAME)
        
        # Validate retrieved customer
        search_customer.validate_customer_in_table(CUSTOMER_FIRST_NAME)
        
        # Close the browser
        browser.close()