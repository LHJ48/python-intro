from bs4 import BeautifulSoup
import requests

class Bugsmusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    class_name = []

    def set_url(self, detail):
        # detail 은 url 뒤에 바뀌는 값
        self.url = requests.get(f'{self.url}{detail}').text

    def get_raking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='p', attrs={"class":"title"})
        for idx, title in enumerate(ls1):
            print(f'{idx+1}위 {title.find("a").text}')

    @staticmethod
    def main():
        bugs = Bugsmusic()
        bugs.set_url('chartdate=20210605&charthour=15')
        bugs.get_raking()

Bugsmusic.main()