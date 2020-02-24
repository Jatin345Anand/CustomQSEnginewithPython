import websocket
import ssl
import json

header_user = {'header_user': 'user1'}

ws = websocket.create_connection("ws://localhost:4848/app", sslopt={"cert_reqs": ssl.CERT_NONE},header=header_user)
# ws.recv_data()
result = ws.recv_data()
print('Recieved Session')
print(result)

data=json.dumps({
	"handle": -1,
	"method": "GetDocList",
	"params": [], 
	"outKey": -1, 
	"id": 1,
}
)
print('Sending Request')
ws.send(data)
print("Sent")
result = ws.recv_data()
print('Recieved Doc List')
print(result)
# GetDocListOrConnecttoEngine = json.dumps({
#      	"handle": -1,
# 	"method": "GetDocList",
# 	"params": [],
# 	"outKey": -1,
# 	"id": 2
# })
# ws.send(GetDocListOrConnecttoEngine)
# result2 = ws.recv_data()
# print('recieved',result2)
OpenDocJSON = json.dumps({
"method": "OpenDoc",
	"handle": -1,
	"params": [
		"C:\\Users\\jatin.anand\\Documents\\Qlik\\Sense\\Apps\\containerappforjune.qvf"
	],
	"outKey": -1,
	"id": 2
 
})
ws.send(OpenDocJSON)
rOpenDoc = ws.recv_data()
print('r DOC Open ')
print(rOpenDoc)
CreateSessionObjDocJSON = json.dumps({
  	"handle": 1,
	"method": "CreateSessionObject",
	"params": {
		"qProp": {
			"qInfo": {
				"qId": "C:\\Users\\jatin.anand\\Documents\\Qlik\\Sense\\Apps\\containerappforjune..qvf",
				"qType": "Doc"
			},
			"qExtendsId": "",
			"qMetaDef": {},
			"qStateName": ""
		}
	},
	"outKey": -1,
	"id": 3
})
ws.send(CreateSessionObjDocJSON)
result3 = ws.recv_data()
print('recieved CreateSession')
print(result3)
print('request for Get Dimesion')
GetAllInfos = json.dumps({
	"handle": 1,
	"method": "GetAllInfos",
	"params": {},
	"outKey": -1,
	"id": 5
}) 
ws.send(GetAllInfos)
result4 = ws.recv_data()
print('recieved AllInfos')
print(result4)
GetObject= json.dumps({
   "handle": 1,
	"method": "GetObject",
	"params": {
		"qId": "xWJBmz"
	},
	"outKey": -1,
	"id": 4 
})
ws.send(GetObject)
result4 = ws.recv_data()
print('recieved GetObject')
print(result4)
GetEffectiveProperties = json.dumps({
    "handle": 3,
	"method": "GetEffectiveProperties",
	"params": {},
	"outKey": -1,
	"id": 5
})
ws.send(GetEffectiveProperties)
result4 = ws.recv_data()
print('recieved Get EffectiveProperties')
print(result4)
GetHyperCubeData = json.dumps({
    "handle": 3,
	"method": "GetHyperCubeData",
	"params": {
		"qPath": "/qHyperCubeDef",
		"qPages": [
			{
				"qLeft": 0,
				"qTop": 0,
				"qWidth": 17,
				"qHeight": 500
			}
		]
	},
	"outKey": -1,
	"id": 6
})
ws.send(GetHyperCubeData)
result4 = ws.recv_data()
print('recieved Get HyperCubeData')
print(result4)
closed = ws.close()
print('Closed',closed)