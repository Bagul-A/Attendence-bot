from selenium import webdriver
import time
import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

def attend(link):
    b.get(link)
    time.sleep(3)
    try :
        attendence = b.find_element_by_css_selector('td.lastcol:nth-child(3) > a:nth-child(1)')
        attendence.click()
        b.find_element_by_name('status').click()
        b.find_element_by_css_selector('#id_submitbutton').click()
    except NoSuchElementException:
        pass
'''change teachers according to classes down here'''

mahesh = 'http://moodle.mitsgwalior.in/mod/attendance/view.php?id=49974'
amit = 'http://moodle.mitsgwalior.in/mod/attendance/view.php?id=48695'
pooja = 'http://moodle.mitsgwalior.in/mod/attendance/view.php?id=48687'
maheshlab = 'http://moodle.mitsgwalior.in/mod/attendance/view.php?id=49009'
ankita = 'http://moodle.mitsgwalior.in/mod/attendance/view.php?id=48649'
puneet = 'http://moodle.mitsgwalior.in/mod/attendance/view.php?id=49155'

now = datetime.datetime.now()
'''change classs timing in the if loop here. Time is compared in hours so for  a class from 12 to 1PM setting end time as 12 works because in 12:59 we get hour as 12 '''
if 10 <= now.hour and now.hour <= 12:
    name = input("ENter your id: ")
    pa = input("Enter password: ")
    print('Automated attendence initialised')
    while True:
        now = datetime.datetime.now()
        '''you can change time here as well'''
        if 10 <= now.hour and now.hour <= 12:
            options= Options()
            options.headless = True
            b= webdriver.Firefox(options=options)
            b.get('http://moodle.mitsgwalior.in/login/index.php')
            user= b.find_element_by_id('username')
            user.send_keys(name)
            passw= b.find_element_by_id('password')
            passw.send_keys(pa)
            passw.submit()
            time.sleep(5)
            '''Got more classes than usual? u can add their attendence as well by using attend(variable name u specified above)'''
            attend(mahesh)
            attend(amit)
            attend(pooja)
            attend(maheshlab)
            attend(puneet)
            attend(ankita)
            b.close()
            time.sleep(600)
        else:
            print('Come again tommorow')
            break
else:
    print('Come again tommorow')