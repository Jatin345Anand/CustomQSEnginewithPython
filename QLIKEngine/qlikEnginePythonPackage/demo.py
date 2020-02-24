import json
import websocket
import ssl
def demoprint():
    print('printing...')
def TakeDocName():
    val = input("Enter your Doc Name: ")
    return val
def TakeDocID():
    val = input("Enter your Doc Id: ")
    return val
def TakeExtensionNameorObjectName():
    val = input("Enter your Object ID or Extension Id: ")
    return val
def TakeFieldsofQlikApp():
    val = input("Enter your field name of Qlik App: ")
    return val
def TakeDimensionofQlikApp():
    val = input("Enter your dimension name of Qlik App: ")
    return val
def TakeObjectID():
    val = input("Enter your object id of Qlik App: ")
    return val

def GetSession(URL):
    header_user = {'header_user': 'user1'}
    # "ws://localhost:4848/app"
    ws = websocket.create_connection(URL, sslopt={"cert_reqs": ssl.CERT_NONE},header=header_user)
    print(ws.recv_data())    
    return ws
def GetDocList(ws):
    data=json.dumps({
        "handle": -1,
        "method": "GetDocList",
        "params": [], 
        "outKey": -1, 
        "id": 2,
    }
    )
    ws.send(data)
    result = ws.recv_data()
    print('All Document List : ')
    print('S.N     qDocName     qFileSize       qFileTime         qConnectedUsers          qDocId')
    print('Doc List ',result)
    # sn2=1
    # for i in json.loads(result[1])['result']['qDocList']:
    #     print(sn2,'      '+str(i['qDocName']),'      '+str(i['qFileSize']),'     '+str(i['qFileTime']),'    '+str(i['qConnectedUsers']),'      '+str(i['qDocId']))
    #     sn2 = sn2 +1
    return ws
def OpenDoc(ws,DocId):
    # C:\\Users\\jatin.anand\\Documents\\Qlik\\Sense\\Apps\\containerappforjune.qvf
    #  "eb6d6f63-6a97-4366-9ca6-7dc4e0d7491c"
    OpenDocJSON = json.dumps({
    "method": "OpenDoc",
        "handle": -1,
        "params": [
           DocId
        ],
        "outKey": -1,
        "id": 3
     
    })
    ws.send(OpenDocJSON)
    rOpenDoc = ws.recv_data()
    print('Your App / Document :')
    print(rOpenDoc)
    GetAllInfos = json.dumps({
        "handle": 1,
        "method": "GetAllInfos",
        "params": {},
        "outKey": -1,
        "id": 5
    }) 
    ws.send(GetAllInfos)
    result4 = ws.recv_data()
    print('All Object Name and Object ID of your chosen Document : ')
    print('S.N   |           -: qID : -             |  qType ')
    sn=1
    for i in json.loads(result4[1])['result']['qInfos']:
        print(sn,'    '+i['qId'],' '+i['qType'])
        sn = sn +1
    # print(json.loads(result4[1])['result']['qInfos']['qId'])
    # print(json.loads(result4[1])['result']['qInfos']['qType'])
    
    return ws
def GetObjectData(ws,ObjectID):
    GetObject= json.dumps({
    "handle": 1,
        "method": "GetObject",
        "params": {
            "qId": ObjectID
        },
        "outKey": -1,
        "id": 4 
    })
    ws.send(GetObject)
    result4 = ws.recv_data()
    print('Your Object :')
    print(result4)
    GetEffectiveProperties = json.dumps({
        "handle": 2,
        "method": "GetEffectiveProperties",
        "params": {},
        "outKey": -1,
        "id": 5
    })
    ws.send(GetEffectiveProperties)
    result4 = ws.recv_data()
    # print('Your Object EffectiveProperties for Hyper Cube Data')
    qW=''
    qH=''
    for i in json.loads(result4[1])['result']['qProp']['qHyperCubeDef']['qInitialDataFetch']:
        qW = i['qWidth']
        qH = i['qHeight']
    # qW = json.loads(result4[1])['result']['qProp']['qHyperCubeDef']['qInitialDataFetch']['qWidth']
    # qH = json.loads(result4[1])['result']['qProp']['qHyperCubeDef']['qInitialDataFetch']['qHeight']
    # print(qW,type(qW))
    # print(qH,type(qH))
    GetHyperCubeData = json.dumps({
        "handle": 2,
        "method": "GetHyperCubeData",
        "params": {
            "qPath": "/qHyperCubeDef",
            "qPages": [
                {
                    "qLeft": 0,
                    "qTop": 0,
                    "qWidth": qW,
                    "qHeight": qH
                }
            ]
        },
        "outKey": -1,
        "id": 6
    })
    ws.send(GetHyperCubeData)
    result4 = ws.recv_data()
    print('Your HyperCubeData of your object : ')
    qMatrix = json.loads(result4[1])['result']['qDataPages'][0]['qMatrix']
    print('           Dimension  Details         ||            Measure Details  ')
    print('S.N  qText  qNum  qElemNumber  qState &&  qText  qNum  qElemNumber  qState ')
    sn2=1
    for i in qMatrix:
        print(sn2,'   '+i[0]['qText'],'  '+str(i[0]['qNum']),'       '+str(i[0]['qElemNumber']),'     '+str(i[0]['qState']),'         '+i[1]['qText'],'  '+str(i[1]['qNum']),'       '+str(i[1]['qElemNumber']),'     '+str(i[1]['qState']))
        # print(sn2,' '+i[0]['qText'],' '+i[0]['qNum'],' '+i[0]['qElemNumber'],' '+i[0]['qState'],' '+i[1]['qText'],' '+i[1]['qNum'],' '+i[1]['qElemNumber'],' '+i[1]['qState'])
        sn2 = sn2 +1
    # closed = ws.close()
    return ws