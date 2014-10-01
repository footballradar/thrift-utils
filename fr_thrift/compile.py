import atexit
import subprocess
import shutil
import tempfile


def compile_thrift(fname):
    d = tempfile.mkdtemp()
    subprocess.check_call([
        "thrift",
        "-r",
        "--gen", "py",
        "-out", d,
        fname
    ])
    atexit.register(lambda: shutil.rmtree(d))
    return d
