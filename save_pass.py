from getpass import getpass

import keyring


def save_password_to_os():
    mid = input("Please input MID: ")
    password = getpass(prompt='Please input password(It does not display): ')
    retry_password = getpass(prompt='Please input password again(It does not display): ')

    # OSにパスワード保存(1回実行すれば良い)
    if password == retry_password:
        keyring.set_password('keyring_selenium', mid, password)
        print("Success! Store your login info.")
    else:
        print("Don't same password! Please again.")


if __name__ == '__main__':
    save_password_to_os()
