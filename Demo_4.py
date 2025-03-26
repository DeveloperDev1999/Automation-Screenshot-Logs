import os
import time
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pyautogui

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

def highlight_element(driver, element):
    """Highlights a web element by adding a red border using JavaScript."""
    driver.execute_script("arguments[0].style.border='3px solid red'", element)

def take_screenshot_and_log(driver, test_case_name):
    """Captures a screenshot and logs test execution details."""

    # Create a unique screenshot filename
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = os.path.join(screenshot_dir, f"{test_case_name}_{timestamp}.png")

    try:
        logging.info(f"Starting test case: {test_case_name}")
        driver.get("https://the-internet.herokuapp.com/")  # Open the website
        logging.info("Website loaded successfully")

        # Take and save the screenshot
        driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved at: {screenshot_path}")

        # Test case passed
        logging.info("Test case passed")
        print("Website Loaded Test Case Successful")

    except Exception as e:
        logging.error(f"Test case failed with error: {e}")
        print("Website Loaded Test Case Failed")

    try:
        logging.info(f"Click Event Test Case: {test_case_name}")

        # Locate the element
        element_xpath = """//*[@id="content"]/ul/li[7]/a"""  # Xpath of the element
        element_xpath2 = """//*[@id="hot-spot"]"""
        element_xpath3 = """//*[@id="hot-spot"]"""

        try:
            element = driver.find_element(By.XPATH, element_xpath)
            highlight_element(driver, element)
            time.sleep(1)  # Pause to ensure highlight is visible
            screenshot_path = os.path.join(screenshot_dir, f"screenshot_{int(time.time())}.png")
            driver.save_screenshot(screenshot_path)
            logging.info(f"Screenshot saved at: {screenshot_path}")
            element.click()
            time.sleep(3)
            logging.info("Click Event Test Case Passed")
            print("Click Event Test Case Successful")

        except NoSuchElementException:
            logging.error(f"Context Click Test Case Failed: Element not found at {element_xpath}")
            failure_screenshot_path = os.path.join(screenshot_dir, f"context_click_failed_{timestamp}.png")
            driver.save_screenshot(failure_screenshot_path)
            logging.info(f"Failure screenshot saved at: {failure_screenshot_path}")
            print("Click Event Test Case Failed")

        try:
            element = driver.find_element(By.XPATH, element_xpath2)
            highlight_element(driver, element)
            time.sleep(1)
            screenshot_path = os.path.join(screenshot_dir, f"screenshot_{int(time.time())}.png")
            driver.save_screenshot(screenshot_path)
            element.click()
            logging.info("Box Right Click Test Case Successful")
            print("Box Right Click Test Case Successful")

        except NoSuchElementException:
            logging.error(f"Box Right Click Test Case Failed: Element not found at {element_xpath2}")
            failure_screenshot_path = os.path.join(screenshot_dir, f"Box_Right_Click_{timestamp}.png")
            driver.save_screenshot(failure_screenshot_path)
            logging.info(f"Failure screenshot saved at: {failure_screenshot_path}")
            print("Box Right Click Test Case Failed")

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
