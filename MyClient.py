import websocket, http.client, sys, asyncore


def connect(server, port):
    print("connecting to: %s:%d" % (server, port))

    conn = http.client.HTTPConnection(server + ":" + str(port))
    conn.request('POST', '/test', "{'balls' : 2}")
    resp = conn.getresponse()
    #hskey = resp.read().split(':')[0]

    ws = websocket.WebSocket(
        'ws://' + server + ':' + str(port),
        onopen=_onopen,
        onmessage=_onmessage,
        onclose=_onclose)

    return ws


def _onopen():
    print("opened!")


def _onmessage(msg):
    print("msg: " + str(msg))


def _onclose():
    print("closed!")
