import re

def removezero_ip(ip):
    string = re.sub('\.[0]*', '.', ip)
    return string

print(removezero_ip("108.250.350.450"))
