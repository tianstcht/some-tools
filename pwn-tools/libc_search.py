from pwn import *
import os


def get_libc_names():
    libc_path = "./libc"
    for root, dirs, libc_names in os.walk(libc_path):
        return libc_names


def get_func_offset(func_name, libc_name):
    libc = ELF(libc_name, checksec=False)
    try:
        return libc.symbols[func_name]
    except:
        return ""
    

def input_leak_address():
    func_names = []
    offsets = []
    while True:
        func_name = raw_input("Function Name: ").strip()
        offset = raw_input("Leak Info(low 12 bits) : ").strip()
        func_names.append(func_name)
        offsets.append(offset)
        while True:
            choose = "y"
            choose = raw_input("Continue[Y/n]: ")
            if choose.strip() == "":
                break
            elif choose.strip().lower()[0] == "n":
                return func_names, offsets
            elif choose.strip().lower()[0] == "y":
                break
            else:
                print "Invalid Choose"
                continue


def match_libc(libc_names_list, func_names, leaks):
    match_libcs = []
    for libc_name in libc_names_list:
        next_flag = 0

        for func_name, leak in zip(func_names, leaks):
            if len(leak) > 3:
                leak = leak[-3:]

            if leak != hex(get_func_offset(func_name, libc_name))[-3:]:
                next_flag = 1
                # log.info("NOT MATCH : %s" % libc_name)
                break

        if not next_flag:
            # log.success("MATCH : %s " % libc_name)
            match_libcs.append(libc_name)
    
    return match_libcs
                

if __name__ == "__main__":
    libc_names_list = []
    libc_names_list = get_libc_names()
    
    os.chdir("./libc")
    func_names, leaks = input_leak_address()
    
    match_libc_list = []
    match_libc_list = match_libc(libc_names_list, func_names, leaks)
    
    for match_libc in match_libc_list:
        log.success("MATCH : %s" % match_libc)
    
    
    







