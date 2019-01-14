# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:00:25 2018

@author: USER
"""

import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from sklearn.feature_extraction.text import CountVectorizer
from selenium.webdriver.support import expected_conditions as EC


def post_summarizer(article):
    vec_art = [article]
    sentence_list = re.split('\.', article)
    vectorizer = CountVectorizer(stop_words='english')
    x_train = vectorizer.fit_transform(vec_art)
    num_samples, num_features = x_train.shape

    va = 0
    xab = {}
    for i in vectorizer.get_feature_names():
        xab[i] = x_train.toarray().transpose()[va][0]
        va += 1
    
    max_weight = max(xab.values())

    xac = {}
    for j in xab.keys():
        xac[j] = xab[j]/max_weight
    
    xad = {}
    for k in sentence_list:
        xae = 0
        split_k = re.split("\s|,", k)
        for l in split_k:
            if l in xac.keys():
                xae += xac[l]
            else: pass
        xad[k] = xae
    
    maxy = sorted(xad.values())
    maxx = [maxy[-1]]
    
    summary_list = []
    for m in maxx:
        for n in xad.keys():
            if xad[n] == m:
                summary_list.append(n)
            else: pass

    summary = ' '.join(summary_list)
    del article, vec_art, sentence_list, x_train, num_samples, num_features, va, xab, max_weight, xac, xad, xae, split_k, maxy, maxx, summary_list
    return(summary)
    
 #3653, 3901, 3671, 3917, 3677, 3923, 3709, 3953, 3733, 3973, 3743, 3989, 3749, 3991   
post_targets = [3509, 3751, 3517, 3761, 3523, 3763, 3529, 3769, 3539, 3781, 3547, 3793, 3557, 3803, 3643, 3889]
post_var = 0
todays_post_target = post_targets[post_var]
sec_intervals = (54000/todays_post_target) + 1
completed = 0
landage = 0
pager = 0
serum = False

def waka_handler():
    global post_var
    global completed
    global landage
    global pager
    global serum
    if time.localtime()[3] >= 7: #this section starts the day activities and picks the post target for the day
        chrome_exec_shim = '/app/.apt/usr/bin/google-chrome'
        chrome_options = Options() #the code to open/connect to the site starts here, the code to handle the login goes here
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--disable-infobars")
        chrome_options.binary_location = chrome_exec_shim 
        driver = webdriver.Chrome(executable_path="chromedriver",   options=chrome_options)
        driver.get("https://wakanda.ng/login")
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'nameField')))
        except:
            driver.refresh()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'nameField')))
        
        print('page opened')
        username = driver.find_element_by_id('nameField')
        ActionChains(driver).move_to_element(username).perform()
        username.click()
        username.clear()
        username.send_keys('Tinchysvenom')
        
        passiv = driver.find_element_by_id('passwordField')
        ActionChains(driver).move_to_element(passiv).perform()
        passiv.click()
        passiv.clear()
        passiv.send_keys('audaceusfortunaiuvat456')
        
        logbut = driver.find_element_by_xpath('//*[@id="main"]/div[4]/div/div/div[1]/div/div/form/div[4]/button')
        ActionChains(driver).move_to_element(logbut).perform()
        logbut.click()
        #the code to automate the facebok postings go here
        
        driver.implicitly_wait(10)
        del username, passiv, logbut
        
        if serum == False:
            first_post_box = driver.find_element_by_class_name('blog-list-details') #this section would select the first post ont he landing page and proceed
            la_herd = first_post_box.find_elements_by_class_name('item-details')
            first_post = la_herd[completed].find_element_by_tag_name('a')
            first_post.click()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'plan2-recommended')))
            driver.refresh()
        else:
            if pager == 0:
                first_post_box = driver.find_element_by_class_name('blog-list-details') #this section would select the first post ont he landing page and proceed
                la_herd = first_post_box.find_elements_by_class_name('item-details')
                first_post = la_herd[completed].find_element_by_tag_name('a')
                first_post.click()
                WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'plan2-recommended')))
                driver.refresh()
            else:
                noci = 0
                while noci <= pager:
                    land_contents = driver.find_element_by_class_name('blog')
                    next_but = land_contents.find_elements_by_tag_name('a')
                    next_button = next_but[-1]
                    ActionChains(driver).move_to_element(next_button).perform()
                    next_button.click()
                    noci += 1
                    driver.implicitly_wait(3)
                
                first_post_box = driver.find_element_by_class_name('blog-list-details') #this section would select the first post ont he landing page and proceed
                la_herd = first_post_box.find_elements_by_class_name('item-details')
                first_post = la_herd[landage].find_element_by_tag_name('a')
                first_post.click()
                WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'plan2-recommended')))
                driver.refresh()
        
        del first_post_box, la_herd, first_post, noci, land_contents, next_but, next_button        
        while completed < todays_post_target:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'plan2-recommended')))
            titlar = driver.find_element_by_class_name('plan2-recommended')
            start_time = time.time()
            end_time = start_time + sec_intervals
            while True and time.time() <= end_time: #this section find the post needed and summarize it scroll down to the comments section and post the summary, scroll back up and hover over some ads
                try:
                    text_parent = driver.find_element_by_class_name('topic-content') #find the post and needed and summarize it
                    try:
                        text_list = text_parent.find_elements_by_tag_name('p')
                        post_block = []
                        for note in text_list:
                            post_block.append(note.text)
                            needed_post = ''.join(post_block)
                    except:
                        needed_post = ' '
                        
                    try:
                        summary_comment = post_summarizer(needed_post)
                    except:
                        summary_comment = titlar.text
                        
                    comment_box = driver.find_element_by_id('editor') #scroll down to the comments section and post the summary
                    ActionChains(driver).move_to_element(comment_box).perform()
                    ifram = comment_box.find_element_by_tag_name('iframe')
                    driver.switch_to.frame(ifram)
                    frame_body = driver.find_element_by_tag_name('p')
                    ActionChains(driver).move_to_element(frame_body).perform()
                    frame_body.click()
                    driver.execute_script("arguments[0].innerText = arguments[1] ", frame_body, summary_comment)
                    driver.switch_to.default_content()
                    send_comment = driver.find_element_by_id('ReplyButton')
                    ActionChains(driver).move_to_element(send_comment).perform()
                    send_comment.click()
                    if end_time > time.time():
                        time.sleep(end_time-time.time())
                    else: pass
                except:
                    driver.refresh()
                    continue
                break
            
            del titlar, start_time, end_time, text_parent, text_list, post_block, needed_post, summary_comment, comment_box, ifram, frame_body, send_comment
            #this section moves to the next post
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'plan2-recommended')))
            driver.execute_script("window.history.go(-2)") #first go back to the landing page
            driver.refresh() #refresh the page
            land_contents = driver.find_element_by_class_name('blog') #find all elements that represent an article
            post_herd = land_contents.find_elements_by_class_name('item-details')
            
            if landage > len(post_herd): #if the landage variable is greater than the number of articles present go to the next page on the pagination
                landage = 0 #set the landage variable to 0
                next_but = land_contents.find_elements_by_tag_name('a')
                next_button = next_but[-1]
                ActionChains(driver).move_to_element(next_button).perform()
                next_button.click() #click the next button
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'blog-list-details')))
                new_land_contents = driver.find_element_by_class_name('blog-list-details') #find all elements that represent an article
                new_post_herd = new_land_contents.find_elements_by_class_name('entry-title')
                
                post_pika = new_post_herd[landage].find_element_by_tag_name('a') #use landage variable to select one page
                ActionChains(driver).move_to_element(post_pika).perform()
                post_pika.click() #open the selected page
                driver.implicitly_wait(4)
                driver.refresh()
                
            else:
                post_pika = post_herd[landage].find_element_by_tag_name('a') #use landage variable to select one page
                ActionChains(driver).move_to_element(post_pika).perform()
                post_pika.click() #open the selected page
            
            del land_contents, post_herd, next_but, next_button, new_land_contents, new_post_herd
            landage += 1
            completed += 1
            if completed % 20 == 0 or completed == 2:
                print(completed)
            else:
                pass
            
            if time.localtime()[3] > 22:
                post_var += 1
                completed = 0
                landage = 0
                driver.close()
                driver.quit()
                time.sleep(33000)
                waka_handler()
            else: pass 
    else:
        pass


while True and time.localtime()[3] >= 7:
    try:
        waka_handler()
    except:
        serum = True
        continue
    break
