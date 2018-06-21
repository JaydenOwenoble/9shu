# -*- coding:utf-8 -*-

import conf
import json
import socket


class NetOpt(object):
    def __init__(self):
        pass

    def listen_tasks(self):
        skt = socket.socket()
        skt.bind(("", conf.listen_task_port))
        skt.listen(1)

        while 1:
            cli, addr = skt.accept()
            req_data = ""
            while True:
                data = cli.recv(1024)
                if not data:
                    break
                req_data += data
            cli.close()
            self.__structuring_reqs(req_data)

    # 请求结构化
    # {id: (header, post_data)}
    # header: {key: val}
    # post_data: {key: val}
    def __structuring_reqs(self, reqs_str):
        print(reqs_str)
        return json.load(reqs_str)


glb_net_opt = NetOpt()
