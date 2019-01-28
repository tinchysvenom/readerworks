# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:55:45 2019

@author: USER
"""


import re
import gc
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
    gc.collect()
    return(summary)
    
 #3509, 3653, 3901, 3671, 3917, 3677, 3923, 3709, 3953, 3733, 3973, 3743, 3989, 3749, 3991   
post_targets = [3509, 3751, 3517, 3761, 3523, 3763, 3529, 3769, 3539, 3781, 3547, 3793, 3557, 3803, 3643, 3889]
post_var = 0
todays_post_target = post_targets[post_var]
sec_intervals = (54000/todays_post_target) + 1
completed = 0
landage = 0
pager = 0
serum = False


while True and time.localtime()[3] <= 22 or time.localtime()[3] >= 7:
    try:
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
            print('page opened')
            
            while True: #log in
                try:
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'nameField')))
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
                
                except:
                    print('error at login section')
                    driver.refresh()
                    time.sleep(2)
                    continue
                break

            del username, passiv, logbut
            gc.collect()
            print('logged in')
            
            while True: #click post
                try:
                    if serum == False:
                        first_post_box = driver.find_element_by_class_name('blog-list-details') #this section would select the first post ont he landing page and proceed
                        la_herd = first_post_box.find_elements_by_class_name('item-details')
                        first_post = la_herd[completed].find_element_by_tag_name('a')
                        first_post.click()
                        time.sleep(2.5)
                        driver.refresh()
                    else:
                        if pager == 0:
                            first_post_box = driver.find_element_by_class_name('blog-list-details') #this section would select the first post ont he landing page and proceed
                            la_herd = first_post_box.find_elements_by_class_name('item-details')
                            first_post = la_herd[completed].find_element_by_tag_name('a')
                            first_post.click()
                            time.sleep(2.5)
                            driver.refresh()
                        else:
                            noci = 0
                            while noci <= pager:
                                username = driver.find_element_by_class_name('blog')
                                passiv = username.find_elements_by_tag_name('a')
                                logbut = passiv[-1]
                                ActionChains(driver).move_to_element(logbut).perform().click()
                                noci += 1
                                time.sleep(2)
                                
                            del username, passiv, logbut, noci
                            gc.collect()
                
                            first_post_box = driver.find_element_by_class_name('blog-list-details') #this section would select the first post ont he landing page and proceed
                            la_herd = first_post_box.find_elements_by_class_name('item-details')
                            first_post = la_herd[landage].find_element_by_tag_name('a')
                            first_post.click()
                            time.sleep(2.5)
                            driver.refresh()
                except:
                    print('error at click post section')
                    driver.refresh()
                    time.sleep(2)
                    continue
                break
            del first_post_box, la_herd, first_post
            gc.collect()
            print('first post clicked')
            
            while completed < todays_post_target: 
                try: #read post and send reply
                    try:
                        username = driver.find_element_by_class_name('plan2-recommended')
                    except:
                        username = driver.find_element_by_class_name('float-left')
                        username = username.text[0:64] 
                    start_time = time.time()
                    end_time = start_time + sec_intervals
                    
                    while True and time.time() <= end_time: #this section find the post needed and summarize it scroll down to the comments section and post the summary, scroll back up and hover over some ads
                        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'topic-content')))
                        try:
                            passiv = driver.find_element_by_class_name('topic-content') #find the post and needed and summarize it
                            try:
                                logbut = passiv.find_elements_by_tag_name('p')
                                first_post_box = [note.text for note in logbut]
                                la_herd = ''.join(first_post_box)
                            except:
                                try:
                                    logbut = passiv.find_element_by_tag_name('p')
                                    noci = logbut.find_elements_by_tag_name('span')
                                    first_post_box = [note.text for note in noci]
                                    la_herd = ''.join(first_post_box)
                                except:
                                    la_herd = ' '
                                    
                            try:
                                summary_comment = post_summarizer(la_herd)
                            except:
                                summary_comment = username.text
                            
                            username = driver.find_element_by_id('editor') #scroll down to the comments section and post the summary
                            ActionChains(driver).move_to_element(username).perform()
                            passiv = username.find_element_by_tag_name('iframe')
                            driver.switch_to.frame(passiv)
                            logbut = driver.find_element_by_tag_name('p')
                            ActionChains(driver).move_to_element(logbut).perform().click()
                            driver.execute_script("arguments[0].innerText = arguments[1] ", logbut, summary_comment)
                            driver.switch_to.default_content()
                            first_post_box = driver.find_element_by_id('ReplyButton')
                            ActionChains(driver).move_to_element(first_post_box).perform().click()
                            if end_time > time.time():
                                time.sleep(end_time-time.time())
                            else: pass
                        except:
                            driver.refresh()
                            continue
                        break
                except:
                    print('error at reasum section')
                    driver.refresh()
                    time.sleep(2)
                    continue
                break
                del start_time, end_time, username, passiv, logbut, la_herd, first_post_box, summary_comment
                gc.collect()
                
                driver.execute_script("window.history.go(-2)") #first go back to the landing page
                time.sleep(1.5)
                driver.refresh() #refresh the page
                time.sleep(1)
                
                while True: #go to the next post
                    try:
                        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.CLASS_NAME, 'blog')))
                        username = driver.find_element_by_class_name('blog') #find all elements that represent an article
                        passiv = username.find_elements_by_class_name('item-details')
                        
                        if landage > len(passiv): #if the landage variable is greater than the number of articles present go to the next page on the pagination
                            landage = 0 #set the landage variable to 0
                            logbut = username.find_elements_by_tag_name('a')
                            first_post_box = logbut[-1]
                            ActionChains(driver).move_to_element(first_post_box).perform().click()#click the next button
                            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'blog-list-details')))
                            la_herd = driver.find_element_by_class_name('blog-list-details') #find all elements that represent an article
                            first_post = la_herd.find_elements_by_class_name('entry-title')
                            noci = first_post[landage].find_element_by_tag_name('a') #use landage variable to select one page
                            ActionChains(driver).move_to_element(noci).perform().click() #open the selected page
                            driver.implicitly_wait(4)
                            driver.refresh()
                
                            del logbut, first_post_box, la_herd, first_post
                            gc.collect()
                        else:
                            noci = passiv[landage].find_element_by_tag_name('a') #use landage variable to select one page
                            ActionChains(driver).move_to_element(noci).perform()
                            noci.click() #open the selected page
                
                        del username, passiv, noci
                        gc.collect()
            
                        landage += 1
                        completed += 1
            
                        if completed <=5:
                            print('No of posts:', completed)
                        elif completed % 10 == 0:
                            print('No of posts:', completed)
                        else: pass
            
                        if time.localtime()[3] > 22 or completed == todays_post_target:
                            post_var += 1
                            completed = 0
                            landage = 0
                            driver.close()
                            driver.quit()
                            print('about to sleep')
                            time.sleep(33000)
                    except:
                        print('error at next post section')
                        driver.refresh()
                        time.sleep(2)
                        continue
                    break
        
        
        
        else:
            pass
    except:
        serum = True
        continue
    break
        
