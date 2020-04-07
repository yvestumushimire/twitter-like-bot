# Twitter auto like
# Dev: YV3s

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class KwibukaBot:
    def __init__(self, email, password):
        self.email = email
        self.password= password
        self.bot = webdriver.Firefox()
    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login/")
        time.sleep(20)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(20)

    def like(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=%23' + hashtag + '&src=trend_click&f=live')
        time.sleep(20)
        for i in range(1,3):
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(20)
            tweets = bot.find_elements_by_css_selector('[data-testid="tweet"]')
            for tweet in tweets:
                # tweet.click()
                bot.find_element_by_css_selector('[data-testid="like"]').click()
                time.sleep(30)
                
                    





