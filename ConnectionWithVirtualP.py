import websocket
import ssl
import json

header_user = {'header_user': 'user1'}

ws = websocket.create_connection("ws://contextbi-qs.contextbi.net/hub/my/work", sslopt={"cert_reqs": ssl.CERT_NONE},header=header_user)
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
CreateSessionField = json.dumps({
"method": "CreateSessionObject",
	"handle": 1,
	"params": [
		{
			"qInfo": {
				"qType": "FieldList"
			},
			"qFieldListDef": {
				"qShowSystem": True,
				"qShowHidden": True,
				"qShowDerivedFields": True,
				"qShowSemantic": True,
				"qShowSrcTables": True,
				"qShowImplicit": True
			}
		}
	],
	"outKey": -1,
	"id": 6 
})
ws.send(CreateSessionField)
result5 = ws.recv_data()
print('recieved Create Session for Field')
print(result5)
GetLayoutforField = json.dumps({
     "method": "GetLayout",
	"handle": 3,
	"params": [],
	"outKey": -1,
	"id": 7
})
ws.send(GetLayoutforField)
result5 = ws.recv_data()
print('recieved Get layout for Field')
print(result5)
GetHyperCubeData = json.dumps({
		"handle": 2,
	"method": "GetHyperCubeData",
	"params": {
		"qPath": "/qHyperCubeDef",
		"qPages": [
			{
				"qLeft": 0,
				"qTop": 0,
				"qWidth": 2,
				"qHeight": 1
			}
		]
	},
	"outKey": -1,
	"id": 8

})
ws.send(GetHyperCubeData)
result5 = ws.recv_data()
print('recieved Get Hyper Cube Data ')
print(result5)
closed = ws.close()
print('Closed',closed)

