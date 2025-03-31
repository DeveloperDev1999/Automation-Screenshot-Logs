import logging
from selenium import webdriver
from Controller.Controller import HomePage, Screencapture

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    homepage = HomePage(driver)

    screenshot = Screencapture(test_name="Context_Click")  # Separate folder for this test

    homepage.navigate("https://the-internet.herokuapp.com/")
    screenshot.screenshots()
    homepage.time_sleep2()

    homepage.click_test_link()
    screenshot.screenshots()
    homepage.time_sleep2()

    homepage.right_click_context_menu()
    screenshot.screenshots()
    homepage.time_sleep2()

    homepage.repetitive_task_click()
    screenshot.screenshots()
    homepage.time_sleep2()

    homepage.click_event()
    screenshot.screenshots()
    homepage.time_sleep2()

    logging.info("First Test Execution Completed Successfully.")
    print("First Test Execution Completed Successfully.")
    print("Please Wait To Start Next Execution.")

    homepage.alert1()

if __name__ == "__main__":
    main()
