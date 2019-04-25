from pwn import log

bases = ["172.1.1", "172.1.2"]
hosts = [1,2,3,4]

def get_ip_list(bases, hosts):
    with open("ip.txt", "a+") as f:
        for base in bases:
            for host in hosts:
                f.write("{}.{}\n".format(base, host))
  
if __name__ == "__main__":
    try:
        get_ip_list(bases, hosts)
        log.success("generate ip list successfully\n")
    except Exception as e:
        log.failure(repr(e))
      
