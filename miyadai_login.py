"""
selenium自動ログイン
"""
import platform

from selenium import webdriver
import keyring
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(mid):
    if keyring.get_password('keyring_selenium', mid) is None:
        print("Please store your login info!",)
        print("Run script in terminal: pipenv python save_pass.py")
        return

    # WebDriverのパスを指定してChromeを起動
    os_name = platform.system()
    if os_name == "Darwin":
        driver_pass = "bin/chromedriver_mac_v2_41"
    elif os_name == "Linux":
        driver_pass = "bin/chromedriver_linux_v2_41"
    elif os_name == "Windows":
        driver_pass = "bin/chromedriver_win32_v2_41.exe"
    else:
        print("Unknown System. Please send Issue.")
        return
    driver = webdriver.Chrome(driver_pass)

    # Yahooのページをブラウザで開きます
    miyadai_url = "https://www.miyazaki-u.ac.jp/"
    driver.get(miyadai_url)
    print(driver.current_url)
    try:
        WebDriverWait(driver, 10).until(lambda driver: driver.current_url != miyadai_url)
        login_url = driver.current_url
        print(login_url)
        input_mid = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-username")))
        print(driver.current_url)
    except TimeoutException:
        print("Already login or don't connecting.")
        driver.quit()
        return

    input_mid.send_keys(mid)
    input_pass = driver.find_element_by_id("login-password")
    input_pass.send_keys(keyring.get_password('keyring_selenium', mid))

    # 検索ボタン要素の取得
    button_login = driver.find_element_by_id("btn-login")

    # 検索ボタンをクリックする
    button_login.click()

    try:
        WebDriverWait(driver, 10).until(lambda driver: driver.current_url != login_url)
        print(driver.current_url)
    except TimeoutException:
        print("Failed login. Please check MID or password.")
    driver.quit()
    return


def read_user_file():
    path = 'user.txt'
    with open(path, mode='r') as f:
        name = f.readline()
    return name


if __name__ == '__main__':
    mid = read_user_file()
    login(mid)
