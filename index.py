from time import sleep
from login import login
from talent_search import TalentSearchForm
from results_filtering import ResultFilter
from download_profile import ProfileDownloader

from selenium import webdriver

#options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome()
driver.set_window_size(1200, 800)


driver.get("r")

keyword_list = "Graphic Designer UI UX"
job_function_id = "283"
industry_list = ["Medical", "Science", "Laboratory"]

if __name__ == "__main__":
    login(driver)

    form = TalentSearchForm(driver)

    form.keywords(keyword_list)
    form.job_function(job_function_id)
    form.last_activity(1)

    form.yrs_of_exp(0, 20)

    form.submit()
    sleep(2)
    form.is_loading()

    filter = ResultFilter(driver)
    
    filter.wait_for_results()
    filter.wait_for_coin_balance()
    sleep(10)
    next_page = True

    while next_page is True:
        result_profiles = filter.get_results()

        print("Results Found: " + str(result_profiles.__len__()))

        for i, profile in enumerate(result_profiles):
            profile_can_buy = filter.can_purchase(profile)
            correct_industry = filter.is_correct_industry(profile, industry_list)

            if profile_can_buy and correct_industry:
                filter.moveTo(profile)
                print("Buying")
                filter.add_profile_to_cart(profile, i)
            
        downloader = ProfileDownloader(driver)
        footer = downloader.check_footer_visibility()
        if footer is True:
            downloader.open_buy_confirm_dialog()
            downloader.wait_for_iframe()

        print("Orange Button Ready To Click")

        input("Press any key to continue next page. Ctrl C to quit. ")

    driver.quit()