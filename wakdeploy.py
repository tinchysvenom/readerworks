# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 17:32:06 2019

@author: USER
"""


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def naira_handler():
    chrome_exec_shim = '/app/.apt/usr/bin/google-chrome'
    chrome_options = Options() #the code to open/connect to the site starts here, the code to handle the login goes here
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-infobars")
    chrome_options.binary_location = chrome_exec_shim 
    driver = webdriver.Chrome(executable_path="chromedriver",   options=chrome_options)
    driver.get("https://www.nairaland.com/")

    logbut_list = driver.find_elements_by_tag_name('a')
    logbut_list[2].click()

    uname = driver.find_element_by_name('name')
    uname.click()
    uname.send_keys('saltycreatordra')

    pasiv = driver.find_element_by_name('password')
    pasiv.click()
    pasiv.send_keys('herokubot456')

    login = driver.find_element_by_xpath('/html/body/div/table[2]/tbody/tr[2]/td/form/input[3]')
    login.click()


    val_no = 1

    while val_no <= 20:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="up"]/tbody/tr/td/a[10]')))
        fi_trend = driver.find_element_by_xpath('//*[@id="up"]/tbody/tr/td/a[10]')
        fi_trend.click()
    
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'tr')))
        article_list = driver.find_elements_by_tag_name('tr')
        article_list[val_no].click()
    
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'h2')))
        heda = driver.find_element_by_tag_name('h2')
        reply = heda.text + ' ' + 'hero sele without display'
        rep_find = driver.find_element_by_class_name('nocopy')
        rep = rep_find.find_element_by_tag_name('a')
        ActionChains(driver).move_to_element(rep).perform()
        rep.click()
    
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body"]')))   
        text_box = driver.find_element_by_xpath('//*[@id="body"]')
        text_box.send_keys(reply)
        sub_but = driver.find_element_by_xpath('//*[@id="postform"]/p[2]/input[1]')
        sub_but.click()
        print('finished: ', val_no)
        val_no += 1
    

    driver.close()
    driver.quit()
