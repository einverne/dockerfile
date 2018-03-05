#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time

import pychrome
from bs4 import BeautifulSoup


class EventHandler(object):
    screen_lock = threading.Lock()

    def __init__(self, browser, tab):
        self.browser = browser
        self.tab = tab
        self.start_frame = None
        self.html_content = None
        self.is_first_request = True

    def frame_start_loading(self, frameId):
        if not self.start_frame:
            self.start_frame = frameId

    def request_intercepted(self, interceptionId, request, **kwargs):
        if self.is_first_request:
            self.is_first_request = False
            headers = request.get('headers', {})
            self.tab.Network.continueInterceptedRequest(
                interceptionId=interceptionId,
                headers=headers,
                method='POST',
                postData="hello post data: %s" % time.time()
            )
        else:
            self.tab.Network.continueInterceptedRequest(
                interceptionId=interceptionId
            )

    def frame_stop_loading(self, frameId):
        if self.start_frame == frameId:
            self.tab.Page.stopLoading()
            result = self.tab.Runtime.evaluate(expression="document.documentElement.outerHTML")
            self.html_content = result.get('result', {}).get('value', "")
            print self.html_content
            self.tab.stop()


def close_all_tabs(browser):
    if len(browser.list_tab()) == 0:
        return
    for tab in browser.list_tab():
        try:
            tab.stop()
        except pychrome.RuntimeException:
            pass

        browser.close_tab(tab)
    assert len(browser.list_tab()) == 0


def perform_click(browser):
    tab = browser.new_tab()

    # def loading_finished(**kwargs):
    #     print "[loading finished]"
    #
    # # when HTTP request has finished loading
    # tab.set_listener("Network.loadingFinished", loading_finished)

    tab.start()

    # call method
    # tab.Network.enable()
    tab.Network.enable()
    tab.Page.enable()
    tab.Runtime.enable()

    def dom_content_event_fired(**kwargs):
        print "[content] dom content event fired"
        tab.DOM.enable()
        root = tab.DOM.getDocument()
        root_node_id = root.get('root', {}).get('nodeId', '')
        # 找到输入框
        input_box = tab.DOM.querySelector(nodeId=root_node_id, selector='#kw')
        # tab.DOM.setNodeValue(nodeId=input_box, value='hello')
        tab.Runtime.evaluate(expression='document.getElementById("kw").value="Chrome"', )
        # 找到搜索按钮
        search_btn = tab.DOM.querySelector(nodeId=root_node_id, selector='#su')
        remote_node = tab.DOM.resolveNode(nodeId=search_btn.get('nodeId', ''))
        # 执行点击
        tab.Runtime.callFunctionOn(functionDeclaration='(function() { this.click(); })',
                                   objectId=remote_node.get('object', {}).get('objectId', {}))
        tab.wait(3)
        # 输出结果
        html = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")
        html_value = html.get('result', {}).get('value', '').encode('utf-8')
        soup = BeautifulSoup(html_value, 'html.parser')
        l = soup.select('h3 > a')
        for result in l:
            print result.text
            print result['href']

        screen_base64 = tab.call_method("Page.captureScreenshot")
        image_data = screen_base64.get('data', '')
        with open("test.png", 'wb') as f:
            f.write(image_data.decode('base64'))

        # tab.DOM.performSearch(query='xpath', includeUserAgentShadowDOM=True)
        # stop the tab (stop handle events and stop recv message from chrome)
        tab.stop()

        # close tab
        browser.close_tab(tab)

    tab.set_listener("Page.domContentEventFired", dom_content_event_fired)

    # 刷新当前页面，ignoreCache 是否忽略cache，如果为 true，则强行刷新，类似于 Shift+refresh
    # tab.call_method("Page.reload", ignoreCache=False)
    tab.call_method("Page.navigate", url='https://www.baidu.com', _timeout=5)
    tab.wait(20)


