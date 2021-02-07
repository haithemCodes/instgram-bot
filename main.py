from selenium import webdriver
from time import sleep
import sys
import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import random


def login_to_account():
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    user_n = WebDriverWait(driver, 10).until(Ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')))
    user_n.click()
    user_n.send_keys(username)
    pass_w = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
    pass_w.click()
    pass_w.send_keys(password)
    login_btn = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
    login_btn.click()
    en_iden = WebDriverWait(driver, 10).until(Ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#react-root > section > main > div > div > div > div > button')))
    en_iden.click()
    not_btn = WebDriverWait(driver, 10).until(Ec.presence_of_element_located(
        (By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')))
    not_btn.click()
    root_following = get_following(username)
    view_accounts_stories(root_following)
    for user_n_rf in root_following:
        view_accounts_stories(get_following(user_n_rf))


def get_following(username_get_f):
    driver.get('https://www.instagram.com/' + username_get_f + '/')
    following_list = []
    following_btn = WebDriverWait(driver, 10).until(Ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(3) > a')))
    following_count = driver.find_elements_by_css_selector('#react-root > section > main > div > header > section > '
                                                           'ul > li:nth-child(3) > a > span')[0].text
    try:
        following_btn.click()
    except:
        pass
    sleep(3)
    i = 1
    while i <= int(str(following_count).replace(' ', '')):
        try:
            scr1 = driver.find_elements_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > '
                                                        'li:nth-child(' + str(i) + ')')[0]
            driver.execute_script("arguments[0].scrollIntoView(true);", scr1)
            user_name_f = scr1.text.split()[0]
            following_list.append(user_name_f)
            i += 1
        except:
            if i == int(str(following_count).replace(' ', '')):
                i += 1
            pass
    return following_list


def get_followers(username_get_f):
    driver.get('https://www.instagram.com/' + username_get_f + '/')
    followers_list = []
    followers_btn = WebDriverWait(driver, 10).until(Ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')))
    followers_count = driver.find_elements_by_css_selector('#react-root > section > main > div > header > section > '
                                                           'ul > li:nth-child(2) > a > span')[0].text
    try:
        followers_btn.click()
    except:
        pass
    i = 1
    sleep(3)
    while i <= int(str(followers_count).replace(' ', '')):
        try:
            scr1 = driver.find_elements_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > '
                                                        'li:nth-child(' + str(i) + ')')[0]
            driver.execute_script("arguments[0].scrollIntoView(true);", scr1)
            user_name_f = scr1.text.split()[0]
            followers_list.append(user_name_f)
            i += 1
        except:
            if i == int(str(followers_count).replace(' ', '')):
                i += 1
            pass
    return followers_list


def view_accounts_stories(accounts):
    global story_viewed
    for user_a in accounts:
        driver.get('https://www.instagram.com/' + user_a + '/')
        try:
            story_open = WebDriverWait(driver, 10).until(Ec.presence_of_element_located(
                (By.CSS_SELECTOR, '#react-root > section > main > div > header > div > div.h5uC0')))
            story_open.click()
        except:
            pass
        sleep(3)
        i = 1
        try:
            length_story = driver.find_elements_by_css_selector(
                '#react-root > section > div > div > section > div.w9Vr-._6ZEdQ > div._7zQEa')
            while i <= len(length_story):
                story_viewed += 1
                try:
                    question_buttons = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/section'
                                                                    '/div[2]/div[1]/div/div/div/div/div[ '
                                                                    '2]/div/div[2]/div[1]/div[' + str(
                        random.randint(1, 2)) + ']')
                    question_buttons.click()
                except:
                    pass
                next_story = WebDriverWait(driver, 10).until(Ec.presence_of_element_located(
                    (By.CSS_SELECTOR, '#react-root > section > div > div > section > div.GHEPc > button.ow3u_')))
                next_story.click()
                i += 1
        except:
            pass


def view_hashtags_stories():
    list_hash_tags = ['algerie', 'algeria', 'dz']
    global story_viewed
    global accounts_size
    fa = open("accounts.txt", "a")
    for tag in list_hash_tags:
        driver.get('https://www.instagram.com/explore/tags/' + tag + '/')
        story_open = WebDriverWait(driver, 10).until(Ec.presence_of_element_located(
            (By.CSS_SELECTOR, '#react-root > section > main > header > div.T7reQ._0FuTv.pkWJh > div')))
        story_open.click()
        sleep(3)
        length_story = driver.find_elements_by_css_selector(
            '#react-root > section > div > div > section > div.w9Vr-._6ZEdQ > div._7zQEa')
        i = 1
        while i <= len(length_story):
            fa.write(driver.find_elements_by_css_selector(
                '#react-root > section > div > div > section > header > div > div.MS2JH > '
                'div.Igw0E._56XdI.eGOV_._4EzTm.soMvl > a')[0].text + '\n')
            accounts_size += 1
            story_viewed += 1
            next_story = WebDriverWait(driver, 10).until(Ec.presence_of_element_located(
                (By.CSS_SELECTOR, '#react-root > section > div > div > section > div.GHEPc > button.ow3u_')))
            next_story.click()
            i += 1

    fa.close()
    # accounts = list(dict.fromkeys(fr.read().split('\n')))


try:
    story_viewed = 0
    accounts_size = 0
    root_following = []
    root_followers = []
    other_accounts = []
    username = ""
    password = ""
    if os.path.isfile('access.nd'):
        print('[+] Found old access :) .\n')
    ques_f = input('[*] If you want change access account type:"Y" to skip this step click Enter : ')
    if ques_f == 'y' or ques_f == 'Y':
        print('[!] Enter Username & Password .\n')
        username = input('[*] Username : ')
        password = input('[*] Password : ')
        fw = open('access.nd', 'w')
        fw.write(username + ":" + password)
        fw.close()
    else:
        print('[+] Connect to old access account .\n')
        fr = open('access.nd', 'r')
        root_account_info = fr.read().split(':')
        username = root_account_info[0]
        password = root_account_info[1]
        fr.close()

    driver = webdriver.Chrome()
    login_to_account()
except:
    print('[!] Somthing wrong !')
