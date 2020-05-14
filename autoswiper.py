import random
from time import sleep
from getpass import getpass
# import selenium modules
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

def pauseRandomTime(a=1, b=3):
    sleep(random.randint(1, 3))

def faceBookLogIn(email, password):
    driver.find_element_by_name('email').send_keys(email)
    pauseRandomTime()
    driver.find_element_by_name('pass').send_keys(password)
    pauseRandomTime()
    driver.find_element_by_xpath('//*[@id="email_container"]/div/label').click()
    pauseRandomTime()
    driver.find_element_by_id('u_0_0').click()
    pauseRandomTime()


if __name__ == '__main__':
    email = input('Please enter your Facebook login Email: ')
    password = getpass('Please enter your Facebook login password: (Hidden) ')

    # open tinder.com
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://tinder.com/app/recs")

    # store current_window as main_page
    main_page = driver.current_window_handle

    sleep(5)

    try:
        driver.find_element_by_xpath('//button[text()="More Options"]').click()
        pauseRandomTime()
    except NoSuchElementException:
        pass

    driver.find_element_by_xpath(
        '//button[@aria-label="Log in with Facebook"]').click()

    sleep(5)

    for handle in driver.window_handles:
        if handle != main_page:
            login_page = handle

    driver.switch_to.window(login_page)

    faceBookLogIn(email, password)

    driver.switch_to.window(main_page)

    pauseRandomTime()
    driver.find_element_by_xpath('//span[text()="Allow"]').click()
    pauseRandomTime()
    driver.find_element_by_xpath('//span[text()="Not interested"]').click()
    pauseRandomTime(8,10)


    for i in range(0, 100):
        try:
            driver.find_element_by_xpath('//button[@aria-label="Like"]').click()
            sleep(0.3)

        except ElementClickInterceptedException:
            print(i,' Log: ElementClickInterceptedException')
            try:
                elem_not_int = driver.find_element_by_xpath(
                    '//span[text()="Not interested"]')
                elem_not_int.click()
                elem_no_thx = driver.find_element_by_xpath(
                    '//span[text()="No Thanks"]')
                elem_no_thx.click()

            except NoSuchElementException:
                print(i,' Log: NoSuchElementException')
                pass

            pass
