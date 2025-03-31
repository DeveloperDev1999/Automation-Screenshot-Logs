import logging
from selenium import webdriver
from Controller.Controller import HomePage, Screencapture

def main3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    homepage = HomePage(driver)

    screenshot = Screencapture(test_name="Horizontal_Click")  # Separate folder for this test

    homepage.navigate("https://the-internet.herokuapp.com/")
    homepage.time_sleep2()

    homepage.horizontal_click()
    screenshot.screenshots()
    homepage.time_sleep2()

    homepage.horizontal_function_down()
    screenshot.screenshots()

    homepage.horizontal_function_up()
    screenshot.screenshots()

    logging.info("Test Execution Completed Successfully.")
    print("Test Execution Completed Successfully.")

    homepage.alert_end()

if __name__ == "__main__":
    main3()
