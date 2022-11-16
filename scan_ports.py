#!/usr/bin/env python3
import os
import sys
import time
import logging
try:
    import socket
except:
    sys.exit("Install missing library: pip install sockets")

def helplk():
    print("follow the example: ")
    print()
    print("%s --save out.txt"%(sys.argv[0]))
    sys.exit()

if len(sys.argv) <=1:
    helplk()
    sys.exit()
elif len(sys.argv) ==2:
    choice = str(sys.argv[1])
    if choice == "--save":
        print("enter a destination location")
        sys.exit()
    else:
        print("invalid option, correct is --save")
        print()
        helplk()
        sys.exit()
elif len(sys.argv) >=4:
    helplk()
    sys.exit()
else:
    pass

LOG = sys.argv[2]
logging.basicConfig(level=logging.INFO, filename=LOG, format="%(message)s")

try:
    print("[1] - start")
    print()

    loop = True
    while loop:
        op = str(input('choose an option above: '))

        if op == '1':
            host = input("insert ip(ex: 40.114.177.156): ")

            print("""
[2] - insert specific port
[3] - range 100 ports
[4] - range 1000 ports
[5] - common ports
[6] - all ports
""")

        elif op == '2':
            port = input("enter the port: ")
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            code = client.connect_ex((host, int(port)))
            if code == 0:
                print(f"code: {code}")
                print("port: {}".format(port))
                print("status: open")
                print("")
                logging.info(f"code: {code}")
                logging.info("port: {}".format(port))
                logging.info("status: open")
                logging.info("")
            elif code == 11:
                print(f"code: {code}")
                print("port: {}".format(port))
                print("status: closed")
                print("")
                logging.info(f"code: {code}")
                logging.info("port: {}".format(port))
                logging.info("status: closed")
                logging.info("")
            else:
                print(f"code: {code}")
                print("port: {}".format(port))
                print("status: undefined")
                print("")
                logging.info(f"code: {code}")
                logging.info("port: {}".format(port))
                logging.info("status: undefined")
                logging.info("")
            loop = False

        elif op == '3':
            ports = range(100)
            for port in ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.5)
                code = client.connect_ex((host, port))
                if code == 0:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: open")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: open")
                    logging.info("")
                elif code == 11:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: closed")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: closed")
                    logging.info("")
                else:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: undefined")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: undefined")
                    logging.info("")
                loop = False

        elif op == '4':
            ports = range(1000)
            for port in ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.5)
                code = client.connect_ex((host, port))
                if code == 0:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: open")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: open")
                    logging.info("")
                elif code == 11:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: closed")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: closed")
                    logging.info("")
                else:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: undefined")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: undefined")
                    logging.info("")
                loop = False

        elif op == '5':
            ports = [21, 22, 23, 25, 53, 80, 135, 139, 443, 445, 2280, 3306, 8080, 8081, 8443, 9050, 9051, 9150]
            for port in ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.5)
                code = client.connect_ex((host, port))
                if code == 0:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: open")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: open")
                    logging.info("")
                elif code == 11:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: closed")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: closed")
                    logging.info("")
                else:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: undefined")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: undefined")
                    logging.info("")
                loop = False

        elif op == '6':
            ports = range(65535)
            for port in ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.5)
                code = client.connect_ex((host, port))
                if code == 0:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: open")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: open")
                    logging.info("")
                elif code == 11:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: closed")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: closed")
                    logging.info("")
                else:
                    print(f"code: {code}")
                    print("port: {}".format(port))
                    print("status: undefined")
                    print("")
                    logging.info(f"code: {code}")
                    logging.info("port: {}".format(port))
                    logging.info("status: undefined")
                    logging.info("")
                loop = False

        else:
            print("invalid option. going out...")
            loop = False
            break
except socket.gaierror:
    print("socket error")
    pass
except socket.error as e:
    if e.errno != errno.EINTR:
        raise
    else:
        pass
except Exception as error:
    print(error)
    pass
except KeyboardInterrupt:
    sys.exit()
