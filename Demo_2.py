import os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

base_path = os.path.dirname(os.path.abspath(__file__))
chrome_driver_path = os.path.join(base_path, r"C:\Users\Bacancy\PycharmProjects\Practice_1\chromedriver.exe")

# driver = webdriver.Chrome()
# driver.maximize_window()

options = webdriver.ChromeOptions()
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)

pyautogui.alert("Automation Script is running, Please press OK!")
successarray = []
unsuccesarray = []

try:
    #Context Click
    driver.find_element(By.XPATH, """//*[@id="content"]/ul/li[7]/a""").click()
    time.sleep(3)
    successarray.append("Context Click Test Case Successful")
    print("Context Click Test Case Successful")
except NoSuchElementException:
    unsuccesarray.append("Context Click Test Case Failed")
    print("Context Click Test Case Failed")

try:
    #Box Right Click
    element = driver.find_element(By.XPATH, """//*[@id="hot-spot"]""")
    actions = ActionChains(driver)
    actions.context_click(element).perform()
    # pyautogui.moveTo(399, 500)
    # pyautogui.click()
    time.sleep(1)
    pyautogui.press('Enter')
    # pyautogui.alert("Right Click has successfully called, Click OK!")
    successarray.append("Box Right Click Test Case Successful")
    print("Box Right Click Test Case Successful")
except NoSuchElementException:
    unsuccesarray.append("Box Right Click Test Case Failed")
    print("Box Right Click Test Case Failed")

try:
    for _ in range(10):
        pyautogui.press('down')
        time.sleep(0.5)
        successarray.append("Repetitive Task Successful")
        print("Repetitive Task Successful")
except NoSuchElementException:
    unsuccesarray.append("Repetitive Task Failed")
    print("Repetitive Task Failed")

try:
    pyautogui.press("enter")
    time.sleep(1)
    successarray.append("Enter Key Pressed Task Successful")
    print("Enter Key Task Successful")
except NoSuchElementException:
    unsuccesarray.append("Enter Key Task Failed")
    print("Enter Key Task Failed")

try:
    pyautogui.alert("Browser Will Close Upon Click Of OK!")
    driver.close()
    driver.quit()
    successarray.append("Browser Close Task Successful")
    successarray.append("Browser Close Task Successful")
except NoSuchElementException:
    unsuccesarray.append("Browser Close Task Failed")
    print("Browser Close Task Failed")

print("Array Logs:\n" + "\n".join(successarray))
print("Array Logs:\n" + "\n".join(unsuccesarray))
