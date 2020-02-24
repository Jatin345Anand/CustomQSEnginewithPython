from websocket import create_connection as cc
import json
# Connect with Local Qlik Sense Server
# ws  = cc("ws://localhost:4848/app/")
ws = cc("ws://contextbi-qs.contextbi.net/hub/my/work")
data=json.dumps({
	"handle": -1,
	"method": "GetDocList",
	"params": [], 
	"outKey": -1,
	"id": 1,
}
)
# Sending First Request (Connect to Engine)
print('Sending Request')
ws.send(data)

print("Sent")
result = ws.recv_data()
print('Recieved ')
# Response of First Request
print(type(result))
for i in result:
	print(i)
	print(result[i])
 
# Sending Second Request (GetAppList)
GetDocListOrConnecttoEngine = json.dumps({
     	"handle": -1,
	"method": "GetDocList",
	"params": [],
	"outKey": -1,
	"id": 4
})
ws.send(GetDocListOrConnecttoEngine)
result2 = ws.recv_data()
# Response of Second Request
print('recieved',result2)
# Sending request to Create Seesion ID for App
CreateSessionViaApp=json.dumps({
    "handle": -1,
	"method": "CreateSessionAppFromApp",
	"params": {
		"qSrcAppId": "C:\\Users\\jatin.anand\\Documents\\Qlik\\Sense\\Apps\\UseContainerApp.qvf"
	},
	"outKey": -1,
	"id": 2
})
rSessionViaApp = ws.recv_data()
print('Response Session App')
# Response of CreateSessionFromApp
print(rSessionViaApp)
# Sending request to Create Session Obj for App
CreateSessionObjDocJSON = json.dumps({
  	"handle": 1,
	"method": "CreateSessionObject",
	"params": {
		"qProp": {
			"qInfo": {
				"qId": "C:\\Users\\jatin.anand\\Documents\\Qlik\\Sense\\Apps\\UseContainerApp.qvf",
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
result3 = ws.recv_data()
print('recieved CreateSession')
# Response of Create Session Obj
print(result3)
# Sending Request to OpenDoc
OpenDocJSON = json.dumps({
    "method": "OpenDoc",
	"handle": -1,
	"params": [
		"C:\\\\Users\\\\jatin.anand\\\\Documents\\\\Qlik\\\\Sense\\\\Apps\\\\UseContainerApp.qvf"
	],
	"outKey": -1,
	"id": 2
})
rOpenDoc = ws.recv_data()
print('r Open DOC')
# Response of Open Doc
print(rOpenDoc)
# Sending request to Get All Infos (All Generic Objects / Custom Extensions ObjectID and ObjectName)
getAllInfos = json.dumps({
    "handle": 1,
	"method": "GetAllInfos",
	"params": {},
	"outKey": -1,
	"id": 3
}) 
result4 = ws.recv_data()
print('recieved ')
# Response of GetAllInfos
print(result4)
closed = ws.close()
print('Closed',closed)

