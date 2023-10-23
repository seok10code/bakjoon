ONE = 1


def test(n):
    result = 0
    for i in range(n+ONE):
        result +=i

    return result


if __name__ == '__main__':
    input0 = input()
    print(test(int(input0)))
