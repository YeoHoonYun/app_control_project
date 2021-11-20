#!/usr/bin/env python
# coding: utf-8
import time
import unittest
from appium import webdriver


def reservation_join():
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[1]/android.view.View[@index="0"]/android.widget.Button').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.TextView[@index="0"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[@index="0"]/android.view.View[3]/android.widget.EditText[@index="1"]').send_keys(
        ID)
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[@index="0"]/android.view.View[4]/android.widget.EditText[@index="1"]').send_keys(
        PW)
    driver.find_elements_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[@index="0"]/android.view.View[6]/android.view.View[@index="0"]')[
        0].click()
    time.sleep(1)
    driver.find_elements_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.widget.ListView[2]/android.view.View[1]/android.view.View')[
        0].click()
    time.sleep(7)

def reservation_config():
    # 버스/시간 설정
    t = driver.find_elements_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.widget.ListView[@index="1"]//android.view.View')[
        2]
    time.sleep(3)
    print(driver.page_source)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[4]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.view.View[3]/android.view.View[@index="0"]//android.view.View[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[4]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.view.View[6]/android.view.View[@index="0"]').click()
    time.sleep(2)
    # 출발지 설정
    s = driver.find_elements_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.widget.ListView[@index="1"]//android.view.View')[
        3]
    s.click()
    time.sleep(2)
    driver.find_elements_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[4]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.view.View[3]/android.view.View[@index="0"]/android.view.View')[
        1].click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[4]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.view.View[5]/android.view.View[@index="0"]').click()
    time.sleep(1)
    # 도착지 설정
    e = driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.widget.ListView[@index="1"]/android.view.View[3]/android.view.View[@index="0"]/android.view.View[@index="0"]')
    time.sleep(2)
    driver.find_elements_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[4]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.view.View[3]/android.view.View[@index="0"]//android.view.View')[
        1].click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[4]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.view.View[5]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.widget.TextView').click()
    time.sleep(2)

def reservation_process():
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[2]/android.widget.ListView[@index="0"]/android.view.View[2]/android.view.View[@index="0"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[1]/android.view.View[@index="0"]/android.widget.GridView[@index="0"]/android.view.View[5]//android.view.View[5]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[2]//android.widget.Button[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[3]/android.widget.ListView[@index="0"]/android.view.View[2]/android.view.View[@index="0"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.view.View[3]//android.view.View[1]').click()
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.view.View[1]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.widget.ListView[@index="3"]/android.view.View[%s]/android.widget.Button[@index="0"]' % NUM).click()
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.view.View[2]//android.widget.Button[2]').click()
    driver.find_element_by_xpath(
        '/hierarchy[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.LinearLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.widget.FrameLayout[@index="0"]/android.webkit.WebView[@index="0"]/android.webkit.WebView[@index="0"]/android.view.View[@index="0"]/android.view.View[2]/android.view.View[@index="0"]/android.view.View[@index="0"]/android.view.View[3]//android.view.View[1]').click()

#사용자 정보
ID = "cjswo9207@naver.com"
PW = "0rhk@tkdl#"
NUM = 43

# 실행 디바이스 정보
desired_caps = dict(
    platformName='Android',
    platformVersion='11',
    # automationName='miniplus_auto',
    deviceName='Android Emulator',
    app='C:\\Users\\tlsot\IdeaProjects\\app_control_project\\MiRi플러스_v3.8_apkpure.com.apk'
)
# 실행
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)

# 가입
reservation_join()

#예약 설정
reservation_config()

# 예약 프로세스
reservation_process()

#앱 종료
driver.close_app()