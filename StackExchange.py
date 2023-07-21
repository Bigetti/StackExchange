import requests
from bs4 import BeautifulSoup
import pandas as pd



url = 'https://stackoverflow.com/'

def get_request_status(url):
    try:
        response = requests.get(url)
        if response.status_code in [200, 210]:
            return "Статус запроса: Успешно (200)"
        else:
            return f"Статус запроса: Ошибка ({response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Ошибка при выполнении запроса: {e}"

def StackSearch (query):
    res = requests.get('https://stackoverflow.com/')
    soup = BeautifulSoup(res.text, features="html.parser")
    posts = soup.find_all('div', class_="js-search-result")
    print(posts)

    stack_posts = pd.DataFrame(columns=['title', 'link', 'date'])

    for post in posts:
        title = post.find('h3', class_='s-link__title').text
        print(title)
        link = post.find('a', class_='s-link').get('href')
        print(link)
        date = post.find('time', class_='s-user-card-time').text
        print(date)

        stack_posts = stack_posts.append({'title': title, 'link': link, 'date': date}, ignore_index = True)

    return stack_posts
    

get_request_status(url)

posts_df = StackSearch('python')
print(posts_df)
