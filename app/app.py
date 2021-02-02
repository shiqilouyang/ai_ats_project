from queue import Queue
from flask import  abort
from info import app
from conf.Setting import   utils_init_path
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer



at = abort
path = utils_init_path
body = {}
client_list = []
q = Queue()

# @app.route('/websocket')
# def websocket():
#      client_socket = request.environ.get('wsgi.websocket')
#      client_list.append(client_socket)
#      userId_ = request.args.get("userId")
#      from TestPoolModel.model import Operationtable
#      # print(len(client_list), client_list)
#      while 1:
#          msg_from_cli = client_socket.receive()
#          print(msg_from_cli)
#          #收到任何一个客户端的信息都进行全部转发（注意如果某个客户端连接断开，在遍历发送时连接不存在会报错，需要异常处理）
#          for client in client_list:
#              try:
#                  userMessage = Operationtable.query.filter(Operationtable.user_id == msg_from_cli).first()
#                  client.send(userMessage.message)
#                  print(userMessage.message)
#              except Exception as e:
#                  continue


# if __name__ =="__main__":
#     app.run(host="0.0.0.0", threaded=True, debug=True, port=8080)


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8080), application=app, handler_class=WebSocketHandler)
    http_server.serve_forever()
