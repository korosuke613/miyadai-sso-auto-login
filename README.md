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
2. Run `sudo pip install pipenv`
3. Run `git clone --depth=1 https://github.com/korosuke613/miyadai-sso-auto-login.git`
4. Run `cd miyadai-sso-auto-login`
5. Run `pipenv --python 3.6`
6. Run `pipenv install`
7. Run `pipenv run python ./save_pass.py`
8. Run `pipenv run python ./miyadai_login.py`
9. Perform clone setting.(参照: [Windowsで定期自動ログインする
](https://github.com/korosuke613/miyadai-sso-auto-login/wiki/Windows%E3%81%A7%E5%AE%9A%E6%9C%9F%E8%87%AA%E5%8B%95%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%99%E3%82%8B))
