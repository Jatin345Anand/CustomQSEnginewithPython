from websocket import create_connection

import json

data=json.dumps({

                    'jsonrpc': '2.0',

                    'id': 0,

                    'method': 'OpenDoc',

                    'handle': -1,

                    'params': ['IPvisulualizations.qvf']

                },

                    sort_keys=True,

                 indent=4,

                 separators=(',', ': '))

ws = create_connection("ws://localhost:4848")

print("Sending req...")

ws.send(data)

print("Sent")

print("Receiving...")

result =  ws.recv()

print("Received '%s'" % result)
qclosed = ws.close()
print('Closed',qclosed)