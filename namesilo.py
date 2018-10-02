from requests import Session
from xmltodict import parse

def makeFQDN(host, domain):
  return "{0}.{1}".format(host, domain)

def makeUrl(operation, key, data={}):
	res = 'https://www.namesilo.com/apibatch/{0}?version=1&type=xml&key={1}'.format(operation, key)
	for key, value in data.items():
		res += '&{0}={1}'.format(key, value)
	return res

def getRequestIp(data):
  return data['request']['ip']

def getDnsRecord(data):
  res = data['reply']['resource_record']
  if type(res) is not list:
    return [res]
  else:
    return res

def printInfo(s1, s2, s3, s4):
  text = "  {0:<5}{1:<6}{2:<16}{3}".format(s1[:4], s2, s3, s4)
  print(text)

def printDnsRecord(rec):
  printInfo(rec['record_id'], rec['type'], rec['value'], rec['host'])

def printReply(data):
  reply = data['reply']
  print("  Reply: {1} ({0})".format(reply['code'], reply['detail']))

class NamesiloClient:
  def __init__(self, key, domain):
    self.key = key
    self.domain = domain
    print('Connecting to namesilo.com... ', end='', flush=True)
    self.ses = Session()
    self.ses.get('https://www.namesilo.com')
    print('Done.')
    print()

  def _getData(self, url):
    return parse(self.ses.get(url).content)['namesilo']

  def dnsListRecord(self):
    url = makeUrl('dnsListRecords', self.key, {
      'domain': self.domain
    })

    print("- List records:")
    data = self._getData(url)
    printReply(data)
    records = getDnsRecord(data)
    for r in records:
      printDnsRecord(r)
    print()
    return records, getRequestIp(data)

  def dnsUpdateRecord(self, rrid, rrhost, rrvalue):
    url = makeUrl('dnsUpdateRecord', self.key, {
      'domain': self.domain,
      'rrid': rrid,
      'rrhost': rrhost,
      'rrvalue': rrvalue,
      'rrttl': 7207
    })

    print("- Update record:")
    printInfo(rrid, '-', rrvalue, makeFQDN(rrhost, self.domain))
    data = self._getData(url)
    printReply(data)
    print()

  def dnsAddRecord(self, rrtype, rrhost, rrvalue):
    url = makeUrl('dnsAddRecord', self.key, {
      'domain': self.domain,
      'rrtype': rrtype,
      'rrhost': rrhost,
      'rrvalue': rrvalue,
      'rrttl': 7207
    })

    print("- Add record:")
    printInfo('-', rrtype, rrvalue, makeFQDN(rrhost, self.domain))
    data = self._getData(url)
    printReply(data)
    print()

  def dnsDeleteRecord(self, rrid):
    url = makeUrl('dnsDeleteRecord', self.key, {
      'domain': self.domain,
      'rrid': rrid
    })

    print("- Delete record:")
    printInfo(rrid, '-', '-', '-')
    data = self._getData(url)
    printReply(data)
    print()
