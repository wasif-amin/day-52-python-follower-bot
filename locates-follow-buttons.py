from  selenium import webdriver
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  time
EMAIL = "day32.pythonudemycourse@gmail.com"
PASSWORD = "21070212"
USERNAME = "wasif_day52"

class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/chefsteps")
        wait = WebDriverWait(self.driver, 10)
        login  = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log In")))
        login.click()
        email = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        email.send_keys(EMAIL)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        not_now = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='button'][text()='Not now']")))
        not_now.click()

    def find_followers(self):
        wait = WebDriverWait(self.driver, 10)
        followers = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()=' followers']")))
        followers.click()

    def follow(self):
        time.sleep(3)
        all_buttons = self.driver.find_elements(By.XPATH, value="//button[.//div[text()='Follow']]")
        print(f"Located {len(all_buttons)} 'Follow' buttons on the screen.")



insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()
