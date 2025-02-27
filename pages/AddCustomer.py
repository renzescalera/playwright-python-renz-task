from playwright.sync_api import Page

class AddCustomerPage:
    def __init__(self, page: Page):
        self.page = page

    def add_new_customer(self, first_name, last_name, postal_code):
        # Fill in the Add Customer form
        self.page.fill("input[ng-model='fName']", first_name)
        self.page.fill("input[ng-model='lName']", last_name)
        self.page.fill("input[ng-model='postCd']", postal_code)
        
        # Click the submit button
        self.page.click('[type="submit"]')