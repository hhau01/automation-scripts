#!/usr/bin/env python3

# Various Selenium tools - Feel free to comment out

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')

# Elements that use the CSS class 'name'
browser.find_element_by_class_name(name)
browser.find_elements_by_class_name(name)

# Elements that match the CSS 'selector'
browser.find_element_by_css_selector(selector)
browser.find_elements_by_css_selector(selector)

# Elements with a matching 'id' attribute value
browser.find_element_by_id(id)
browser.find_elements_by_id(id)

# <a> elements that completely match the 'text' provided
browser.find_element_by_link_text(text)
browser.find_elements_by_link_text(text)

# <a> elements that contain the 'text' provided
browser.find_element_by_partial_link_text(text)
browser.find_elements_by_partial_link_text(text)

# Elements with a matching 'name' attribute value
browser.find_element_by_name(name)
browser.find_elements_by_name(name)

# Elements with a matching tag 'name' (case insensitive; an <a> element is matched by 'a' and 'A')
browser.find_element_by_tag_name(name)
browser.find_elements_by_tag_name(name)

try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <{}> element with that class name!'.format(elem.tag_name))
except:
    print('Was not able to find an element with that name.')

# Find link tag and then click it
linkElem = browser.find_element_by_link_text('Read It Online')
linkElem.click()

# Filling out and submitting forms
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
passwordElem.submit()
# emailElem.submit()

# Special keys
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) # scrolls to bottom
htmlElem.send_keys(Keys.HOME) # scrolls to top

# Clicking browser buttons
browser.back()
browser.forward()
browser.refresh()
browser.quit()
