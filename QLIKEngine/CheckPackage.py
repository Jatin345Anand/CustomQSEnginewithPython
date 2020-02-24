import qlikEnginePythonPackage.demo as ENGINEVIAPYTHON
print('WELCOME QLIK ENGINE')
URL = input('Enter the url of qlik hub to Connect Engine: ')
ws = ENGINEVIAPYTHON.GetSession('ws://'+URL)
# ws = ENGINEVIAPYTHON.GetSession(URL)
url = 'localhost:4848/app'
url1 = 'contextbi-qs.contextbi.net:4343/hub'
url2 = 'contextbi-qs.contextbi.net:4343/app'
url3 = 'contextbi-qs.contextbi.net:4848/app'


ws = ENGINEVIAPYTHON.GetDocList(ws)
DocID = ENGINEVIAPYTHON.TakeDocID()
ws = ENGINEVIAPYTHON.OpenDoc(ws,DocID)
ObjectID = ENGINEVIAPYTHON.TakeObjectID()
ws = ENGINEVIAPYTHON.GetObjectData(ws,ObjectID)
ws.close() 