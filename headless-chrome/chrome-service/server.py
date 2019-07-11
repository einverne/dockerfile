#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from flask import Flask
from flask import request, jsonify, make_response
from selenium import webdriver

app = Flask(__name__)


def rest_response(code, reason=None, content=None):
    return {
        "code": code,
        "reason": reason,
        "content": content
    }


@app.route("/")
def home():
    return "hello world"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('disable-gpu')
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument("proxy-server=")
chrome_options.add_argument('window-size=1280x800')
chrome_options.add_argument('--dns-prefetch-disable')


@app.route("/html", methods=['POST'])
def html():
    if request.is_json:
        url = request.get_json(silent=True)['url']
    else:
        url = request.form['url']
    if not url:
        print("url is empty")
        return json.dumps(rest_response(3001, "url is empty"))
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',
                              chrome_options=chrome_options)
    driver.set_page_load_timeout(10)
    driver.set_script_timeout(5)
    driver.get(url)
    driver.delete_all_cookies()
    driver.implicitly_wait(2)
    page_source = driver.page_source
    driver.close()
    return make_response(jsonify(rest_response(200, content=page_source)), 200)


@app.route("/screenshot", methods=['POST'])
def screenshot():
    if request.is_json:
        url = request.get_json(silent=True)['url']
    else:
        url = request.form['url']
    if not url:
        print("url is empty")
        return "url is empty"
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',
                              chrome_options=chrome_options)
    driver.set_page_load_timeout(10)
    driver.set_script_timeout(5)
    driver.get(url)
    shot_base64 = driver.get_screenshot_as_base64()
    driver.close()
    return make_response(jsonify(rest_response(200, content=shot_base64)), 200)


if __name__ == '__main__':
    app.run(port=9233, host='0.0.0.0')