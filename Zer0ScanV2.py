#! /usr/bin/python

from threading import Thread
import sys, re, getopt, signal, socket


version="2.0"
name = "Zer0ScanV2"


def usage():

	print ("Zer0Scan " + version + " for multiplatform. A simple local network scanner.")
	print ("Scanning method: Tries to connect the socket to a remote address with the library socket")
	print ("Version of python used: 3.6.2")
	print ()
	print ("Usage: " + name + ".py HOST")
	print ()
	print ("-p --port: port to connect (default: 80 (HTTP)).")
	print ()
	print ("Examples: ")
	print (name + ".py 192.168.0.0/24")
	print (name + ".py 192.168.0.10-40 -p 21")
	print (name + ".py 192.168.0.200-192.168.1.200,192.168.0.50")

	sys.exit(0)


class Scan(Thread):

	hostFound = hostScanned = 0


	def __init__(self, host, port):

		Thread.__init__(self)

		self.host = host

		self.port = port


	@property
	def host(self):
		return self._host


	@host.setter
	def host(self, host):

		if not isHost(splitIntoInt(host)):
			msgError(host)

		self._host = host


	def run(self):

		Scan.hostScanned += 1

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			s.connect((self.host, self.port))

		except ConnectionError:
			pass

		except:
			return

		print (self.host)

		Scan.hostFound += 1

		s.close()


class Host(object):

	def __init__(self, rangeHost):
		self.rangeHost = rangeHost


	@property
	def rangeHost(self):
		return self._rangeHost


	@rangeHost.setter
	def rangeHost(self, rangeHost):

		if not type(rangeHost) is str:
			msgError(rangeHost)

		self._rangeHost = rangeHost


	@property
	def fromHost(self):
		return self._fromHost


	@fromHost.setter
	def fromHost(self, fromHost):

		if not isHost(fromHost):
			msgError(fromHost)

		self._fromHost = fromHost


	@property
	def toHost(self):
		return self._toHost


	@toHost.setter
	def toHost(self, toHost):

		if not isHost(toHost):
			msgError(toHost)

		try:
			cond = toHost < self.fromHost

		except:
			msgError(toHost, "fromHost must be declared before toHost")

		if cond:
			msgError(toHost, "toHost < fromHost")

		self._toHost = toHost


	def run(self):

		host = self.rangeHost.split(',')

		for self.rangeHost in host:

			lhost = self.listRange()

			for h in lhost:
				h.start()

			for h in lhost:
				h.join()

		print ()
		print ("Zer0Scan " + version + " done: {} IP addresses ({} hosts up) scanned".format(Scan.hostScanned, Scan.hostFound))


	def listRange(self):

		method = self.method()

		self.fromHost = self.from_host()

		self.toHost = method()

		print ()

		if self.fromHost == self.toHost:
			print ("Send ping to {}...".format('.'.join(list(map(str, self.fromHost)))))
		
		else:
			print ("Send pings from {} to {}...".format('.'.join(list(map(str, self.fromHost))), '.'.join(list(map(str, self.toHost)))))

		print ()
		print ("Result:")

		lhost = []

		i = 3

		while(True):

			if self.fromHost[i] > 255:

				self.fromHost[i] = 0

				i -= 1

			else:
				lhost.append(Scan('.'.join(list(map(str, self.fromHost))), port))

			if self.fromHost == self.toHost:
				break

			self.fromHost[i] += 1

			if i < 3:
				i += 1

		return lhost


	def method(self):

		for cond, fct in {
			"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$": self.toHostWithNothing,
			"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})$": self.toHostWithMask,
			"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})-(\d{1,3}\.){,3}\d{1,3}$": self.toHostWithEnd
		}.items():

			self.rsearch = re.search(cond, self.rangeHost)

			if not self.rsearch is None:

				return fct

		msgError(self.rangeHost)


	def toHostWithMask(self):

		try:
			mask = int(self.rsearch.group(5))

		except:
			msgError(self.rsearch.group(5))

		for i in range(1, 4):
			if mask is i*8:

				rest = 4 - i

				if not self.fromHost[i:] == [0] * rest:
					msgError(mask, "host does not match the mask")

				return self.fromHost[:i] + [255] * rest

		msgError(mask)


	def toHostWithEnd(self):

		end = splitIntoInt(self.rsearch.group(0).split('-')[1])

		lenEnd = len(end)

		if not isHost(end, lenEnd):
			msgError(end)

		if lenEnd > 4:
			msgError(end, "end too large")

		return self.fromHost[:4 - lenEnd] + end


	def toHostWithNothing(self):
		return self.fromHost[:]


	def from_host(self):

		fromHost = []

		for i in range(1, 5):
			fromHost.append(self.rsearch.group(i))

		try:	
			fromHost = list(map(int, fromHost))

		except:
			msgError(fromHost)

		return fromHost


def splitIntoInt(host):

	try:
		return list(map(int, host.split('.')))

	except:
		msgError(host)


def isHost(host, byte = 4):

	if not type(host) is list or not type(byte) is int:
		return False

	numberByte = 0

	for h in host:
		try:

			assert h in range(256)

			numberByte += 1

		except:
			return False

	return numberByte is byte


def msgError(var, cause = None):

	print ("Failed to resolve \"{}\".".format(var))

	if not cause is None:
		print ("Raison: \"{}\".".format(cause))

	print ("WARNING: No hosts were specified, so 0 hosts scanned.")

	sys.exit(1)


def signal_handler(signal, frame):
    sys.exit(0)


def main():

	if not len(sys.argv[1:]) or sys.argv[1] in ('-h', '--help'):
		usage()

	global port

	port = 80

	try:
		opts, args = getopt.getopt(sys.argv[2:], "p:d", ["port="])
	
	except getopt.GetoptError as e:
		msgError(e)

	for opt, arg in opts:   

		if opt == '-d': 

			global _debug

			_debug = 1  

		elif opt in ("-p", "--port"):

			try:

				port = int(arg) 

				assert port > 0

			except:
				msgError(arg)

		else:
			msgError(opt)

	Host(sys.argv[1]).run()


if __name__ == "__main__":

	signal.signal(signal.SIGINT, signal_handler)

	main()
