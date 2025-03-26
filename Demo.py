from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = webdriver.Chrome()
driver.get("https://bacancy.keka.com/#/me/attendance/logs")
time.sleep(5)

pyautogui.alert("Automation Script is running, Please press OK!")

successarray = []
unsuccesarray = []
try:
    #Login Click
    driver.find_element(By.XPATH, """/html/body/div/div[2]/div[1]/div[2]/div/div[2]/button""").click()
    time.sleep(3)
    successarray.append("Login Test Case Successfull")
    print("Login Test Case Successfull")
except NoSuchElementException:
    unsuccesarray.append("Login Test Case Failed")
    print("Login Test Case Failed")

try:
    #Login with Email
    driver.find_element(By.XPATH, """//*[@id="identifierId"]""").send_keys("devarsh.shah@bacancy.com")
    time.sleep(3)
    successarray.append("Login with Email Test Case Successfull")
    print("Login with Email Test Case Successfull")
except NoSuchElementException:
    unsuccesarray.append("Login with Email Test Case Failed")
    print("Login with Email Test Case Failed")

try:
    #Next Button
    driver.find_element(By.XPATH, """//*[@id="identifierNext"]/div/button/span""").click()
    time.sleep(3)
    successarray.append("Next Button Test Case Successfull")
    print("Next Button Test Case Successfull")
except NoSuchElementException:
    unsuccesarray.append("Next Button Test Case Failed")
    print("Next Button Test Case Failed")

try:
    #Login with Password
    driver.find_element(By.XPATH, """//*[@id="password"]/div[1]/div/div[1]/input""").send_keys("Developer@22")
    # pyautogui.alert("Please enter the CAPTCHA, bot will wait for 15 seconds upon selecting OK!")
    time.sleep(3)
    successarray.append("Login with Password Test Case Successfull")
    print("Login with Password Test Case Successfull")
except NoSuchElementException:
    unsuccesarray.append("Login with Password Test Case Failed")
    print("Login with Password Test Case Failed")

try:
    #Next Button - 2
    driver.find_element(By.XPATH, """//*[@id="passwordNext"]/div/button/span""").click()
    time.sleep(7)
    successarray.append("Next Button - 2 Test Case Successfull")
    print("Next Button - 2 Test Case Successfull")
except NoSuchElementException:
    unsuccesarray.append("Next Button - 2 Test Case Failed")
    print("Next Button - 2 Test Case Failed")

try:
    #Inbox Click
    driver.find_element(By.XPATH, """//*[@id="accordion"]/li[3]/a/span[1]""").click()
    time.sleep(3)
    successarray.append("Inbox Click Test Case Successfull")
    print("Inbox Click Test Case Successfull")
except NoSuchElementException:
    unsuccesarray.append("Inbox Click Test Case Failed")
    print("Inbox Click Test Case Failed")

finally:
    pyautogui.alert("Script is completed, Please press OK to quit the browser!")
    driver.quit()


print("Array Logs:\n" + "\n" .join(successarray))
print("Array Logs:\n" +"\n" .join(unsuccesarray))
