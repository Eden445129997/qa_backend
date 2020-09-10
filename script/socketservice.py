#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

def get_ip():
    """获取本机ip"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        # print(s.getsockname())
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello , world ! <h1>套接字测试</h1>'''

response_params = [
    'HTTP/1. 0 200 OK',
    'Date : Sun , 27 may 2018 01 : 01 : 01 GMT',
    'Cotent-Tγpe: text/html ; charset=utf-8',
    'Content-Length : {} \r\n'.format(len(body.encode())),
    body,
]
response = '\r\n'.join(response_params)

def handle_connection(conn , addr):
    print(conn, addr)
    import time
    time.sleep(10)
    request = b""
    while EOL1 not in request and EOL2 not in request :
        request += conn.recv(1024)
    print(request)
    conn.send(response.encode()) #response 转为 bytes 后传
    conn.close ()

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1',8838))
    serversocket.listen(5)
    try:
        while True:
            conn,address = serversocket.accept()
            handle_connection(conn,address)
    finally:
        serversocket.close()

if __name__ == '__main__':
    main()