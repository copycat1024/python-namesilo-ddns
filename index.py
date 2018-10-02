#! /usr/bin/python3

import time
import config
from namesilo import NamesiloClient, makeFQDN

client = NamesiloClient(config.api_key, config.domain)

print("Before:")
records, public_ip = client.dnsListRecord()

for sub in config.subdomains:
  host = makeFQDN(sub, config.domain)
  print("For {}:".format(host))
  host_rec = [r for r in records if r['host']==host]

  non_a_rec = [r for r in host_rec if r['type']!='A']
  for rec in non_a_rec:
    client.dnsDeleteRecord(rec['record_id'])

  a_rec = [r for r in host_rec if r['type']=='A']
  del_rec = []
  if len(a_rec) > 0:
    keep_rec = [r for r in a_rec if r['value']==public_ip]
    if len(keep_rec) == 1:
      del_rec = [r for r in a_rec if r['value']!=public_ip]
    else:
      rec = a_rec[0]
      client.dnsUpdateRecord(rec['record_id'], sub, public_ip)
      del_rec = a_rec[1:]
  else:
    client.dnsAddRecord('A', sub, public_ip)

  for rec in del_rec:
    client.dnsDeleteRecord(rec['record_id'])

print("After:")
client.dnsListRecord()
