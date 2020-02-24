from websocket import create_connection as cc
import json
ws  = cc("ws://localhost:4848/app/")
print(ws)
# data  = json.dumps({
#     'jsonrpc':'2.0',
#     'id':2,
#     'method':'DoReload',
#     'handle':1,
#     'params':['C:\\Users\\jatin.anand\\Documents\\Qlik\Sense\\Apps\\IPvisulualizations.qvf']
# })
data=json.dumps({
	"handle": -1,
	"method": "GetDocList",
	"params": [],
	"outKey": -1,
	"id": 1,
                    # 'jsonrpc': '2.0',

                    # 'id': 0,

                    # 'method': 'OpenDoc',

                    # 'handle': -1,

                    # 'params': ['IPvisulualizations.qvf']

}
)
print('Sending Request')
ws.send(data)
print("Sent")
result = ws.recv_data()
print('Recieved ')
print(result)
print('Get Documents List Send')
# GetDoctListData = json.dumps({
#     "jsonrpc":"2.0",
#     "id":2,
#     "handle": -1,
# 	"method": "GetDocList",
# 	"params": {}
# })
# CreatApp=json.dumps({
#       "handle": -1,
#   "method": "CreateApp",
#   "params": {

#   "qAppName": "Test-App",
#   "qLocalizedScriptMainSection": ""
#   },
#   "jsonrpc": "2.0",
#   "id": 5
# })
OpenDoc = json.dumps({
     	"handle": -1,
	"method": "GetDocList",
	"params": [],
	"outKey": -1,
	"id": 1
})
ws.send(OpenDoc)
print('sent get doc list')
ResultList = ws.recv()
print('Recieved , Result')
print(ResultList)
qclosed = ws.close()
print('Closed',qclosed)