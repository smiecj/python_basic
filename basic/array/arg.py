# sort array
def sort_array():
    test_str_array = ["10.20.10.3", "10.20.10.2", "10.20.10.1"]
    print("before sort arr: {}".format(test_str_array))
    test_str_array.sort()
    print("after sort arr: {}".format(test_str_array))


if __name__ == '__main__':
    sort_array()