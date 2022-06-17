from telnetlib import EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element_presence(browser, method, keywords):
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((
                method,
                keywords
            ))
        )
    finally:
        return

def wait_for_element_disappear(browser, method, keywords):
    try:
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element((
                method,
                keywords
            ))
        )
    finally:
        return