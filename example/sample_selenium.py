"""
seleniumチュートリアル
参考：https://www.inet-solutions.jp/technology/python-selenium/
"""

# webdriverモジュールをインポート
from selenium import webdriver


def main():
    # WebDriverのパスを指定してChromeを起動
    driver = webdriver.Chrome("bin/chromedriver_mac_v2_41")

    # Yahooのページをブラウザで開きます
    driver.get("http://www.yahoo.co.jp")

    """6行目は入力したいテキストフィールドの要素を取得しています。
    このページのHTMLソースを見ると、検索語を入力するテキストフィールドのIDがsrchtxtということがわかるので、
    find_element_by_idメソッドを使ってこの要素を取得します。"""
    elem_search_word = driver.find_element_by_id("srchtxt")

    """7行目は取得した要素にsend_keysメソッドを使ってseleniumという文字を入力しています。"""
    elem_search_word.send_keys("selenium")

    # 検索ボタン要素の取得
    elem_search_btn = driver.find_element_by_id("srchbtn")

    # 検索ボタンをクリックする
    elem_search_btn.click()

    elements_a = driver.find_elements_by_css_selector("#WS2m .w .hd h3 a")
    for elem in elements_a:
        url = elem.get_property("href")
        print(url)


if __name__ == '__main__':
    main()
