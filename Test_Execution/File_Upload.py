import logging
from selenium import webdriver
from Controller.Controller import HomePage, Screencapture

def main2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    homepage = HomePage(driver)

    screenshot = Screencapture(test_name="File_Upload")  # Separate folder for this test

    homepage.navigate("https://the-internet.herokuapp.com/upload")
    screenshot.screenshots()
    homepage.time_sleep2()

    homepage.navigate_to_file_upload()
    screenshot.screenshots()
    homepage.time_sleep2()

    homepage.upload_file()
    screenshot.screenshots()
    homepage.time_sleep2()

    homepage.submit_file()
    screenshot.screenshots()
    homepage.time_sleep2()

    logging.info("Second Test Execution Completed Successfully.")
    print("Second Test Execution Completed Successfully.")
    print("Please Wait To Start Next Execution.")

    homepage.alert2()

if __name__ == "__main__":
    main2()
