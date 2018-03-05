#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_jd_price(driver):
    driver.get("https://item.jd.com/5218185.html")
    # wait up to 10 seconds for the elements to become available
    driver.implicitly_wait(10)

    price = driver.find_element_by_class_name("p-price")
    driver.implicitly_wait(10)
    print price.text
    driver.implicitly_wait(10)
    driver.page_source  # 获取源代码
    return price.text


def search(driver):
    driver.get("http://www.douban.com")
    driver.implicitly_wait(10)
    search_ele = driver.find_element_by_name('q')
    search_ele.send_keys("call me")
    search_ele.send_keys(Keys.ENTER)
    driver.save_screenshot('screenshot.png')
    # driver.get_screenshot_as_file('main-page.png')


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.binary_location = '/usr/bin/google-chrome-stable'
    chromedriver_path = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver_path)

    get_jd_price(driver)
    search(driver)
    driver.close()

    # # use css selectors to grab the login inputs
    # email = driver.find_element_by_css_selector('input[type=email]')
    # password = driver.find_element_by_css_selector('input[type=password]')
    # login = driver.find_element_by_css_selector('input[value="Log In"]')
    #
    # driver.find_element_by_xpath('//*[@id="_ctl0__ctl0_LoginLink"]').click()
    #
    # email.send_keys('evan@intoli.com')
    # password.send_keys('hunter2')
    # driver.get_screenshot_as_file('main-page.png')
    # # login
    # login.click()
    #
    # # navigate to my profile
    # driver.get('https://www.facebook.com/profile.php?id=100009447446864')
    #
    # # take another screenshot
    # driver.get_screenshot_as_file('evan-profile.png')
    # posts = driver.find_elements_by_css_selector('#stream_pagelet .fbUserContent')
    # for post in posts:
    #     try:
    #         author = post.find_elements_by_css_selector('a[data-hovercard*=user]')[-1].get_attribute('innerHTML')
    #         content = post.find_elements_by_css_selector('div.userContent')[-1].get_attribute('innerHTML')
    #     except IndexError:
    #         # it's an advertisement
    #         pass
    #     print(f'{author}: "{content}"')
