# encoding=utf-8
'''
Created on 2012-11-7

@author: Steven
http://www.lifeba.org
基于BaseHTTPServer的http server实现，包括get，post方法，get参数接收，post参数接收。
'''
import io
import json
import shutil
import urllib
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.process(2)

    def do_POST(self):
        self.process(1)

    def process(self, type):

        content = "True"
        if type == 1:  # post方法，接收post参数
            datas = self.rfile.read(int(self.headers['content-length']))
            datas = datas.decode("utf-8", 'ignore')  # 指定编码方式
            datas = transDicts(datas)  # 将参数转换为字典
            # if 'data' in datas:
            #     content = "data:" + datas['data'] + "\r\n"
            if datas != None:
                for keys, values in datas.items():
                    content += keys
                    content += '='
                    content += values + ';'

        if '?' in self.path:
            # query = urllib.splitquery(self.path)
            # action = query[0]
            #
            # if query[1]:  # 接收get参数
            #     queryParams = {}
            #     for qp in query[1].split('&'):
            #         kv = qp.split('=')
            #         queryParams[kv[0]] = urllib.unquote(kv[1]).decode("utf-8", 'ignore')
            #         content += kv[0] + ':' + queryParams[kv[0]] + "\r\n"
            self.queryString = urllib.parse.unquote(self.path.split('?', 1)[1])
            params = urllib.parse.parse_qs(self.queryString)
            print(params)
        # 指定返回编码
        enc = "UTF-8"

        content = json.dumps({'errorcode': '0', 'msg': 'OK'})
        content = content.encode(enc)
        f = io.BytesIO()
        f.write(content)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        shutil.copyfileobj(f, self.wfile)


def transDicts(params):
    dicts = {}
    if len(params) == 0:
        return
    params = params.split('&')
    for param in params:
        dicts[param.split('=')[0]] = param.split('=')[1]
    return dicts


if __name__ == '__main__':

    try:
        server_address = ('', 8000)
        httpd = HTTPServer(server_address, MyRequestHandler)
        httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.socket.close()

    pass
