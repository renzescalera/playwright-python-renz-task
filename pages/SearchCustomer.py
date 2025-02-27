from playwright.sync_api import Page

class SearchCustomerPage:
    def __init__(self, page: Page):
        self.page = page

    def search_existing_customer(self, search_parameter):
        # Search for customer based on the given search parameter
        self.page.fill("input[ng-model='searchCustomer']", search_parameter)
        
    def validate_customer_in_table(self, expected_data):
        customer_table = self.page.locator('tbody .ng-scope')
        assert expected_data in customer_table.inner_text(), "Customer does not exists"