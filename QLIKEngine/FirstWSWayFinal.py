from websocket import create_connection as cc
import json
import qlikEnginePythonPackage.demo as demoprint
# ws  = cc("ws://localhost:4848/app/")
ws  = cc("ws://ap.qlikcloud.com/hub/personal")
# here, i have used only url to connect... it was run correctlly.
print(ws) 
data=json.dumps({
	"handle": -1,
	"method": "GetDocList",
	"params": [], 
	"outKey": -1,
	"id": 1,
}
)
demoprint.demoprint()
print('Sending Request')
ws.send(data)
print("Sent")

result = ws.recv_data()
print('Recieved ')
print(result)
print('Get Documents List Send')
OpenDocOrSelctanApp = json.dumps({
	"method": "OpenDoc",
	"handle": -1,
	"params": [
		"Procurement (1).qvf"
	],
	"outKey": -1,
	"id": 2
	# "handle": -1,
	# "method": "OpenDoc",
	# "params": {
	# 	"qDocName": "IPvisulualizations.qvf",
	# 	"qUserName": "Jatin123",
	# 	"qPassword": "Jaibajrangbali123",
	# 	"qSerial": "",
	# 	"qNoData": False
	# },
	# "outKey": -1,
	# "id": 2
})
GetObject=json.dumps({
	"handle": 1,
	"method": "GetObject",
	"params": {
		"qId": "ffe99d60-15fe-4a8a-8995-262ad296391e"
	},
	"outKey": -1,
	"id": 5
})
GetHyperCubeData=json.dumps({
"handle": 2,
	"method": "GetHyperCubeData",
	"params": {
		"qPath": "/qHyperCubeDef",
		"qPages": [
			{
				"qLeft": 0,
				"qTop": 0,
				"qWidth": 0,
				"qHeight": 0
			}
		]
	},
	"outKey": -1,
	"id": 6
})
GetAllInfos=json.dumps({
	"handle": 1,
	"method": "GetAllInfos",
	"params": []
})
GetDocListOrConnecttoEngine = json.dumps({
     	"handle": -1,
	"method": "GetDocList",
	"params": [],
	"outKey": -1,
	"id": 1
})
# ws.send(GetDocListOrConnecttoEngine)
ws.send(OpenDocOrSelctanApp)
# ws.send(GetAllInfos)
# ws.send(GetObject)
print('sent get doc list')
ResultList = ws.recv()
print('Recieved , Result')
print(ResultList)
print(type(ResultList),len(ResultList))
ParsedData = json.loads(ResultList)
DumpedData = json.dumps(ResultList)
print('Parsed',type(ParsedData),type(ParsedData['result']),type(ParsedData['result']['qDocList']))
# print(ParsedData)
for i in ParsedData['result']['qDocList']:
	for j in i:
		if(j.find('qDocName')>-1):
			if(i[j].find('Procurement (1).qvf')>-1):
				for k in i:
					print(k,' - ',i[k])
		# print(j==Human Capital Management.qvf)
# print('Dumped',type(DumpedData))
# print(DumpedData)
qclosed = ws.close()
print('Closed',qclosed)