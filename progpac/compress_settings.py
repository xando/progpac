from settings import *
import subprocess

DEBUG=True
COMPRESS_OFFLINE_MANIFEST = subprocess.Popen(
    "git rev-parse HEAD", shell=True, stdout=subprocess.PIPE
).stdout.read().strip("\n")

