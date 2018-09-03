from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as COptions
import time

EMAIL = '812773954@qq.com'
PASSWORD = 'Lovey520'


class CrackGeetest():
    def __init__(self):
        self.url = 'https://account.geetest.com/login'

        options = COptions()
        options.add_argument('-headless')
        self.browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe",
                                        chrome_options=options)
        # self.browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe")
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    # 获取到按钮
    def get_geetest_button(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    # 获取位置
    def get_position(self):
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'],\
                                   location['x'], location[x] + size['width']
        return top, bottom, left, right

    # 获取图片
    def get_image(self, name = 'captcha.png'):
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screen_shot = self.get_screen_shot()
        captcha = screen_shot.crop((top, bottom, left, right))
        return captcha

    # 获取滑块
    def get_slider(self):
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

