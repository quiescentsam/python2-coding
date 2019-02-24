import random

def rand5():
    return random.randint(0,5)


def rand7():
    return ((rand5() + rand5() + rand5() + rand5() + rand5() + rand5() + rand5()) % 7 )


if __name__ == '__main__':
    print rand5()
    print rand7()

