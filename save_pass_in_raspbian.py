from getpass import getpass


def save_password_to_os():
    mid = input("Please input MID: ")
    password = getpass(prompt='Please input password(It does not display): ')
    retry_password = getpass(prompt='Please input password again(It does not display): ')

    # OSにパスワード保存(1回実行すれば良い)
    if password == retry_password:
        create_user_file(mid, password)
        print("Success! Store your login info.")
    else:
        print("Don't same password! Please again.")


def create_user_file(name, passwd):
    path_w = 'user.txt'
    with open(path_w, mode='w') as f:
        f.write(name)
        f.write('\n')
        f.write(passwd)


if __name__ == '__main__':
    save_password_to_os()
