import pandas as pd
from bs4 import BeautifulSoup
import requests
from splinter import Browser


def f1(url):
    print(url)
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    soup = BeautifulSoup(browser.html, "html.parser")
    results = soup.find('div', class_="list_text")
    news_title = results.find('div', class_='content_title').text
    news_p = results.find('div', class_='article_teaser_body').text
    browser.quit()
    return news_title, news_p


def f2(url):
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    soup = BeautifulSoup(browser.html, "html.parser")

    featured_image_url = soup.find('div', class_="carousel_items")
    featured_image_url = featured_image_url.article['style'].split()
    featured_image_url = featured_image_url[1]
    st = featured_image_url.find('(')
    featured_image_url = featured_image_url[st+2:]
    st = featured_image_url.find(')')
    featured_image_url = featured_image_url[:st-1]
    featured_image_url = 'https://www.jpl.nasa.gov' + featured_image_url
    browser.quit()
    return featured_image_url


def f3(url):
    print(url)
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    soup = BeautifulSoup(browser.html, "html.parser")
    marstweet = soup.find_all('div', class_='js-tweet-text-container')
    mars_weather = marstweet[1].p.text
    mars_weather = mars_weather.replace('\n', ' ').replace(
        'hPapic.twitter.com/9YLawm67zS', '')
    mars_weather = mars_weather.strip()
    browser.quit()
    return mars_weather


def f4(url):
    print(url)
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    soup = BeautifulSoup(browser.html, "html.parser")

    mars = soup.find('table', id='tablepress-p-mars')
    data = mars.tbody
    
    left = data.find_all('strong')
    right = data.find_all('td', class_="column-2")
    
    html_table = []
    
    for i in range(len(left)):
        html_table.append({'key':left[i].text, 'value': right[i].text})
   
    browser.quit()
    return html_table


def f5(url):
    if url.strip() != '':
        print(url)
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)
        browser.visit(url)
        soup = BeautifulSoup(browser.html, "html.parser")
        mars_images = soup.find_all('div', class_='item')

        hemisphere_image_urls = []
        for image in mars_images:
            url = 'https://astrogeology.usgs.gov' + image.a['href']
            browser.visit(url)
            soup = BeautifulSoup(browser.html, "html.parser")
            hemisphere_image_urls.append({'title': image.h3.text, 'image_url': soup.find(
                'div', class_='downloads').a['href']})
        browser.quit()
        return hemisphere_image_urls


class Mission_to_mars:

    url = ''
    news_title = ''
    news_p = ''
    featured_image_url = ''
    mars_weather = ''
    html_table = ''
    hemisphere_image_urls = ''

    def news():
        Mission_to_mars.news_title, Mission_to_mars.news_p = f1(
            Mission_to_mars.url)

    def featuredImageUrl():
        Mission_to_mars.featured_image_url = f2(Mission_to_mars.url)

    def marsWeather():
        Mission_to_mars.mars_weather = f3(Mission_to_mars.url)

    def htmlTable():
        Mission_to_mars.html_table = f4(Mission_to_mars.url)

    def hemisphereImageUrls():
        Mission_to_mars.hemisphere_image_urls = f5(Mission_to_mars.url)
