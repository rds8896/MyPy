#v1.0.1
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
menu=input("1.CS-1 \n2.CS-2 \n3.English\n")
id=input("Enter Username:")
pwd=input("Enter Password:")

driver = webdriver.Chrome('D:\\Users\Stephen\Dev\Git\Python\chromedriver.exe')

def cs1():
    driver.get("https://www.edusol.colscol.com/mod/attendance/view.php?id=652")
    #login
    id_in=driver.find_element_by_xpath('//*[@id="username"]')
    id_in.send_keys(id)
    pwd_in=driver.find_element_by_xpath('//*[@id="password"]')
    pwd_in.send_keys(pwd)
    #button
    login_button=driver.find_element_by_xpath('//*[@id="loginbtn"]').click()    
    #attendance(submit_your_attendance)
    submit_link = driver.find_elements_by_partial_link_text("Submit")[0].click()
    #present_button
    pr_button=driver.find_element_by_name('status').click()
    #save attendance
    save_button =driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
    #logout
    logout_1=driver.find_element_by_xpath('//*[@id="dropdown-1"]/span/span/span/img').click() #
    logout_2=driver.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[6]').click()

def cs2():
    driver.get("https://www.edusol.colscol.com/mod/attendance/view.php?id=651")
    #login
    id_in=driver.find_element_by_xpath('//*[@id="username"]')
    id_in.send_keys(id)
    pwd_in=driver.find_element_by_xpath('//*[@id="password"]')
    pwd_in.send_keys(pwd)
    #button
    login_button=driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
    #attendance(submit_your_attendance)
    submit_link = driver.find_elements_by_partial_link_text("Submit")[0].click()
    #present_button
    pr_button=driver.find_element_by_name('status').click()
    #save attendance
    save_button =driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
    #logout
    logout_1=driver.find_element_by_xpath('//*[@id="dropdown-1"]/span/span/span/img').click()
    logout_2=driver.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[6]').click()

def eng():
    driver.get("https://www.edusol.colscol.com/mod/attendance/view.php?id=1630")
    #login
    id_in=driver.find_element_by_xpath('//*[@id="username"]')
    id_in.send_keys(id)
    pwd_in=driver.find_element_by_xpath('//*[@id="password"]')
    pwd_in.send_keys(pwd)
    #button
    login_button=driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
    #attendance(submit_your_attendance)
    submit_link = driver.find_elements_by_partial_link_text("Submit")[0].click()
    #present_button
    pr_button=driver.find_element_by_name('status').click()
    #save attendance
    save_button =driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
    #logout
    logout_1=driver.find_element_by_xpath('//*[@id="dropdown-1"]/span/span/span/img').click()
    logout_2=driver.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[6]').click()
    
if menu=='1':
    cs1()
elif menu=='2':
    cs2()
elif menu=='3':
    eng()
