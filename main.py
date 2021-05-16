import time
from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
similar_account = "homecookingshow"  # sample
INSTAGRAM_USERNAME = "_express_eats_105"  # sample
INSTAGRAM_PASSWORD = "YOU_PASSWORD"


class InstaFollower:
    def __init__(self, driver):
        self.driver = webdriver.Chrome(executable_path=driver)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        user_name = self.driver.find_element_by_name('username')
        user_name.send_keys(INSTAGRAM_USERNAME)
        password = self.driver.find_element_by_name('password')
        password.send_keys(INSTAGRAM_PASSWORD)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        time.sleep(2)
        save_info = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        save_info.click()
        time.sleep(2)
        notification_not_now = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification_not_now.click()

    def find_followers(self):
        self.driver.get('https://www.instagram.com/homecookingshow/')
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)

    def follow(self):
        n = 0
        while n < 1000:
            find_follow_buttons = self.driver.find_elements_by_css_selector(".PZuss button")
            for i in range(n, len(find_follow_buttons)):
                if find_follow_buttons[i].text == "Follow":
                    find_follow_buttons[i].click()
                n += 1
                time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)


insta_follower = InstaFollower(chrome_driver_path)
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()
