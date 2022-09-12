from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from phrasal_verbs.models import PhrasalVerb


class FloSpider:

    def __init__(self, level, url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = f'https://www.flo-joe.co.uk/{level}/students/wordbank{url}'.format(level=level, url=url)
        self.form_xpath = '//div[contains(@class, "col-md-6 col-md-push-3")]/form/p'
        self.title_xpath = '//div[contains(@class, "col-md-6 col-md-push-3")]/h4'

    def __find_element_xpath(self, xpath, attribute='text'):
        if attribute == 'value':
            return self.driver.find_element(By.XPATH, xpath).get_attribute('value')

        return self.driver.find_element(By.XPATH, xpath).text

    def __find_elements_xpath(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def __execute_btn_score(self):
        score_btn = self.driver.find_element(By.XPATH, '//input[@type="button"][@name="button"]')
        self.driver.execute_script("arguments[0].click();", score_btn)

    def __use_url(self):
        self.driver.get(self.base_url)

    def check_form_type(self):
        self.__use_url()
        self.__execute_btn_score()

        form = self.__find_elements_xpath(self.form_xpath)
        if len(form) == 1:
            return 'small'

        return 'large'

    def get_form_small(self):
        self.__use_url()
        self.__execute_btn_score()

        return {
            "title": self.__find_element_xpath(self.title_xpath),
            "subtitle": self.__find_element_xpath(self.form_xpath,'text').split('\n')[0],
            "correct_answer": self.__find_element_xpath('//input[@name="solutions"]', 'value')
        }

    def get_form_large(self):
        self.__use_url()
        self.__execute_btn_score()

        subtitles = self.__find_elements_xpath(self.form_xpath)
        subtitles_arr = []
        for i in range(3):
            subtitles_arr.append(subtitles[i].text)

        return {
            "title": self.__find_element_xpath(self.title_xpath),
            "subtitle": subtitles_arr,
            "correct_answer": self.__find_element_xpath('//textarea[@name="solutions"]', 'value').strip().split('\n')
        }


if __name__ == '__main__':

    levels = ['fce', 'cae', 'cpe']
    urls = ['/pverb.htm', '/wform.htm', '/colloc.htm']

    for level in levels:
        for url in urls:
            spider = FloSpider(level, url)
            form_type = spider.check_form_type()

            print(spider.get_form_small() if form_type == 'small' else spider.get_form_large())
