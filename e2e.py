from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import sys


def test_scores_service(app_url):
    # נתיב לקובץ chromedriver.exe שלך
    chrome_driver_path = "C:/Users/sergey.b/chromedriver/win64-125.0.6422.142/chromedriver-win64/chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(app_url)

    try:
        # נסה למצוא את האלמנט עם ה-ID "score"
        score_element = driver.find_element(By.ID, "score")
        score = score_element.text
        score = int(score)
        if 1 <= score <= 1000:
            print(f"Score is within range: {score}")
            return True
        else:
            print(f"Score is out of range: {score}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

    return False


def main_function():
    app_url = "http://localhost:8777"
    test_result = test_scores_service(app_url)
    if test_result:
        return 0
    else:
        return -1


if __name__ == "__main__":
    sys.exit(main_function())
