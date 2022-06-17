from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from download_profile import ProfileDownloader
from results_filtering import ResultsFiltering
from talent_search import TalentSearchForm
from login import login

browser = webdriver.Chrome()
browser.get("https://rms.jobsdb.com/hk/en/empmycandidates/talent_search?Source=From%20Navigation%20Bar")

custom_keywords = "laboratory technician research assistant"
custom_industry_list = ["Laboratory", "Clinical", "Medical", "Science"]

if __name__ == "__main__":
    login(browser)
    setup_search_form = TalentSearchForm(browser, custom_keywords)
    setup_search_form.run()

    filter_result = ResultsFiltering(browser, ["Laboratory", "Midical", "Science"])
    filter_result.run()

    browser.quit()

