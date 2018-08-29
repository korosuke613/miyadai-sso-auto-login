# miyadai-sso-auto-login
miyadai-sso-auto-login is auto login system in University of Miyazaki.

![](https://github.com/korosuke613/miyadai-sso-auto-login/blob/master/images/use.gif)

## install
Please install Python3.6.6 in advance.
Don't work Python3.7 for Windows.

### Windows
1. Open PowerShell with Administrator.
2. Run `pip install pipenv`
3. Run `git clone --depth=1 https://github.com/korosuke613/miyadai-sso-auto-login.git`
4. Run `cd miyadai-sso-auto-login`
5. Run `pipenv install`
6. Run `pipenv run python ./save_pass.py`
7. Run `pipenv run python ./miyadai_login.py`
8. Perform clone setting.(参照: [Windowsで定期自動ログインする
](https://github.com/korosuke613/miyadai-sso-auto-login/wiki/Windows%E3%81%A7%E5%AE%9A%E6%9C%9F%E8%87%AA%E5%8B%95%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%99%E3%82%8B))

### Linux
1. Open terminal.
2. Run `sudo pip install secretstorage`
3. Run `sudo pip install pipenv`
4. Run `git clone --depth=1 https://github.com/korosuke613/miyadai-sso-auto-login.git`
5. Run `cd miyadai-sso-auto-login`
6. Run `pipenv install`
7. Run `pipenv run python ./save_pass.py`
8. Run `pipenv run python ./miyadai_login.py`
9. Perform clone setting.(参照: [Ubuntuで定期自動ログインする
](https://github.com/korosuke613/miyadai-sso-auto-login/wiki/Ubuntu%E3%81%A7%E5%AE%9A%E6%9C%9F%E8%87%AA%E5%8B%95%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%99%E3%82%8B))

### Raspbian

__!!!Caution!!!__
This script cannot run at Raspberry Pi ZERO!
Please run at Raspberry Pi using __armv7l__!

Checking method: Run `uname -a`

1. Open terminal
1. Run `sudo apt install libffi-dev`
1. Run `sudo pip install cffi`
1. Run `sudo pip install secretstorage`
1. Run `sudo pip install pipenv`
1. Install chromedriver
    1. Run `sudo apt install chromium-chromedriver`
    1. If the above is OK, next 7
    1. Else, run `wget https://github.com/electron/electron/releases/download/v1.6.0/chromedriver-v2.21-linux-armv7l.zip`
    1. Run `unzip chromedriver-v2.21-linux-armv7l.zip -d /open/your/path/chromedriver`
1. Run `git clone --depth=1 https://github.com/korosuke613/miyadai-sso-auto-login.git`
1. Run `cd miyadai-sso-auto-login`
1. Edit 17 line to `        driver_path = "/path/in/your/chromedriver/chromedriver"` in miyadai_login_in_raspbian.py
1. Run `pipenv --python 3.6.6 install`
1. Run `pipenv install selenium`
1. Run `pipenv run python ./save_pass_in_raspbian.py`
1. Run `pipenv run python ./miyadai_login_in_raspbian.py`
1. Perform clone setting.(参照: [Ubuntuで定期自動ログインする
](https://github.com/korosuke613/miyadai-sso-auto-login/wiki/Ubuntu%E3%81%A7%E5%AE%9A%E6%9C%9F%E8%87%AA%E5%8B%95%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%99%E3%82%8B))
