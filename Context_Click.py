import logging
from selenium import webdriver
from Controller import HomePage, Screencapture

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    homepage = HomePage(driver)

    screenshot_obj = Screencapture()

    homepage.navigate("https://the-internet.herokuapp.com/")
    screenshot_obj.screenshots()
    homepage.time_sleep2()

    homepage.click_test_link()
    screenshot_obj.screenshots()
    homepage.time_sleep2()

    homepage.right_click_context_menu()
    screenshot_obj.screenshots()
    homepage.time_sleep2()

    homepage.repetitive_task_click()
    screenshot_obj.screenshots()
    homepage.time_sleep2()

    homepage.click_event()
    screenshot_obj.screenshots()
    homepage.time_sleep2()

    logging.info("First Test Execution Completed Successfully.")
    print("First Test Execution Completed Successfully.")
    print("Please Wait To Start Next Execution.")

    homepage.alert()

if __name__ == "__main__":
    main()
