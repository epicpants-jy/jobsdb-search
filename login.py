from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(driver):

    email = "recruitment@prenetics.com"
    password = ""

    email_input = driver.find_element(By.NAME, "c_ErLnMnPeItDap_UrId0")
    password_input = driver.find_element(By.NAME, "c_ErLnMnPeItDap_Pd0")

    email_input.clear()
    password_input.clear()

    email_input.send_keys(email)
    password_input.send_keys(password, Keys.RETURN)

    return
