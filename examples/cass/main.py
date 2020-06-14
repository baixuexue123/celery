from app import add


import threading

def main():
    for i in range(5):
        add.delay(3, i)
        # add.apply_async((4, i))
        # add.s(5, i).delay()
        # add.s(6, i).apply_async()


if __name__ == '__main__':
    import time
    st = time.time()

    main()

    print(time.time() - st)
