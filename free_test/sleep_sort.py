import threading
import time


def haha(num, list_out:list):
    time.sleep(num/1000)
    print(f"{num}")
    list_out.append(num)


if __name__ == '__main__':
    list_in = [1, 223, 443, 535, 54, 5, 355, 111]
    list_out = []
    for x in list_in:
        t = threading.Thread(target=haha, args=(x, list_out))
        t.start()
    time.sleep(2)
    print(list_out)