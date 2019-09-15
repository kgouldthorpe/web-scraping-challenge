#Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os

#Define Executable Path Function
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

#Define Scrape Function
def scrape():
    browser = init_browser()
    mars_facts_data = {}

    #Scrape NASA News
    url_1 = "https://mars.nasa.gov/news/"
    browser.visit(url_1)

    html = browser.html
    soup_1 = BeautifulSoup(html, "html.parser")

    mars_news_headline= soup_1.find("div", class_="content_title")
    mars_news_teaser= soup_1.find("div", class_="article_teaser_body")
    
    mars_facts_data["mars_news_headline"] = mars_news_headline.text
    mars_facts_data["mars_news_teaser"] = mars_news_teaser.text

    #Scrape Space Images
    #url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    #browser.visit(url_2)
   
    #html = browser.html
    #soup_2 = BeautifulSoup(html, "html.parser")

    #featured_image_url = soup_2.find("img", class_= "fancybox-image")["src"]
    #complete_url = os.path.join(url_2, featured_image_url)
        
    #mars_facts_data["featured_image_url"] = complete_url

    #Scrape Mars Twitter
    url_3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_3)

    html = browser.html
    soup_3 = BeautifulSoup(html, "html.parser")

    mars_weather = soup_3.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
        
    mars_facts_data["mars_weather"] = mars_weather.text

    #Scrape Mars Facts
    url_4 = "https://space-facts.com/mars/"
    mars_facts = pd.read_html(url_4)
    mars_table = mars_facts[1]
    mars_df= pd.DataFrame(mars_table)
    mars_facts_data["Equatorial Diameter"] = mars_df.at[1,1]
    mars_facts_data["Polar Diameter"] = mars_df.at[1,2]
    mars_facts_data["Mass"] = mars_df.at[1,3]
    mars_facts_data["Moons"] = mars_df.at[1,4]
    mars_facts_data["Orbit Distance"] = mars_df.at[1,5]
    mars_facts_data["Orbit Period"] = mars_df.at[1,6]
    mars_facts_data["Surface Temperature"] = mars_df.at[1,7]
    mars_facts_data["First Record"] = mars_df.at[1,8]
    mars_facts_data["Recorded By"] = mars_df.at[1,9]

    # Scrape Mars Hemispheres - Cerberus
    url_5 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url_5)

    html = browser.html
    soup_5 = BeautifulSoup(html, "html.parser")

    c_img_url= soup_5.find("img", class_="wide-image")["src"]
    c_title=soup_5.find("h2", class_="title")

    real_c_title = c_title.text

    cerberus={"Title": real_c_title, "Image URL": url_5 + c_img_url}
    mars_facts_data["hemisphere_cerberus"] = cerberus

    #Scrape Mars Hemispheres - Schiaparelli
    url_6 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(url_6)

    html = browser.html
    soup_6 = BeautifulSoup(html, "html.parser")

    s_img_url= soup_6.find("img", class_="wide-image")["src"]
    s_title=soup_6.find("h2", class_="title")

    real_s_title = s_title.text

    schiaparelli={"Title": real_s_title, "Image URL": url_6 + s_img_url}
    mars_facts_data["hemisphere_schiaparelli"] = schiaparelli

    #Scrape Mars Hemispheres - Syrtis
    url_7 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(url_7)

    html = browser.html
    soup_7 = BeautifulSoup(html, "html.parser")

    sy_img_url= soup_7.find("img", class_="wide-image")["src"]
    sy_title=soup_7.find("h2", class_="title")

    real_sy_title = sy_title.text

    syrtis={"Title": real_sy_title, "Image URL": url_7 + sy_img_url}
    mars_facts_data["hemisphere_syrtis"] = syrtis

    #Scrape Mars Hemispheres - Valles Marineris
    url_8 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(url_8)

    html = browser.html
    soup_8 = BeautifulSoup(html, "html.parser")

    v_img_url= soup_8.find("img", class_="wide-image")["src"]
    v_title=soup_8.find("h2", class_="title")

    real_v_title = v_title.text

    valles={"Title": real_v_title, "Image URL": url_8 + v_img_url}
    mars_facts_data["hemisphere_valles_marineris"]= valles

    return mars_facts_data