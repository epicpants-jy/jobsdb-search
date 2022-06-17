from time import sleep
from misc.util import wait_for_element_disappear, wait_for_element_presence

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TalentSearchForm:

    css_selector = {
        "search_form": ".fn-ts-search-body",
        "keyword_input": "input#keywordInput",
        "years_of_exp": ".search-for-yrs-of-exp"
    }

    def __init__(self, driver):
       self.driver = driver
       
    def keywords(self, phrase):
        try:
            wait_for_element_presence(self.driver, By.CSS_SELECTOR, "{} {}".format(self.css_selector['search_form'], self.css_selector['keyword_input']))

            keywords_input = self.driver.find_element(By.CSS_SELECTOR, "{} {}".format(self.css_selector['search_form'], self.css_selector['keyword_input']))
            keywords_input.send_keys(phrase)
            return

        except:
            return

    def yrs_of_exp(self, min, max):
        input_group = self.driver.find_element(By.CSS_SELECTOR, "{} {}".format(
            self.css_selector['search_form'],
            self.css_selector['years_of_exp']
        ))
        activate = input_group.find_element(By.CSS_SELECTOR, "a.pillow-element.pillow-element-arrow-south")

        min_value_handle = input_group.find_element(By.CSS_SELECTOR, ".noUi-handle-lower")
        max_value_handle = input_group.find_element(By.CSS_SELECTOR, ".noUi-handle-upper")

        actions = ActionChains(self.driver)
        actions.click(activate)
        actions.drag_and_drop_by_offset(min_value_handle, min * (306 * 0.047619), 0).release()
        actions.drag_and_drop_by_offset(max_value_handle, (21 - max) * (306 * -0.047619), 0).release()
        actions.perform()

        return

    def job_function(self, index):
        self.driver.find_element(By.CSS_SELECTOR, "div#tsJobFunctionSelect a").click()

        wait_for_element_presence(self.driver, By.CSS_SELECTOR, "li#tsJobFunctionSelect-group_{} a".format(index))
        rnd_list = self.driver.find_element(By.CSS_SELECTOR, "#tsJobFunctionSelect-priOptionContain li#tsJobFunctionSelect-group_{} a".format(index))
        ActionChains(self.driver).move_to_element(rnd_list).click(rnd_list).perform()

        wait_for_element_presence(self.driver, By.CSS_SELECTOR, "input#tsJobFunctionSelect_{}".format(index))
        self.driver.find_element(By.CSS_SELECTOR, "input#tsJobFunctionSelect_{}".format(index)).click()

        wait_for_element_presence(self.driver, By.CSS_SELECTOR, "div#tsJobFunctionSelect-topbar a.fancyselect-done.button.button-secondary")
        self.driver.find_element(By.CSS_SELECTOR, "div#tsJobFunctionSelect-topbar a.fancyselect-done.button.button-secondary").click()

        return

    def last_activity(self, index):
        input_group = self.driver.find_element(By.CSS_SELECTOR, "div.search-for-updated-time")


        input_group.find_element(By.CSS_SELECTOR, "a.pillow-element.pillow-element-arrow-south").click()
        wait_for_element_presence(self.driver, By.CSS_SELECTOR, "div.search-for-updated-time .singleselect-body")

        input_group.find_element(By.CSS_SELECTOR, ".singleselect-body menu.selector-main li:nth-child({}) a".format(index)).click()

        return


    def submit(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "menu.ts-search-ctrl li a.ts-search-submit").click()
        except:
            print("Error in submit search button")
            return


    def is_loading(self):
        wait_for_element_disappear(self.driver, By.CSS_SELECTOR, ".loadmask")

