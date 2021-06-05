from bs4 import BeautifulSoup
import requests

class Melon(object):
    url = 'https://www.melon.com/chart/index.htm?'
    header = {'User-Agent':'Mozilla/5.0'} #벅스와 달리 멜론에서 설정해야 하는 헤더값
    class_name = []

    def set_url(self, detail):
        # detail 은 url 뒤에 바뀌는 값
        self.url = requests.get(f'{self.url}{detail}', headers=self.header).text

    def get_raking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='div', attrs={"class":"ellipsis rank01"})
        for idx, title in enumerate(ls1):
            print(f'{idx+1}위 {title.find("a").text}')

    @staticmethod
    def main():
        melon= Melon()
        melon.set_url('dayTime=2021060515')
        melon.get_raking()

Melon.main()