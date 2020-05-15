import random
from time import sleep
from getpass import getpass
# import selenium modules
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

def pauseRandomTime(a=1, b=3):
    '''
    pause browser action for random time
    '''
    sleep(random.randint(1, 3))

def faceBookLogIn(email, password):
    '''
    faceBookLogIn: 
    Search for email and pass input, and send key to those field
    Then click anywhere else to able login click button. 
    After that just click the button to login
    '''
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

    # sometimes log in UI for Tinder doesn't show Facebook login, instead 'More Options'

    try:
        driver.find_element_by_xpath('//button[text()="More Options"]').click()
        pauseRandomTime()
    except NoSuchElementException:
        pass

    # click 'Log in with Facebook
    driver.find_element_by_xpath(
        '//button[@aria-label="Log in with Facebook"]').click()

    # After five-second pause, switch handling page to login_page
    sleep(5)

    for handle in driver.window_handles:
        if handle != main_page:
            login_page = handle

    driver.switch_to.window(login_page)

    # Log into FB and switch back the handling window
    faceBookLogIn(email, password)

    driver.switch_to.window(main_page)

    # handle popup after initial login
    sleep(5)
    driver.find_element_by_xpath('//span[text()="Allow"]').click()
    pauseRandomTime()
    driver.find_element_by_xpath('//span[text()="Not interested"]').click()
    pauseRandomTime(8,10)


    # Keep swiping right 1000 times, with 20% chance that swipes left
    for i in range(0, 1000):
        try:
            # control random swipe-left: Current 20%
            if random.randint(0, 4) == 0 :
                driver.find_element_by_xpath('//button[@aria-label="Nope"]').click()
            else :
                driver.find_element_by_xpath('//button[@aria-label="Like"]').click()

            sleep(0.2)

        # Handling some pop up that blocks clicking on the button
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
