import keyring


def main():
    # OSにパスワード保存(1回実行すれば良い)
    keyring.set_password('keyring_selenium', 'hirakoba', 'aaaaa')

    # パスワード取り出し
    print(keyring.get_password('keyring_test', 'hirakoba'))


if __name__ == '__main__':
    main()
