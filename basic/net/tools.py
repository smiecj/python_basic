# sort array
def get_local_ip():
    import socket
    return socket.gethostbyname(socket.gethostname())


if __name__ == '__main__':
    print(get_local_ip())