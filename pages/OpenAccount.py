from playwright.sync_api import Page

class OpenAccountPage:
    def __init__(self, page: Page):
        self.page = page

    def select_customer_and_currency(self, customer_name, currency):
        # Fill in the Add Customer form
        self.page.click('#userSelect')
        self.page.select_option('select[ng-model="custId"]', label=customer_name)
        self.page.click('.mainhdr')
        
        self.page.click('#currency')
        self.page.select_option('select[ng-model="currency"]', label=currency)
        self.page.click('.mainhdr')

    def click_process_button(self):
        # Click the submit button
        self.page.click('[type="submit"]')