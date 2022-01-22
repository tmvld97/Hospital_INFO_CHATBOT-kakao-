
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def location_url(start="포천시", dst="신읍동 243-1번지") :
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://map.naver.com/v5/directions/-/-/-/transit?c=14100056.2429646,4528662.3699081,15,0,0,0,dh")
    elem = driver.find_element_by_css_selector("#directionStart0")
    elem.send_keys(start)
    elem.send_keys(Keys.RETURN)
    sleep(0.2)
    goal = driver.find_element_by_css_selector("#directionGoal1")
    goal.send_keys(dst)
    goal.send_keys(Keys.RETURN)
    sleep(0.2)
    driver.find_element_by_xpath("//*[@id='container']/shrinkable-layout/div/directions-layout/directions-result/div[1]/div/directions-search/div[2]/button[2]").click()
    sleep(0.1)
    url = driver.current_url
    return url

print(location_url())