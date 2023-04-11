# func_with_args
def func_with_args(name, *args):
    print("name: {}, args len: {}".format(name, len(args)))


# func_with_argv
def func_with_argv(name, *args, **argv):
    print("name: {}, args len: {}, argv len: {}".format(name, len(args), len(argv)))
    for key, value in argv.items():
        print("{} -> {}".format(key, value))
    if "not_exist_key" not in argv:
        print("key not exist")


if __name__ == '__main__':
    func_with_args("test", "1", "2", "3")
    func_with_argv("test", "1", "2", "3", test_key="test_value")