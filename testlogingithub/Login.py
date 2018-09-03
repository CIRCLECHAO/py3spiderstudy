import requests
from lxml import etree
from pyquery import PyQuery as pq


class Login(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        # selector = etree.HTML(response.text)
        # print(response.text)
        doc = pq(response.text)
        # token = selector.xpath('//div//input[@name="authenticity_token"]/@value')[0]
        token = doc('input[name="authenticity_token"]').val()
        print(token)
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            # print(response.text)
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        # print(html)
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
        for item in dynamics:
            dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)

    def profile(self, html):
        # selector = etree.HTML(html)
        # print(html)
        doc = pq(html)
        # name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        # email = selector.xpath('//select[@id="user_profile_email"]/option[@value=""]/text()')
        name = doc('#user_profile_name').val()
        email = doc('#user_profile_email').val()
        print(name, email)


if __name__ == "__main__":
    login = Login()
    login.login(email='circlechao@gmail.com', password='Lovey520')

