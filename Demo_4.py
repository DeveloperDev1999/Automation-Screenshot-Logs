import os
import time
import logging
import mss
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
from tkinter import filedialog


def capture_screenshot(save_path):
    with mss.mss() as sct:
        sct.shot(output=save_path)


# Ask user for the folder path
pyautogui.alert("Please enter the path after clicking OK Button!")
folder_path = input("Enter the folder path to save screenshots and logs: ").strip()
if not folder_path:
    pyautogui.alert("Default Path will be taken as no input is given")
    folder_path = os.path.join(os.getcwd(), "Results")  # Default to "Results" in the script directory

# Ensure directories exist
screenshot_dir = os.path.join(folder_path, "screenshots")
log_dir = os.path.join(folder_path, "logs")

os.makedirs(screenshot_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

# Configure logging once
log_file = os.path.join(log_dir, "script.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logging.info(f"Logs will be saved in: {log_file}")

Success = []
Unsuccess = []


def highlight_element(driver, element):
    """Highlights a web element by adding a red border using JavaScript."""
    driver.execute_script("arguments[0].style.border='3px solid red'", element)


def take_screenshot_and_log(driver, test_case_name):
    """Captures a screenshot and logs test execution details."""

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = os.path.join(screenshot_dir, f"{test_case_name}_{timestamp}.png")

    try:
        logging.info(f"Starting test case: {test_case_name}")
        driver.get("https://the-internet.herokuapp.com/")  # Open the website
        logging.info("Website loaded successfully")

        driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved at: {screenshot_path}")
        print("Website Loaded Test Case Successful")

    except Exception as e:
        logging.error(f"Test case failed with error: {e}")
        print("Website Loaded Test Case Failed")

    try:
        logging.info(f"Click Event Test Case: {test_case_name}")
        element_xpath = "//*[@id=\"content\"]/ul/li[7]/a"
        element_xpath2 = "//*[@id=\"hot-spot\"]"
        element_xpath3 = "//*[@id=\"content\"]/ul/li[18]/a"
        # element_xpath4 = "//*[@id=\"drag-drop-upload\"]"
        element_xpath4 = "//*[@id=\"file-upload\"]"
        element_xpath5 = "//*[@id=\"file-submit\"]"

        try:
            element = driver.find_element(By.XPATH, element_xpath)
            highlight_element(driver, element)
            time.sleep(1)
            driver.save_screenshot(screenshot_path)
            element.click()
            time.sleep(3)
            logging.info("Click Event Test Case Passed")
            Success.append("Click Event Test Case Passed")
            print("Click Event Test Case Successful")
        except NoSuchElementException:
            logging.error(f"Context Click Test Case Failed: Element not found at {element_xpath}")
            Unsuccess.append("Click Event Test Case Failed")
            print("Click Event Test Case Failed")

        try:
            element = driver.find_element(By.XPATH, element_xpath2)
            highlight_element(driver, element)
            time.sleep(1)
            actions = ActionChains(driver)
            actions.context_click(element).perform()
            time.sleep(2)

            menu_screenshot_path = os.path.join(screenshot_dir, "alert.png")
            capture_screenshot(menu_screenshot_path)
            logging.info(f"Context menu screenshot saved at: {menu_screenshot_path}")

            alert = driver.switch_to.alert
            print(f"Alert detected: {alert.text}")
            alert.accept()
            print("Alert accepted.")
            Success.append("Alert Detected and Accepted")
            element.click()
            time.sleep(2)
            pyautogui.press('Enter')
            time.sleep(1)
            menu_screenshot_path = os.path.join(screenshot_dir, "context_menu.png")
            capture_screenshot(menu_screenshot_path)
            logging.info("Box Right Click Test Case Successful")
            Success.append("Box Right Click Test Case Successful")
            print("Box Right Click Test Case Successful")
        except NoSuchElementException:
            logging.error(f"Box Right Click Test Case Failed: Element not found at {element_xpath2}")
            menu_screenshot_path = os.path.join(screenshot_dir, "alert_failed.png")
            capture_screenshot(menu_screenshot_path)
            time.sleep(1)
            menu_screenshot_path = os.path.join(screenshot_dir, "context_menu_failed.png")
            capture_screenshot(menu_screenshot_path)
            Unsuccess.append("Box Right Click Test Case Failed")
            print("Box Right Click Test Case Failed")

        try:
            for _ in range(9):
                pyautogui.press('down')
                time.sleep(0.5)
                Success.append("Repetitive Click is Successful")
                print("Repetitive Task Successful")
        except NoSuchElementException:
            Unsuccess.append("Repetitive Click Has Failed")
            print("Repetitive Task Failed")

        try:
            pyautogui.press("Enter")
            time.sleep(2)
            menu_screenshot_path = os.path.join(screenshot_dir, "source_code.png")
            capture_screenshot(menu_screenshot_path)
            Success.append("Auto Click Event is Successful")
            print("Auto Click Event is Successful")
        except NoSuchElementException:
            menu_screenshot_path = os.path.join(screenshot_dir, "source_code_failed.png")
            capture_screenshot(menu_screenshot_path)
            Unsuccess.append("Auto Click Event Has Failed")
            print("Auto Click Event Failed")

        try:
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(2)
            pyautogui.hotkey('alt', 'left')
            time.sleep(2)
            Success.append("Shortcut Action case executed successfully")
            print("Shortcut Action case executed successfully")
        except NoSuchElementException:
            Unsuccess.append("Shortcut Action Case Failed")
            print("Shortcut Action Case Failed")

        try:
            element = driver.find_element(By.XPATH, element_xpath3)
            highlight_element(driver, element)
            time.sleep(1)
            element.click()
            time.sleep(1)
            menu_screenshot_path = os.path.join(screenshot_dir, "file_upload.png")
            capture_screenshot(menu_screenshot_path)
            logging.info(f"File Upload Screenshot Saved At: {menu_screenshot_path}")
            Success.append("File Upload Click Test Case Successful")
            print("File Upload Click Test Case Successful")
        except NoSuchElementException:
            menu_screenshot_path = os.path.join(screenshot_dir, "file_upload_failed.png")
            capture_screenshot(menu_screenshot_path)
            logging.error(f"File Upload Click Test Case Failed: Element not found at {element_xpath3}")
            Unsuccess.append("File Upload Click Test Case Failed")
            print("File Upload Click Test Case Failed")

        try:
            pyautogui.alert("Please provide the file to upload or default file will be taken!")
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            # Open file dialog and get selected file path
            file_path = filedialog.askopenfilename(title="Select a File to Upload")
            if file_path:  # If user selects a file
                file_input = driver.find_element(By.XPATH, '//*[@id="file-upload"]')
                file_input.send_keys(file_path)  # Upload selected file
            else:
                element = driver.find_element(By.XPATH, element_xpath4)
                highlight_element(driver, element)
                time.sleep(3)
                element.send_keys(r"C:\Users\Bacancy\PycharmProjects\Practice_1\dummy.pdf")
                print("No file selected!")

            menu_screenshot_path = os.path.join(screenshot_dir, "choose_file.png")
            capture_screenshot(menu_screenshot_path)
            logging.info(f"File Upload Screenshot Saved At: {menu_screenshot_path}")
            pyautogui.press("Enter")
            Success.append("Choose File Click Event Test Case Successful")
            print("Choose File Click Event Test Case Successful")
        except NoSuchElementException:
            menu_screenshot_path = os.path.join(screenshot_dir, "choose_file_failed.png")
            capture_screenshot(menu_screenshot_path)
            logging.error(f"Choose File Click Event Test Case: Element not found at {element_xpath4}")
            Unsuccess.append("Choose File Click Event Test Case Failed")
            print("Choose File Click Event Test Case Failed")

        try:
            element = driver.find_element(By.XPATH, element_xpath5)
            highlight_element(driver, element)
            time.sleep(1)
            element.click()
            time.sleep(3)
            menu_screenshot_path = os.path.join(screenshot_dir, "upload_file.png")
            capture_screenshot(menu_screenshot_path)
            logging.info(f"File Uploaded Screenshot Saved At: {menu_screenshot_path}")
            Success.append("File Upload Test Case Successful")
            print("File Upload Test Case Successful")
        except NoSuchElementException:
            menu_screenshot_path = os.path.join(screenshot_dir, "upload_file_failed.png")
            capture_screenshot(menu_screenshot_path)
            logging.error(f"File Uploaded Test Case: Element not found at {element_xpath5}")
            Unsuccess.append("File Uploaded Test Case Failed")
            print("File Uploaded Test Case Failed")

        try:
            pyautogui.alert("Test Execution Has Completed Please Press OK!")
            Success.append("Test Execution Alert Is Successful")
            print("Test Execution Alert Is Successful")
        except NoSuchElementException:
            Unsuccess.append("Test Execution Alert Has Failed")
            print("Alert is not working and has failed to close the browser")
    finally:
        logging.info("Test case execution completed.")


# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Run the test
take_screenshot_and_log(driver, "TestCase")

# Close WebDriver
driver.quit()
logging.info("Browser closed")

print("Array Logs:")
print("\n".join(Success))
print("\n".join(Unsuccess))
