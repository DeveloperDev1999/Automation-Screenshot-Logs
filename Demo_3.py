import os
import time
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def setup_logging(log_file_path):
    """Configures logging to write messages to the log file."""
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def highlight_element(driver, element):
    """Highlights a web element by adding a red border using JavaScript."""
    driver.execute_script("arguments[0].style.border='3px solid red'", element)


def take_screenshot_and_log(test_case_name):
    """Creates a unique folder, captures a screenshot, and logs test execution details."""

    # Create a unique folder for each test case
    timestamp = time.strftime("%Y%m%d-%H%M%S")  # Format: YYYYMMDD-HHMMSS
    folder_name = f"screenshots/{test_case_name}_{timestamp}"
    os.makedirs(folder_name, exist_ok=True)

    # Define file paths
    screenshot_path = os.path.join(folder_name, "Website_Load.png")
    log_file_path = os.path.join(folder_name, "test_log.txt")

    # Setup logging only once
    if not logging.getLogger().hasHandlers():
        setup_logging(log_file_path)

    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        logging.info(f"Starting test case: {test_case_name}")
        driver.get("https://the-internet.herokuapp.com/")  # Open the website
        logging.info("Website loaded successfully")

        # Take and save the screenshot
        driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved at: {screenshot_path}")

        # Test case passed
        logging.info("Test case passed")

    except Exception as e:
        logging.error(f"Test case failed with error: {e}")

    try:
        logging.info(f"Click Event Test Case: {test_case_name}")
        # Locate the element
        element_xpath = """//*[@id="content"]/ul/li[7]/a"""  # Xpath of the element
        element_xpath2 = """//*[@id="hot-spot"]"""

        try:
            element = driver.find_element(By.XPATH, element_xpath)
            highlight_element(driver, element)  # Highlight if found
            time.sleep(1)  # Pause to ensure highlight is visible
            screenshot_path = f"screenshots/screenshot_{int(time.time())}.png"
            driver.save_screenshot(screenshot_path)
            logging.info(f"Screenshot saved at: {screenshot_path}")
            logging.info("Click Event Test Case Passed")
            element.click()
            time.sleep(3)
            logging.info("Context Click Test Case Successful")
            print("Context Click Test Case Successful")

        except NoSuchElementException:
            logging.error(f"Context Click Test Case Failed: Element not found at {element_xpath}")
            print(f"Context Click Test Case Failed: Element not found at {element_xpath}")

            # Take failure screenshot of the full page
            failure_screenshot_path = os.path.join(folder_name, "context_click_failed.png")
            driver.save_screenshot(failure_screenshot_path)
            logging.info(f"Failure screenshot saved at: {failure_screenshot_path}")

        try:
            element = driver.find_element(By.XPATH, element_xpath2)
            highlight_element(driver, element)
            screenshot_path = f"screenshots/screenshot_{int(time.time())}.png"
            driver.save_screenshot(screenshot_path)
            logging.info(f"Screenshot saved at: {screenshot_path}")
            logging.info("Box Right Click Test Case Passed")
            time.sleep(1)
            element.click()
            logging.info("Box Right Click Test Case Successful")
            print("Box Right Click Test Case Successful")
        except NoSuchElementException:
            logging.error(f"Box Right Click Test Case Failed: Element not found at {element_xpath2}")
            print(f"Box Right Click Test Case Failed: Element not found at {element_xpath2}")

            failure_screenshot_path = os.path.join(folder_name, "Box_Right_Click.png")
            driver.save_screenshot(failure_screenshot_path)
            logging.info(f"Failure screenshot saved at: {failure_screenshot_path}")

    finally:
        driver.quit()
        logging.info("Browser closed")


# Example usage
take_screenshot_and_log("TestCase")
