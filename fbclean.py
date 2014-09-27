import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)

user = os.environ['FBC_USER']
password = os.environ['FBC_PASSWORD']


def get_dialog(owner):
    print("Getting dialog for %s" % owner)
    return browser.find_element_by_xpath("//div[@data-ownerid='%s']" % owner)


def find_action(dialog, label):
    return dialog.find_element_by_xpath("//a/span[span='%s']" % label)


def find_button(label):
    return browser.find_element_by_xpath("//button[.='%s']" % label)


def do_delete_post(dialog):
    e = find_action(dialog, 'Delete')
    print("Deleting post")
    e.click()

    time.sleep(2)
    try:
        find_button('Delete Post').click()
        time.sleep(6)
    except:
        pass
    print("Post deleted")


def do_unlike(dialog):
    e = find_action(dialog, 'Unlike')
    print("Unliking")
    e.click()
    print("Unliked")


def do_delete_photo(dialog):
    e = dialog.find_element_by_xpath("//a/span[span='Delete Photo']")
    print("Deleting photo")
    e.click()
    try:
        find_action(dialog, 'Report/Remove Tag').click()
        time.sleep(1)
        browser.find_element_by_name("untag").click()
        time.sleep(0.1)
        find_button('Remove Tag').click()
        time.sleep(5)
    except:
        pass
    print("Photo deleted")


def do_remove_tag(dialog):
    e = find_action(dialog, 'Report/Remove Tag')
    print("Removing tag")
    e.click()
    time.sleep(1)
    try:
        browser.find_element_by_name("untag").click()
        time.sleep(0.1)
        find_button('Remove Tag').click()
        time.sleep(5)
    except:
        try:
            find_button('Continue').click()
            time.sleep(0.1)
            find_button('Continue').click()
        except:
            pass
    print("Tag removed")


def do_hide(dialog):
    e = find_action(dialog, 'Hidden from Timeline')
    print("Hiding")
    e.click()
    print("Hid")


def clean(reload_site):
    if(reload_site):
        browser.get('https://www.facebook.com/%s/allactivity' % user)

    elements = browser.find_elements_by_xpath(
        "//a[@aria-label='Allowed on Timeline']")

    for elm in elements:
        elm.click()
        elm.click()  # Stupid, but works
        time.sleep(1)

        owner = elm.get_attribute('id')
        dialog = get_dialog(owner)

        # Delete post
        try:
            do_delete_post(dialog)
            return True
        except:
            # Unlike
            try:
                do_unlike(dialog)
                return True
            except:
                # Delete photo
                try:
                    do_delete_photo(dialog)
                    return True
                except:
                    # Remove tag
                    try:
                        do_remove_tag(dialog)
                        return True
                    except:
                        try:
                            do_hide(dialog)
                            return True
                        except:
                            print("Could not figure out what to do")
                            continue
    # print("Nothing to do")
    return False


def main():
    browser.get('https://facebook.com')
    email_field = browser.find_element_by_id('email')
    email_field.send_keys(user)
    pw = browser.find_element_by_id('pass')
    pw.send_keys(password)
    pw.submit()
    r = True
    while(True):
        r = clean(r)
        if(not r):
            # print("Scrolling down")
            for i in range(0, 10):
                actions = ActionChains(browser).send_keys(Keys.PAGE_DOWN)
                actions.perform()

if __name__ == '__main__':
    main()
