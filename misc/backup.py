from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://rms.jobsdb.com/hk/en/empmycandidates/talent_search?Source=From%20Navigation%20Bar")

target_profiles = []

custom_keywords = "laboratory technician research assistant"
custom_industry_list = ["Laboratory", "Clinical", "Medical", "Science"]

def login():
    email = "recruitment@prenetics.com"
    password = "Prenetics2009"

    email_field = browser.find_element(By.NAME, "c_ErLnMnPeItDap_UrId0")
    password_field = browser.find_element(By.NAME, "c_ErLnMnPeItDap_Pd0")

    email_field.clear()
    password_field.clear()

    email_field.send_keys(email)
    password_field.send_keys(password, Keys.RETURN)


def wait(method, keywords):
    try:
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located(
                (method, keywords)
            )
        )
    finally:
        return

"""
def search_filter():
    wait(By.ID, "keywordInput")

    keyword_input = browser.find_element(By.CSS_SELECTOR, "input#keywordInput")
    keyword_input.send_keys(custom_keywords)

    job_function()
    last_activity()

    browser.find_element(By.CSS_SELECTOR, "a.ts-search-submit").click()

def job_function():
    browser.find_element(By.CSS_SELECTOR, "div#tsJobFunctionSelect a").click()

    wait(By.CSS_SELECTOR, "li#tsJobFunctionSelect-group_283 a")
    rnd_list = browser.find_element(By.CSS_SELECTOR, "#tsJobFunctionSelect-priOptionContain li#tsJobFunctionSelect-group_283 a")
    ActionChains(browser).move_to_element(rnd_list).click(rnd_list).perform()

    wait(By.CSS_SELECTOR, "input#tsJobFunctionSelect_283")
    browser.find_element(By.CSS_SELECTOR, "input#tsJobFunctionSelect_283").click()

    wait(By.CSS_SELECTOR, "div#tsJobFunctionSelect-topbar a.fancyselect-done.button.button-secondary")
    browser.find_element(By.CSS_SELECTOR, "div#tsJobFunctionSelect-topbar a.fancyselect-done.button.button-secondary").click()


def last_activity():
    browser.find_element(By.CSS_SELECTOR, "div.search-for-updated-time a").click()

    wait(By.CSS_SELECTOR, "div.search-for-updated-time div.singleselect-body")
    browser.find_element(By.CSS_SELECTOR, "div.search-for-updated-time li:nth-child(2) a").click()
"""

def search_results():
    # Get away with loadmask
    try:
        WebDriverWait(browser, 5).until(EC.invisibility_of_element((By.CLASS_NAME, "loadmask")))
    finally:
        profiles = browser.find_elements(By.CSS_SELECTOR, ".ts-result-tbl-container .candi-slip.ts-result-slip")
        for profile in profiles:
            searched_profile = individual_profile_search(profile)
            if searched_profile:
                target_profiles.append(profile)
        return nextPage()

def individual_profile_search(profile):
    try:
        buy_button = profile.find_element(By.CSS_SELECTOR, ".ts-tools-resume-unlock")
        if "Buy" in buy_button.text:
            
            if "day" in profile.find_element(By.CSS_SELECTOR, ".ts-slip-update").text:
                sentence = profile.find_element(By.CSS_SELECTOR, ".candi-slip-ind").text

                for industry in custom_industry_list:
                    if industry in sentence:
                        return True

    except:
        return False

def nextPage():
    try:
        current_page = browser.find_element(By.CSS_SELECTOR, ".rms-pagination-body li.current")
        next_page = current_page.find_element(By.XPATH, "./following-sibling::li//a").click()
        return search_results()
    except:
        print("No more next page")

def wait_for_download_loader():
    try:
        WebDriverWait(browser, 5).until(EC.invisibility_of_element((By.CLASS_NAME, "TB_wrapper")))
    finally:
        return

def download_profile(profile):
    wait_for_download_loader()
    browser.find_element(By.CSS_SELECTOR, ".fn-lyr-ts-resume-buy a#buyresume_btn").click()
    wait_for_download_loader()
    browser.find_element(By.CSS_SELECTOR, "div.fn-ts-resume-buy-action-prime a#buyresume_btn").click()
    wait_for_download_loader()
    browser.find_element(By.CSS_SELECTOR, "a.btnBatchDownload").click()
    browser.implicitly_wait(1)
    browser.find_element(By.CSS_SELECTOR, "div#iframeContentPageContainer a.btnCloseDialog").click()
    return

if __name__ == "__main__":
    login()
    search_filter()
    search_results()
    print(target_profiles.__len__())
    browser.quit()