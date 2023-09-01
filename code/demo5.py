import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 获取电影列表
movies_list = soup.find('ol', class_='grid_view')
movies = movies_list.find_all('li')

# 遍历电影列表，获取电影信息
for movie in movies:
    # 电影名称和评分
    title = movie.find('span', class_='title').text
    rating_num = movie.find('span', class_='rating_num').text

    # 导演、主演和年份
    info = movie.find('p', class_='').text.strip()
    info_list = info.split('\n')
    director = info_list[0].split(':')[1].strip()
    actors = info_list[1][3:].strip()
    year = info_list[2].split('/')[0].strip()

    # 输出电影信息
    print(f'电影名称：{title}')
    print(f'电影评分：{rating_num}')
    print(f'导演：{director}')
    print(f'主演：{actors}')
    print(f'上映年份：{year}')