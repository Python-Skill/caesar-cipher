# create by Egoshin Alexey 07/2022
# encoding: UTF-8


def show_info():
    print(
        "Шифр Цезаря.",
        "Автор: Алексей Егошин alexegoshin0403@yandex.ru",
        sep='\n')


def caesar_cipher(value: str, key: int):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    result = ""

    for i in range(len(value)):
        if value[i] in alphabet:
            index = alphabet.find(value[i])

            index += key

            if index > len(alphabet):
                index -= len(alphabet)
            elif index < 0:
                index += len(alphabet)

            result += alphabet[index]
        else:
            result += value[i]

    return result


def main():
    show_info()


if __name__ == '__main__':
    main()
