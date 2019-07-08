from selenium import webdriver
import os
import time
import requests
import json
import re
import time
import pprint
from addict import Dict
import random
import pathlib
import string
import uuid
driver = webdriver.Chrome('/Users/tanay/Desktop/important files/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://grover.allenai.org/')
while True:
    elem = driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/div[2]/div[1]/div[3]/button')
    elem.click()
    time.sleep(17)
    elem = driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/div[2]/div[1]/div[5]/button')
    elem.click()
    time.sleep(14)

    elem = driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/div[2]/div[1]/div[7]/button')
    elem.click()
    time.sleep(15)

    elem = driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/div[2]/div[1]/div[9]/button')
    elem.click()
    time.sleep(10)

    elem = driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/div[2]/div[1]/div[11]/button')
    elem.click()
    time.sleep(45)


    title = driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/div[2]/div[2]/div[2]/div[2]/span').text
    article = driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/div[2]/div[2]/div[2]/div[4]/span').text

    randomstr = str(uuid.uuid4());
    filename = title + ".txt"
    with open(filename, "w") as text_file:
        text_file.write(" %s \n %s" % (title, article))
    print(filename + '\n')
