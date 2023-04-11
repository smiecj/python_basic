from tempfile import NamedTemporaryFile, TemporaryDirectory
import time
import os

with TemporaryDirectory(dir="/tmp", prefix='tmp_smiecj_') as tmp_dir, NamedTemporaryFile(
    mode="wb", dir=tmp_dir, suffix="smiecj"
) as f:
    os.chmod(tmp_dir, 0o766)
    os.chmod(f.name, 0o766)
    print("success")
    time.sleep(10)