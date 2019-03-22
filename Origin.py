from selenium import webdriver
import time
from random import randint
from random import choice
import xlwings

while True:
    #open page
    webpage = 'INPUT REFERALL LINK HERE'
    driver = webdriver.Chrome()
    driver.get(webpage)
    webpage = driver.page_source
    #driver.close()

    #click register
    driver.find_element_by_xpath('//*[@id="__layout"]/div/header/div[1]/div[2]/div/div[3]/button').click()
    time.sleep(0.1)

    #click register email
    driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/section/div/div[2]').click()

    #click Australia country code
    driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/section/div[1]/form/div[2]/div/div[1]/section[1]').click()
    time.sleep(0.1)
    driver.find_element_by_xpath('/html/body/div[5]/section/div/div[3]/div').click()
    time.sleep(0.1)

    #click DOB
    #Month, rand int 1-12
    driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/section/div[1]/form/div[3]/div/div/section[1]').click()
    rand = "/html/body/div[7]/section/div/div[" + str(randint(1,11)) + ']/div'
    time.sleep(0.5)
    scr1 = driver.find_element_by_xpath(rand)
    driver.execute_script("arguments[0].scrollIntoView();", scr1)
    driver.find_element_by_xpath(rand).click()

    #Date, randint 1-28
    driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/section/div[1]/form/div[3]/div/div/section[2]/div[1]').click()
    rand = "/html/body/div[9]/section/div/div[" + str(randint(1,28)) + ']/div'
    time.sleep(0.5)
    scr1 = driver.find_element_by_xpath(rand)
    driver.execute_script("arguments[0].scrollIntoView();", scr1)
    driver.find_element_by_xpath(rand).click()

    #Year, randint 1-5
    driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/section/div[1]/form/div[3]/div/div/section[3]').click()
    rand = "/html/body/div[11]/section/div/div[" + str(randint(21,45)) + ']/div'
    time.sleep(0.5)
    scr1 = driver.find_element_by_xpath(rand)
    driver.execute_script("arguments[0].scrollIntoView();", scr1)
    driver.find_element_by_xpath(rand).click()

    #mobile numbers
    mobile = '04' + str(randint(10000000,99999999))
    driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/section/div[1]/form/div[2]/div/div[1]/section[2]/input').send_keys(mobile)

    #type Perth
    driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/section/div[1]/form/div[4]/div/input').send_keys('Perth')

    #Type WA
    driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/section/div[1]/form/div[5]/div/input').send_keys('WA')

    #Fake names/emails
    bookname = r'C:\Users\Ben\Desktop\name.xlsx'
    industrysheet = 'Names'
    workbook = xlwings.Book(bookname)
    sheet = workbook.sheets[industrysheet]
    ranint = str(randint(0,69592))
    firstname = workbook.sheets.active.range('A' + ranint).value
    surname = workbook.sheets.active.range('B' + ranint).value
    randemail= choice(['C','D','E','F','G','H'])
    email = workbook.sheets.active.range(randemail+ranint).value

    print(firstname)
    print(surname)
    print(email)

    #inputting fake details
    driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(firstname)
    driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(surname)
    driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/section/div[1]/form/div[1]/div[1]/input').send_keys(email)

    #click through to end
    i = 0
    while i<6:
        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div[2]/button').click()
        i+=1
        time.sleep(0.3)

    driver.close()
    time.sleep(1)




