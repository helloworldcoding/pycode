#!/usr/bin/python3
# encoding:utf-8


def manual_iter(file_path='/etc/passwd'):
    with open(file_path, 'r') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


def manual_iter2(file_path='/usr/local'):
    try:
        with dir(file_path) as f:
            while True:
                line = next(f, None)  # 用None来指定标记结尾
                if line is None:
                    break
                print(line, end='')
    except Exception as err:
        print(err)


# manual_iter()
# manual_iter2()

items = [1, 3, 4]
it = iter(items)
