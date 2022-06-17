from selenium.webdriver.common.by import By

from misc.util import wait_for_element_presence


class ProfileDownloader:

    css_selector = {
        "footer": ".fn-ts-results-batch-body",
        "batch_buy": "menu.ts-results-batch-menu a.ts-results-batch-item.batch-buy",
        "iframe": "iframe#TB_iframeContent"
    }

    def __init__(self, driver):
        self.driver = driver

    def check_footer_visibility(self):
        try:
            wait_for_element_presence(self.driver, By.CSS_SELECTOR, "{} {}".format(
                self.css_selector['footer'],
                self.css_selector['batch_buy']
            ))
            self.driver.find_element(By.CSS_SELECTOR, "{} {}".format(
                self.css_selector['footer'],
                self.css_selector['batch_buy']
            ))

            return True
        except:
            return False

    def open_buy_confirm_dialog(self):
        self.driver.find_element(By.CSS_SELECTOR, "{} {}".format(
            self.css_selector['footer'],
            self.css_selector['batch_buy']
        )).click()

    def wait_for_iframe(self):
        wait_for_element_presence(self.driver, By.CSS_SELECTOR, self.css_selector['iframe'])