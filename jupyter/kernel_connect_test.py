"""连接已经打开的 kernel 并执行代码"""

import jupyter_core
kernel_config_path = jupyter_core.paths.jupyter_runtime_dir()
print("kernel folder: {}".format(kernel_config_path))

from os import listdir
from os.path import isfile, join
from os.path import abspath
onlyfiles = [f for f in listdir(kernel_config_path) if isfile(join(kernel_config_path, f)) and "kernel-" in abspath(f)]
for f in onlyfiles:
    print(abspath(f))

kernel_config_file = "/home/jupyter/.local/share/jupyter/runtime/kernel-3deb89d5-0bda-4e89-9bba-6845207b14b3.json"


## 直接通过 client 连接 -- 可能会导致原来正常运行的 kernel 被停止
from jupyter_client import BlockingKernelClient
import queue

client = BlockingKernelClient(connection_file=kernel_config_file)
client.load_connection_file()
client.start_channels()

client.execute("print(1+2)")
reply = client.get_shell_msg(10)
print(reply['content'])
print("")

while True:
    try:
        io_msg = client.get_iopub_msg(timeout=1)
        print(io_msg['content'])
    except queue.Empty:
        print('timeout kc.get_iopub_msg')
        break
