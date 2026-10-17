
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import pytest
import time


@pytest.fixture
def setup_teardown():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Selenium Manager automatically manages ChromeDriver
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


def get_alert_text(driver):
    alert = Alert(driver)
    text = alert.text
    alert.accept()
    return text


def test_empty_username(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "pwd").send_keys("Password123")
    driver.find_element(By.NAME, "sb").click()

    time.sleep(1)

    assert get_alert_text(driver) == "Username cannot be empty."


def test_short_password(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "username").send_keys("Tanzila")
    driver.find_element(By.NAME, "pwd").send_keys("abc1")
    driver.find_element(By.NAME, "sb").click()

    time.sleep(1)

    assert get_alert_text(driver) == (
        "Password must be at least 6 characters long."
    )


def test_valid_input(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "username").send_keys("Tanzila")
    driver.find_element(By.NAME, "pwd").send_keys("abc123")
    driver.find_element(By.NAME, "sb").click()

    time.sleep(2)

    assert "/submit" in driver.current_url

    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Hello, Tanzila! Welcome to the website" in body_text
