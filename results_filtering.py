from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from misc.util import wait_for_element_presence

class ResultFilter:

    css_selectors = {
        "container": ".ts-result-tbl-container",
        "result": ".candi-slip.ts-result-slip",
        "coin_balance": ".ts-coins-balance-txt var.ng-binding"
    }

    def __init__(self, driver):
        self.driver = driver

    def wait_for_results(self):
        try:
            wait_for_element_presence(self.driver, By.CSS_SELECTOR, self.css_selectors['container'])

            section_container = self.driver.find_element(By.CSS_SELECTOR, self.css_selectors['container'])

            all_profiles = section_container.find_elements(By.CSS_SELECTOR, ".ts-result-slip")
            
            if all_profiles.__len__():
                return True
        except:
            return False

    def wait_for_coin_balance(self):
        try:
            wait_for_element_presence(self.driver, By.CSS, self.css_selectors['coin_balance'])

            if (self.driver.find_element(By.CSS_SELECTOR, self.css_selectors['coin_balance'])):
                return True
            return False
        except:
            return False

    def get_results(self):
        try:
            container = self.driver.find_element(By.CSS_SELECTOR, self.css_selectors['container'])

            return container.find_elements(By.CSS_SELECTOR, self.css_selectors['result'])
        except:
            return []

    def moveTo(self, profile):
        ActionChains(self.driver).move_to_element(profile).perform()

    def can_purchase(self, profile):
        try:
            profile.find_element(By.CSS_SELECTOR, ".candi-slip-tools a.ts-tools-resume-unlock")
            return True
        except:
            return False

    def is_correct_industry(self, profile, phrases):
        try:
            if phrases.__len__() > 0:
                industry_text = profile.find_element(By.CSS_SELECTOR, ".candi-slip-bdy.ts-slip-bdy-curind p.candi-slip-ind")

                for industry in phrases:
                    if industry in industry_text.text:
                        return True
            else:
                return True
                
            return False

        except:
            return False

    def add_profile_to_cart(self, profile, index):
        checkbox = profile.find_element(By.CSS_SELECTOR, "{} {}:nth-of-type({}) .candi-slip-bdy .candi-applicant-selector input.ts-slip-checkbox".format(self.css_selectors['container'], self.css_selectors
        ['result'], index+1))
        ActionChains(self.driver).move_to_element(checkbox).click(checkbox).perform()
        