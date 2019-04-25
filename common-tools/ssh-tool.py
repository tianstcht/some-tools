from pwn import log
import paramiko


ip_addr = "39.96.13.77"
port = 22
username = "root"
password = ""
new_password = ""

def ssh_change_passwd(ssh, ip_addr, port, username, password, new_password):
    try:
        ssh.connect(ip_addr, port, username, password, timeout=3)
        stdin, stdout, stderr = ssh.exec_command("passwd")
        stdin.write(new_password + '\n' + new_password + '\n')
        out, err = stdout.read(), stderr.read()
        if "updated successfully" in err:
            log.success("change passwd successfully: %s" %ip_addr)
        else:
            log.failure("change passwd failed: %s" %ip_addr)
    except:
        log.failure("Error!")
    finally:
        ssh.close()


if __name__ == "__main__":

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_change_passwd(ssh, ip_addr, port, username, password, new_password)
    except Exception as e:
        log.failure(repr(e))





