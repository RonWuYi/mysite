import requests
import pyodbc

from util.constant import *

ip51  = '172.16.98.51'
ip149  = '172.16.66.149'
url = 'http://{}/PIsys/Sector/Sector.asmx'

operatorTag = '000'
serialNumber = '2129133568'
nationality = 'USA'
regionTag = 'zz'
productTagList1 = '1'
productTagList2 = ''
refreshSectorCreate = '1'
locationTag = ''
headers = {'Content-Type': 'application/soap+xml; charset=utf-8'}

body = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <createSector xmlns="http://irdeto.com/pisys/sector">
      <operatorTag>{}</operatorTag>
      <serialNumber>{}</serialNumber>
      <nationality>{}</nationality>
      <regionTag>{}</regionTag>
      <productTagList>
        <string>{}</string>
      </productTagList>
    </createSector>
  </soap12:Body>
</soap12:Envelope>"""
response = requests.post(url.format(ip149), data=body.format(operatorTag, serialNumber, nationality, regionTag, productTagList1)
, headers=headers)
print(response)
print(response.reason)


