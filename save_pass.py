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
        create_user_file(mid)
    else:
        print("Don't same password! Please again.")


def create_user_file(name):
    path_w = 'user.txt'
    with open(path_w, mode='w') as f:
        f.write(name)


if __name__ == '__main__':
    save_password_to_os()
