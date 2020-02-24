TEST_LOAD = {

  "method": "OpenDoc",
	"handle": -1,
	"params": [
		"C:\\Users\\jatin.anand\\Documents\\Qlik\\Sense\\Apps\\IPvisulualizations.qvf"
	],
	"outKey": -1,
	"id": 2
}

class QlikClient(Protocol):

  def connectionMade(self):

  self.transport.write(bytes(json.dumps(TEST_LOAD), encoding='utf-8'))

  print('Sent ', json.dumps(TEST_LOAD), 'to the server.')

  def dataReceived(self, data):

  print("Server said:", data)

  self.transport.loseConnection()