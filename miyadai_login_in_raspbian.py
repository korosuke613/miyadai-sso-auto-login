"""
selenium自動ログイン
"""
import platform

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(mid):
    # WebDriverのパスを指定してChromeを起動
    os_name = platform.system()
    if os_name == "Linux":
        driver_path = ""
    else:
        print("Unknown System. Please send Issue.")
        return
    if driver_path is "":
        print("Please edit driver_path in 17 line!")
        return
    driver = webdriver.Chrome(driver_path)
    driver.set_page_load_timeout(10)

    try:
        # 宮崎大学公式ホームページをブラウザで開きます
        miyadai_url = "https://www.miyazaki-u.ac.jp/"
        driver.get(miyadai_url)
        print(driver.current_url)

        WebDriverWait(driver, 10).until(lambda driver: driver.current_url != miyadai_url)
        login_url = driver.current_url
        print(login_url)
        input_mid = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-username")))
        print(driver.current_url)
    except TimeoutException:
        print("Already login or don't connecting.")
        driver.quit()
        return

    input_mid.send_keys(mid[0])
    input_pass = driver.find_element_by_id("login-password")
    input_pass.send_keys(mid[1])

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
    name_and_path = [];
    with open(path, mode='r') as f:
        name_and_path.append(f.readline().replace('\n', ''))
        name_and_path.append(f.readline())
    return name_and_path


if __name__ == '__main__':
    mid = read_user_file()
    login(mid)
