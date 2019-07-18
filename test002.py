import requests


ip  = '172.16.98.51'
url = 'http://{}/PIsys/Sector/Sector.asmx/createSector'.format(ip)

operatorTag = '000'
serialNumber = '2060713988'
nationality = 'USA'
regionTag = 'zz'
productTagList1 = '1'
productTagList1 = '1'
productTagList2 = '2'
refreshSectorCreate = '1'
locationTag = ''

data = 'operatorTag={}&serialNumber={}&nationality={}&regionTag={}&productTagList={}'.format(operatorTag, serialNumber, nationality, regionTag, productTagList1)


r = requests.post(url, data={})

print(r.status_code, r.reason)