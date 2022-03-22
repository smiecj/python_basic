"""创建 Kernel 并执行代码"""

# 获取执行结果
import queue
import jupyter_client

kernel_manager, kernel_client = jupyter_client.manager.start_new_kernel(kernel_name = 'py3')

msg_id = kernel_client.execute("print(1+2)")
reply = kernel_client.get_shell_msg(10)
print(reply['content'])
print("")

while True:
    try:
        io_msg = kernel_client.get_iopub_msg(timeout=1)
        print(io_msg['content'])
    except queue.Empty:
        print('timeout kc.get_iopub_msg')
        break
