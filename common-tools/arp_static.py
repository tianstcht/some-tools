import os
from pwn import log

# [ip, mac]
arps = [
    ['192.168.73.2', '00:50:56:f5:d3:2a'],
    ['111.111.111.1', 'ff:ff:33:12:22:56']
]


for arp in arps:
    try:
        os.system("sudo arp -i ens33 -s {} {}".format(arp[0], arp[1]))
    except Exception as e:
        log.failure(e)
        continue

