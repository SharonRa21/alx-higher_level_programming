def argv(*args):
    a = ""
    if len(args) <= 1:
        a = "{} argument.".format(len(args))
    else:
        a = "{} arguments:".format(len(args))

    while True:
        print(a)
        for i, n in enumerate(args):
            print("{}: {}".format(i+1, n))
        break

if __name__ == '__main__':
    argv("Sharon", "Sam")
