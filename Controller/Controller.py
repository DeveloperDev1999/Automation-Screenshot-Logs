import os
import time
import logging
import mss
import pyautogui
import tkinter as tk
from tkinter import filedialog
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Configure Logging
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "script.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logging.info("Starting Test Execution")

# Page Object Model Classes
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def highlight_element(self, element):
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)

class Screencapture:
    def __init__(self, test_name="General"):
        """Initialize the directory paths for a specific test case."""
        self.test_name = test_name
        self.folder_path = os.path.join(os.getcwd(), "Results")
        self.screenshot_dir = os.path.join(self.folder_path, "screenshots", self.test_name)
        os.makedirs(self.screenshot_dir, exist_ok=True)  # Create test-specific directory if not exist

    def get_next_filename(self, base_name="Screenshot", extension=".png"):
        """Find the next available filename by incrementing a counter."""
        counter = 1
        while True:
            screenshot_name = f"{base_name}_{counter}{extension}"
            screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)
            if not os.path.exists(screenshot_path):
                return screenshot_path
            counter += 1

    def capture_screenshot(self, save_path):
        """Captures a screenshot and saves it to the specified path."""
        with mss.mss() as sct:
            sct.shot(output=save_path)

    def screenshots(self):
        """Captures a screenshot and saves it with an auto-incremented filename."""
        screenshot_path = self.get_next_filename()
        self.capture_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.test_link = (By.XPATH, "//*[@id=\"content\"]/ul/li[7]/a")
        self.context_menu = (By.XPATH, "//*[@id=\"hot-spot\"]")
        self.file_upload_page = (By.XPATH, "//*[@id=\"content\"]/ul/li[18]/a")
        self.file_upload_input = (By.XPATH, "//*[@id=\"file-upload\"]")
        self.file_submit_button = (By.XPATH, "//*[@id=\"file-submit\"]")
        self.horizontal_click_locater = (By.XPATH, "//*[@id =\"content\"]/ul/li[24]/a")
        self.horizontal_slider_function = (By.XPATH, "//*[@id=\"content\"]/div/div/input")
        self.slider_call = (By.XPATH, "//*[@id=\"content\"]/div/div/input")

    def navigate(self, url):
        time.sleep(2)
        self.driver.get(url)

    def click_test_link(self):
        element = self.driver.find_element(*self.test_link)
        self.highlight_element(element)
        element.click()

    def right_click_context_menu(self):
        try:
            element = self.driver.find_element(*self.context_menu)
            self.highlight_element(element)
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
            alert = self.driver.switch_to.alert
            logging.info(f"Alert detected: {alert.text}")
            alert.accept()
            logging.info("Right Click Context Menu Test Passed")
        except NoSuchElementException:
            logging.error("Right Click Context Menu Test Failed: Element Not Found")

    def repetitive_task_click(self):
        try:
            for _ in range(10):
                pyautogui.press('down')
                time.sleep(0.5)
                print("Repetitive Task Successful")
            logging.info(f"Repetitive Task Successful")
        except NoSuchElementException:
            print("Repetitive Task Failed")
            logging.error("Repetitive Task Failed")

    def time_sleep2(self):
        time.sleep(2)

    def click_event(self):
        try:
            pyautogui.press("Enter")
            time.sleep(2)
            print("Auto Click Event is Successful")
        except NoSuchElementException:
            print("Auto Click Event Task Failed")

    def tab_switch(self):
        try:
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(2)
            pyautogui.hotkey('alt', 'left')
            time.sleep(2)
            print("Shortcut Action case executed successfully")
        except NoSuchElementException:
            print("Shortcut Action Case Failed")

    def navigate_to_file_upload(self):
        try:
            element = self.driver.find_element(*self.file_upload_page)
            self.highlight_element(element)
            element.click()
            logging.info("Navigated to File Upload Page Successfully")
        except NoSuchElementException:
            logging.error("File Upload Page Navigation Failed")

    def upload_file(self):
        try:
            pyautogui.alert("Please upload your desire file, if you press cancel then default file will be chosen!")
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(title="Select a File to Upload")
            if not file_path:
                file_path = r"C:\Users\Bacancy\PycharmProjects\Practice_1\Test_Execution/dummy.pdf"
                logging.warning("No file selected. Using default file.")
            file_input = self.driver.find_element(*self.file_upload_input)
            self.highlight_element(file_input)
            file_input.send_keys(file_path)
            logging.info("File Selected for Upload")
        except NoSuchElementException:
            logging.error("File Upload Input Field Not Found")

    def submit_file(self):
        try:
            submit_button = self.driver.find_element(*self.file_submit_button)
            self.highlight_element(submit_button)
            submit_button.click()
            logging.info("File Upload Submitted Successfully")
        except NoSuchElementException:
            logging.error("File Upload Submission Failed")

    def alert1(self):
        pyautogui.alert("First Test Scenario has completed, Press OK to to start next Test Scenario.")
        self.driver.quit()

    def alert2(self):
        pyautogui.alert("Second Test Scenario has completed, Press OK to to start next Test Scenario.")
        self.driver.quit()

    def alert_end(self):
        pyautogui.alert("All Test Scenarios have been executed, Press OK to Close the Browser.")
        self.driver.quit()

    def horizontal_click(self):
        try:
            pyautogui.press('End')
            element = self.driver.find_element(*self.horizontal_click_locater)
            self.highlight_element(element)
            element.click()
            logging.info("Horizontal Slider Page Loaded Successfully")
        except NoSuchElementException:
            logging.error("Horizontal Slider Page Load Has Failed")

    def horizontal_function_down(self):
        try:
            sliding = self.driver.find_element(*self.slider_call)
            self.highlight_element(sliding)
            sliding.click()
            for _ in range(10):
                pyautogui.press('right')
                time.sleep(0.2)
                print("Right Slider Call Successful")
            logging.info(f"Right Slider Call Successful")
        except NoSuchElementException:
            print("Right Slider Call Failed")
            logging.error("Right Slider Call Failed")

    def horizontal_function_up(self):
        try:
            sliding = self.driver.find_element(*self.slider_call)
            self.highlight_element(sliding)
            sliding.click()
            for _ in range(10):
                pyautogui.press('left')
                time.sleep(0.2)
                print("Right Slider Call Successful")
            logging.info(f"Right Slider Call Successful")
        except NoSuchElementException:
            print("Right Slider Call Failed")
            logging.error("Right Slider Call Failed")