def get_html(browser, url):
    tab = browser.new_tab()
    tab.start()
    tab.call_method('Page.navigate', url=url, _timeout=5)
    tab.wait(10)
    html = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")
    tab.stop()
    browser.close_tab(tab)
    return html['result']['value']


def get_cookies(tab):
    all = tab.Network.getAllCookies()
    return all


def screenshot(tab):
    screen_base64 = tab.call_method("Page.captureScreenshot")
    image_data = screen_base64.get('data', '')
    with open("test.png", 'wb') as f:
        f.write(image_data.decode('base64'))


def screenshot(browser, url, filename='image.png'):
    tab = browser.new_tab()
    tab.start()
    tab.call_method('Page.navigate', url=url, _timeout=5)
    tab.wait(10)
    # 截取当前Tab屏幕，结果为图片内容Base64
    screen_base64 = tab.call_method("Page.captureScreenshot")
    image_data = screen_base64.get('data', '')
    with open(filename, 'wb') as f:
        f.write(image_data.decode('base64'))
    tab.stop()
    browser.close_tab(tab)


def print_to_pdf(browser, url, filename='file.pdf'):
    tab = browser.new_tab()
    tab.start()
    tab.call_method('Page.navigate', url=url, _timeout=5)
    tab.wait(10)
    pdf_data = tab.call_method('Page.printToPDF', landscape=False).get('data')
    with open(filename, 'wb') as f:
        f.write(pdf_data.decode('base64'))
    tab.stop()
    browser.close_tab(tab)


def demo(browser):
    print browser.version()

    # create a tab
    tab = browser.new_tab()

    # register callback
    def request_will_be_sent(**kwargs):
        print("[start] start loading: %s" % kwargs.get('request').get('url'))

    tab.set_listener("Network.requestWillBeSent", request_will_be_sent)

    def received_callback(**kwargs):
        print "[received] response type %s" % kwargs.get('type', '')
        resp = kwargs.get('response', {})
        resp_status = resp.get('status', '')
        resp_headers = resp.get('headersText')
        # print "response status %s %s" % (resp_status, resp_headers)

    tab.set_listener("Network.responseReceived", received_callback)

    def frame_stop_loading():
        print "frame stop loading"

    tab.set_listener("Page.frameStoppedLoading", frame_stop_loading)

    # def loading_finished(**kwargs):
    #     print "[loading finished]"
    #
    # # when HTTP request has finished loading
    # tab.set_listener("Network.loadingFinished", loading_finished)

    # start the tab
    tab.start()

    # call method
    # tab.Network.enable()
    net = tab.call_method("Network.enable")
    tab.call_method("Page.navigate", url='https://www.douban.com', _timeout=5)
    tab.stop()
    browser.close_tab(tab)


def perform_input(browser):
    """向下浏览页面"""
    tab = browser.new_tab()
    tab.start()
    tab.Page.enable()
    tab.Page.navigate(url='https://www.douban.com/', _timeout=5)
    tab.wait(5)
    # 更多 keycode 可以参考 https://msdn.microsoft.com/en-us/library/dd375731(VS.85).aspx
    keycode = int(0x22)
    tab.Input.dispatchKeyEvent(type='keyDown', windowsVirtualKeyCode=keycode, nativeVirtualKeyCode=keycode)
    tab.wait(3)
    screen_base64 = tab.call_method("Page.captureScreenshot")
    image_data = screen_base64.get('data', '')
    with open("keyDown.png", 'wb') as f:
        f.write(image_data.decode('base64'))
    tab.stop()
    browser.close_tab(tab)


if __name__ == '__main__':
    # create a browser instance
    browser = pychrome.Browser(url="http://127.0.0.1:9222")
    # demo(browser)
    # perform_click(browser)
    # screenshot(browser, 'http://www.einverne.info', 'screenshot.png')
    # print_to_pdf(browser, 'http://www.einverne.info', 'filename.pdf')
    perform_input(browser)
